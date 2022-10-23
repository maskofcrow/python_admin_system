from msilib import datasizemask
import string
import tkinter 
from lib2to3.pytree import type_repr


isim = input("isim giriniz: ")
soyisim = input("soy isim giriniz: ")

print(type (isim))
print(type (soyisim))

toplam = str(isim) + ' ' + str(soyisim)

print(toplam)

yas = int(input("Doğum yılını giriniz: "))
yıl= 2022 - int(yas)
print("Yaşınız " + str(yıl))

evet = str(input("Yaşınız doğruysa Evet , değilse Hayır yazınız: ")) 
proceed="evet" or "hayır"

if evet==proceed:
    print("Teşekkürler bir sonraki adıma hoş geldiniz")
else:
    print("Lütfen bilgilerinizi baştan giriniz")
    exit()

tarih =str(input("Doğum tarihinizi giriniz (gg/aa) şeklinde yazınız: "))

dogrulama= toplam ,yas ,tarih
print(dogrulama)

answer = input("Bilgileriniz doğru mu? " )



proceed="evet" or "hayır" 
proceed = "evet", "hayır"
if answer in proceed: 
    print("devam ediniz")

key=input("adminlerin size verdiği key'i giriniz: ")
secim="AUGZ-KELM"
secim1="as"
secim2="as"
secim3="as"
secim4="as"
secim5="as"
secim6="as"
secim7="as"


if key==secim:
    print('Key aktif. Giriş başarılı!')
if key==secim1:
    print("Key aktif. Giriş başarılı!")
if key==secim2:
    print('Key aktif. Giriş başarılı!')
if key==secim3:
    print("Key aktif. Giriş başarılı!")
if key==secim4:
    print('Key aktif. Giriş başarılı!')
if key==secim5:
    print("Key aktif. Giriş başarılı!")
if key==secim6:
    print('Key aktif. Giriş başarılı!')
if key==secim7:
    print("Key aktif. Giriş başarılı!")

else: 
    print("Giriş key'i bulunmamaktadır lütfen tekrar deneyiniz! ")
    exit()
 


