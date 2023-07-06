from tkinter import colorchooser
import cv2
import numpy as np
import colorsys

def hex2rgb(hex_value):
    h = hex_value.strip("#")
    rgb = list(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def rgb2hsv(rgb_list):
    (r, g, b) = rgb_list
    r /= 255
    g /= 255
    b /= 255
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    h, s, v = int(h*179), int(s*255), int(v*255)
    print('HSV of Selected Colour: ', h, s, v)
    return np.array([h,s,v])

def change_colour(hex_value):
    #Convert Hex code of selected colour to RGB
    rgb_list = hex2rgb(hex_value)

    #Convert this RGB to HSV
    hsv = rgb2hsv(rgb_list)
    #Read the Image
    img = cv2.imread('bugatti.png')

    #Converting the image to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Converting RGB values of a specific colour in the Image to HSV
    hsv_1 = np.array([85, 95, 15])
    hsv_2 = np.array([125, 255, 255])

    #Masking pixel values; White pixels of all the pixels falling in the HSV range; else black
    mask = cv2.inRange(hsv_img, hsv_1, hsv_2)
    inv_mask = cv2.bitwise_not(mask)

    h, s, v = cv2.split(hsv_img)
    h[h>0] = hsv[0]
    hsv = cv2.merge([h, s, v])

    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    result = cv2.bitwise_or(cv2.bitwise_and(img, img, mask=inv_mask), cv2.bitwise_and(bgr, bgr, mask=mask))
    cv2.imwrite("output_buggati.png", result)
    cv2.imshow('Output',result)

count = 0
while count < 6:
    color = colorchooser.askcolor(title="Select a color")
    if color[1]:
        selected_colour = color[1]
        print('Hex code of the selected colour: ',selected_colour)
        change_colour(selected_colour)
        print()
        count += 1
