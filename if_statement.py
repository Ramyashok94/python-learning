question ='''
if it is a hot, print statement related to hot day,
if it is a cold, print statement related to cold day,
else print its a lovely day.
'''

# is_hot = input("is it a hot day?(true/false): ").lower()=="true"; #is_hot =false
# is_cold =input("is it a cold day?(true/false): ").lower()=="true";#is_cold =true
# print(is_hot)
# print(type(is_hot))
#
# if is_hot:
#     print("it's a hot day")
#     print('drink plenty of water')
# elif is_cold:
#     print("it's a cold day")
#     print("wear warm clothes")
# else:
#     print("its a lovely day")
#
# print("enjoy your day")


#exercise

# question=''' a buyer buy a house for $1M
# if a buyer has good credit , he has to put 10% to buy
# otherwise, he has to put 10% to buy
# '''
#
# #solution
# house_price=1000000
# has_good_credit = input("Does the buyer have good credit? (true/false) ").lower() == "true";
#
# if has_good_credit:
#     downpayment = (10/100)*house_price
# else:
#     downpayment =(20/100)*house_price
# print(f'downpayment: ${downpayment}')

#logical operator
# and => execute the block, if all the conditions are true
# or => execute the block , if atleast one condition is true
# not => inverse the value , if true , inverse to false

#exercise:
#if has good credit and has home , eligible for loan
#if has good credit or has home, eligible for loan
#if has good credit and not a criminal record, eligible for loan

# has_good_credit=input("enter the employee has good credit?(true/false): ").lower() == "true"
# has_home=input("enter the employee has home?(true/false): ").lower() == "true"
#
# if has_good_credit and has_home:
#     print("eligible for loan")

# has_good_credit=input("enter the employee has good credit?(true/false): ").lower() == "true"
# has_home=input("enter the employee has home?(true/false): ").lower() == "true"
#
# if has_good_credit or has_home:
#     print("eligible for loan")

# has_good_credit=input("enter the employee has good credit?(true/false): ").lower() == "true"
# has_criminal_record=input("enter the employee has criminal record?(true/false): ").lower() == "true"
#
# if has_good_credit or not has_criminal_record:
#     print("eligible for loan")

#comparison operators
#>,<,==(comparison operator)
# "=" is an assignment operator

#exercise:
name= input('Enter your name: ')
name_size = len(name)

if name_size<3:
    print("Name must be atleast 3 characters")
elif name_size>50:
    print("Name must be within 50 characters")
else:
    print("Name looks good")

