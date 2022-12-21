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

Prepare for dataset
=================
- ` Download Java files from PROMISE database.`

Build running environment (windows)
=================
- ` Install required packages.`
```
pip install -r requirements.txt
```
- ` Install accimage.`
- ` Official installation link：` https://github.com/pytorch/accimage
```
$ conda install -c conda-forge accimage
```
If you have problems, solutions can be found in this link：https://blog.csdn.net/weixin_43856668/article/details/119146989

Train and test
=================

**2. install accimage (support Windows, Linux and MacOS). 
```
python train.py
```
Batch training
===============
```
sh run.sh
```
