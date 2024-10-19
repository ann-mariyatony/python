'''
Author:Ann mariya tony
Date: 19-10-2024
Description:Python program to Create, concatenate, and print a string and access a sub-string from a given string.
'''
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
name=first_name + " "+ last_name
print(name)
first_name_length = len(first_name)
print(first_name_length)
extrated_first_name = name[:first_name_length]
print(extrated_first_name)

