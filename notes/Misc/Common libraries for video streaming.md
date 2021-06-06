---
title: Common libraries for video streaming
tags: Misc
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Introduction](#introduction)
  * [GStreamer](#gstreamer)
<!-- /TOC -->

# Introduction
## GStreamer
**GStream basic code flow**.
1. Create elements and pipeline
2. Add elements to pipeline and link them together
3. Set elements' attributes
4. Start playing the stream
5. Wait until error or EOS
6. Parse and display error message
7. Free resource
