name = (input("What's your name? "))

correctcheck = input(f'So....your name is ' + name + '. Is that correct? [y/n] ')
if correctcheck == 'y':
    print("Great. Stored your name.")
else:
    print("Sorry about that.")
    name = (input("Let's try again. What's your name? "))
