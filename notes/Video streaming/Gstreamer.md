
## GstElements
**Elements**. A black box, i.e. when we put something in, the element does something with it, and something else comes out at the other side

### Types of Gst elements
**Source elements**. Generate data for use by a pipeline

>**NOTE**. Source elements do not accept data, they only generate data

**Filters, converters, demuxers, muxers, and decoders**.
* *Filters and filter-like elements*. Operate on data which they receive on their input (sink) pads, and provide data on their output (source) pads
    * *Example*. Volume element (filter), video scaler (convertor), Ogg demuxer, etc.
    * *Pads*. Both have input and output pads
* *Filter elements*. Can have one source pad and one sink pad
* *Filter-like elements*. Can have any number of source of sink pads, e.g. a video demuxer

**Sink elements**. End points in a media pipeline, i.e. they accept data without producing anything

### Element states
**States of a GstElement**. After being created, an element will not actually perform any actions yet

$\to$ We need to change elements state to make it do something
* *`GST_STATE_NULL` (Default state)*. No resources are allocated, thus transitioning to this state will free all resources
    
    >**NOTE**. The element must be in this state when its `refcount` reaches 0 and it is freed
* *`GST_STATE_READY`*. The element has allocated all of its global resources, i.e. resources which can be capt within streams

    >**NOTE**. The stream is not opened in this state, i.e. the stream positions is automatically zero
    >$\to$ If a stream was previously opened, it should be closed in this state, and position, properties, and such should be reset

* *`GST_STATE_PAUSED`*. The element has opened the stream, but is not actively processing it
    * *Purpose*. Allow the element to modify a stream's position, read, and process data, etc. to prepare for playback as soon as state is changed to `GST_STATE_PLAYING`

    >**NOTE**. It is not allowed to play the data, which would make the clock run, in this state

    >**NOTE**. Elements going to `PAUSED` state should prepare themselves for moving over to the `PLAYING` state as soon as possible
    >* *Example*. Video or audio outputs would wait for data to arrive and queue it so that they can play it right after the state change

* *`GST_STATE_PLAYING`*. The element does exactly the same as in `PAUSED` state, excep that the clock now runs

**State change**. If we set an element to another state, GST will internally traverse all intermediate states
* *Recursive state change*. When we set a bin or pipeline to a certain target state

    $\to$ It usually propagate the state change to all elements within the bin or pipeline automatically
* *Dynamic pipeline*. When adding elements dynamically to a running pipeline, e.g. via some callback

    $\to$ We need to set it to the desired target state by hand with `gst_element_set_state()` or `gst_element_sync_state_with_parent()`

**Pipeline running**. Internally, GST will start threads running the pipeline, and take care of message switching from the pipeline's thread into the application's thread, using a `GstBus`

## GstBaseTransform
**GstBaseTransform**. The base class for filter elements which process data
* *Suitable elements*. Ones where the size and caps of the output is known entirely from the input caps and buffer sizes
    * *Example*.
        * Elements which directly transform one buffer into another
        * Elements which modify the contents of a buffer in-place
        * Elements which collate multiple input buffers into one output buffer
        * Elements which exapnd one input buffer into multiple output buffers
* *Characteristics*.
    * There is one sinkpad and one srcpad
    * Possible formats on sink and source pad implemented with custom `transform_caps` function

        >**NOTE**. By default, the same format on sink and source is used
  
    * Handle state changes
    * Does flushing
    * Push mode and pull mode (if the sub-class transform can operate on arbitrary data)

### Processing modes
**Passthrough mode**. The element has no interest in modifying the buffer, i.e. it may want to inspect the buffer

$\to$ In this case, the element should have a `transform_ip` function, otherwise, the buffer is pushed intact

**Modification in-place**. Input buffer and output buffer are the same thing

$\to$ In this case, the element should have a `transform_ip` function

>**NOTE**. If `always_in_place` flag is set, non-writable buffers will be copied and passed to the `transform_ip` function. Otherwise, a new buffer will be created and the transform function called

