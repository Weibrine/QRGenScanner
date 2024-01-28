import pyqrcode
import png
from pyqrcode import QRCode

link = 'https://time.is'
url = pyqrcode.create(link)

url.png('timeteller.png', scale = 8)

