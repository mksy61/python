from contextlib import contextmanager


@contextmanager
def file(filename, method):
    file = open(filename, method, encoding="utf-8")
    yield file
    file.close()


with file("a.txt", "r") as f:
    a = f.read()

print(type(a))
print(a)
