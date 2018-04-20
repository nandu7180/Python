a = 0
while a < 15:
    print a
    if a == 10:
        print "Made it to ten!!!"
    a += 1

for y in range(20, 10, -1):
    print y,
print

for y in range(2, 10, 2):
    print y,
print
power = 1
for y in range(0, 21):
    print "2 to the", y, "is", power
    power = 2 * power
fred = ['And', 'now', 'for', 'something', 'completely', 'different.']
for i in range(0, len(fred)):
    print i, fred[i]
