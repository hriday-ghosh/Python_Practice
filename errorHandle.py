try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


Great one 👍 Let’s cover Error Handling in Python from top to bottom in very easy and layman’s language.


---

🟢 What is Error Handling?

👉 Error Handling = dealing with problems in code without crashing the program.

Without handling → program crashes ❌

With handling → program shows a nice message or takes another action ✅


Think of it like driving a car 🚗:

An error = a pothole.

Without handling = car falls and breaks.

With handling = you slow down or take a detour.



---

🟢 Types of Errors in Python

1. Syntax Errors → When you write code wrong (like spelling mistakes).

print("Hello"   # ❌ Missing bracket

👉 Python won’t run this at all.


2. Runtime Errors (Exceptions) → Program runs, but something wrong happens.
Example:

print(10 / 0)   # ❌ Division by zero

👉 This is where Error Handling comes in.




---

🟢 Handling Errors with try...except

Basic Syntax:

try:
    # risky code
except:
    # what to do if error happens

Example:

try:
    x = 10 / 0
except:
    print("Oops! Something went wrong.")

👉 Output:

Oops! Something went wrong.


---

🟢 Handling Specific Errors

Different problems have different error names. You can catch them separately.

try:
    num = int("Hello")  # this will cause ValueError
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("That was not a number")

👉 Output:

That was not a number


---

🟢 Using else with try...except

👉 else runs only if no error happens.

try:
    print("No error here")
except:
    print("Error happened")
else:
    print("Everything went fine")

👉 Output:

No error here
Everything went fine


---

🟢 Using finally

👉 finally runs no matter what (error or no error). Good for cleanup (like closing files).

try:
    x = 10 / 2
except:
    print("Error happened")
finally:
    print("This will always run")

👉 Output:

5.0
This will always run


---

🟢 Raising Your Own Errors

Sometimes you want to stop the program on purpose if something wrong happens.

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

👉 Output:

ValueError: Age cannot be negative


---

🟢 Custom Exceptions (Advanced but simple idea)

You can create your own error types for special cases.

class SalaryError(Exception):
    pass

def set_salary(amount):
    if amount < 0:
        raise SalaryError("Salary cannot be negative")
    else:
        print("Salary set to", amount)

try:
    set_salary(-5000)
except SalaryError as e:
    print("Custom Error:", e)

👉 Output:

Custom Error: Salary cannot be negative


---

🟢 Summary in Layman’s Terms

try → “Try to do this risky task”

except → “If error happens, do this instead”

else → “If no error, do this”

finally → “Always do this, error or not”

raise → “Create your own error”

custom exception → “Make your own error type for your own rules”



---

✅ So in simple words:
Error Handling in Python = making sure your program doesn’t break when something unexpected happens.


---

Would you like me to also give you a real WFM example (like handling errors when reading data, e.g., “file not found” or “zero calls forecasted”) so you can see how this works in your field?

