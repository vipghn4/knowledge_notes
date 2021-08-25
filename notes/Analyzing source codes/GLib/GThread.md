<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [GThread](#gthread)
  - [Introduction](#introduction)
  - [Mutex and locking](#mutex-and-locking)
<!-- /TOC -->

# GThread
## Introduction
## Mutex and locking
**PThread mutex**.
* *Implementation*.

    ```c
    typedef struct {
            struct pthread_queue queue; // waiting threads
            char lock; // lock bit
            struct pthread *owner; // current owner thread
            int flags;
    #ifdef _POSIX_THREADS_PRIO_PROTECT
            int prioceiling;
            pthread_protocol_t protocol;
            int prev_max_ceiling_prio;
    #endif
    } pthread_mutex_t;
    ```

* *PThread queue*. A queue of threads waiting to acquire the mutex lock

    ```c
    typedef struct pthread_queue {
        struct pthread *head;
        struct pthread *tail;
    } *pthread_queue_t;
    ```

**GMutex**. An opaque data structure to represent a mutex, i.e. mutal exclusion, used to protect data against shared access
* *Implementation*.

    ```c
    union _GMutex {
        /*< private >*/
        gpointer p;
        guint i[2];
    };
    ```

    * *`p`*. Pointer to an instance of `pthread_mutex_t` for non-native implementation of locking
    * *`i`*. Integer variable for native implementation of locking

* *Example usage*.

    ```c
    static GMutex *give_me_next_number_mutex = NULL;

    /* this function must be called before any call to give_me_next_number ()
        it must be called exactly once. */
    void init_give_me_next_number () 
    {
        g_assert (give_me_next_number_mutex == NULL);
        give_me_next_number_mutex = g_mutex_new ();
    }

    int give_me_next_number ()
    {
        static int current_number = 0;
        int ret_val;

        g_mutex_lock (give_me_next_number_mutex);
        ret_val = current_number = calc_next_number (current_number); 
        g_mutex_unlock (give_me_next_number_mutex);
        return ret_val;
    }
    ```

* *Notes*. Do not construct a `GMutex` in our own programs, since there will be a race condition while constructing the mutex and the code cannot work reliable
    * *Example*. The example below illustrates a bad usage of `GMutex`

        ```c
        int give_me_next_number ()
        {
            static int current_number = 0;
            int ret_val;
            static GMutex * mutex = NULL;

            if (!mutex)
            mutex = g_mutex_new ();
            g_mutex_lock (mutex);
            ret_val = current_number = calc_next_number (current_number); 
            g_mutex_unlock (mutex);
            return ret_val;
        }
        ```

>**NOTE**. `GLib` allows us to try to lock a mutex and immediately return if the mutex is already locked by another thread, rather than waiting to acquire the lock
>$\to$ This is done via `g_mutex_trylock()`

**Lock and unlock functions for `GMutex`**. The main function used to lock a `GMutex` object
* *Implementation 1*. Use `pthread`
    * If `mutex->p == NULL`, i.e. there is no `pthread_mutex_t` object assigned to `mutex->p`
        
        $\to$ Allocate a new `pthread_mutex_t` object and assign it to `mutex->p`
    * Call `pthread_mutex_lock` on `mutex->p`
* *Implementation 2*. Use native mutex lock
    * Increase `mutex->i[0]` by `1` and examine the previous value of `mutex->i[0]`

        $\to$ If the value is nonzero, i.e. some thread is locking it already, then wait until the thread is released
    * Once the lock is released, i.e. `mutex->i[0] == 0`, we acquire the lock immediately

**`g_mutex_unlock(GMutex *mutex)`**. The main function used to unlock a `GMutex` object
* *Implementation 1*. Similar to `g_mutex_lock`, i.e. invoke `pthread_mutex_unlock`
* *Implementation 2*. Set `mutex->i[0]` to `0` to indicate that the lock has been released