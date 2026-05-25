'''As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
1. if the year number isn't divisible by four, it's a common year;
2. otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, 
3. if the year number isn't divisible by 400, it's a common year;
4. otherwise, it's a leap year.
Write code - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.'''


# year = int(input("Enter a year: "))
# if year % 4 != 0 or year % 100 != 0:
#     print("It's a common year!")
# else :
#     print("It's a leap year!")

# if year >= 1582:
#     print("The entered year falls itno the Gregorian era!")
# else :
#     print("Not within the Gregorian calendar period!")

