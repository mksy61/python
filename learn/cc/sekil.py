class Sekil(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def alan(self):
        return self.x * self.y


class Kare(Sekil):
    def __init__(self, x, y, h):
        super().__init__(x, y)
        self.h = h

    def hacim(self):
        return self.x*self.y*self.h

    def __eq__(self, k):
        return self.hacim == k.hacim

    def __add__(self, k):
        return self.hacim() + k.hacim()


k1 = Kare(3, 4, 5)
k2 = Kare(3, 4, 6)

print(k1 == k2)
print(k1+k2)
print(k1.hacim())
