import pyqrcode
import png
def qrcode():
    q = pyqrcode.create('Hey I am a QR Code.. Here wellcome to my github.. have a good day..')
    
    q.png('myQR.png',scale=6)
    print('QR Code genereted...')
if __name__ == '__main__':
    qrcode()
