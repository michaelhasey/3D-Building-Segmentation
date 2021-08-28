
# Imports
from plyfile import PlyData, PlyElement
import os

# ******************************************************************************
# Select Typology and associated final folder to Convert
typology = 'row'
final_folder = '7654321'
# ******************************************************************************


# Input folder with .ply files to convert
directory = f'data/2_preprocessing_files/5_ply_color/{typology}'

# loop through all .ply files in input folder
for filename in os.listdir(directory):
    ply_file = PlyData.read(directory + '/' + filename)

# Create .pts file *************************************************************

    # create text docs to create ".pts"
    pts_file = f'data/3_final_data/{final_folder}/points/' + filename[:-4] + ".pts"
    # open new file and enable writing functionality
    with open(pts_file, 'w+') as writer:

        # iterate through ply file to extract vertexes
        for elem in ply_file['vertex']:

            # assign x value and shorten to 5 decimal points
            # to match ShapeNet Format
            if (str(elem[0]))[0] == '-':
                x = str(elem[0])[:8]
            else: 
                x = str(elem[0])[:7]
            # assign y value and shorten to 5 decimal points
            # to match ShapeNet Format
            if (str(elem[1]))[0] == '-':
                y = str(elem[1])[:8]
            else: 
                y = str(elem[1])[:7]
            # assign z value and shorten to 5 decimal points
            # to match ShapeNet Format
            if (str(elem[2]))[0] == '-':
                z = str(elem[2])[:8]
            else: 
                z = str(elem[2])[:7]

            # re-assemble new x,y,z values together and write to
            # new .pts file with each x,y,z coord on a seperate line
            coords = f'{x} {y} {z}'
            writer.write(coords + '\n')


# Create .seg file *************************************************************

    # create text docs to create ".seg" file = segmentation category of each 
    # point as categorized by point color
    seg_file = f'data/3_final_data/{final_folder}/points_label/' + filename[:-4] + ".seg"
    # open new file and enable writing functionality
    with open(seg_file, 'w+') as writer_2:

        # iterate through ply file to extract point color
        for elem in ply_file['vertex']:

            # if red
            if elem[3] == 255:
                color = 1

            # if green
            if elem[4] == 255:
                color = 2

            # if blue
            if elem[5] == 255:
                color = 3

            # if yellow
            if elem[3] == 255 and elem[4] == 255:
                color = 4

            # if pink
            if elem[3] == 255 and elem[5] == 255:
                color = 5

            # if light blue
            if elem[4] == 255 and elem[5] == 255:
                color = 6

            # if black
            if elem[3] == 0 and elem[4] == 0 and elem[5] == 0:
                color = 7

            # re-assemble new x,y,z values together and write to
            # new .pts file with each x,y,z coord on a seperate line
            color_final = f'{color}'
            writer_2.write(color_final + '\n')


print('.pts & .seg file creation complete!')