girdi = input("Sayı Girin:")

try:
    sayi = int(girdi)
    print(sayi)
except Exception as identifier:
    print("Hata oldu:", identifier)
finally:
    print("^^^^^^^^^^")
