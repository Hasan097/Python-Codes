known_users = ["Alex", "Bob", "Emma", "Dan", "Fred","Georgie", "Harry"]
print(len(known_users))

while True:
      print("Hello! My name is Travis")
      name = input("What is your name? ").strip().capitalize()
      if name in known_users:
            print("Hello {}!".format(name))
            remove = input("Would you like to be removed from the suystem (y/n)? ").lower()
            
            if remove == "y":
                  known_users.remove(name)
            elif remove == "n":
                  print("No problem I didnt want you to leave anyway!")
            else:
                  print("Invalid input, quitting program by default")
                  break
      else:
            print("I have'nt met you yet {}".format(name))
            addem = input("Would you like to be added in the list(y/n)? ").strip().lower()
            if addem == "y":
                  known_users.append(name)
                  print("Success! Welcome to the crew!")
            elif addem == "n":
                  print("No problem I didnt want you anyway!")
            else:
                  print("Invalid input, quitting program by default")
                  break
      prexit = input("Do you want to continue?(y/n) ").capitalize()
      if prexit == "Y":
            print("Splendid lets try this again.")
            continue
      elif prexit == "N":
            break
      else:
            print("Invalid input, quitting program by default")
            break
