my_str = 'malan'
my_str = my_str.casefold()
rev_str = reversed(my_str)
print()
if list(my_str) == list(rev_str):
    print("THE STRING IS A PALINDROME.")
else:
    print("THE STRING IS NOT A PALINDROME.")