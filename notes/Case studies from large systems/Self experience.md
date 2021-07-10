**Custom ONNX graph then export to TRT**.
* *Notes*.
    * Customized op name in ONNX graph should match one of the customized TensorRT plugin
    * There are tons of implemented TRT plugins in `TensorRT` repository
* *Consequence*. The model conversion workflow is `torch` to `onnx` to`tensorrt`
    
    $\to$ We can optimize, i.e. reduce the model graph, our model at any of these step
    * *Optimization strategies*.
        * *Local optimization*. Optimize model in PyTorch, then in ONNX, then in TensorRT individually
        * *Global optimization*. Optimize model in PyTorch with attention to ONNX and TRT, then optimize ONNX with attention to TRT, then optimize TRT
* *References*.
    * https://github.com/NVIDIA/TensorRT/tree/master/plugin
    * ~/Downloads/TensorRT-7.1.3.4/samples/python/onnx_packnet

**Engine refitting**. We can refit TRT engines without having to rebuild it

**Custom preprocessing with Deepstream**.
* *Option 1*. Modify `nvinfer` source code
    * *Pros*. Exploit GPU buffers to speed up preprocessing
    * *Cons*. All TRT engines have to have the same preprocessing?
    * *Reference*. https://forums.developer.nvidia.com/t/how-to-integrate-custom-data-preprocessing-before-infering-with-tensorrt-in-deepstream/122809/3
* *Option 2*. Use a customized `GstPlugin`
    * *Pros*. Custom preprocessing for each model in the pipeline
    * *Cons*. How to use GPU buffer instead of CPU buffers?
    * *Reference*. https://forums.developer.nvidia.com/t/image-preprocessing-before-nvinfer/147734
* *Option 3*. Use GstPad probe
    * *Pros*. Easy to implement
    * *Cons*. The same as option 2
* *Option 4*. Implement preprocessing steps using TensorRT custom plugin
    * *Pros*. Take time to implement
    * *Cons*. Most flexible option

**Key notes**.
* Setting `output-tensor-meta=1` does not prevent Deepstream from running bounding box and classification parsing functions