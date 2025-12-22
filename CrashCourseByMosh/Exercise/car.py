#car exercise
#
# command = "";
#
# startCount = 0;
# stopCount = 0;
#
# while True:
#     command = input(">").lower();
#
#     if command == "help":
#         print('''
# Start -> to start the car
# Stop -> to stop the car')
# quit -> to exit the car
#         ''')
#     elif command == "start":
#         startCount += 1;
#         if startCount == 1:
#             print('Car started...Ready to go')
#         else:
#             print('car already started')
#     elif command == "stop":
#         stopCount += 1
#         if stopCount == 1 :
#             print("Car stopped..")
#         else:
#             print('car already stopped')
#     elif command == "quit":
#         break
#     else:
#         print("I dont understand.")


#Another way:
#car exercise

command = "";
started = False
stopped = False

while True:
    command = input(">").lower();

    if command == "help":
        print('''
Start -> to start the car
Stop -> to stop the car')
quit -> to exit the car
        ''')
    elif command == "start":
        if not started:
            print('Car started...Ready to go')
            started = True
        else:
            print('car already started')
    elif command == "stop":

        if not stopped:
            print("Car stopped..")
            stopped = True
        else:
            print('car already stopped')
    elif command == "quit":
        break
    else:
        print("I dont understand.")














