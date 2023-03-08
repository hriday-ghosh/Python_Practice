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
