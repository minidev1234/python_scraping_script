#!/usr/bin/python3

import sys
from PIL import Image
from PIL.ExifTags import TAGS

def treat_one_img(image):
    exif = {}
    im = Image.open(image)
    exif["Img_name"] = image
    exifdata = im.getexif()
    if exifdata:
        for  tag_id in exifdata:
            tagname = TAGS.get(tag_id, tag_id)
            value = exifdata.get(tag_id)
            exif[tagname] = value
        return dict(exif)
    print(f"metadata not found: {image}")

def treat_all_exif(lst_image):
    metadata = []
    for im in lst_image:
        metadata.append(treat_one_img(im))

def main():
    if len(sys.argv) < 2:
        print(f"Usage: ./scorpion <img_one> <img_two> ...")
    else:
        treat_all_exif(sys.argv[1:])

if __name__ == "__main__":
    main()