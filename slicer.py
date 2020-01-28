#get the users email address

email = input("What is your email address?: ").strip()

#slice out the users name

user = email[:email.index("@")]

#slice domain name

domain = email[email.index("@")+1:]

#format the message

output = "Your username is {} and your domain name is {}".format(user,domain)

#display output message

print(output)

