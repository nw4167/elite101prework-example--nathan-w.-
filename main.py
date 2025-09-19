print("Welcome to the Clothing Shop Chatbot")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

print("how can I help you today?")
print("1. Browse clothes")
print("2. Check store hours")
print("3. Talk to customer service")
print("4. Exit the store")

choice = input("Choose an option (1-4): ")

if choice == "1":
    print("*you look through clothes and you buy the one you like*")
elif choice == "2":
    print("*you see the store hours and find out it hasn't opened yet...😔*")
elif choice == "3":
    print("*you speak with the manager*")
elif choice == "4":
    print("Have a good day and thanks for visiting, " + name + "!")
else:
    print("dude, thats not in the option list...")
