import pyqrcode
from pyqrcode import QRCode
import time




preurl = input("Please enter the URL you would like to convert into a QR Code:\n")

url = pyqrcode.create(preurl)
time.sleep(2)
print("Done!")

url.svg("qrcode.svg", scale = 8)

time.sleep(5)