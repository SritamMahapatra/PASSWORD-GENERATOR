import random 
import string
def create(length):
    char=string.ascii_lowercase+string.digits+string.ascii_uppercase+string.punctuation
    password=''.join(random.choice(char)for i in range(length))
    return password
length=int(input("enter a suitable length for your password:"))
print("your password is:",create(length))