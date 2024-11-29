import random

alfabe = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifreuzunlugu = int(input("Şifrenin uzunluğu kaç harf olsun?"))
sifre = ""

for i in range(sifreuzunlugu):
    sifre += random.choice(alfabe)

print(sifre)
