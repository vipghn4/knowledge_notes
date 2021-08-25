<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [GstBus](#gstbus)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# GstBus
# Appendix
## Concepts
**Coding practices in C/C++**.
* *Struct declaration and definition*. In C projects, private structs are declared in header files and defined in source files, e.g.
    * *Header file*.

        ```c
        typedef struct _GstBusPrivate GstBusPrivate;
        ```
    
    * *Source file*.

        ```c
        struct _GstBusPrivate {
            GstAtomicQueue *queue;
            GMutex queue_lock;
            SyncHandler *sync_handler;
            guint num_singal_watchers;
            guint num_sync_message_emitters;
            GSource *gsource;
            gboolean enable_async;
            GstPoll *poll;
            GPollFD pollfd;
        };
        ```