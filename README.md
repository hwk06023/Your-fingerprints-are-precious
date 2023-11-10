# Save Your Biometric Information

## Project explanation
Because of Covid-19, our society changes to use more cameras through distance education, Video Conference or SNS.  <br/>
But resents high resolution cameras accidentally expose our important biometric information such as  fingerprints or iris. <br/>
Exposed fingerprints can easily be copied and can pass electric security. <br/>
So, we propose to manipulate biometric information automatically that enhance people’s biometric security.

<br/>

## Project process

### Step 1: Label iris and fingerprints
Label fingertip and iris from selfie dataset with instance segmentation format.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172348783619735622/image.png?ex=655ffde3&is=654d88e3&hm=2ae98e7db38c74925ac583cae21dd119d9a82200a6213d890a68aa78f2b31cc2&=&width=619&height=469">

### Step 2: Train Yolov8 Instance Segmentation
Train Yolov8 instance segmentation model with dataset we made at Step 1.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172354529510031360/image.png?ex=6560033d&is=654d8e3d&hm=6e2229a25d51d7ccfea00a6b28791a957cb8feb21d663ca7e44ad4c32ee00883&=&width=326&height=469">

### Step 3: Train Auto Encoder Model
Train Auto Encoder model with Identity Loss to make model reconstruct input image as same as they can. Nature of Auto Encoder architecture will destroy subtle feature like fingerprint.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172355102410014770/image.png?ex=656003c5&is=654d8ec5&hm=c6a0225a4352f53d8e831c73f6991faa582715a091f47e1850fb99909886277b&=&width=960&height=405">

## Result
We can check that fingerprint is efficiently destroyed without making discomfort to the human eye.
<img src="https://media.discordapp.net/attachments/363994928533078018/1172357267149033603/image.png?ex=656005c9&is=654d90c9&hm=8387022a3166744b25d73ff85e971a49259dd36c8f5ded9731294a2fd45865a6&=&width=960&height=294">
