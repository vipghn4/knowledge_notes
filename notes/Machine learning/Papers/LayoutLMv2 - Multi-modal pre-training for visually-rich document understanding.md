<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [LayoutLMv2: Multi-modal pre-training for visually-rich document understanding](#layoutlmv2-multi-modal-pre-training-for-visually-rich-document-understanding)
  - [Approach](#approach)
    - [Model architecture](#model-architecture)
    - [Pretraining tasks](#pretraining-tasks)
- [Appendix](#appendix)
<!-- /TOC -->

# LayoutLMv2: Multi-modal pre-training for visually-rich document understanding
**Recent approaches to visually-rich document understanding (VrDU)**.
* *Option 1*. Use a shallow fusion between textual and visual / layout / style information
    * *Idea*. These approaches leverage the pre-trained NLP and CV models individually

        $\to$ These models are combined for supervised learning
    * *Drawback*. The domain knowledge of one document type cannot be easily transferred into another
        
        $\to$ These models often need to be re-trained once the document type is changed
        * *Consequence*. The local invariance in general document layout, i.e. key-value pairs in a left-right layout, tables in a grid layout, etc., cannot be fully exploited
* *Option 2*. Use a deep fusion among textual, visual, and layout information from a great number of unlabeled documents in different domains
    
    $\to$ Pre-training techniques play an important role in learning the cross-modality interaction in an end-to-end fashion
    * *Consequence*. 
        * The pre-trained models absorb cross-modal knowledge from different document types, where the local invariance among these layouts and styles is preserved. 
        * When the model needs to be transferred into another domain with different document formats
            
            $\to$ Only a few labeled samples would be sufficient to fine-tune the generic model to achieve state-of-the-art accuracy

**LayoutLMv2**.
* *Visual information incorporation*. Different from the vanilla LayoutLM model where visual embeddings are combined in the fine-tuning stage
    
    $\to$ We integrate the visual information in the pre-training stage in LayoutLMv2 by taking advantage of the Transformer architecture to learn the cross-modality interaction between visual and textual information
* *2D relative position representation*. Inspired by the 1-D relative position representations, we propose the spatial-aware self-attention mechanism for LayoutLMv2, involving a 2-D relative position representation for token pairs
    * *Benefits*. The relative position embeddings explicitly provide a broader view for the contextual spatial modeling
* *Pretraining tasks*. We use two new training objectives for LayoutLMv2 in addition to the masked visual-language modeling
    * *Text-image alignment*. Align the text lines and the corresponding image regions
    * *Text-image matching*. The model learns whether the document image and textual content are correlated

## Approach
### Model architecture
**Text embedding**. We use WordPiece (Wu et al., 2016) to tokenize the OCR text sequence and assign each token to a certain segment $s_i ∈ {[A], [B]}$
* *Special tokens*.
    * *`[CLS]` token*. Added at the beginning of the sequence
    * *`[SEP]` token*. Added at the end of each text segment
    * *Extra `[PAD]` tokens*. Appended to the end so that the final sequence’s length is exactly the maximum sequence length $L$
* *Final text embedding*. The sum of three embeddings
    * Token embedding represents the token itself
    * 1D positional embedding represents the token index
    * Segment embedding is used to distinguish different text segments
* *Formulation*. The $i$-th text embedding is given as

    $$\mathbf{t}_i=\text{TokEmb}(w_i) + \text{PosEmb1D}(i) + \text{SegEmb}(s_i)$$

**Visual embedding**. Although all information we need is contained in the page image

$\to$ The model has difficulty capturing detailed features in a single information-rich representation of the entire page
* *CNN visual encoder*. We leverage the output feature map of a CNN-based visual encoder, which converts the page image to a fixed-length sequence
    1. Given a document page image $I$, it is resized to $224 \times 224$ then fed into the visual backbone
    2. The output feature map is average-pooled to a fixed size with the width $W$ and height $H$
    3. The output feature map is flattened into a visual embedding sequence $\text{VisTokEmb}(I)$ of length $W \times H$
    4. A linear projection layer is applied to each visual token embedding to unify the dimensionality with the text embeddings
* *1D positional embedding*. Since the CNN-based visual backbone cannot capture the positional information
    
    $\to$ We add a 1D positional embedding to these visual token embeddings
    
    >**NOTE**. The 1D positional embedding is shared with the text embedding layer

* *Segment embedding*. We attach all visual tokens to the visual segment
* *Formulation*. The $i$-th visual embedding can be given as

    $$\mathbf{v}_i=\text{Proj}(\text{VisTokEmb}(I)_i) + \text{PosEmb1D}(i) + \text{SegEmb}(\text{[C]})$$

**Layout embedding**. Embed the spatial layout information represented by axis-aligned token bounding boxes from the OCR results
* *Box normalization*. Following the vanilla LayoutLM
    
    $\to$ We normalize and discretize all coordinates to integers $i$ the range $[0, 1000]$
* *Box embedding*. We use two embedding layers to embed $x$-axis features and $y$-axis features separately
* *Token-level 2D positional embedding (layout embedding)*.
    * *Assumption*.
        * The normalized bounding box of the $i$-th, where $0 \leq i < W H + L$, text/visual token is

            $$\text{box}_i = (x_\min, x_\max, y_\min, y_\max, \text{width}, \text{height})$$

    * *Layout embedding*. Concatenate six bounding box features to construct a token-level 2D positional embedding

        $$\mathbf{l}_i = \text{Concat}(\text{PosEmb2Dx}(x_\min, x_\max, \text{width}), \text{PosEmb2Dy}(y_\min, y_\max, \text{height}))$$

* *Visual tokens as evenly divided grids*. Since CNNs perform local transformation
    
    $\to$ The visual token embeddings can be mapped back to image regions one by one with neither overlap nor omission
    * *Consequence*. When calculating bounding boxes, the visual tokens can be treated as evenly divided grids
    
    >**NOTE**. An empty bounding box `boxPAD = (0, 0, 0, 0, 0, 0)` is attached to special tokens `[CLS]`, `[SEP]` and `[PAD]`

**Multimodal encoder with spatial-aware self-attention mechanism**.

<div style="text-align:center">
    <img src="https://i.imgur.com/NHn02qj.png">
    <figcaption>LayoutLMv2 architecture</figcaption>
</div>

* *Encoder inputs*. The encoder concatenates visual embeddings $\{\mathbf{v}_0,\dots,\mathbf{v}_{WH-1}\}$ and text embeddings $\{\mathbf{t}_0,\dots,\mathbf{t}_{L-1}\}$ to a unified sequence

    $\to$ It then fuses spatial information by adding the layout embedding to get the $i$-th, where $0\leq i<WH+L$, first layer input

    $$\mathbf{x}_i^{(0)}=X_i+l_i,\quad X=\{\mathbf{v}_0,\dots,\mathbf{v}_{WH-1},\mathbf{t}_0,\dots,\mathbf{t}_{L-1}\}$$

* *Encoder architecture*. A stack of multihead self-attention layers followed by a feed forward network
    * *Drawback*. The original selfattention mechanism can only implicitly capture the relationship between the input tokens with the absolute position hints
        
        $\to$ To efficiently model local invariance in the document layout, it is necessary to insert relative position information explicitly
    * *Modification*. Introduce the spatial-aware self-attention mechanism into the self-attention layers

        >**NOTE**. For simplicity, we describe a single head in a single self-attention layer with hidden size of $d_\text{head}$ and projection matrics $W_Q$, $W_K$, $W_V$

        * *Original self-attention mechanism*. Capture the correlation between query $\mathbf{x}_i$ and key $\mathbf{x}_j$ by projecting the two vectors and calculating the attention score

            $$\alpha_{ij}=\frac{1}{\sqrt{d_\text{head}}} (\mathbf{x}_i\mathbf{W}^Q) (\mathbf{x}_j \mathbf{W}^K)^T$$
        
        * *Inclusion o semantic relative position and spatial relative position*. Considering the large range of positions, these are modelled as bias terms to prevent adding too many parameters
            * *Assumptions*.
                * $\mathbf{b}^{(1D)},\mathbf{b}^{(2D_x)}, \mathbf{b}^{(2D_y)}$ are the learnable 1D and 2D relative position biases

                    $\to$ These are different among attention heads, but shared in all encoder layers
                * $(x_i,y_i)$ anchors the top-left corner of the $i$-th bounding box
            * *Spatial-aware attention score*.

                $$\alpha_{ij}'=\alpha_{ij} + \mathbf{b}_{j-i}^{(1D)} + \mathbf{b}_{x_j-x_i}^{(2D_x)} + \mathbf{b}_{y_j-y_i}^{(2D_y)}$$
            
* *Output vector representation*. The weighted average of all the projected value vectors w.r.t normalized spatial-aware attention scores

    $$\mathbf{h}_i=\sum_j \frac{\exp(\alpha'_{ij})}{\sum_k \exp(\alpha'_{ik})} \mathbf{x}_j\mathbf{W}^V$$

### Pretraining tasks
**Masked visual-language modeling**. Similar to the vanilla LayoutLM, i.e. to make the model learn better in the language side with the crossmodality clues
* *Idea*. Randomly mask some text tokens and ask the model to recover the masked tokens
    
    $\to$ The layout information remains unchanged, i.e. the model knows each masked token’s location on the page
* *Inference*. Output representations of masked tokens from the encoder are fed into a classifier over the whole vocabulary, driven by a cross-entropy loss
* *Visual clue avoidance*.  Image regions corresponding to masked tokens are masked on the raw page image input before feeding it into the visual encoder

**Text-image alignment**. Help the model learn the spatial location correspondence between image and coordinates of bounding boxes
* *Idea*. Some tokens lines are randomly selected, and their image regions are covered on the document image
* *Training*. A classification layer is built above the encoder outputs to predict a label for each text token depending on whether it is covered, and computes the binary cross-entropy loss
* *Line-level covering*. Considering the input image’s resolution is limited, and some document elements like signs and bars in a figure may look like covered text regions
    
    $\to$ The task of finding a word-sized covered image region can be noisy
    * *Consequence*. The covering operation is performed at the line-level
* *TIA in combination with MVLM*. When MVLM and TIA are performed simultaneously, TIA losses of the tokens masked in MVLM are not taken into account
    
    $\to$ This prevents the model from learning the useless but straightforward correspondence from `[MASK]` to `[Covered]`

**Text-image matching**. Help the model learn the correspondence between document image and textual content
* *Idea*. We feed the output representation at `[CLS]` into a classifier to predict whether the image and text are from the same document page
    * *Training data*. 
        * *Positive samples*. Regular inputs
        * *Negative samples*. An image is either replaced by a page image from another document or dropped
* *Cheating prevention*. We perform the same masking and covering operations to images in negative samples
    
    $\to$ The TIA target labels are all set to `[Covered]` in negative samples
* *Objective function*. Bbinary cross-entropy loss

# Appendix
**Paper information**.
* *Authors*. Microsoft research Asia
* *Year of publication*. 2020