#!/usr/bin/python3
import numpy as np
import argparse
import cv2
import glob
from icecream import ic
from msml.utilities.file_helpers.file_helpers import check_and_create_folder
import os
from tqdm import tqdm
import json

def make_masks(top_level_dir, color_code):
    
    mask_dir = top_level_dir
    ic(mask_dir)
    count = 0
    for file in tqdm(glob.glob(mask_dir+"/*")):
        if file[-4:] == ".png":
            ic(file)
            img = cv2.imread(file)
            H, W, _ = img.shape
            ic(W, H)
            ic(os.path.split(file)[1])
            
            json_data = {
                "imgHeight": H,
                "imgWidth": W,
                "objects": [
                    {
                        "label": os.path.split(file)[1][5:-4].split('_')[1],
                        "polygon": [
                            [
                                0,
                                0
                            ],
                            [
                                0,
                                H
                            ],
                            [
                                W,
                                H
                            ],
                            [
                                W,
                                0
                            ]
                        ]
                    }
                ]
            }
            ic(json_data)
            
            json_obj = json.dumps(json_data, indent=4)
            save_file_name = os.path.split(file)[0]+"/"+os.path.split(file)[1][:-4]+'.json'
            ic(save_file_name)
            with open(save_file_name, "w") as outfile:
                outfile.write(json_obj)
        
def main():
    # Read in the segmentation image and make a mask for where there isn't a mine
    # Create a .json for the different colour codes
    make_masks("datasets/FastDataGen/val/annotations/", "red")
    

if __name__ == "__main__":
    main()