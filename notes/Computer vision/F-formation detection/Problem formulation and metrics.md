# F-formation detection - Individuating free-standing conversational groups in images
## Introduction
### Problem definition
**Motivation**. After years of research on automated analysis of individuals

$\to$ The computer vision community has transferred its attention to modeling gatherings of people, commonly referred as groups
* *Group*. A group ca be broadly understood as a social unit comprising several members stnading in status and relationships with one another
    * *Types of groups*. Depend on dimension, i.e. small groups or crowds, durability, i.e. ephemeral, ad hoc, or stable groups, in/formality of organization, degree of "sense of belonging", level of physical dispersion, etc.
    * *Type of groups of interest*. Free-standing conversational groups (FCGs), or small ensembles of co-present persons engaged in ad hoc focused encounters
* *Applications*. Crtucial for modern automated monitoring and profiling strategies

**Analysis of groups in history**. occurred in video surveillance and meeting analysis, e.g. classroom behavior
* *Video surveillance*.
    * *Definition of group*. Two or more people of similar veolicty, spatially and temporally close to one another

        $\to$ This simplified definition arises from the difficulty of inferring persistent social structure from short video clips
* *Meeting analysis*. People usually sit around a table and remain near a fixed location for most of the time, predominantly interacting through speech and gesture

    $\to$ Activities can be finely monitored using a variety of audiovisual features

**Focused interaction**. Occur when people openly cooperate to sustain a single focus of attention

$\to$ This broad definition covers other collaborative situated systems of activity which entil a more or less static spatial and proxemic organization, e.g. a meeting, playing a board or sport game, having dinner, free conversation, etc.
* *Other definitions*.
    * *From Oxford reference*. The coordinating of face-to-face interaction by two or more actors
    * *By Erving Goffman*. 
    
        >When two persons are mutually present and hence engaged together in some degree of **unfocused interaction**, the mutual proffering of civil inattention-a significant form of unfocused interaction-is not the only way they can relate to one another. They can proceed from there to engage one another in **focused interaction**, the unit of which I shall refer to as a face engagement or an encounter. **Face engagements** comprise all those instances of two or more participants in a situation joining each other openly in maintaining a single focus of cognitive and visual attention-what is sensed as a single mutual activity, entailing preferential communication rights
* *FCGs as a form of focused encounters*. FCGs are another example of focused encounters, which emerge during many and diverse social occasions, e.g. a party, a social dinner, a coffee break, etc.

    $\to$ More generally, when people spontaneously decide to be in each other's immediate presence to interact with one another
    * *Consequence*. FCGs are fundamental social entities, whose automated analysis may bring to a novel level of activity and behavior analysis

**FCGs**. In a FCG, people communicate to the other participants, among, and above all, the rest, what they think they are doing together, what they regard as the activity at hand

$\to$ They do so not only by talking, but also by exploiting non-verbal modalities of expression, i.e. social signals, among which positional and orientational forms play a crucial role
* *Spatial position and orientation of people*. Define one of the most important proxemic notions, which describe an FCG

**F-formation**. Termed by Adam Kendon's *Facing formation* to indicate spatial position and orientation of people
* *Explain*. In Kendon's terms, an F-formation is a socio-spatial formation, in which people have established and maintain a convex space, i.e. o-space, to which everybody in the gathering has direct, easy, and equal access
* *Typical form of o-space*. Circle, ellipse, horsehoe, side-by-side, or L-shape
    * *Explain*. These forms of o-space allow easy and preferential access between people while excluding distractions of the outside word
* *F-formation in computer vision*. In computer vision, spatial position and orientational information can be automatically extracted

    $\to$ These pave the way to the computational modeling of F-formation, and consequentially of the FCGs 

**Arrangements of F-formations**. F-formations can be organized in different arrangements, i.e. spatial and orientational layout
* *vis-a-vis arrangement*. Usually for F-formation of two individuals, where two participants stand and face one another directly

    $\to$ This is preferred for competitive interactions
* *L-arrangement*. When two people lie in a right angle to each other

    $\to$ This is preferred for cooperative interactions
* *Side-by-side arrangement*. People stand close together, both facing the same way

    $\to$ This occurs when people stand at the edges of a setting against walls
* *Circular arrangements*. Hold when F-formations are composed by more than two people
* *Other arrangements*. Linear, semicircular, or rectangular shapes

