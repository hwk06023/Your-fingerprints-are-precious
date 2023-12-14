# Save Your Biometric Information

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

### Step 3: Train Auto Encoder Model
Train Auto Encoder Architecture model with Identity Loss to make model reconstruct input image as same as they can. Nature of Auto Encoder architecture will destroy subtle feature like fingerprint.
<img src="img/3_read.png">

### Result (= Output image)
We can check that fingerprint is efficiently destroyed without making discomfort to the human eye.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172357267149033603/image.png?ex=656005c9&is=654d90c9&hm=8387022a3166744b25d73ff85e971a49259dd36c8f5ded9731294a2fd45865a6&=&width=960&height=294">

<br/><br/>

## Using Dataset

We used Microsoft's [ASL Citizen](https://www.microsoft.com/en-us/research/project/asl-citizen/dataset-description/) the first crowdsourced isolated sign language video dataset for training Yolov8n model. <br/>

<img src="img/annotated.png" width="500">

This Annotation task was automated by using [dlib.get_frontal_face_detector](get_IrisAnnotated.py)


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

### 2. Auto Encoder




<br/><br/>


## Total result

Result of our project

<br/>

**Add**

<br/><br/>



<br/><br/><br/><br/><br/>

***

#### Previous version

[Check previous version](Fingerprint.md)


