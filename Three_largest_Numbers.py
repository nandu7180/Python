data = [-45, 0, 3, 10, 90, 5, -2, 4, 18, 45, 100, 1, -266, 706]

largest = None
second_large = None
third = None

for a in data:
    if largest < a:
        second_large = largest
        largest = a

    if second_large < a & largest != a:
        third = second_large
        second_large = a
        if third < a & second_large != a:
            third = a

print largest
print second_large
print third
