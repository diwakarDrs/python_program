year = int(input("Enter the year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Entered year is Leap year")
        else:
            print("Entered year is not a Leap year")
    else:
        print("Entered year is Leap year")
else:
    print("Entered year is not a Leap year")