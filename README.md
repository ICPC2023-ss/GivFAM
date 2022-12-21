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
absl-py==1.3.0
cachetools==5.2.0
certifi
charset-normalizer==2.1.1
colorama==0.4.6
contourpy==1.0.5
cycler==0.11.0
et-xmlfile==1.1.0
fonttools==4.37.3
google-auth==2.14.1
google-auth-oauthlib==0.4.6
grpcio==1.50.0
idna==3.4
importlib-metadata==5.0.0
joblib==1.2.0
kiwisolver==1.4.4
Markdown==3.4.1
MarkupSafe==2.1.1
matplotlib==3.6.0
numpy==1.23.3
oauthlib==3.2.2
opencv-python==4.6.0.66
openpyxl==3.0.10
packaging==21.3
pandas==1.5.0
Pillow==9.2.0
protobuf==3.20.3
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2022.2.1
requests==2.28.1
requests-oauthlib==1.3.1
rsa==4.9
scikit-learn==1.1.2
scipy==1.9.1
six==1.16.0
tensorboard==2.11.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
threadpoolctl==3.1.0
torch-1.8.1
torchvision-0.9.1
tqdm==4.64.1
typing_extensions==4.3.0
urllib3==1.26.12
Werkzeug==2.2.2
wincertstore==0.2
xlrd==1.2.0
xlwt==1.3.0
zipp==3.10.0

Prepare for dataset
=================

Train and test
=================

**2. install accimage (support Windows, Linux and MacOS). 

pip insatll acc-image

python train.py

Batch training
===============

sh run.sh
