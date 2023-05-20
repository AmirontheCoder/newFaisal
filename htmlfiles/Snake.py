import requests
from bs4 import BeautifulSoup
import urllib
from PIL import Image


query = input(">> ")
    # Make a request to the Google Images search page
res = requests.get(f"https://www.google.com/search?q={query}&tbm=isch")

    # Parse the HTML of the search results page
soup = BeautifulSoup(res.text, "html.parser")

img_tags = soup.find_all("img")[1:]

urls = [img['src'] for img in img_tags]

FFurls = urls[0:5]

icount=1

for i in FFurls:  
    urllib.request.urlretrieve(i, f"image{str(icount)}b.png")
    img = Image.open(f"image{str(icount)}b.png")
    size = (450, 300)
    resized = img.resize(size)
    resized.save(f"image{str(icount)}.png")
    icount+=1