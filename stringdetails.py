#string
title = "python tutorial for beginners";
print(title);

#we have to use the " or ' based on the requirement
#title = 'Ramya's notebook; #this statement throws an error because the single quotes with end in Ramya , so the python interpreter unable to identify it.
#so in this case we have to use double quotes (")
title ="Ramya's notebook";
print(title);

#title = "Ramya learning "python"";  # this statement will also throw an error because the python interpreter cant recognize the code after second double quotes.

title = 'Ramya learning "python"';
print(title);

#indexing
#String can be verified by indexing
title="Ramya likes python";
print(title[0]);
#string indexing starts with 0
#if you want to print the last letter in python
print(title[-1]); #Since the first letter starts with 0 , the last letter can be indexed as -1
print(title[-2]);
#for printing particular series of letter
print(title[2:6]); #the value for end index will not be printed
print(title[:5]); #by default the starting value is assumed as 0
print(title[5:]); #by default python interpreter will take the length of the string
print(title[:]); #bydefault, takes initial index as 0 and end index as length of the string

#multiline text
message = '''
Hi there,
I hope your doing well!!! 

Thanks,
Ramya.A
''';
print(message);


#FORMATTED STRINGS - FORMATTED STRING IS USED TO GENERATE DYNAMIC VALUE OF A STRING IN A SENTENTCE OR MAKE THE STRING CONCATNATION EASIER WITH DYNAMIC values.
first_name ="Ramya";
last_name="Ashok Kumar";
message = first_name+" "+last_name+ " is a developer";
print(message);
#using formatted string: formatted string starts with f
msg = f'{first_name} {last_name} is a developer';
print(msg);

#STRING METHODS
phrase = "Ramya is working"
print(len(phrase)); #this gives the number of characters in the string
#print() len() are the general function which does not depend on ong.
#String has its own functions which are referred as methods to manipulate it.

print(phrase.upper()); # this converters the string to uppercase
print(phrase.lower()); #this converts the string to lower case
print(phrase.find('w')); #this gives the index of the letter.
print(phrase.find('Ramya')); # if you write a word to find , it will give starting index of the word.
print(phrase.find('O')); #if a letter is not found in the string , this function will return -1.
print(phrase.replace('Ramya','Lingesh')) # this will change only where the replace is used.
print(phrase)
print(phrase.replace('w','W')); #we can also replace a letter in the string
print(phrase)

#To validate where a particular word or character in a string , we use "in" operator
print('working' in phrase)
print('Ramya' in phrase)




