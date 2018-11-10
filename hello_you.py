# Ask user for name

name = input("what is your name? : ")

# Ask user for their age

age = input("What is your age? : ")

# Ask user their city

city = input("What is your city? : ")

# Ask user what they enjoy

love = input("What do you love?: ")

# Create output text

string = "Your name is {}and you are {} years old. You live in {} and love {}."
output = string.format(name,age,city,love)

# Print output to screen

print(output)