* *Characteristics*.
    * Output buffer size must be at most input buffer size
    * Incoming writable buffers will be passed to `transform_ip` function immediately
    * Only implementing `transform_ip` and not transform implies `always_in_place=TRUE`

* *`always_in_place` flag*. Determine whether a non-writable buffer will be copied before passing to the `transform_ip` function
    * *Implications*.
        * Implied `TRUE` if no `transform` function is implemented
        * Implied `FALSE` if only `transform` function is implemented

**Modification only to the caps/metadata of a buffer**. The element does not require writable data, but non-writable buffers should be subbuffered so that the meta-information can be replaced
* *Requirements*. Elements wishing to operate in this mode should 
    * Replace the `prepare_output_buffer` method to create subbuffers of the input buffer, and
    * Set `always_in_place` to `TRUE`
* *`prepare_output_buffer`*. Subclasses can override this function from `GstBaseTransform` to do their own allocation of output buffers
    * *Example*. Elements only doing analysis can return a subbuffer, or just a reference to the input buffer (if in passthrough mode)

**Normal mode**. Element will receive an input buffer and output buffer to operate on
* *Characterstics*.
    * `always_in_place` is not set, and there is no `transform_ip` function
    * Output buffer is allocated by calling `prepare_output_buffer` function

## GstSignal
**Signals**.
* *Signals*.
    * `pad-added`. Emitted when a new `GstPad` has been added to the element

        >**NOTE**. The signal is usually be emitted from the context of the streaming thread
        
        * *References*. https://gstreamer.freedesktop.org/documentation/gstreamer/gstelement.html?gi-language=c#GstElement::pad-added
    * `child-added`. 
        * *References*. https://gstreamer.freedesktop.org/documentation/gstreamer/gstchildproxy.html?gi-language=c

## Gstreamer Caps
### Pad Caps
**Pad capabilities**.
* *Pads*. Allow information to enter and leave an element
* *Pad capabilities (or Pad caps)*. Specify what kind of information can travel through the pad
    * *Example*. RGB video with resolution 320x320 pixels and 30 FPS

    >**NOTE**. Pads can support multiple caps, and caps can be specified as ranges, e.g. an audio sink can support samples rates from 1 to 48000 Hz

    >**NOTE**. Some elements query the underlying hardware for supported formats and offer their Pad Caps accordingly
    >$\to$ Shown caps can vary from platform to platform, or even one execution to the next

    * *Example*.

        ```
        SINK template: 'sink'
            Availability: Always
            Capabilities:
                audio/x-raw
                        format: S16LE
                        rate: [ 1, 2147483647 ]
                        channels: [ 1, 2 ]
                audio/x-raw
                        format: U8
                        rate: [ 1, 2147483647 ]
                        channels: [ 1, 2 ]
        ```

        ```
        SRC template: 'src'
            Availability: Always
            Capabilities:
                video/x-raw
                        width: [ 1, 2147483647 ]
                        height: [ 1, 2147483647 ]
                        framerate: [ 0/1, 2147483647/1 ]
                        format: { I420, NV12, NV21, YV12, YUY2, Y42B, Y444, YUV9, YVU9, Y41B, Y800, Y8, GREY, Y16 , UYVY, YVYU, IYU1, v308, AYUV, A420 }
        ```

* *Negotiation*. The process where two linked Pads agree on a common type, and thus the Caps of the Pads become fixed
    * *Problem*. The actual information traveling from Pad to Pad must have only one well-specified type
    * *Requirements for success negotiation*. Two linked pads must share a common subset of caps

        $\to$ This is the main goal of Pad Caps

**Pad templates**. Pads are created from Pad templates, which indicate all possible Caps a Pad could ever have
* *Purpose*.
    * Useful for creating several similar Pads
    * Allow early refusal of connections between elements, i.e. if Caps of the Pads do not have a common subset

        $\to$ There is no need to negotiate further

### Caps structure
**Caps structure**. Caps are composed of an array of `GstStructure`, optionally plus a `GstCapsFeatures` set for `GstStructure`
* *Fixed caps*. Caps are fixed if they only contain a single structure, and this structure is fixed
    * *Fixed structure*. A structure with non of its fields is of an unfixed type, e.g. a range, list, or array
