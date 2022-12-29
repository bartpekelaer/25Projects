import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


data = "Don't scan shady QR-Code :D"
path = "8-qrcode/myqrcode3.png"


def make_qrcode():
    qr = qrcode.QRCode(version=1, box_size=10, border=1)

    qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="black")

    img.save(path)


def read_qrcode():
    img = Image.open(path)

    result = decode(img)

    print(result)


make_qrcode()
