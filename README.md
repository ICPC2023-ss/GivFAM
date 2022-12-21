# GivFAM
Code grayscale image visualization for software defect prediction with fusion attention mechanism (GivFAM).

We proposed a novel GivFAM approach, which simultaneously considers code visualization comprehension and fusion attention mechanism to extract the code feature for software defect prediction.


Prepare for dataset
=================
- `Put the source code of the experiment project in folder ./data/archives. Available via github or other websites.`
- `Generate the code images corresponding to the java files. Please run makeTxt.py and codeVis.py sequentially.`
- `The path structure of the prepared data images is as follows:`

```
-data
  -archives
  -csvs
  -img
    - Project 1
      -file 1.png
      -file 2.png
      ...
    - Project 2
      -file 1.png
      -file 2.png
      ...
  -txt
```


Build running environment
=================
- `Install required packages.`

```
pip install -r requirements.txt
```

- `Install accimage (support Windows, Linux and macOS). Official link: https://github.com/pytorch/accimage`

```
$ conda install -c conda-forge accimage
```

Train and test
=================
- `To train and test, simply run train.py.`
```
python train.py
```

Config batch training
===============

- `Modify and execute the run.sh.`

```
sh run.sh
```

Check experimental result
===============
- `Please check the folder ./temp/result/.`


Supplementary note
===============
- `Our code is mainly extended from the code of the DTL-DP[1]. Related link:`

https://zenodo.org/record/3373409#.XV0Oy5Mza35.

[1]Chen J, Hu K, Yu Y, et al. Software visualization and deep transfer learning for effective software defect prediction[C]//Proceedings of the ACM/IEEE 42nd international conference on software engineering. 2020: 578-589.


Contacts
===============
- `Due to anonymity requested, we will publish contact details in the future.`
