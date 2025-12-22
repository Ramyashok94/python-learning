#exercise
question ='''
user wants to enter their weight,
then ask its lbs or kg, if lb enter l and vice versa
then if its lb convert into kg and display the weight and vice versa for kilogram as well
'''

weight = int(input("Weight: "))
#scale= input('(L)bs or (K)g: ').upper()

# if scale == "L":
#     weight= float(weight) * 2.20
#     print(f'your weight is: {weight} kgs')
# if scale == "K":
#     weight= float(weight) * 0.45
#     print(f'your weight is: {weight} lbs')

scale= input('(L)bs or (K)g: ')
if scale.upper() == "L":
    weight*= 0.45
    print(f'your weight is: {weight} kgs')
if scale.upper() == "K":
    weight//= 0.45
    print(f'your weight is: {weight} lbs')