set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
set3 = {30, 40, 50, 60}
set4 = {5, 6}
print(set1.issubset(set2))
print(set2.issubset(set3))
print(set1.issuperset(set2))
print(set2.issuperset(set3))
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set4))