""" for debugging purpose like is the add result working is or not we can use print function here, but instead of print funtion we need to use logging.debug(var_name) here 

import logging

logging.basicConfig(level=logging.DEBUG)


def add(a, b):
    return a+b


def multiply(a, b):
    return a*b


num_1 = 10
num_2 = 20

# We can write in this way for calling function.
# print(add(num_1, num_2))

add_result = add(num_1, num_2)
logging.debug(add_result)
add_multiply = multiply(num_1, num_2)
logging.debug(add_multiply)

Logging Levels:

1. Debug: Release information useful for debuggig purposes.
2. Info: Provides the information regarding that things are working as we want. 
3. Warning: used to get warn that something happend unexpectedly.
4. Error: used to inform when we are in serious issue.
5. Critical: used to inform when we are in serious issue.
6. Not set: 

Some functions in logging module: 

debug():
info():
warning():
error():
critical():
exception():    

"""

import logging
"""logging.basicConfig(filename="appy.log",
                    level=logging.INFO,
                    filemode="w",  # w means write mode.
                    # changing the format mode and s - means string mode.
                    format=" %(asctime)s:%(name)s:%(levelname)s:%(message)s:%(process)s",
                    datefmt="%d-%b-%y %H:%M:%S")  # datefmt means putting a date format.

# %()s -> Format
# asctime = means figuring date
# we can change swipe the message positions as well.
"""
logging.basicConfig(filename="appy.log",
                    level=logging.INFO,
                    filemode="w",  # w means write mode.
                    # changing the format mode and s - means string mode.
                    style="{",
                    # we can write %(asctime)s => to {asctime}, just we need to style="{"
                    format="{asctime}: {name}:{levelname}:{message}:{process}",
                    datefmt="%d-%b-%y %H:%M:%S")  # datefmt means putting a date format.


"""
Once we write the filename = fileName.log then new file will be created. If we want to log the message into the log file then we need to create the filename = FileName.log thing
"""


logging.debug("This is a debug message")  # Lvl: 10
logging.info("Module 2 ended, now module 3 started")  # Lvl: 20
logging.warning("The warning message is warning")  # Lvl: 30
logging.error("The error message is displaying")  # Lvl: 40
logging.critical("The critical message is displaying")  # Lvl: 50


"""
Level Theory:

If we set level 50 then previous function wont work like Lvl40, Lvl30, Lvl20, Lvl10 wont work. 

If we write (level = logging.DEBUG) then we can debug function will acrive despite being in Lvl 10.

Log Message:
level:name:message

"""


""""
Output:

WARNING:root:The warning message is warning
ERROR:root:The error message is displaying
CRITICAL:root:The critical message is displaying

Output after putting (level=logging.DEBUG)

DEBUG:root:This is a debug message
INFO:root:Module 2 ended, now module 3 started
WARNING:root:The warning message is warning
ERROR:root:The error message is displaying
CRITICAL:root:The critical message is displaying

Output after putting (level=logging.INFO)

INFO:root:Module 2 ended, now module 3 started
WARNING:root:The warning message is warning
ERROR:root:The error message is displaying                                                                                            DEBUG:root:Thisi is a debug mes
CRITICAL:root:The critical message is displaying


After putiing (level=logging.INFO), we can check that debugging function is not working.


"""


# create a custom logger

logger = logging.getLogger(__name__)

# create handlers

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("abc.log")
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# create formatters and add it to handler

c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
c_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

c_handler.setFormatter(c_format)
c_handler.setFormatter(f_format)


# Add Handler to the logger

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("this is a warning")
logger.error("This is Error")



#####################################################



logger = logging.getLogger(__name__) 

# create handlers

c_handler = logging.StreamHandler() 
f_handler = logging.FileHandler("abc.log") 
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# create formatters and add it to handler

c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
c_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

c_handler.setFormatter(c_format)
c_handler.setFormatter(f_format)


# Add Handler to the logger

logger.addHandler(c_handler) 
logger.addHandler(f_handler)

logger.warning("this is a warning")
logger.error("This is Error")


Perfect question 🙌 Let’s break Logging and Debugging in Python into very easy and layman’s language, with all the important syntax + types.


---

🟢 1. Debugging in Python

👉 Debugging = finding and fixing errors (bugs) in your code.
It’s like checking why your washing machine is not working — open it, see what’s wrong, and fix it.


---

🔹 Ways to Debug in Python

(a) Using print() (Basic way)

You just print values to check what’s happening.

def add(a, b):
    print("a =", a)   # debugging
    print("b =", b)
    return a + b

result = add(5, 10)
print("Result:", result)

👉 Output:

a = 5
b = 10
Result: 15

✅ Good for small scripts, but messy in big projects.


---

(b) Using Python Debugger (pdb)

pdb lets you pause the program and check values step by step.

import pdb

def divide(a, b):
    pdb.set_trace()   # sets a breakpoint
    return a / b

print(divide(10, 2))

👉 When you run, program will stop at set_trace() and you can type commands:

n → next line

c → continue

p a → print value of variable a



---

(c) Using IDE Debugger (like PyCharm, VS Code)

You can click on the left side (red dot = breakpoint).

Run in debug mode → program stops at breakpoint → check variables.



---

🟢 2. Logging in Python

👉 Logging = keeping a record of what your program is doing (like CCTV for your code 👀).

Instead of print(), use logging because it’s more professional.

Logs can be saved in a file for later analysis.



---

🔹 Basic Syntax

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is critical")

👉 Output:

DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning
ERROR:root:This is an error
CRITICAL:root:This is critical


---

🔹 Logging Levels (Types)

From lowest → highest severity:

1. DEBUG → Detailed info (for developers, like step-by-step values).


2. INFO → Normal events (program started, function completed).


3. WARNING → Something unusual, but not breaking.


4. ERROR → Problem occurred, program can continue.


5. CRITICAL → Very serious error, program may stop.




---

🔹 Logging into a File

import logging

logging.basicConfig(
    filename="app.log",       # save logs in file
    level=logging.DEBUG,      # log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("Low disk space")
logging.error("File not found")

👉 This will create a file app.log like:

2025-09-01 12:00:00,123 - INFO - Program started
2025-09-01 12:00:01,456 - WARNING - Low disk space
2025-09-01 12:00:02,789 - ERROR - File not found


---

🔹 Custom Logger (Multiple Loggers)

import logging

# Create a logger
logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

# Create handler
file_handler = logging.FileHandler("myapp.log")
formatter = logging.Formatter("%(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)

# Logging
logger.debug("Debugging info")
logger.info("App is running")
logger.error("Something went wrong")


---

🟢 Summary (Layman’s Words)

Debugging → Fixing bugs by checking values step by step.

Small → use print()

Medium → use pdb

Big projects → use IDE debugger.


Logging → Recording everything your program does.

DEBUG → detail

INFO → normal

WARNING → unusual

ERROR → problem

CRITICAL → crash



👉 Debugging = fixing now
👉 Logging = keeping record for later


---

Would you like me to also prepare a real WFM example (like logging “Forecast started”, “Data missing”, “Forecast completed”) so you see how it applies to your domain?

