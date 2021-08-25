<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [GstObject and GstMiniObject](#gstobject-and-gstminiobject)
  - [GstObject](#gstobject)
<!-- /TOC -->

# GstObject and GstMiniObject
## GstObject
**GstObject**. `GstObject` provides a root for the object hierarchy tree filed in by the GStreamer library
* *Idea*. It is currently a thin wrapper on top of `GInitiallyUnowned`, i.e. essentially `_GObject` as given in `glib/gobject/gobject.h`
    
    >**NOTE**. It is an abstract class that is not very usable on its 

* *Struct fields*.
    * *`lock`*. An instance of `GMutex`, which is the lock associated with the object

        $\to$ This is used for object locking
    * *`name`*. A pointer of `char`, which is the name of the object
    * *`parent`*. An instance of `GstObject`, which is the parent object of the object`
    * *`flags`*. A 32-bit integers containing flags associated with this object

        $\to$ Refer to `GstObjectFlags` below
    * *`control_bindings`*. A pointer to a `GList`, which is a list of `GstControlBinding`

        $\to$ This is used for controlled properties
    * *`control_rate`*. The rate, at which control bindings modify the properties of the object
    * *`last_sync`*. The last time control bindings modify the properties of the object
    * *`__gst_reserved`*. Padding memory for memory alignment

**Controlled properties**. Offer a lightweight way to adjust `GObject` properties over stream-time
* *Idea*. Work by using time-stamped value pairs which are queued for element properties

    $\to$ At run-time, the elements continuously pull value changes for the current stream-time
* *Implementation flow*.
    1. Create a `GstControlSource`, e.g.

        ```c
        csource = gst_interpolation_control_source_new (); 
        g_object_set (csource, "mode", GST_INTERPOLATION_MODE_LINEAR, NULL);
        ```
    
    2. Attach the control source on the controller to a property, i.e.

        ```c
        gst_object_add_control_binding (
            object, gst_direct_control_binding_new (object, "prop1", csource)
        );
        ```
    
    3. Set the control values, i.e.

        ```c
        gst_timed_value_control_source_set (
            (GstTimedValueControlSource *)csource, 0 * GST_SECOND, value1
        ); 
        gst_timed_value_control_source_set (
            (GstTimedValueControlSource *)csource, 1 * GST_SECOND, value2
        );
        ```
    
    4. Start the pipeline

**GstObjectFlags**.
* *`GST_OBJECT_FLAG_MAY_BE_LEAKED` (1)*. The object is expected to stay alive, even after `gst_deinit` has been called, and thus should be ignored by leak detection tools
* *`GST_OBJECT_FLAG_LAST` (16)*. Subclasses can add additional flags starting from this flag