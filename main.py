print("Welcome to the Clothing Shop Website!")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")
if int(age) < 18:
    print("We have a wonderful youth clothing selection!")
else:
    print("We have a great selection of clothing for adults!")


print("How can I help you today?")
print("1. Browse clothes")
print("2. Check in-person store hours")
print("3. Talk to customer service")
print("4. Exit the store")

choice = input("Choose an option (1-4): ")

if choice == "1":
    print("(redirect to clothing page*)")
elif choice == "2":
    print("*Store Hours: Mon–Fri: Open, Sat: Open, Sun: Closed*")
elif choice == "3":
    print("*redirect to human customer-service employee*")
elif choice == "4":
    print("Have a good day and thanks for visiting, " + name + "!")
else:
    print("Please choose from the provided options...")
