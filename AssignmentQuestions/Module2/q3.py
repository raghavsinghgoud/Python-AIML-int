'''Once upon a time there was a land, a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
1. if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
2. if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to 
1. write a tax calculator.
It should accept one floating-point value: the income.
2. Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.'''


# income = float(input("Enter your income: "))
# pti = 0 #personal income tax

# if income <= 85528:
#     pti = income*(18/100) - 556.2
# else:
#     pti = 14839.2 + income*(32/100)
# round(pti)
# if pti < 0:
#     pti = 0

# print("Tax: ", pti)
