import re
a = "Iam2ragh34va21"
lis = map(int, re.findall('\d+', a))
nsum = sum(lis)
print nsum

