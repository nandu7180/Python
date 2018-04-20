"""lis1 = [1, 22, 2, 15, 3, 4, 5]
lis1.append(6)
print lis1
lis1.extend([7])
lis1.extend([8, 9])
print lis1
lis1.insert(6, 22)
print lis1
lis1.remove(22)
print lis1
lis1.pop(2)
lis1.pop()
print lis1
print lis1.count(5)

lis1.sort()
print lis1
lis1.reverse()
print lis1"""

"""print repr("hai")
print str('nandu')
print repr(123)
for x in range(1, 11):
    print repr(x).rjust(2), repr(x * x).rjust(3),
    print repr(x * x * x).rjust(4)

print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')"""

import sys

for arg in sys.argv[1:]:
    print 'hello'
    try:
        f = open(arg, 'r')
        print f
    except IOError:
        print 'can not open ', arg

    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
