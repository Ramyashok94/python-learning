#while loop if used to run the statement untill a condition met.

# i=1
# while i<=5:
#     print(i)
#     i=i+1 #this incrementation is important otherwise the loop will run infine time because the value of i remains 1.
# print("while loop executed")

# i=1
# while i<=5:
#     print('*' * i)
#     i=i+1

question='''
user has to guess the number , he has 3 chances. if the number is guess in 3 time display you won. otherwise display you lost
'''


# count =0;
#
# while  count<3:
#     guess = input("Guess: ")
#     if guess in "9":
#         print("you won!!!")
#         break
#
#     count += 1
#     if count == 3:
#         print("you lost!!!")



# In python while condition can have else block like if statement
#rewriting the code with while-else condition

secret_number= 9
total_turn=3
no_of_turns = 0

while no_of_turns < total_turn:
    guess = int(input('Guess: '))
    if guess == secret_number:
        print('you won!!')
        break
    no_of_turns+=1;
else:
    print("Sorry. you failed !!")

