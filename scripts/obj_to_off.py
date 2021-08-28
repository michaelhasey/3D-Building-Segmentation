# OBJ to OFF

# Overcview: A simple script to convert 3d objects from .obj to .off format
# 
# .obj - A geometry definition file format first developed by Wavefront 
#        Technologies for its Advanced Visualizer animation package.
# .off - A geometry definition file format containing the description of the 
#        composing polygons of a geometric object.

# dependancies (install if required)
#pip3 install pymeshlab
#pip3 install tk

# imports
import pymeshlab
import os

from tkinter import Tk
from tkinter.filedialog import askdirectory

# Set Pymeshlab's meshset function.  This helps to load and save files.
ms = pymeshlab.MeshSet()

from time import sleep
from tqdm import tqdm

# ******************************************************************************
# select building typology you wish to convert
typology = 'mansard'


# set input/output folders
input_folder = f'data/2_preprocessing_files/2_obj_user_selected'
output_folder = f'data/2_preprocessing_files/3_off'

# use following to auto request folder locations if necesssary
#input_folder = askdirectory(title='Select Folder') 
#output_folder = askdirectory(title='Select Folder')

# Create progress counter
curr_file = 0
total_files = 0

# Main Script
# iterate through files in "input_folder"
# os.remove(input_folder + '/' + ".DS_Store")

for folder in os.listdir(input_folder):

    if folder == ".DS_Store":
        continue
    else:

        counter = 0

        for obj_file in os.listdir(input_folder + '/' + folder):
            
            counter += 1
            total_files += 1

            try:
                # only load obj files
                if obj_file.endswith(".obj"):
                    # load new mesh per pymeshlab function "ms"
                    ms.load_new_mesh(input_folder + '/' + folder + '/' + f'{obj_file}')
                    # remove ".obj" off of original filename
                    obj_file_short = obj_file[:-4]
                    # save file as .off format in "output_folder"
                    ms.save_current_mesh(output_folder + '/' + folder + '/' + f'{folder}_{counter}.off', 
                    save_vertex_color = False, save_vertex_coord = False,
                    save_face_color = False)
                    # increase curr file by one to track file count
                    curr_file += 1
                    # print progress
                    print(f'{curr_file}' + ' / ' + f'{total_files}')

            # skips any errors caused by bad geometry - bad geometry is not saved
            except Exception:
                pass

print('.obj to .off conversion complete !')