* *Structure order*. The structures are in the preferred order of the creator of the caps, with the preferred structure being first
* *Structure's components*.
    * *Name*. Specify the media type, e.g. `video/x-theora`
    * *Additional fields*. Add additional constraints, and / or information about the media type
        * *Example*. Frame size, the codec profile, etc.

        >**NOTE**. If a field is included in the caps returned by a pad via the CAPS query, it imposes an additional constraint during negotiation
        >$\to$ The caps in the end must have this field with a value that is a subset of the non-fixed value
    
    >**NOTE**. Information that can change for every buffer and is not relevant during negotiation must not be stored inside the caps

>**NOTE**. Only structures with the same name and equal caps features are considered compatible

**Caps features**. For each of the structures in caps, it is possible to store caps features
* *Caps features*. Express addition requirements for a specific structure
    * *Example*. Used to require a specific memory representation or a specific meta to be set on buffers
* *No-features caps*. If no caps features are provided for a structure
    
    $\to$ It is assumed that system memory is required, unless later negotiation steps (e.g. the ALLOCATION query) detect that something else can be used

### Caps operations
**Caps set operations**.
* *Subset*. Caps A is a subset of another caps B if, for each structure in A, there exists a structure in B, which is a superset of the structure in A
    * *Structure subset operation*. A structure A is a subset of a structure B if
        * A and B have the same structure name
        * A and B have the same caps features
        * Each field in B does not exist in A, or the value of the field in A is a subset of the value of the field in B
        * A must not have additional fields which are not in B
        * Fields in B but not in A, i.e. an empty field, are always a subset
    * *Special cases*.
        * EMPTY caps are a subset of every other caps
        * Every caps are a subset of ANY caps
* *Equal*. Caps A and B are equal if A is a subset of B and B is a subset of A
* *Intersection*. The intersection of caps A and caps B are the caps containing the intersection of all their structures with each other
    * *Empty intersection*. 
        * When A and B have different names or their caps features are not equal, or
        * When A and B contain the same field but the intersection of both field values is empty
    
    >**NOTE**. If one structure contains a field, which is not existing in the other structure
    >$\to$ It will be copied over to the intersection with the same value

* *Union*. The union of caps A and caps B are the caps containing the union of all their structures with each other
    * *Structure union operation*. 
        * If the structure names or caps features are not equal
            
            $\to$ Structure A union with structure B are two structures A and B 
        * If the structure names and caps features are equal

            $\to$ The union is the structure containing the union of each fields value
    
    >**NOTE**. If a field is only in one of the two structures, it is not contained in the union

* *Subtraction*. The subtraction of caps A from caps B is the most generic subset of B having an empty intersection with A, but only contains structures with names and caps features existing in B

**Fixating caps**. Caps which are constructed as following
1. Only the first structure is kept, as the order in which they appear is meant to express their precedence
2. Each unfixed field of the kept structure is set to the value making most sense for the media format by the element, or pad implementation
3. The remaining unfixed field is set to an arbitrary value, which is a subset of the unfixed field's values

**Compatibility of caps**. Pads can be linked when the caps of both pads are compatible
* *Explain*. When their intersection is not empty

### Related functions
**Functions**.
* `gst_pad_get_current_caps()`. Retrieve the Pad's current Caps, which can be fixed or not, depending on the state of the negotiation process
* `gst_pad_query_caps()`. Pad Caps can be non-existent, we then use this function to retrieve the currently acceptable Pad Caps
    * *Definition from documentation*. Gets the capabilities this pad can produce or consume
    * *Explain*. Returns all possible caps a pad can operate with, using the pad's CAPS query function
        
        >**NOTE**. If the query fails, this function will return filter , if not NULL, otherwise ANY

        >**NOTE**. The result returned by this function will be the Pad Template's Caps in the NULL state

### References
* https://gstreamer.freedesktop.org/documentation/tutorials/basic/media-formats-and-pad-capabilities.html?gi-language=c

## Caps negotiation
**Caps negotiation**. The act of finding a media format, i.e. GstCaps between elements which they can handle

