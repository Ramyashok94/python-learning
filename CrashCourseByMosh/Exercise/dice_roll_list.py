import random

dice_choice = []
output = ''
for i in range(1, 7):
    for j in range(1, 7):
        dice_choice.append((i, j))


class Dice:
    def roll(self,dice_choice):
       output = random.Random().choice(dice_choice)
       return output

dice = Dice()
result = dice.roll(dice_choice)
print(result)
