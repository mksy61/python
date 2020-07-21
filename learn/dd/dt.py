import datetime

z = datetime.datetime.now()
print(type(z))
print(z)

print(z.day)
print(z.month)
print(z.weekday())
print(z.strftime("%d.%m.%Y %A"))
print(z.strftime("%c"))
