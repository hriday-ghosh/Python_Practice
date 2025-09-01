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


Perfect 👍 Let’s make Error Handling examples in Python for WFM (Workforce Management).
These are realistic situations you might face in forecasting, scheduling, or reporting.


---

🟢 1. File Not Found (Loading Forecast File)

try:
    f = open("forecast_data.csv", "r")
    data = f.read()
except FileNotFoundError:
    print("⚠ Forecast file not found! Please check the file path.")

👉 Useful if someone forgets to keep the forecast file in the right folder.


---

🟢 2. Wrong Data Type in Forecast

try:
    forecast = int("JanForecast")   # someone typed text instead of a number
except ValueError:
    print("⚠ Forecast data is not a number. Please check the input file.")

👉 Prevents crashing if input is text instead of numeric.


---

🟢 3. Division by Zero (AHT / Shrinkage Calculation)

try:
    calls = 100
    agents = 0
    workload = calls / agents
except ZeroDivisionError:
    print("⚠ No agents available. Cannot calculate workload.")

👉 Common when someone mistakenly enters 0 agents in capacity plan.


---

🟢 4. Using else and finally (Schedule Publishing)

try:
    print("Publishing schedule...")
    # pretend success
    status = "success"
    if status != "success":
        raise Exception("Schedule not published")
except Exception as e:
    print("⚠ Error:", e)
else:
    print("✅ Schedule published successfully")
finally:
    print("ℹ Process finished, check the log file")

👉 Ensures schedules are either confirmed or error logged.


---

🟢 5. Raise Your Own Error (Negative Headcount)

def set_headcount(value):
    if value < 0:
        raise ValueError("⚠ Headcount cannot be negative")
    print("Headcount set to:", value)

try:
    set_headcount(-10)
except ValueError as e:
    print("Error:", e)

👉 Prevents wrong planning input (negative staff).


---

🟢 6. Custom Exception (Forecast Error)

class ForecastError(Exception):
    pass

def load_forecast(value):
    if value <= 0:
        raise ForecastError("⚠ Forecast must be greater than zero")
    return value

try:
    forecast = load_forecast(0)
except ForecastError as e:
    print("Custom Error:", e)

👉 WFM often requires validating that forecast ≠ 0.


---

🟢 7. Using assert (Quick Sanity Check on Shrinkage %)

shrinkage = 120  # invalid percentage
assert 0 <= shrinkage <= 100, "⚠ Shrinkage % must be between 0 and 100"

👉 Stops the program immediately if shrinkage % is out of range.


---

🟢 8. Catching Any Error in Automation Script

try:
    # pretend automation steps
    f = open("absenteeism.csv", "r")
    data = f.read()
    rate = 100 / 0
except Exception as e:
    print("⚠ Automation failed. Error:", e)

👉 This way you always get a proper message, instead of script crash.


---

✅ So, in WFM context:

FileNotFoundError → Forecast / Schedule file missing

ValueError → Wrong data input (text instead of number)

ZeroDivisionError → No agents, shrinkage = 0, etc.

raise → Prevent negative headcount or invalid forecast

Custom Exception → Define your own WFM rules (e.g., occupancy limit exceeded)

assert → Quick sanity checks (forecast > 0, shrinkage between 0–100)



---