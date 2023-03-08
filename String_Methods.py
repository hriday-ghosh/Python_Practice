'''
Replace Method:

Here, if we can change the name of "H" char with the "YYY"
name = name.replace("H", "YYY"),
so, what it does, replace method just found the charachter or string and once it found then change it.

So, here we have experimented with "Hriday" word as well.

Ans- 'Hriday" turns into "YYY"

name = "Hriday"
name = name.replace("Hriday", "YYY")
print(name)

A = "012345"
A_Len = len(A)
print(A[0:3])
# The answer is 012

B = "012345"
A_Len = len(B)
print(B[1:3])
# The answer is 12


C = "012345"
A_Len = len(C)
print(C[:3])
# The answer is 012


D = "012345"
A_Len = len(D)
print(D[0:-3])
# The answer is 012

E = "012345"
A_Len = len(E)
print(E[-1:len(E)-3])
# The answer is 012

F = "012345"
A_Len = len(F)
print(F[-3:-1])
# The answer is 012

G = "012345"
A_Len = len(G)
print(G[::-1])
# The answer is 012

Splitting:

Here, split is splitting where it gets paragraph
So, the ans is ['Hriday', 'Joyti', 'Ghosh']

name = "Hriday Joyti Ghosh"
Name_Spliting = name.split(" ")
print(Name_Spliting)


data = input("Bday: DD/MMM/YYYY")
date, month, year = data.split("/")
print(f"Useer is born on date-> {date}, month -> {month},  year-> {year}")

name = input("Enter Your name ")
first, middle, sirname = name.split(" ")
print(f"""
     First Name: {first}
     Middle Name: {middle}
     Sirname: {sirname}
      """
      )

First_Date = input("Enter your first date ")
Second_Date = input("Enter your second date ")
Expression = input("Enter your exoression +,/")
if Expression == "/":
    print(f"{First_Date}/{Second_Date}")
else:
    print(" Wrong Expression")
    

A = input("Enter your name ")
print(f"Upper case: {A.upper()}")
print(f"Lower case: {A.lower()}")
print(f"Title case: {A.title()}")
print(f"Capitilized name: {A.capitalize()}")
print(f"Swap Case: {A.swapcase()}")

Ans - input - Hriday

Upper case: HRIDAY
Lower case: hriday
Title case: Hriday
Capitilized name: Hriday
Swap Case: hRIDAY


Joining: 

A = input("Enter your name: ")
print("_".join(A))

Ans-> 
Enter your name: Hriday
H_r_i_d_a_y


Reversed:

("".join(reversed(A))) - helps to reverse the number.

A = input("Enter your name: ")
print("".join(reversed(A)))

Ans- 
Enter your name: Hriday
yadirH


Replacing: 
A = input("Enter Your name: ")
print(A.replace(" ", "|"))

Ans-
Enter Your name: Hriday Jyoti Ghosh
Hriday|Jyoti|Ghosh


Sometimes we need to remove extra spaces from back anb back of the string

So, there we can use strip 

A = "|Hriday|"
print(A.strip("|"))

Ans-  Hriday

Right Strip: 
A = "|Hriday|"
print(A.rstrip("|"))

Ans-  |Hriday

Left Strip:
A = "|Hriday|"
print(A.lstrip("|"))

Ans- Hriday|

Strip can remove the things from the front and back side only

A = "||Hriday|Jyoti|Ghosh||"
print(A.strip("||"))


Centering: 

Centering adds # front and end side and make 

    #012345
A = "Hriday"
print(A.center(10, "#"))
     #012345678
Ans- ##Hriday##


'''
