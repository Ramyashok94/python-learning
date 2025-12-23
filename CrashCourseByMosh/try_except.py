# try to write the business logic or coe and except to catch the error

# age = int(input("Enter your age: "))
# print(age) # if the user gave alphabetic value for age input, it will give the value error and crash the program. To execute the program with error codes and to send message to the user
# that the wrong value is typed , we are using try except

# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except(ValueError):
#     print("Invalid input. Please enter the correct Age. ")


#Suppose we are calculating the savings
# Age = int(input("Enter your age: "))
# income = int(input("Enter your income: "))
# saving = income / Age # if age is 0, this will throw an ZeroDivisionError with exit code 1
# print(saving)

try:
    Age = int(input("Enter your age: "))
    income = int(input("Enter your income: "))
    savings = income/Age
    print(savings)
except(ZeroDivisionError):
    print("Age should not be 0")

