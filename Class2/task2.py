tip = int(input("Please enter the tip: "))

if tip == 15:
    print("Standard")
elif tip == 18:
    print("Good")
elif tip == 20:
    print("Great")
elif tip > 20:
    print("My Hero")
else:
    print("Please enter 15, 18, 20 or greater")
    