from bs4 import BeautifulSoup
import re
import requests

#url = "https://www.daraz.pk/products/buy-1-get-1-free-blutooth-handfree-wireless-bluetooth-headset-good-quality-bluetooth-handsfree-earphone-i143850138-s1305074376.html?spm=a2a0e.home.flashSale.3.35e34937kZLN16"
#url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
url = "https://en.wikipedia.org/wiki/Baahubali_2:_The_Conclusion"
result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

# find prices with regulare expressions
prices = doc.find_all(text=re.compile("\$.*"), limit=15) # \$.* -> string starts with $ and after that any num of char we dont care

for price in prices:
    print(price.strip())