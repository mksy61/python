bir = "bir"
iki = "iki"
sayi= bir.capitalize() + iki.upper()
print(sayi) 

ad = "murat"
soyad = "aksoy"
isim="Murat Aksoy"

adSoyad="|{:<10}||{:>10}|"

print(adSoyad.format(ad,soyad))
print("*{:^30}*".format(isim))
print("\a")

print("Hello\vWorld")

print("\u0131")
print(r"\u0131")