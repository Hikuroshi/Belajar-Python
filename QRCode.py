# Importing library
import qrcode
import cv2
import random
import string

def linkQR():
	data = input("Masukan Link: ")
	qr = qrcode.QRCode(
		version = 1,
		box_size = 10,
		border = 5)

	qr.add_data(data)

	qr.make(fit = True)
	img = qr.make_image(
		fill_color = 'black',
		back_color = 'white')
	
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	num = string.digits

	all = lower + upper + num
	
	namr = "QRcd.png"
	panjnam = int(5)
	nama = random.sample(all, panjnam)
	namas = ''.join(nama)

	img.save('{}{}'.format(namas, namr))

def QRlink():
	img = cv2.imread(input("Masukan Image: "))
	det = cv2.QRCodeDetector()
	val = det.detectAndDecode(img)
	print(val)


print("Pilih Menu")
print("1.Mengubah link menjadi QR-Code")
print("2.Mengubah QR-Code menjadi link")

pilih = input("Masukan 1/2 untuk memilih: ")


if pilih == '1':
	print(linkQR())
elif pilih == '2':
	print(QRlink())
