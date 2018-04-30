nums=[3,4,-99,78,4,-99]
x=int(input("enter an integer: "))

# must not use count() or in or index()
for num in nums:
    if num==x:
        print("found !!!")
        break # if do not use break here, else below always run 1 time
else:
    # when use else like that (the code above has no result of break, and else just runs 0 time or 1 time)
    print("Not found")
#
# if found:
#     print("Found")
# else:
#     print("not found")
