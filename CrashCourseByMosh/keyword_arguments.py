# functions can have parameters,
#they can have multiple parameters

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
full_name =""
def get_full_name(first_name,last_name):
   name  = f' Full Name : {first_name} {last_name}'
   return name

full_name = get_full_name(first_name,last_name)
print(full_name)

#keyword argument:
# keyword arguments are arguments that are passed while calling the method with the parameter name.
#eg: full_name(first_name,last_name = "Ashok Kumar")
#the parameter without keyword are called positional parameters , if you mention keyword argument before the positional argument it will throw an error.
#eg full_name(last_name = "Ashok Kumar",first_name) THROWS ERROR

full_name1= get_full_name(first_name,last_name = "Smith")
print(full_name1)

#To increase the readability of the code we can use keyword argument or else we can use positional arguments
#eg: cal_principle(50,5,0.3) ===> here to know the use of parameter , we can use keyword argument. like ===> cal_principle(amount=50, yeaars=5, interest=5)



