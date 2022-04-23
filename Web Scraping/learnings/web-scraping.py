from bs4 import BeautifulSoup
import bs4
import requests

print(bs4.__version__)

#url = "https://www.daraz.pk/products/buy-1-get-1-free-blutooth-handfree-wireless-bluetooth-headset-good-quality-bluetooth-handsfree-earphone-i143850138-s1305074376.html?spm=a2a0e.home.flashSale.3.35e34937kZLN16"
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")
#pricesprint(doc.prettify())
prices = doc.find_all(text="$")

for price in prices:
    parent = price.parent
    strong = parent.find("strong")
    print(strong.text)