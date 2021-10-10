print("Welcome to Love Calculator")
name1 = input("What is the name1\n")
name2 = input("what is the name2\n")
combined_string = name1+name2
lowercase_name = combined_string.lower()

# count number time character 'True love'
t = lowercase_name.count('t')
r = lowercase_name.count('r') 
u = lowercase_name.count('u') 
e = lowercase_name.count('e') 
l = lowercase_name.count('l') 
o = lowercase_name.count('o') 
v = lowercase_name.count('v') 
e = lowercase_name.count('e')

# Sum True and Love
true = t + r + u + e 
love = l + o + v + e

Love_Score = int(str(true)+str(love))

if Love_Score > 10 or Love_Score > 90:
    print(f"your score is {Love_Score}, you go together like coke and mentos")

elif Love_Score > 40 and Love_Score > 50:
    print(f"your score is {Love_Score}, you are alright together")

else:
    print(f'your score is {Love_Score}')
