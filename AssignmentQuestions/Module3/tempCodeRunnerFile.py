
string = "U r a a n S 0 f t s k i l l 1 s 1234"
digits = []
for char in string:
    if char.isdigit():
        digits.append(char)
print("Total number of Digits = ", len(digits))
