import re

path = raw_input("Enter File Name: ")
result = []
try:
    f = open(path, 'r')
    data = f.readlines()
    user_input = raw_input("Enter your searching: ")
    for i in data:

        if re.search(user_input.lower(), i.lower()):
            result.append(i)

        if re.search(r'\s', user_input):
            two = user_input.split()
            if re.search(two[0].lower(), i.lower()):
                if re.search(two[1].lower(), i.lower()):
                    result.append(i)
        else:
            pass
except:
    print "File Not Found"

else:
    print "for 1 normal output and for 2 log file will generate"
    user = input("Enter for output 1 or 2: ")
    for i in range(1, 3):
        if int(user) == 1:
            if result:
                for data in result:
                    print data
            else:
                print "Nothing Found"
            break

        if int(user) == 2:
            new = open(path + "_" + user_input + ".txt", 'w')
            new.writelines(result)
            print "Logs Files Generated Your Location"
            break
        else:
            print "Nothing Found"
            break
