#Ask user for the phone number and print the phone number in word

phone_number = input("Enter the phone_number: ")
words = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
}
output = ""
for number in phone_number:
   output +=words.get(number, "!")+" "
print(output)
