

largest = None
smallest = None
first_number = True

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break

    try:
        num = int(num)
        if first_number:
            largest = num
            smallest = num
            first_number = False
        else:
            largest = max(largest, num)
            smallest = min(smallest, num)
    

print "Maximum", largest
print "Minimum", smallest

