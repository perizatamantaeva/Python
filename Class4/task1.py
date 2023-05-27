while True: # while age == age
    age = int(input("Please, enter your age: "))

    if age < 13:
        print("Sorry, you're not allowed to pass.")
    elif age >= 13 and age < 18:
        print("Please call your legal guardian.")
    else:
        print("Welcome!")

    print() 
    


# while True:
#     age = int(input("Enter your age: "))

#     if age < 13:
#         print("Sorry, you're not allowed to pass.")
#         continue
#     elif age < 18:
#         print("Please call your legal guardian.")
#         continue
#     else age > 18:
#         print("Welcome!")
      
