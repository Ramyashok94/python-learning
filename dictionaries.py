#dictionaries are key and value pairs with unique keys. like our real world dictionary


customer = {
     "name" : "Ramya",
     "age" : 23,
     "email" : "ramya@abc.com"
}

print(customer["name"])
#(customer[Name]) #show NameError as a result because the key is not present in the dictionary
#To avoid getting the error we can use get method.
print(customer.get("age"))
print(customer.get("Age")) #we will get None as output. 1. to avoid k
# eyError in the cnsole 2. NOne means no key found. 3. we can assign default value if the key is not found in the dictionary.
print("Nick name:" +customer.get("nick_name", "Abi"))

#we can update the name as well

customer["name"] = "Ramya Ashok" #this will update the name in the dictionary
print(customer)