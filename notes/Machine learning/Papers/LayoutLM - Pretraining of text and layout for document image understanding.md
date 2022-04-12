<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [LayoutLM - Pretraining of text and layout for document image understanding](#layoutlm---pretraining-of-text-and-layout-for-document-image-understanding)
  - [LayoutLM](#layoutlm)
    - [Model architecture](#model-architecture)
    - [Pretraining LayoutLM](#pretraining-layoutlm)
- [Appendix](#appendix)
<!-- /TOC -->

# LayoutLM - Pretraining of text and layout for document image understanding
**Business document understanding**. A very challenging task due to the diversity of layouts and formats, poor quality of scanned document images, and the complexity of template structures

**Existing approaches**. Recent approaches exploit manual efforts, which are time-consuming and expensive, meanwhile requiring manual customization or configuration
* *Overview*. Contemporary approaches for document AI are usually built upon deep neural networks from a computer vision perspective or a natural language processing perspective, or a combination of them
    * *Early works*. Usually focused on detecting and analyzing certain parts of a document, e.g. tabular areas
        
        $\to$ After that, researchers also leveraged more advanced Faster R-CNN model or Mask R-CNN model to improve the accuracy of document layout analysis
    * *Semantic structure extraction*. Researchers presented an end-to-end, multimodal, fully convolutional network for extracting semantic structures from document images, taking advantage of text embeddings from pre-trained NLP models
    * *Graph convolutional networks (GCN) for multimodal information extraction*. More recently, GCN-based models are used to combine textual and visual information for information extraction from business documents
* *Drawbacks*.
    * They rely on a few human-labeled training samples without fully exploring the possibility of using large-scale unlabeled training samples
    * They usually leverage either pre-trained CV models or NLP models, without a joint training of textual and layout information

**LayoutLM**. 

<div style="text-align:center">
    <img src="https://miro.medium.com/max/1400/1*brX2FM9hCSn-jHc7t0k-jg.png">
    <figcaption>LayoutLM architecture</figcaption>
</div>

* *Input embeddings*. Inspired by the BERT model, where input textual information is mainly represented by text embeddings and position embeddings

    $\to$ LayoutLM adds two types of input embeddings
    * A 2-D position embedding denoting the relative position of a token within a document
        
        $\to$ This can capture the relationship among tokens within a document
    * An image embedding for scanned token images within a document
        
        $\to$ This can capture some appearance features, e.g. font directions, types, and colors
* *Pretraining tasks*. We adopt a multi-task learning objective for LayoutLM, i.e. 

    $\to$ This enforces joint pre-training for text and layout
    * Masked Visual-Language Model (MVLM) loss
    * Multi-label Document Classification (MDC) loss

## LayoutLM
**Visual information incorporation**. We propose to utilize the visually rich information from document layouts and align them with the input texts
* *Types of visual features*.
    * *Document layout information*. Relative positions of words contribute a lot to the semantic representation
        
        $\to$ We can embed these relative positions information as 2-D position representation
    * *Visual information*. Visual information is a significantly important feature in document representations
        * *Explain*. Documents contain some visual signals to show the importance and priority of document segments
        * *Document-level visual features*. The whole image can indicate the document layout, i.e. an essential feature for document image classification
        * *Word-level visual features*. Styles are also significant hints for the sequence labeling tasks

### Model architecture
**Brief**. We use the BERT architecture as the backbone and add two new input embeddings, i.e. a 2-D position embedding and an image embedding
* *2-D position embedding*. Aim to model the relative spatial position in a document
    * *Idea*. The bounding box can be precisely defined by $(x_0, y_0, x_1, y_1)$, i.e. `LTRB` format

        $\to$ We can embed $x_0, y_0, x_1, y_1$ by four embedding vectors from two embedding tables
    * *Explain*. We look up the position embedding of $x_0$ and $x_1$ in the embedding table $X$, and look up $y_0$ and $y_1$ in table $Y$
    * *Implementation*. Use two `nn.Embedding()` modules to encode $x, y$ coordinates
* *Image embedding*. To utilize the image feature of a document and align the image feature with the text
    * *Idea*. With the bounding box of each word from OCR results, we split the image into several pieces, and they have a one-to-one correspondence with the words
        
        $\to$ We generate the image region features with these pieces of images from the Faster R-CNN model as the token image embeddings
    * *Image embedding for the `[CLS]` token*. Use the Faster R-CNN model to produce embeddings using the whole scanned document image as the ROI

### Pretraining LayoutLM
**Masked visual-language model**. Proposed to learn the language representation with the clues of 2-D position embeddings and text embeddings
* *Idea*. Randomly mask some of the input tokens while keeping the corresponding 2-D position embeddings
    
    $\to$ The model is trained to predict the masked tokens given the contexts
    * *Consequence*. The model not only understands the language contexts but also utilizes the corresponding 2-D position information

        $\to$ This bridges the gap between the visual and language modalities

**Multi-label document classification**. Many tasks require the model to generate highquality document-level representations

$\to$ We use a Multi-label Document Classification (MDC) loss during the pre-training phase
* *Needs for MDC loss*. Since the MDC loss needs the label for each document image, which may not exist for larger datasets
    
    $\to$ It is optional during the pre-training and may not be used for pre-training larger models in the future

# Appendix
**Paper information**.
* *Authors*. Microsoft research Asia
* *Year of publication*. 2019