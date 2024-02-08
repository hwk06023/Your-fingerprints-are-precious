# Your Fingerprints are precious

### Project explanation
The important of cameras in our society is increasing as the demand for Online Education, Video Conference, or SNS increases.  <br/>
But resents high resolution cameras accidentally expose our important biometric information such as  fingerprints or iris. <br/>
Exposed fingerprints can easily be copied and can pass electric security. <br/>
So, we propose to manipulate biometric information automatically that enhance people’s biometric security. <br/><br/><br/>

### Related paper & news
**Paper** <br/>
[Real-Time Flying Object Detection with YOLOv8](https://arxiv.org/abs/2305.09972), 2023, Object Detection/Segmentation/Classification, Configurable for fast and simple architecture for localizing fingerprints and iris in pixel level. Unlike Hand keypoint approach, it demands lots of fingerprint and iris data to train model.

[U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597), 2015, Autoencoder, Can manipulate images' detailed information such as fingerprint without making discomfort of human vision. It doesn't conside

[고해상도로 찍은 이미지에서의 손가락 지문 채취 방지에 관한 연구](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE09409018), 2020, 



**News** <br/>
[Chaos Computer Clubs breaks iris recognition system](https://www.ccc.de/en/updates/2017/iriden) <br/>
[Scientists Extract Fingerprints from Photos Taken From up to Three Meters Away](https://www.bleepingcomputer.com/news/security/scientists-extract-fingerprints-from-photos-taken-from-up-to-three-meters-away/#google_vignette)




<br/><br/>

## Proposed model

### Step 1: Labeling & Annotating iris and fingerprints
Labeling & Annotating fingertip and iris from selfie dataset with instance segmentation format.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172348783619735622/image.png?ex=655ffde3&is=654d88e3&hm=2ae98e7db38c74925ac583cae21dd119d9a82200a6213d890a68aa78f2b31cc2&=&width=619&height=469">

### Step 2: Train Yolov8n Instance Segmentation
Train Yolov8 nano model instance segmentation model with dataset we made at Step 1.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172354529510031360/image.png?ex=6560033d&is=654d8e3d&hm=6e2229a25d51d7ccfea00a6b28791a957cb8feb21d663ca7e44ad4c32ee00883&=&width=326&height=469">

### Step 3: Train Reconstruction Model
Train Auto Encoder & U-Net Architecture model with Identity Loss to make model reconstruct input image as same as they can. Nature of Auto Encoder architecture will destroy subtle feature like fingerprint.
<img src="img/3_read.png">

### Result (= Output image)
We can check that fingerprint is efficiently destroyed without making discomfort to the human eye.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172357267149033603/image.png?ex=656005c9&is=654d90c9&hm=8387022a3166744b25d73ff85e971a49259dd36c8f5ded9731294a2fd45865a6&=&width=960&height=294">

<br/><br/>

## Using Dataset

We used Microsoft's [ASL Citizen](https://www.microsoft.com/en-us/research/project/asl-citizen/dataset-description/) the first crowdsourced isolated sign language video dataset for training Yolov8n model. <br/>

<img src="img/annotated1.png" width="500"> <br/>
<img src="img/annotated2.png" width="500">

This Annotation task was automated by using [dlib.get_frontal_face_detector](get_IrisAnnotated.py) <br/>

<img src="img/hagrid1.png" width="200"> 
<img src="img/hagrid2.png" width="180"> <br/>


Additional, We used [hagrid dataset(FHD)](https://github.com/hukenovs/hagrid) and Roboflow's dataset  for training for reconstruct(U-net ..) model. <br/>


<br/>


## Experiment

How we performed experiments 

### 1. Yolov8n Instance Segmentation

|Class|Images|Instances|Box( P| R| mAP50|mAP50-95 )|
|:---:|---:|---:|---:|---:|---:|---:|
|all|217|666|0.831|0.725|0.82|0.456|
|-|217|422|0.856|0.988|0.988|0.581|
|-|217|244|0.806|0.461|0.653|0.331|

<br/>

Speed : 0.9ms preprocesse, 5.5ms inference, 0.0ms loss, 3.0ms postprocess (per image)

<br/>

### 2. Reconstruction

#### - Speed

| AutoEncoder (Vanilla) | AutoEncoder (Conv) | U-Net |
|---:|---:|:---:|
| 0.0014s | 0.0036s | 0.05s |

#### - Output

| Original | AutoEncoder (Vanilla) | AutoEncoder (Conv) | U-Net |
|---:|---:|---:|--:|
|<img src="img/original.png" width="200"> | <img src="img/aev.png" width="200"> | <img src="img/aefc.png" width="200"> | <img src="img/unet.png" width="200"> |

<br/>

Due to the nature of skip-connection in U-net, performance is very good for reconstruction
However, compared to other Auto Encoders, the experimental results show a drop in the speed area, 
which will be very important when applied to real life such as real-time.
We test various U-net models currently available and propose a U-Net structure-based reconstruction model 
that performs the purpose of modulation with less damage. <br/>

In order to further reduce the number of parameters, pruning was performed to remove the weight of the network based on the normalized value of the weight, but pruning was not performed because there was a problem that could create a sense of incompatibility in the picture where the color tone of the result value changed. <br/>

<img src="img/Result_Unets.png" width=600>

#### - Speed (with cuda)

| U-Net3p | U-Net | U-Net_light |
|---:|---:|---:|
| 0.013s | 0.0066s | **0.0031s** |

FPS = 1000 // 0.0031 = 322


#### - Summary

**U-Net** <br/>
<img src="img/U-Net_Summary.png" width=300> <br/>

**U-Net_light (Our suggestion)** <br/>
<img src="img/light_Summary.png" width=300> <br/>

#### - Result

The parameter kernel layer has been drastically reduced. <br/>

This task reliably improves the inference speed. <br/>

This is because the features that can be expressed within the fingerprint itself are limited anyway. 
And because Reconstruction itself is not a task with a clear answer, 
Performance indicators are more unclear than they are used for segmentation purposes,
These tasks were possible because only the purpose (modulation with less damage) was achieved. <br/>

<img src="img/Total_Unets.png" width=600>

<br/>

### 3. Enhancement

When Segmentation is incomplete, Since there is no guarantee that the autoencoder will always be the same color as the original image, apply a Gaussian filter to the mask to ensure the color lasts naturally.

<img src='img/GaussianFilter.png' width=600>

<br/><br/>


## Total result

### Fingerprints (part of the original image)

**Before -> After**

<img src='img/result1.png' width=400>
<img src='img/result2.png' width=400>
<img src='img/result3.png' width=400>

### Original Image

<img src='img/resultall.png' width=400>



<br/><br/><br/><br/><br/>

***

#### Previous version

[Check previous version](Fingerprint.md)


