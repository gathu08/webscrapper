from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    
    search = input("Search for:")
    params = {"q":search}
    dir_name = search.replace(" ","-").lower()
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        
    r = requests.get("https://www.bing.com/images/search",params=params)
    soup = BeautifulSoup(r.text,features="html.parser")
    link = soup.find_all("a",{"class":"thumb"})
    for item in link:
        imag_obj = requests.get(item.attrs ["href"])
        print("Getting".item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:
            imag= Image.open(BytesIO(imag_obj.content))
        
            imag.save("./" +dir_name + "/"+ title,imag.format)
        except:
            print("Could not save image")
        
    StartSearch()
StartSearch()