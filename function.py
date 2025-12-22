#func is a container to performa specific task
#in larger programs we have to break our code into simple functions

#def means defining the function
#camel_case for function name(use meaningful name)
def emojiConverter(message):
    words = message.split()
    emoji = {
        ":)": "😊",
        ":(": "😒",
        "XD": "😀",
        ":')": "😂"
    }
    output = ""

    for word in words:
        if word in emoji:
            output += emoji.get(word) + " "
        else:
            output += word + " "
    return output   # if nothing is returned, python will return NOne as default return statement which means no value
