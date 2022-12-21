# GivFAM
Code grayscale image visualization for software defect prediction with fusion attention mechanism (GivFAM).

In this paper, we proposed a novel GivFAM approach, which
simultaneously considers code visualization comprehension
and fusion attention mechanism to extract the code feature. In
software visualization, we improve the code image generation
mechanism, avoiding the information loss caused by element
mixing and image cropping. In fusion attention learning,
we improve the deep neural network structure and feature
extraction method and introduce a fusion attention learning
of spatial and channel attention weights. Defect prediction
is carried out with the GivFAM-based feature.

Build running environment
=================

**1. Prepare for dateset. 

**2. install accimage (support Windows, Linux and MacOS). 

pip insatll acc-image

**3. Train and test

python train.py

**4. Batch training

sh run.sh
