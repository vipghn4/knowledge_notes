---
title: MTMC performance evaluation
tags: Computer vision
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Performance measures](#performance-measures)
  * [Within-camera issues](#within-camera-issues)
  * [Handover issues](#handover-issues)
  * [The truth-to-result match](#the-truth-to-result-match)
<!-- /TOC -->

## Performance measures
### Within-camera issues
**Current event-based MTMC tracking performance measures**. Count mismatches bewteen ground-truth and system output through changes of identity over time  
* *Problem*. A truly-unique trajectory switching between two computed identities over $n$ frames can incur penalties
    * *Penalty range*. Anywhere between $1$, i.e. when there is exactly one switch, and $n-1$, i.e. in the extreme case of one identity switch per frame
    * *Consequence*. Inconsistencies if correct identities are crucial

**Idea to quantify the extent of mistakes**. Decide which of the two computed identities we should match with the true identity

$\to$ Once the choice is made, every frame, in which the true identity is assigned to wrong computed identity, is a frame in which the tracker is in error

>**NOTE**. The choice should be made for each tracker, under evaluation, e.g. for each tracker, we choose the output ID which matches the corresponding true ID for most frames, to ensure fair evaluation

* *Consequence*. The penalty is consistent, since it reflects precisely what the choice made maximizes the number of frame, over which the tracker is correct about who is there
* *Another point of view for the proposed solution*. The evaluation procedure starts with, for each given computed tracker's output trajectory, choosing the longest ground-truth trajectory as the correct match

### Handover issues
**Current event-based MTMC tracking performance measures**. Evaluate handover errors separately from within-camera errors
* *Idea*. Whether a mismatch is within-camera or handover depends on the identities associated to
    * The last frame, in which a trajectory in seen in one camera
    * The first frame, in which the trajectory is seen in the next camera
* *Consequence*. This proposition is not very good

**First proposed method**.
* *Idea*. Count the number of incorrectly matched frames (even across different cameras), ragardless of other consideration

    $\to$ If only one frame is wrong, the penalty is small
* *Example*. In the example below, the proposed measure charges a one-frame penalty in case (a) and a penalty nearly equal to the trajectory length in camera II in case (b)

    <div style="text-align:center">
        <img src="/media/n2wx6QP.png">
    </div>

* *Drawback*. The penalty for (b) in the example above is too large and unreasonable

### The truth-to-result match
**Fixing the first proposed method**. Measure performance not by "how often mismatches occur", but by "how long the tracker correctly identifies targets"

$\to$ Ground-truth identities are matched to computed identities
* *Truth-to-result matching*. A bipartie match associates one ground-truth trajectory to exactly one computed trajectory by minimizing the number of mismatched frames over all the available data
* *Performance measrues*. Standard measures, e.g. precision, recall, and F1 score are built on top of this truth-to-result match

    $\to$ These scores then measure the number of mismatched or unmatched detection-frames, regardless of where the discrepancies start or end, or which cameras are involved

**Graph definition**.
* *Assumptions*.
    * $G=(V_T, V_C, E)$ is a bipartie graph
    * $V_T$ is a vertex set having one "regular" node $\tau$ for each true trajectory, and one "false positive" node $f_\gamma^+$ for each computed trajectory $\gamma$
    * $V_C$ is a vertex set having one "regular" node $\gamma$ for each computed trajectory, and one "false negative" node $f_\tau^-$ for each true trajectory $\tau$
    * $E$ is a set of edges where
        * Two regular nodes are connected with an edge $e\in E$ if their trajectories overlap in time
        * Every regular node $\tau$ is connected to its corresponding $f_\tau^-$
        * Every regular node $\gamma$ is connected to its corresponding $f_\gamma^+$
        * Edge weight, i.e. cost on edge, $(\tau, \gamma)\in E$ tallies the number of FN and FP frames, which would be incurred if that match were chosen
* *Matching idea*.
    * A true trajectory, i.e. a regular node in $V_T$, can be matched with a computed trajectory, i.e. a regular node in $V_C$, or matched with nothing (meaning that the true trajectory is a false negative), i.e. $f_\tau^- \in V_C$
    * A computed trajectory, i.e. a regular node in $V_C$, can be matched with a true trajectory, i.e. a regular node in $V_T$, or matched with nothing (meaning that the computed trajectory is a false positive), i.e. $f_\tau^- \in V_C$
* *Miss definition*.
    * *Miss definition for two regular nodes $\tau,\gamma$*.
        * *Assumptions*.
            * $\tau(t)$ is the sequence of detections for true trajectory $\tau$, i.e. one detection for each frame $t$ in the set ${\cal{T}}_\tau$ over which $\tau$ extends
            * $\gamma(t)$ is the sequence of detections for computed trajectory $\gamma$, i.e. one detection for each frame $t$ in the set ${\cal{T}}_\gamma$ over which $\gamma$ extends
        * *Miss definition*. Two simultaneous detections $\tau(t)$ and $\gamma(t)$ are a miss if they do not overlap in space
            * *Formula*.

            $$m(\tau, \gamma, t, \Delta) = \begin{cases}
            1 & \text{mismatched}\\
            0 & \text{otherwise}
            \end{cases}$$

            * *Miss definition with spatial overlap measured in the image plane*. $m(\tau, \gamma, t, \Delta) = 1$ when

                $$\text{IOU}(\tau(t), \gamma(t)) < \Delta$$

                where $\Delta \in (0,1)$
            * *Miss definition with spatial overlap measured in the ground plane*. $m(\tau, \gamma, t, \Delta) = 1$ when the positions of $\tau(t)$ and $\gamma(t)$ are more than $\Delta = 1$ meter apart
    * *Miss definition for one regular node and one irregular node*. If either $\tau$ or $\gamma$ is an irregular node, i.e. $f_\tau^-$ or $f_\gamma^+$

        $\to$ Any detections in the other, i.e. the regular node, are misses
    * *Miss definition for two irregular nodes*. If $\tau$ and $\gamma$ are irregular, then $m$ is undefined
* *Edge cost definition*. Defined in terms of binary misses, i.e. so that a miss between regular positions has the same cost as a miss between a regular position and an irregular one

    >**NOTE**. Matching two irregular trajectories incurs zero cost since they are empty

    * *Edge cost*. $c(\tau,\gamma,\Delta) = \sum_{t\in {\cal{T}}_\tau} m(\tau, \gamma, t, \Delta) + \sum_{t\in {\cal{T}}_\gamma} m(\tau,\gamma,t,\Delta)$
    * *False negatives*. $\sum_{t\in {\cal{T}}_\tau} m(\tau, \gamma, t, \Delta)$
    * *False positives*. $\sum_{t\in {\cal{T}}_\gamma} m(\tau,\gamma,t,\Delta)$

**Graph matching solution**. A minimum-cost solution to this bipartite matching problem determines a one-to-one matching, which minimizes the cumulative FP and FN errors, and the overall cost is the number of mis-aligned detections for all types of errors
* *TP, FP, FN, and TN*.
    * Every $(\tau,\gamma)$ match is a TP ID (IDTP)
    * Every $(f_\gamma^+,\gamma)$ match is a FP ID (IDFP)
    * Every $(\tau,f_\tau^-)$ match is a FN ID (IDFN)
    * Every $(f_\gamma^+,f_\tau^-)$ match is a TN ID (IDTN)
* *Matched ground-truth trajectories*. $MT=\{\tau:(\tau,\gamma)\in \text{IDTP}\}$
* *Matched computed trajectories*. $MT=\{\gamma:(\tau,\gamma)\in \text{IDTP}\}$
* *Trajectory mapping functions*. The bipartite implies functions
    * *MT-to-MC*. $\gamma = \gamma_m(\tau)$
    * *MC-to-MT*. $\tau=\tau_m(\gamma)
