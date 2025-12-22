#List in python : we can add, remove, insert, pop and clear the list
# name = ['Ramya','Ashok','kumar','Lingesh','Thara']
# print(name) #print the list
# print(name[:]) #start as 0 and end as length of the list, print the whole list
# print(name[:2])
# print(name[2:5])
# print(name) # print the whole list will not modify
#
# name[1] = 'Ashpkk'
# print(name)

#exercise
#print largest number in the list

number =[3,6,2,8,4,10]
largest=number[0]
for num in number:
    if num>largest:
        largest = num
print(largest)

#list method
number1 = [12,45,2,4,46,21]
number1.append(20) #add the value at the end of the list
print(f'append method: {number1}')
number1.insert(0,22) #adds the value at mentioned index
print(f'insert method: {number1}')
number1.remove(21)
print(f'remove method: {number1}')
number1.count(45)
print(f'count method: {number1.count(45)}')
number1.reverse()
print(f'reverse method: {number1}')
# number1.clear()
# print(f'clear method: {number1}')
number1.sort()  #sort the list in ascending order
print(f'sort method: {number1}')
number1.reverse()
print(f'reverse method: {number1}')

number_copy = number1.copy()
print(f'copy method: {number_copy}')

number1.append(5)
print(f'append method: {number1}')