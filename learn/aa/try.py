a = float(input("1. Sayı:"))
b = float(input("2. Sayı:"))

try:
    print("Sonuç", a/b)
except ZeroDivisionError as identifier:
    print("Hata E:", identifier)
else:
    pass
finally:
    print("Bu hep çalışır")