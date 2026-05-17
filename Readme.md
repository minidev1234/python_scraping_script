#Project name
spider.py

##Description
The spider program allow you to extract all the images from a website, recursively, by
providing a url as a parameter.

##Installation
'''bash
git clone git@github.com:minidev1234/python_scraping_script.git
cd python_scraping_script/spider/spider.py
chmod +x spider.py

__Usage__
./spider [-rlp] URL

__Options__
• Option -r : recursively downloads the images in a URL received as a parameter.
• Option -r -l [N] : indicates the maximum depth level of the recursive download.If not indicated, it will be 5.
• Option -p [PATH] : indicates the path where the downloaded files will be saved.If not specified, ./data/ will be used.

__Features__
The program will download the following extensions by default:
• .jpg/jpeg
• .png
• .gif
• .bmp
    
__Author__
Minidev1234
