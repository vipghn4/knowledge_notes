<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [BERT - Pretraining of deep bidirectional transformers for language understanding](#bert---pretraining-of-deep-bidirectional-transformers-for-language-understanding)
  - [Related works](#related-works)
    - [Unsupervised feature-based approaches](#unsupervised-feature-based-approaches)
    - [Unsupervised fine-tuning approaches](#unsupervised-fine-tuning-approaches)
  - [WordPiece tokenization](#wordpiece-tokenization)
  - [BERT](#bert)
    - [Pre-training BERT](#pre-training-bert)
      - [Masked LM](#masked-lm)
      - [Next sentence prediction (NSP)](#next-sentence-prediction-nsp)
  - [Fine-tuning BERT](#fine-tuning-bert)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# BERT - Pretraining of deep bidirectional transformers for language understanding
**Existing strategies for applying pre-trained language representations to downstream tasks**.
* *Feature-based approach*. Use task-specific architectures including the pre-trained representations as additional features
    * *Example*. ELMo
* *Fine-tuning approach*. Introduces minimal task-specific parameters, and is trained on the downstream tasks by simply fine-tuning all pretrained parameters
    * *Example*. GPT
* *Common point*. The two approaches share the same objective function during pre-training, i.e. use unidirectional language models to learn general language representations
    * *Drawback*. This restricts the power of the pre-trained representations, especially for the fine-tuning approaches
        * *Explain*. Standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training
        * *Example*. In OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer
        * *Consequence*. 
            * The restrictions are sub-optimal for sentence-level tasks
            * The restrictions could be very harmful when applying finetuning based approaches to token-level tasks, e.g. question answering, where it is crucial to incorporate context from both directions

**Proposed method**.
* Use a “masked language model” (MLM) pre-training objective, inspired by the Cloze task
    * *Idea*. Randomly mask some tokens from the input, and try to predict the original vocabulary ID of the masked token based on its context
    * *Benefits*. Enable the representation to fuse the left and the right context

        $\to$ This allows us to pretrain a deep bidirectional Transformer
* Use a “next sentence prediction” task that jointly pretrains text-pair representations

## Related works
### Unsupervised feature-based approaches
**Word embedding learning**. Learning widely applicable representations of words has been an active area of research for decades

$\to$ Pre-trained word embeddings are an integral part of modern NLP systems, offering significant improvements over embeddings learned from scratch (Turian et al., 2010)
* *Categories of methods*. Non-neural (Brown et al., 1992; Ando and Zhang, 2005; Blitzer et al., 2006) and neural (Mikolov et al., 2013; Pennington et al.)

**Unidirectional word embeddings**.
* *Pretraining word embedding vectors*. Use left-to-right language modeling objectives (Mnih and Hinton, 2009), and objectives to discriminate correct from incorrect words in left and right context (Mikolov et al., 2013)
* *Variations*. These approaches have been generalized to coarser granularities, e.g. sentence embeddings or paragraph embeddings
    * *Sentence representation learning*. The model is trained by 
        * Use objectives to rank candidate next sentences
        * Left-to-right generation of next sentence words given a representation of the previous sentence
        * Denoising autoencoder derived objectives

**Bidirectional word embeddings**. 
* *ELMo*. ELMo and its predecessor generalize traditional word embedding research along a different dimension
    * *Idea*. Extract context-sensitive features from a left-to-right and a right-to-left language model
        
        $\to$ The contextual representation of each token is the concatenation of the left-to-right and right-to-left representations
    * *Results*. ELMo advances the state of the art for several major NLP benchmarks
* *Melamud et al. (2016)*. Propose learning contextual representations through a task to predict a single word from both left and right context using LSTMs
    
    $\to$ Similar to ELMo, their model is feature-based and not deeply bidirectional
* *Fedus et al. (2018)*. Show that the cloze task can be used to improve the robustness of text generation models

### Unsupervised fine-tuning approaches
**Recent approaches**.
* The first works in this direction only pre-trained word embedding parameters from unlabeled text
* In recent works, sentence or document encoders, which produce contextual token representations, have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task

**Advantages**. Only few parameters need to be learned from scratch

**Training strategy**. Left-to-right language modeling and auto-encoder objectives have been used for pre-training such models

## WordPiece tokenization
**Subword-based tokenization**. A solution between word and character-based tokenization
* *Problem of interest*. Solve the issues faced by 
    * Word-based tokenization, i.e. very large vocabulary size, large number of OOV tokens, and different meaning of very similar words
    * Character-based tokenization, i.e. very long sequences and less meaningful individual tokens
* *Idea*. Split the rare words into smaller meaningful subwords
    * *Example*. "boy" is not split but "boys" is split into "boy" and "s"
        
        $\to$ The model can learn that the word “boys” is formed using "boy" with slightly different meanings but the same root word
* *WordPiece*. Used in language models like BERT, DistilBERT, Electra. 
    * *Implementations*.
        * *Bottom-up approach*. Based on BPE
        * *Top-down approach*. Used in BERT

**Byte-pair encoding (BPE)**. A simple form of data compression algorithm
* *Idea*. The most common pair of consecutive bytes of data is replaced with a byte not in the data

    $\to$ The process repeats until there is no byte pairs appearing more than once
* *Example*.

    $$aaabdaaabac\to ZabdZabac\to ZYdZYac\to XdXac$$

    where $Z=aa,Y=ab,X=ZY$
* *Essential idea applied to NLP*. The most common words are represented in the vocabulary as a single token, while the rare words are broken down into two or more subword tokens
    
    $\to$ This is in agreement with what a subword-based tokenization algorithm does
* *Application of BPE to NLP*. Consider a corpus of words, each of which has its frequency counted
    1. Add a special token `</w>`, i.e. word boundary, at the end of each word

        $\to$ This helps the algorithm to look through each character and find the highest frequency character pairing
    2. Split each word into characters and count their occurrences
    3. Look for the most frequent pairing, and merge them

        $\to$ Add the newly created token to the vocabulary and calculate its frequency
        * *Token merging*. Allow representing the corpus with the least number of tokens, i.e. the main goal of BPE algorithm
    4. Repeat again until reaching token limit size or iteration limit
* *Encoding and decoding*.
    * *Decoding*. Concatenate all tokens together to get the whole word
    * *Encoding*. 
        1. Iterate through all tokens in our corpus, from longest to shortest

            $\to$ We then try to replace substrings in our given sequence of words using these tokens
        2. Replace substrings left with unknown tokens
* *Drawback*. A word can be encoded in more than one way

    $\to$ The algorithm cannot choose subword tokens, since there is no prioritize which one to use first
    * *Consequence*. The accuracy of the learned representations

**WordPiece tokenization**.
* *Idea*. Take into account the impact which merging of a particular byte-pair has at each step
    * *Difference from BPE*. The way in which symbol pairs are added to the vocabulary
* *Iterative step*. At each step, WordPiece chooses a symbol pair, which will result in the largest increase in likelihood upon merging, i.e.

    $$\max_{(x,y)} \frac{p([x;y])}{p(x)p(y)}$$

    where $[x;y]$ means the concatenation of $x$ and $y$
    * *Interpretation*. WordPiece evaluates what it will lose by merging two symbols

        $\to$ This is to ensure that the step is actually worth it or not
* *Procedure*.
    1. Initialize the word unit inventory with the base characters
    2. Build a language model on the training data using the word inventory from step 1
    3. Generate a new word unit by combining two units out of the current word inventory

        $\to$ The word unit inventory will be incremented by 1 after adding this new word unit
        * *Choosing word unit*. The new word unit is chosen from all the possible ones to increase the likelihood of the training data the most when added to the model
    4. Repeat until reaching the token limit size of the likelihood falls below a threshold
* *Computational complexity*. $O(K^2)$ where $K$ is the number of current word units

## BERT
**Pre-training and fine-tuning**. A distinctive feature of BERT is its unified architecture across different tasks

$\to$ There is minimal difference between the pre-trained architecture and the final downstream architecture
* *Pre-training*. The model is trained on unlabeled data over different pre-training tasks
* *Finetuning*. The model is first initialized with the pre-trained parameters, and all of the parameters are fine-tuned using labeled data from the downstream tasks
    * *Downstream task*. Each task has separate fine-tuned models, even though they are initialized with the same pre-trained parameters

**Model architecture**. A multi-layer bidirectional Transformer encoder based on the original implementation of Transformer

<div style="text-align:center">
    <img src="https://miro.medium.com/max/764/1*bYO5tEcRzdHtjHV_P6-4ig.png">
    <figcaption>BERT architecture</figcaption>
</div>

* *Model sizes*. `BERTBASE (L=12, H=768, A=12, Total Parameters=110M)` and `BERTLARGE (L=24, H=1024, A=16, Total Parameters=340M)`
    * $L$ is the number of layers, i.e. Transformer blocks
    * $H$ is the hidden size
    * $A$ is the number of self-attention heads

>**NOTE**. `BERTBASE` was chosen to have the same model size as OpenAI GPT for comparison purposes

* *Bidirectional self-attention*. BERT Transformer uses bidirectional self-attention, while the GPT Transformer uses constrained self-attention where every token can only attend to context to its left

**Input-output representation**. To make BERT handle a variety of down-stream tasks

$\to$ The input representation is able to unambiguously represent both a single sentence and a pair of sentences in one token sequence
* *Definition of sentence*. An arbitrary span of contiguous text, rather than an actual linguistic sentence
    
    $\to$ A “sequence” refers to the input token sequence to BERT, which may be a single sentence or two sentences packed together
* *WordPiece embeddings*. We use WordPiece embeddings with a 30,000 token vocabulary
    * *First token of every sequence*. Always a special classification token `[CLS]`
* *Output representation*. The final hidden state corresponding to this token is used as the aggregate sequence representation for classification tasks
* *Sentence pair representation*. Sentence pairs are packed together into a single sequence
    * *Sentence differentiation*.
        1. Separate two sentences with a special token ([SEP])
        2. Add a learned embedding to every token indicating whether it belongs to sentence `A` or sentence `B`
*Input token representation*. For a given token, its input representation is constructed by summing the corresponding token, segment, and position embeddings

### Pre-training BERT
#### Masked LM
**Brief**. Intuitively, it is reasonable to believe that a deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-toright and a right-to-left model
* *Unidirectional pretraining*. Standard conditional language models can only be trained left-to-right or right-to-left
    * *Explain*. 
        * Bidirectional conditioning would allow each word to indirectly see itself
        * The model could trivially predict the target word in a multi-layered context

**Bidirectional pretraining**. To train a deep bidirectional representation, we mask some percentage of the input tokens at random, and then predict those masked tokens,i.e. “masked LM” (MLM)
* *Model architecture for pretraining*. The final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM
* *Experiment settings*. We mask 15% of all WordPiece tokens in each sequence at random

>**NOTE**. In contrast to denoising auto-encoders (Vincent et al., 2008), we only predict the masked words rather than reconstructing the entire input

* *Drawback*. We are creating a mismatch between pre-training and fine-tuning
    * *Explain*. The `[MASK]` token does not appear during fine-tuning
* *Improvement*. We do not always replace “masked” words with the actual `[MASK]` token, i.e.
    1. The training data generator chooses 15% of the token positions at random for prediction
    2. If the i-th token is chosen, we replace the i-th token with
        * The [MASK] token 80% of the time, or
        * A random token 10% of the time, or 
        * The unchanged $i$-th token 10% of the time

#### Next sentence prediction (NSP)
**Brief**. Many important downstream tasks such as Question Answering (QA) and Natural Language Inference (NLI) are based on understanding the relationship between two sentences, which is not directly captured by language modeling

$\to$ We need to train a model that understands sentence relationships
* *Solution*. Pre-train for a binarized next sentence prediction task, which can be trivially generated from any monolingual corpus

**Task modeling**. When choosing the sentences `A` and `B` for each pretraining example

$\to$ 50% of the time B is the actual next sentence that follows `A`, and 50% of the time it is a random sentence from the corpus
* *Model's task*. Predict if the second sentence in the pair is the subsequent sentence in the original document

## Fine-tuning BERT
**Finetuning with single text and text pairs**. Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream tasks, i.e. whether they involve single text or text pairs, by swapping out the appropriate inputs and outputs
* *Finetuning with text pairs*. Encode a concatenated text pair with self-attention to effectively include bidirectional cross attention between two sentences

**Computational complexity**. Compared to pre-training, fine-tuning is relatively inexpensive

# Appendix
**Paper information**.
* *Authors*. Google AI Language
* *Year of publication*. 2018

## Concepts
**Cloze test**. An exercise, test, or assessment consisting of a portion of language with certain items, words, or signs removed

$\to$ The participant is asked to replace the missing language item