import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><{}[]"

all_chars = lower + upper + numbers + symbols
lenght = int(input("Enter a lenght of password: "))

password = ''.join(random.sample(all_chars,lenght))
print("Generated Password:", password)