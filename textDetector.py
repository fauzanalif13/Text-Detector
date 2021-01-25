import pytesseract
import cv2
import numpy as np
#mendeteksi tulisan, mengubah tulisan menjadi terbaca oleh komputer

#mengalokasikan path tesseract
pathTesseract = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = pathTesseract

img = cv2.imread('text.png')
#mengubah gambar dari BGR ke RGB
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#image to string adalah menerjemahkan tulisan yg berada pada image menjadi sebuah tulisan
#print (pytesseract.image_to_string(img))

hImg, wImg,_ = img.shape
print (img.shape)
#361, 586, 0
#deteksi dimana lokasi text berada pada gambar
#print (pytesseract.image_to_boxes(img))
#ini akan mengeluarkan stat (Huruf, lokasi x, y, w, h)

# #Huruf Detector
# #sekarang kita ingin membuat box pada text yang dideteksi
# boxes = pytesseract.image_to_boxes(img)
# #img2 = img.copy()
# for b in boxes.splitlines():
#     #print (b)
#     #ini utk memisahkan per kata
#     b = b.split(' ')
#     print (b)
#
#     #ini utk membuat rectangle pada text, dan cv2.puttext
#     x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4]) #dimulai dari 1, karena 0 adalah text
#     cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (255,0,0), 1)
#     cv2.putText(img, b[0], (x, hImg-y+17), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)

# # Text Detector
# # sekarang kita ingin membuat box pada text yang dideteksi
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     print (b)
#     if x!=0:
#         # ini utk memisahkan per kata
#         b = b.split() #kita hapuskan split, biarkan python split sndiri
#         #if dibawah ini: jika jumlah data ada 12, maka akan dibaca sbg parameter
#         #4 pertama hanya 11, karena tdk ada kata yg dideteksi
#         if len(b)==12:
#         # ini utk membuat rectangle pada text, dan cv2.puttext
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])  # dimulai sesuai koordinat titik
#             cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 1)
#             cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)

# Number Detector, hanya mendeteksi per-angka
cong = r'--oem 3 --psm 6 outputbase digits'
#OEM adalah engine mode, penjelasan oem 3 dapat dilihat pada folder textDetector
#PSM adalah page segmentation mode, penjelasan psm jg sdh ada pada folder
boxes = pytesseract.image_to_data(img, config=cong)
for x,b in enumerate(boxes.splitlines()):
    print (b)
    if x!=0:
        # ini utk memisahkan per kata
        b = b.split() #kita hapuskan split, biarkan python split sndiri
        #if dibawah ini: jika jumlah data ada 12, maka akan dibaca sbg parameter
        #4 pertama hanya 11, karena tdk ada kata yg dideteksi
        if len(b)==12:
        # ini utk membuat rectangle pada text, dan cv2.puttext
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])  # dimulai sesuai koordinat titik
            cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 1)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)


cv2.imshow('Hasil Img', img)
#cv2.imshow('Hasil Img2', img2) ini td digunakan utk testing
cv2.waitKey(0)


cv2.destroyAllWindows()
