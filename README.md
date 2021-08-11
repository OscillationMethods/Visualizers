# OscMethods: Animated Visualizers

This is the source repository for animated visualizations for the [OscillationMethods](https://onlinelibrary.wiley.com/doi/10.1111/ejn.15361) project.

## Overview

This repository includes the code used to create the animated visualization, as well as copies of the final output. Each visualization is created by a dedicated notebook. Note that the code in this repository creates all the images needed for the gifs, but that the gifs need to be stitched together, which is currently done with an external service.

This collection of animated visualizers, with descriptions, is also available on the 
[project website](https://oscillationmethods.github.io/), 
on 
[vizualizations page](https://oscillationmethods.github.io/docs/viz.html).

Note that each of the visualizations is an animated version of one of the figures from the 
[paper](https://onlinelibrary.wiley.com/doi/10.1111/ejn.15361).
The original code that these animations are based on is available in the 
[project repository](https://github.com/OscillationMethods/OscillationMethods).

## ReUse

Copies of the animated visualizations are avaialble in the `gifs` folder.
If you wish to re-use these animations, you are free to do so under a Creative Commons 
[CC-BY-NC](https://creativecommons.org/licenses/by-nc/4.0/) 
license, meaning all non-commercial purposes are fine. 

If you re-use these animations, please cite the associated project paper. 

Citation:

    Donoghue T, Schaworonkow N, & Voytek B. Methodological considerations for
    studying neural oscillations. European Journal of Neuroscience. DOI: 10.1111/ejn.15361

Direct Link: https://onlinelibrary.wiley.com/doi/10.1111/ejn.15361

The code is this repository is under an 
[MIT License](https://github.com/OscillationMethods/Visualizers/blob/main/LICENSE), 
meaning if you wish use and adapt this code for creating your own visualizations, you may do so. 

## Visualizations

This repository creates the following visualizations:

#### #0 - Oscillations Introduction

An introductory visualization showing oscillations, with the time series, filtered trace, and power spectrum:

![fig0](/gifs/fig0.gif)

#### #1 - Oscillation Presence

A visualization showing illustory oscillations, whereby filtered aperiodic activity can look rhythmic:

![fig1](/gifs/fig1.gif)

#### #2 - Center Frequency

A visualization showing how variable center frequency can impact measures:

![fig2](/gifs/fig2.gif)

#### #3 - Aperiodic Activity

A visualization showing how dynamic aperiodic activity can impact measures:

![fig3](/gifs/fig3.gif)

#### #4 - Temporal Variability

A visualization showing how temporal variability (burstiness) can impact measures:

![fig4](/gifs/fig4.gif)

#### #5 - Waveform Shape

A visualization showing how waveform shape can impact measures:

![fig5](/gifs/fig5.gif)

#### #6 - Overlapping Sources

A visualization showing how overlapping sources can lead to different results at a recording electrode:

![fig6](/gifs/fig6.gif)

#### #7 - Signal-to-noise ratio

A visualization showing how variable signal-to-noise ratio can impact measures:

![fig7](/gifs/fig7.gif)
