import string
import random
length=int(input("Enter a password length:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password+=random.choice(characters)
print("Generated Password:",password)    
