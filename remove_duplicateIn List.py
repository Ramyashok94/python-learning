#exercise to remove the duplicates in list

number = [1,1,2,3,4,5,6,3,7,8,4]
unique = []
for num in number:
    if num not in unique:
        unique.append(num)
    else:
        continue
print(unique)

