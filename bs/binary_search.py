def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
            print("Found! at location {}".format(midpoint))
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    if not found: print("Key not found")

print("Enter the unsorted array")	
testlist = list(map(int, input().split()))
print("Sorted array is: ")
testlist.sort()
print(testlist)
print("Enter the search key")
key = int(input())
binarySearch(testlist, key)
