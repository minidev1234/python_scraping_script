__Project name__<br>
spider.py<br>

__Description__<br>
The spider program allow you to extract all the images from a website, recursively, by
providing a url as a parameter.<br>

__Installation__<br>
```bash  
git clone git@github.com:minidev1234/python_scraping_script.git  

cd python_scraping_script/spider/spider.py
  
chmod +x spider.py  
```

__Usage__<br>
./spider [-rlp] URL<br>

__Options__<br>
- **'Option -r'** : recursively downloads the images in a URL received as a parameter.<br>
- **'Option -r -l [N]'** : indicates the maximum depth level of the recursive download.If not indicated, it will be 5.<br>
- **' Option -p [PATH]'** : indicates the path where the downloaded files will be saved.If not specified, ./data/ will be used.<br>

__Features__<br>
The program will download the following extensions by default:<br>
- **.jpg/jpeg**<br>
- **.png**<br>
- **.gif**<br>
- **.bmp**<br>
    
__Author__<br>
Minidev1234<br>
