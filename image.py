from dotenv import load_dotenv
load_dotenv()
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
import os
config = cloudinary.config(secure=True)
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")


def uploadImage(filepath):
    fileId = input("Enter an image ID: ")
    cloudinary.uploader.upload(filepath, public_id= fileId, unique_filename = False, overwrite=True)
    imgUrl = cloudinary.CloudinaryImage(fileId).build_url()
    
    return imgUrl, fileId


def genFill(filepath):
    baseUrl, baseId = uploadImage(filepath)
    imgWidth = input("desired image width(px): ")
    imgHeight = input("desired image height (px): ")
    return cloudinary.CloudinaryImage(baseId).build_url(width=int(imgWidth), height=int(imgHeight), gravity="center", background="gen_fill", crop="pad")

def runTest():
    os.chdir("images")
    for file in os.listdir():
        print(genFill(file))


runTest()