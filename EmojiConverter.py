import function

message = input("enter the message: ")

# words = message.split()
#
# emoji ={
#     ":)" : "😊",
#     ":(" : "😒",
#     "XD" : "😀",
#     ":')" : "😂"
# }
# output =""
#
# for word in words:
#     if word in emoji:
#         output += emoji.get(word) +" "
#     else:
#         output += word +" "

output = function.emojiConverter(message)


print(output)