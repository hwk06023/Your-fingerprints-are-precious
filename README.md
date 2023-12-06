# Save Your Biometric Information

### Project explanation
The important of cameras in our society is increasing as the demand for Online Education, Video Conference, or SNS increases.  <br/>
But resents high resolution cameras accidentally expose our important biometric information such as  fingerprints or iris. <br/>
Exposed fingerprints can easily be copied and can pass electric security. <br/>
So, we propose to manipulate biometric information automatically that enhance people’s biometric security. <br/><br/><br/>

### Related paper & news
**Paper** <br/>
Real-Time Flying Object Detection with YOLOv8, 2023, Object Detection/Segmentation/Classification, Configurable for fast and simple architecture for localizing fingerprints and iris in pixel level. Unlike Hand keypoint approach, it demands lots of fingerprint and iris data to train model.

U-Net: Convolutional Networks for Biomedical Image Segmentation, 2015, Autoencoder, Can manipulate images' detailed information such as fingerprint without making discomfort of human vision. It doesn't conside



<br/>


### Our approach
We propose to manipulate biometric information automatically that enhance people’s biometric security. <br/>
We use Yolov8n Instance Segmentation model to detect iris and fingerprints. <br/>
And we use Auto Encoder model to destroy fingerprint and iris. <br/><br/><br/>

<br/>

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


 <br/>

<br/>

**Add**

<br/><br/>


## Experiment

How we performed experiments 

<br/>

**Add**

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


