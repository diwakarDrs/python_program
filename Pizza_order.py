print("Welcome to Pizaa delivery order ")
size = input("what size of pizza do you want ? S,M,L : ")
add_pepperoni = input("Do you want pepperoni ? Y OR N : ")
extra_cheese = input ("Do you want extra cheese ? Y OR N : ")
Bill = 0
small_pizza = 15
Medium_pizza = 20
Large_pizza = 25

# Adding Size
if size =='S':
    Bill+=small_pizza
elif size == 'M':
    Bill+=Medium_pizza
else:
    Bill+=Large_pizza

# Adding Pepperoni
if add_pepperoni == 'Y':
    if size =='S':
        Bill+=2
    elif size == 'M':
        Bill +=3
    else:
        Bill +=3
# Adding extra cheese
if extra_cheese == 'Y':
    Bill +=1

print(f"your final bill : {Bill}")