**Caps negotiation basics**. The sink pads only suggest formats and the source pads need to decide

$\to$ The most complicated work is done in the source pads
* *Caps negotiation rules*. There are simply rules for the negotiation of the media format
    * A downstream element suggest a format on its sinkpad and places the suggestion in the result of the CAPS query performed on the sinkpad
    * An upstream element decides on a format and sends the selected media format downstream on its source pad with a CAPS event
        
        $\to$ Downstream elements reconfigure themselves to handle media type in the CAPS event on the sinkpad
    * A downstream element can inform unstream that it would like to suggest a new format, by sending a RECONFIGURE event upstream

        $\to$ The RECONFIGURE event simply instructs an upstream element to restart the negotiation phase

        >**NOTE**. Since the element sending out the RECONFIGURE event is suggesting another format
        >$\to$ The format in the pipeline might change
* *ACCEPT_CAPS query*. A quick to quickly check if a certain caps can be accepted by an element

### Push-mode caps negotiation
**Caps negotiation use cases for source pads**.
* *Fixed negotiation*. An element can output one format only
* *Transform negotiation*. There is a (fixed) transform between the input and output format of the element, usually based on some element property
    * *Produced caps*. The caps that the element will produce depend on the upstream caps
    * *Accepted caps*. The caps that the element can accept depend on the downstream caps
* *Dynamic negotiation*. An element can output many formats

**Fixed negotiation**. Source pad can only produce a fixed format, which is usually encoded inside the media

>**NOTE**. No downstream element can ask for a different format
>$\to$ The only way the source pad will renegotiate is when the element decides to change the caps itself

**Fixed negotiation elements**. Elements which are not renegotiable
* *Examples*.
    * *Type-finder*. A type found is part of the actual data stream and thus cannot be re-negotiated
    * *Almost all demuxers*. The contained elementary data streams are defined in the file headers, thus not renegotiable
    * *Some decoders*. When the format is embedded in the data stream, and not part of peercaps, and when the decoder itself is not reconfigurable
    * *Fixed-format sources*

>**NOTE**. These types of elements do not have a relation between the input format and the output format
>* *Explain*. Input caps simply do not contain the information required to produce the output caps

**Transform negotiation**. There is a fixed transform between the element input caps and the output caps, which can be parametrized by element properties but not the content of the stream
* *Caps event*. Transform negotiation can usually set caps on its source pad from the `_event()` function on the sink pad, when it received the CAPS event, i.e. event with type `GST_EVENT_CAPS`
    
    $\to$ The caps transform function transforms a fixed caps into another fixed caps
    * *Explain*.
        1. The sink pad received a CAPS event, whose content contains the information to produce the caps of the source pad
        2. A callback is used to produce and set the caps of the source pad 
* *Example*.
    * *Video box*. This adds configurable border around a video frame depending on the object properties
    * *Identity elements*. All elements which do not change the data format, only the content, e.g. video and audio effects
    * *Some decoders and encoders*. When the output format is defined by the input format, e.g. mulawdec and mulawenc

        >**NOTE**. These decoders usually have no headers defining the content of the stream

**Dynamic negotiation**. The most complex and powerful negotiation
* *Idea*. Convert fixed caps to unfixed caps

    $\to$ Both transform negotiation and dynamic negotiation transform fixed caps to other caps
    * *Consequence*. The source pad will have to choose a format from all the possibilities

        $\to$ The selection of format should also depend on the caps which can be accepted downstream
    * *Source format choice*. It would usually like to choose a format which requires the least amount of effort to produce, but it does not have to be
* *Typical flow*.
    1. Caps are received on the sink pad of the element
    2. If the element prefers to operate in passthrough mode, then check if downstream accepts the caps (with ACCEPT_CAPS query)

        $\to$ If it does, we can complete negotiation and we can operate in passthrough mode
    3. Calculate the possible caps for the source pad
    4. Query the downstream peer pad for the list of possible caps
    5. Select from the downstream list the first caps which we can transform to, and set this as the output caps

        >**NOTE**. We may have to fixate the caps to some reasonable defaults to construct fixed caps

