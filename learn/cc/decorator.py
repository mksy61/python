def toUpper(f):
    def makeUpper(s):
        print("***")
        f(s.upper())
        print("---")
    return makeUpper


def toLower(f):
    def makeLower(s):
        print("***")
        f(s.lower())
        print("---")
    return makeLower


@toUpper
def a(s):
    print(s)


@toLower
def b(s):
    print(s)


a("merhaba")
b("MeRHaBa")
