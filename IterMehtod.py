"""class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('balu')
for char in rev:
    print char"""


"""def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


val = reverse("balu")
print val.next()
print val.next()
print val.next()
print val.next()
print
for vals in reverse("nandu"):
    print val"""

import glob

print glob.glob('*.py')

import sys
sys.stderr.write("error occur")