# 3D Building Classification & Segmentation Pipeline

### Background: 
Autonomous classification and segmentation of 3d objects using Deep Neural Networks (DNN) has become an extremely useful and effective technique leveraged within many fields including but not limited to the autonomous vehicle industry for roadway navigation, the robotics field for object interaction, and the medical field for 3d image analysis.  Though its accuracy, speed and clear benefits are well known, DNN based 3D object segmentation & classification methods have yet to be widely adopted within the Architecture, Engineering, & Construction (AEC) idustry.  However, as interest in AI continues to grow within the AEC industry, as indicated by increased investment and research in Con-Tech tools such real-time construction site tracking, autonomous robotic navigation of architectural environments, and DNN-based architectural generation & analysis methods, the ability to rapidly classify and segment buildings into their parts and pieces becomes increasingly important.  ****** SAY SOMETHING ABOUT CAPTURING STYLE & SITUATED CHARACTERISTICS ******

### Intro
This project provides a robust pipeline for the autonomous classification and segmentation of individual buildings extracted from large 3d urban models through the seamless combination of parametric modelling tools (Grasshopper), dataset preprocessing scripts, and DNN algorithms (PointNet).  

### Pipeline Overview
The pipeline presented here can be broken down into 3 main phases; the building extraction phase, the data pre-processing stage, and the model training stage.  - Within the first phase, large 3d urban models are broken down into thousands of individual buildings which can then be extracted and exported one-by-one as closed .obj files. Within this experiment, the city of Montreal 3d city model was used and approx. 50,000 buildings were exported as individual .obj files. These individual 3d buildings will be used to train the DNN PointNet model in the final step. 
