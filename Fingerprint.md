
### Step 1: crop fingertip

1. Get hand key-points with Mediapipe

<img src="./img/1.png" width="500px" height="300px"> <br/>

2. bring distal phalanges from hand key-points to get fingerprints

<img src="./img/2.png" width="300px" height="300px"> <br/>

3. extend the fingertip position to the end of the finger.

<img src="./img/3.png" width="300px" height="300px"> <br/>

4. Get end of the finger and distal phalanges vector to calculate orthogonal vectors, and get coordinate of the box.

<img src="./img/4.png" width="300px" height="300px"> 

<br/><br/>


### Step 2: Label cropped fingertip
<img src="./img/5.png" width="600px" height="200px"> 

<br/><br/>


### Step 3: Train efficientNet for predicting whether fingerprint is exposed or not

<img src="./img/6.png" width="500px" height="300px">


<br/><br/>

### Step 4 : Train Auto-Encoder with U-net architecture to manipulate fingerprint


<img src="./img/7.png" width="500px" height="300px">


<br/><br/>

### Step 5 : Annotate fingerprint and training segmentation model

<img src="./img/8.png" width="500px" height="250px">

After apply those models appropriately, the result is below.

<img src="./img/9.png" width="500px" height="800px">

<br/> <br/>

## Result

#### Before
<img src="./img/10.png" width="500px" height="700px">

<br/>

#### After
<img src="./img/12.png" width="500px" height="700px">


