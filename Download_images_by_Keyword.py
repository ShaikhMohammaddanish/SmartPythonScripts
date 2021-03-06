#import modules
import googlesearch
import cv2
import requests
import subprocess
import os
import urllib.request
from bs4 import BeautifulSoup

# Give Download Folder 
Download_folder = "Downloads_from_prog"

#Make folder is not exist
if not os.path.exists(Download_folder):
    os.mkdir(Download_folder)
    
def url_to_image(quary, download_path):
    """ This will download all images from Keyword in Given Folder """
    
    try:  
        #Get urls from google sir
        a = googlesearch.search_images(quary, stop = 100, pause = 2)
        
    except Exception as e:
        print("Error while googling : ",e)
        pass
    
    for Url in a:
        try:
            request = requests.get(Url)
            content = request.content
            soup = BeautifulSoup(content, "html.parser")
            element = soup.find_all("img")

            for img in element:
                if ".jpg"in (img.get('src'))or ".png" in (img.get('src')):
                    urllib.request.urlretrieve(img.get('src'), download_path+"/"+img.get('src').split("/")[-1])
                    print("Downloading : ", img.get('src'))

        except Exception as e:
            print("Error while downloading image : ",e)
            pass

    
#Getting input from user
quary = input("Give your Keyword >>>")
url_to_image(quary, Download_folder)
