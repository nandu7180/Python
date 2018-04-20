d1 = {"john": 40, "peter": 45}
d2 = {"john": 466, "peter": 45}
d1 == d2

t = (1, 2, 3, 4)
print t[1:-1]
print t[:-1]
print t[1:]
t1 = (1, 2, 4, 3, 8, 9)
output = [t1[i] for i in range(0, len(t1), 2)]
print output

t2 = (1, 2)
print 2 * t2

t11 = (1, 2, 4, 3)
t22 = (1, 2, 3, 4)
print t11 > t22

s1 = 'I\m single' + "\n" + 'Dont give up'
print s1
print "Hi\nth\ere,\thow \141\x72\145\x20you?"
print r"Hi\nth\ere,\thow \141\x72\145\x20you?"

fred = ['The', 'answer', 'to', 'your', 'question', 'is', 24]
print 'A:', fred
print 'B:', fred[0], fred[2], fred[6], fred[-1], fred[-4]
print "C:", fred[2:5], fred[-6:-3], fred[4:5], fred[3:3]

fred[1] = 'response'
print fred

fred[-1] = fred[-1] + 200
fred[3] = fred[3] + " name"
print fred

fred[-3] = "balu"
print "D:", fred

fred[0:2] = ['an', 'unlikely', 'answer']
fred[-1:-1] = ['a', 'conservative']
print "E:", fred

# Sub List
balu = [3, 4, ['and', 'also', 'a'], 52]
print balu[2][0]

balu[0] = [2, '+', 1]
print balu
fred[1:3] = [fred[1:3]]
fred[-1:] = [balu]
print fred

fred.extend(['with', 'balu'])
print fred
