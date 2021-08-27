# 3D Building Classification & Segmentation Pipeline


## Overview

### Background: 
Autonomous classification and segmentation of 3d objects using Deep Neural Networks (DNN) has become an extremely useful and effective technique leveraged within many fields including but not limited to the autonomous vehicle industry for roadway navigation, the robotics field for object interaction, and the medical field for 3d image analysis.  Though its accuracy, speed and clear benefits are well known, DNN based 3D object segmentation & classification methods have yet to be widely adopted within the Architecture, Engineering, & Construction (AEC) idustry.  However, as interest in AI continues to grow within the AEC industry as indicated by increased investment and research in Con-Tech tools such real-time construction site tracking, autonomous robotic navigation of architectural environments, and DNN-based architectural generation & analysis methods, the ability to rapidly classify and segment buildings into their parts and pieces becomes increasingly important.  ****** SAY SOMETHING ABOUT CAPTURING STYLE & SITUATED CHARACTERISTICS ******

### Intro
This project provides a robust pipeline for the autonomous classification and segmentation of individual buildings extracted from large 3d urban models through the seamless combination of parametric modelling tools (Grasshopper), dataset preprocessing scripts, and DNN algorithms (PointNet).  

### Pipeline Description
The pipeline presented here can be broken down into 3 main stages; the building extraction stage, the dataset pre-processing and creation stage, and the model training stage.  

1. Within the first stage, large 3d urban models are broken down into thousands of individual buildings which can then be extracted and exported one-by-one as closed .obj files. In this experiment, the city of Montreal 3d city model was used and approx. 50,000 buildings were exported as individual .obj files. After further pre-processing, a portion of these 3d buildings (as chosen by the user) will be used as the training data to train the DNN PointNet model in step 3.

2. Within the second stage, individual .obj building files chosen for training are pre-processed to match the input-data requirements of the PointNet model.  Requirements include size normalization, conversion into a 2048 point point-cloud, and pre-segmentation.  After these requirements are achieved via custom scripts, individual building models are then split into two file formats: a .pts model which is a list of coordinates (x,y,z) of all of its 2048 points, and a .seg file which contains the segementation category that corresponds to each individual point (ex. the segmentation category "1" representing "roof" which corresponds to the first point).  These two files represent the final data format to be used to train the model. In addition, train-test-evaluate JSON files are created via a custom script in order to break up the dataset into its corresponding categories as well as various .txt files required for training.  After completion of the previously mentioned steps, the training dataset is ready to be used.

3. Within the final stage, two PyTorch-based PointNet models are trained on the previously created dataset; one for 3d object classification and one for 3d object part-segmentation. Both of these models are based on the [original PointNet paper](https://arxiv.org/abs/1612.00593) and were sourced from [fxia22's PointNet Implimentation repo](https://github.com/fxia22/pointnet.pytorch) with slight modifications made to accomodate custom building data.  After training, these models can then be used to predict the class and part segmentation category for new unseen 3d building data.


## Process

### Step 1