* *Example*.
    * *Converter elements*. Such as `videoconverter`, `audioconverter`, `audioresample`, etc.
    * *Source elements*. Such as `audiotestsrc`, `videotestsrc`, `v4l2src`, etc.

**Upstream caps renegotiation**. 
* *Primary use*. Renegotiate part of an already-negotiated pipeline to a new format
    * *Example*. Select a different video size, since the size of the video window changed, and the video output is not capable of rescaling
* *Responsibilities of elements*.
    * *Elements proposing a new format upstream*. Need to 
        1. Check if the new caps are acceptable upstream with an `ACCEPT_CAPS` query
        2. Send a `RECONFIGURE` event and be prepared to answer the `CAPS` query with the new preferred format

        >**NOTE**. If there is no upstream element which want to renegotiate
        >$\to$ The element needs to deal with the currently configured format
    
    * *Elements operating in transform negotiation*. Pass the `RECONFIGURE` event upstream
        * *Explain*. These elements do fixed transforms based on the upstream caps

            $\to$ They need to send the event upstream so that it can select a new format
    * *Elements operating in fixed negotiation*. Drop the `RECONFIGURE` event, i.e. since they cannot reconfigure and their output do not depend on the upstream caps
    * *Elements which can be reconfigured on the source pad*. Check its `NEED_RECONFIGURE` flag and start renegotiation when the function returns `TRUE`

### References
* https://gstreamer.freedesktop.org/documentation/plugin-development/advanced/negotiation.html?gi-language=c

# Appendix
## Case studies
**Deep SORT for deepstream**
* *Changes to test2 sample code*.
    * Change config to
        * None-async classifier
        * Decrease input min width / height
    * Disable tracker (so that all objects are processed)
* *References*.
    * https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_plugin_gst-nvinfer.html
    * https://docs.nvidia.com/metropolis/deepstream/5.0DP/python-api/NvDsInfer/NvDsInferLayerInfoDoc.html
    * https://docs.nvidia.com/metropolis/deepstream/5.0DP/python-api/NvDsInfer/NvDsInferTensorMetaDoc.html
    * https://docs.nvidia.com/metropolis/deepstream/python-api/PYTHON_API/NvDsMeta/NvDsUserMeta.html
    * https://docs.nvidia.com/metropolis/deepstream/5.0DP/python-api/NvDsMeta/NvDsObjectMeta.html
    * https://docs.nvidia.com/metropolis/deepstream/5.0DP/python-api/Methods/methodsdoc.html#nvds-acquire-obj-meta-from-pool
    * https://docs.nvidia.com/metropolis/deepstream/python-api/PYTHON_API/NvDsMeta/NvDsFrameMeta.html
    * https://github.com/riotu-lab/deepstream-facenet/blob/master/deepstream_test_2.py
    * https://forums.developer.nvidia.com/t/facenet-with-deepstream-python-not-able-to-parse-output-tensor-meta/159139/14

## Concepts
**Ghost Pads**. Useful when organizing pipelines with GstBins like elements

<div style="text-align:center">
    <img src="https://i.imgur.com/RPfMNKu.png">
    <figcaption>Ghost sink pad at the beginning of the bin</figcaption>
</div>

* *Idea*. Create hierarchical element graphs, with each bin element containing a sub-graph

    $\to$ One would like to treat the bin-element like any other `GstElement`
* *Ghost pad*. A pad from some element in the bin, which can be accessed directly from the bin
    * *Purpose*. Act as a proxy for another pad, i.e. the bin can have sink and source ghost-pads associated with sink and source pads of the child elements
    * *Related functions*.
        * *`gst_ghost_pad_new`*. Get a ghost-pad if the target pad is known at creation time
        * *`gst_ghost_pad_new_no_target`*. Create a ghost-pad
        * *`gst_ghost_pad_set_target`*. Establish the association between ghost-pad and target pad after `gst_ghost_pad_new_no_target`
* *References*.
    * http://eisfuchs.info/eisfuchs/gstreamer/
    * https://gstreamer.freedesktop.org/documentation/application-development/basics/pads.html?gi-language=c#visualisation-of-a-gstbin-------element-with-a-ghost-pad