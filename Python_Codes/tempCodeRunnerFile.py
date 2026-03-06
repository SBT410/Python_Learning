lists = [1,2,3,3,2,4,5,6,7,7,7,3,3,3,7]

n = 4  
count = {}
for list in lists:
    count[list] = lists.count(list)
sorted_num = sorted(count, key=count.get, reverse = True)
print(f"{n} most occurring number is:", sorted_num[n-1])