### Related works
**Bazzani et al**. The first work on F-formation in 2013, which proposed the use of positional and orientational information to capture steady conversational groups (SCGs)
* *Reference*. Bazzani L, Cristani M, Tosato D, Farenzena M, Paggetti G, Menegaz G, et al. Social interactions by visual focus of attention in a three-dimensional environment. Expert Systems. 2013 May;30(2):115–127.

**Cristani et al**. Designed a sampling technique to seek F-formations centres by performing a greedy maximization in Hough voting space
* *Reference*.  Cristani M, Bazzani L, Paggetti G, Fossati A, Tosato D, Del Bue A, et al. Social interaction discovery by statistical analysis of F-formations. In: British Machine Vision Conference (BMVC); 2011. p. 23.1–23.12.

**Hung and Krose**. Detected F-formations by finding distinct maximal cliques in weighted graphs via graph-theoretic clustering
* *Reference*.  Hung H, Kröse B. Detecting F-formations as Dominant Sets. In: International Conference on Multimodal Interfaces (ICMI); 2011. p. 231–238.

**Setti et al**. Proposed a multi-scale extension of the Hough-based approach, i.e. explicitly model F-formations of different cardinalities
* *Reference*.  Setti F, Lanz O, Ferrario R, Murino V, Cristani M. Multi-scale F-formation discovery for group detection. In: IEEE International Conference on Image Processing (ICIP); 2013.

**Tran et al**. Followed the graph-based approach of Hung and Krose, extending it to deal with video-sequences and recognizing five kinds of activities

**Francesco Setti et al**. Detect an arbitrary number of F-formations on a single images, using a monocular camera, by considering as input the position of people on the ground floor and their orientation, captured as the head and/or body pose
* *Idea*. An iterative approach starting by assuming an arbitrarily high number of F-formations, then use a hill-climbing optimization to alternate between assigning individuals to F-formations using the efficient graph-cut -based optimization
* *Reference*. F-Formation Detection: Individuating Free-Standing Conversational Groups in Images

### Evaluation metrics
**Correctly estimated groups**. 
* *Assumptions*.
    * $G$ is a ground-truth group
    * $T \in [0,1]$ is some tolerance threshold
* *Correctly estimated groups*. A groupd is correctly estimated if 
    * At least $\lceil T \cdot |G| \rceil$ of their members are found by the grouping method and correctly detected by the tracker, and
    * No more than $1 - \lceil T\cdot |G|\rceil$ false subjects of the detected tracks are identified

**Precision and recall**.
* *TP, TN, FP, and FN*.
    * *TP*. Indicate correctly detected groups
    * *FN*. Indicate the miss-detected groups
    * *FP*. Indicate the hallucinated groups
* *Precision, recall, and F1 score*. Formulated based on the definitions above

**Global tolerant matching score (mF1 score)**. The area under the curve (AUC) in the F1-against-T graph with T varying from 1/2 to 1
* *Explain*. We do not use $T \in [0,1/2)$ since, in this range, we are accepting as good those groups where more than the half of the subjects is missing or false positive

    $\to$ This results in useless estimates

# Appendix
## Concepts
**Proxemic**. Related to proxemics
* *Proxemics*. The study of human use of space and the effects which population density has on behavior, communication, and social interaction

**Civil inattention**. The process whereby strangers who are in close proximity demonstrate that they are aware of one another, without imposing on each other

$\to$ This is a recognition of claims of others to a public space, and of their own personal boundaries
* *Other definitions*.
    * *From IGI global*. The ways in which people maintain a comfortable social order in public spaces by explicitly disattending to one another and their actions
    * *From thoughtco*. 
        * Civil attention involves giving others a sense of privacy when they are in public
        * We engage in civil attention to be polite and to show others that we are not a threat to them
        * When people do not provide us with civil inattention in public, we may become annoyed or distressed

**o-space, p-space, and r-space**.

<div style="text-align:center">
    <img src="https://i.imgur.com/klZTOI1.png">
    <figcaption>o-space, p-space, and r-space</figcaption>
</div>

* *o-space*. A convex empty space surrounded by the people invovled in a social interaction, where every participant is oriented inward into it, and no external people are allowed to lie
    * *Determination of o-space*. The o-space is determined by the overlap of transactional segments
        * *Transactional segment*. The area in front of the body, which can be reached easily, and where hearing and sight are most effective

            >**NOTE**. In practice, in a F-formation, the transactional segment of a person coincides with the o-space
* *p-space*. The belt of space enveloping the o-space, where only the bodies of the F-formation participants are placed
* *r-space*. The space enveloping o-space and p-space, and is also monitored by the F-formation participants

# References
* https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0123783