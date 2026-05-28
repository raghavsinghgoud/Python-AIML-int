# dictionary = {
#     "cat": "chat",
#     "dog": "chien",
#     "horse": "cheval"
# }
# phone_numbers= {'boss': 454545454545, 'suzy':37373737337}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))


'''calling elements'''

# print(dictionary['cat'])
# print(phone_numbers['suzy'])


#print(phone_numbers['President']) '''type error'''


# Words = {'cat', 'lion', 'horse'}
# for word in Words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

'''items()'''

# print(dictionary.keys())
# for key in dictionary.keys():
#     print(key,"->", dictionary[key])


# for key,value in dictionary.items():
#     print(key,"->", value)

'''values()'''

# print(dictionary.values())

# for value in dictionary.values():
#     print(value)

'''copy()'''

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
# }
# print("pol_eng_dictionary: ", pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()

# print("copy_dictionary: ", copy_dictionary)

# pol_eng_dictionary["zamek"]= "lock" # assigning new value
# item = pol_eng_dictionary["zamek"]
# print(item)

# phonebook ={}
# print(phonebook)
# phonebook["Adam"]= 34563524623 # create or add a key-value pair
# print(phonebook)

# del phonebook["Adam"]
# print(phonebook)


'''update(), popitem()'''

# pol_eng_dictionary = {"kwiat": "flower"}

# pol_eng_dictionary.update(
#     {
#         "gleba":"soil"
#     }
# )
# print(pol_eng_dictionary)

# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)


'''finding item'''

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
# }

# if "zamek1" in pol_eng_dictionary:
#     print("Yes! zamek1 is present in the dictionary.")
# else :
#     print("NO! zamek1 is not present in the dictionary.")


'''del and clear()'''


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
# }

# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))
# del pol_eng_dictionary["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear() # clear removes all the element.
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))
# del pol_eng_dictionary # deletes the dictionary
# print(pol_eng_dictionary)


