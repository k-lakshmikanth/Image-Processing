# importing required libraries and functions
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def list_workspace():
    """This function list all the files in the workspace"""
    print(f"workspace dir: \"{os.getcwd()}\"\n")
    print("Workspace files:")
    for i in os.listdir():
        print(f"- {i}")


def plt_img(img, size = None):
    if size is not None:
        plt.figure(figsize=size)
    img_new = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.axis("off")
    plt.imshow(img_new)

def img_similarity(diff):
    total_pixels_value_count = diff.shape[0] * diff.shape[1] * diff.shape[2] * 255
    print(f"Similarity between two images: {round((1 - (np.sum(diff)/total_pixels_value_count))*100,2)}%")

def img_props(img):
    # Image properties
    print(f"""
    Type of the image: {type(img)}
    Shape of the image: {img.shape}
    Size of the image: {img.size}
    Data type of the image: {img.dtype}
    """)
