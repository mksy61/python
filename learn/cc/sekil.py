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


k1 = Kare(3, 4, 5)

print(k1.hacim())
