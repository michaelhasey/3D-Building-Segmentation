
# Create train/test/validation JSON arrays that splits up lists the
# names of files in dataset into train/test/valid categories

# Split as follows:  Train = 70%, Test = 20%, Valid = 10%

# Step 1: create normal python lists for train/test/valid
# Step 2: convert python lists into JSON array

# Imports
import os
import json

# ******************************************************************************
# Select Typology and associated final folder to Convert
typology = 'row'
final_folder = '7654321'
# ******************************************************************************


# Create empty train/test/val lists
list_train = []
list_test = []
list_val = []

input_folder = 'data/3_final_data'

for folder_num in os.listdir(input_folder):

    if folder_num == "train_test_split":
        continue

    if folder_num == "synsetoffset2category.txt":
        continue

    if folder_num == ".DS_Store":
        continue

    else:

        # Input folder containing all final .pts files
        directory = f'data/3_final_data/{folder_num}/points'
        category = directory[-14:-7] 

        # determine number of files
        num_files = len(os.listdir(directory))

        # determine where to make breaks to start new list
        test_start = int(num_files * 0.7)
        val_start = int(num_files * 0.9)

        # Track count to determine how many files have been processed
        count = 0

        # loop through all .pts files in input folder
        for filename in os.listdir(directory):

            if filename == ".DS_Store":
                continue
            
            else:
                count += 1
                filename_short = filename[:-4]

                # create file name to append to lists
                new_filename = f"shape_data/{category}/{filename_short}"

                # add to train list
                if count < test_start:
                    list_train.append(new_filename)

                # add to test list
                if count >= test_start:
                    if count < val_start:
                        list_test.append(new_filename)

                # add to val list
                if count >= val_start:
                    list_val.append(new_filename)

# Convert lists to JSON array
json_train = json.dumps(list_train)
json_test = json.dumps(list_test)
json_val = json.dumps(list_val)

# Save train JSON files
jsonFile = open("data/3_final_data/train_test_split/shuffled_train_file_list.json", "w")
jsonFile.write(json_train)
jsonFile.close()

# Save test JSON files
jsonFile = open("data/3_final_data/train_test_split/shuffled_test_file_list.json", "w")
jsonFile.write(json_test)
jsonFile.close()

# Save val JSON files
jsonFile = open("data/3_final_data/train_test_split/shuffled_val_file_list.json", "w")
jsonFile.write(json_val)
jsonFile.close()