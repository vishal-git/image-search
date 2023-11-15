# searches for images using keywords and downloads those images 
from fastbook import search_images_ddg, download_url
from urllib import request
import sys
sys.path.append('..')
from config import classes, max_images

for c in classes:
    # extract urls for matching images from duckduckgo
    urls = search_images_ddg(c, max_images=max_images)

    for i in range(len(urls)):
        try:
            resp = request.urlopen(urls[i])
        except Exception as e:
            continue
        else:
            # download the image to the /images directory
            download_url(urls[i], f'./images/{c}_{i}.jpg')
