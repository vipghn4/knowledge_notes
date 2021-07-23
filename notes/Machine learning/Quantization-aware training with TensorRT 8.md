# Achieving FP32 accuracy for INT8 inference with quantization aware training with TensorRT
## Quantization methods
**Simple quantization method**: $x_q = \text{clip}(\text{round}(x_f / \text{scale}))$
* *Drawback*.
    * Large dynamic range means more values are represented by lower precision and larger rounding error
    * Smaller dynamic range reduces rounding error but introduce a clipping error
* *Solutions*. Post-training quantization (PTQ) and quantization-aware training (QAT)

**Post-training quantization**. Performed after a high-precision model has been trained
* *Idea*.
    * *Weight quantization*. Access the weight tensors and can measure their distributions
    * *Activation quantization*. Quantizing the activation is more challenging since the activation distributions must be measured using real input data
* *Solution to activation quantization*. Use a small dataset representative of the task's real input data
    
    $\to$ Statistics about the interlayer activation distributions are collected
    * *Calibration dataset*. The representative dataset
* *Pros and cons*.
    * *Pros*. Simple and does not involve the training pipeline
    * *Cons*. Not able to achieve acceptable task accuracy

**Quantization-aware training**. Include the quantization error from PTQ in the training phase to enable the network to adapt to the quantized weights and activations
* *Idea*. 
    1. Start with an pretrained model
    2. Change the training regiment to include the quantization error in the training loss
        * *Explain*. Insert fake-quantization operations into the training graph to simulate quantization of data and parameters
    3. After the QAT is done, the fake-quantization layers hold the quantization scales which we use to quantize the weights and activations of model
* *Fake quantization operations*. Quantize the data then immediately dequantize the data so the operation's compute remains in floating-point decision
    * *Forward pass*. Fake-quantize the floating-point weights and activations, then use these weights and activations to perform the layer's operation
    * *Backward pass*. Use the weights' gradients to update the floating-point weights
        * *Quantization gradient*. Zero almost everywhere except for points where it is undefined
        * *Solution*. Use straight-through estimator (STE), which passes the gradient as-is through the fake-quantization operator
            * *Explain*. Ignore the fake-quantization operator during back propagation

>**NOTE**. Experiments show that QAT and roughly achieve the same accuracy as FP32 models

## Quantization with TensorRT
**Processing modes with INT8 models in TensorRT 8.0**. According to [this](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#tensorrt-process-qdq)
* *Full TensorRT PTQ mode*. Use the TensorRT tensor dynamic-range API and also uses INT8 precision compute and data opportunistically to optimize inference latency
* *External scales mode*. Used when processing floating-point ONNX networks with `QuantizeLayer` and `DequantizeLayer` layers to use external scales

**TensorRT quantization toolkit for PyTorch**. Compliment TensorRT by providing a convenient PyTorch library to help produce optimizable QAT models

$\to$ This toolkit provides an API to automatically or manually prepare a model for QAT and PTQ