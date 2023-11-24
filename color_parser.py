# https://github.com/yumingj/DeepFashion-MultiModal

from PIL import Image
import numpy as np

#https://stackoverflow.com/questions/36476659/how-to-add-a-relative-path-in-python-to-find-image-and-other-file-with-a-short-p

import os

# https://www.geeksforgeeks.org/python-bilateral-filtering/

import cv2

import colorsys

# 0: 'background'	1: 'top'	2: 'outer'	3: 'skirt'
# 4: 'dress'	5: 'pants'	6: 'leggings'	7: 'headwear'
# 8: 'eyeglass'	9: 'neckwear'	10: 'belt'	11: 'footwear'
# 12: 'bag'	13: 'hair'	14: 'face'	15: 'skin'
# 16: 'ring'	17: 'wrist wearing'	18: 'socks'	19: 'gloves'
# 20: 'necklace'	21: 'rompers'	22: 'earrings'	23: 'tie'

def parse_color(current_file_segm, current_file_image, label):

    script_dir = os.path.dirname(__file__)
    rel_path_image = "images/"
    abs_path_image = os.path.join(script_dir, rel_path_image)

    img = cv2.imread(abs_path_image + current_file_image)
    bilateral = cv2.bilateralFilter(img, 15, 75, 75) # tune

    #https://stackoverflow.com/questions/48182791/how-do-you-lightness-thresh-hold-with-hsl-on-opencv

    imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    rel_path_segm = "segm/"
    abs_path_segm = os.path.join(script_dir, rel_path_segm)
    segm = Image.open(abs_path_segm + current_file_segm, 'r')
    segm = np.array(segm)

    i = len(segm)
    for j in range(len(segm[0])):
        imgHLS[i][j]

filename_segm = "MEN-Denim-id_00000080-01_7_additional_segm.png"
filename_image = "MEN-Denim-id_00000080-01_7_additional.jpg"
parse_color(filename_segm, filename_image, 1)
print("done")