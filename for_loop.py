# for item in ['ashok', 'kumar', 'ramya', 'lingesh','Thara']:
#     print(item)
# for item in range(12,20,2): #range method is a special obj that we can iterate over
#     print(item)

#for loop exercise
# numbers=[5,2,5,2,2]
# for number in numbers:
#    print('x' * number)

numbers=[5,2,5,2,2]
for number in numbers:
    output =''
    for x_count in range(number):
        output+= 'x'
    print(output)


