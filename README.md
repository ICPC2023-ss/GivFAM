# GivFAM
Code grayscale image visualization for software defect prediction with fusion attention mechanism (GivFAM).

In this paper, we proposed a novel GivFAM approach, which
simultaneously considers code visualization comprehension
and fusion attention mechanism to extract the code feature. In
software visualization, we improve the code image generation
mechanism, avoiding the information loss caused by element
mixing and image cropping. In fusion attention learning,
we improve the deep neural network structure and feature
extraction method and introduce fusion attention learning
of spatial and channel attention weights. Defect prediction
is carried out with the GivFAM-based feature.

Prepare for dataset
=================
- ` Download Java files from PROMISE database.`
- ` Generate code images, run `makeTxt.py` and `codeVis.py`.`
- ` Data storage format should be like:`

```
-data
  -archives
  -csvs
  -img
    -Java project 1
      -file 1
      -file 2
      ...
    -Java project 2
      -file 1
      -file 2
      ...
  -txt
```

Build running environment (windows)
=================
- ` Install required packages.`

```
pip install -r requirements.txt
```

- ` Install accimage (support Windows, Linux and macOS).`
- ` Official installation link:`

https://github.com/pytorch/accimage

```
$ conda install -c conda-forge accimage
```

- ` If you have problems, solutions can be found in this link:`

https://blog.csdn.net/weixin_43856668/article/details/119146989

Train and test
=================
- ` To run and test network, simply run `train.py`.`
```
python train.py
```

Batch training
===============

- ` Modified the `run.sh`.`

```
sh run.sh
```

Experimental result
===============
- ` In the `./temp/result/`.`

Supplementary Note
===============

- ` Our code is mainly extended from the code of the DTL-DP[1] paper. Here is the link:`

https://zenodo.org/record/3373409#.XV0Oy5Mza35.


[1]Chen J, Hu K, Yu Y, et al. Software visualization and deep transfer learning for effective software defect prediction[C]//Proceedings of the ACM/IEEE 42nd international conference on software engineering. 2020: 578-589.

Contacts
===============
- ` If any issues, please feel free to contact us.`
