from contextlib import contextmanager


@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()


with file("a.txt", "r") as f:
    a = f.read()
