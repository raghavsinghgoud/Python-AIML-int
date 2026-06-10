'''negative indexing'''

# city = 'Bhopal'
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])


'''slicing'''

# name = 'priya sharma'

# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])

# print(len(city))
# print(len(name))

'''split or trim method for clearing white space'''

'''in for searching the text in list'''

# text = '  Hello Python World! '
'''Case'''

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

'''Strip whitespace'''
# print(text.strip())

'''search'''

# print('python' in text) #true
# print(text.find('python')) # 8 space count including hello and white space
# print(text.count('l'))


'''Split and join'''

# csv = 'Rahul,22,Bhopal,Engineering'
# parts= csv.split(',')
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

'''Check Content'''

# print('hello123'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print(' '.isspace())

'''Start/end check'''

# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))


'''f string'''

# name, marks , rank = 'Anita', 92.567, 3

#basic

# print(f'Hello, {name}!')

#Format numbers

# print(f'Marks: {marks:.2f}')
# print(f'Marks: {marks:.0f}')
# print(f'Count: {1000000:,}')

#Padding and alignment

# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')  # left/right align
#Anita            | 92.57|Rank:3
# print(f'Hello {name:^10}')
# print(f'Hello {name:<10}')
# print(f'Hello {name:>10}')
# print(f'Hello {name:*^10}')


#Expression inside{}

# price, gst = 500, 0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')


