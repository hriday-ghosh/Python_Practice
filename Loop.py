👉 A loop means repeating something again and again, until a condition is met.


---

🟢 1. for loop

Think of it like:
👉 “Go through each item in a list or range, one by one.”

Example:

for i in range(5):
    print(i)

➡ Output: 0 1 2 3 4
💡 It prints numbers from 0 to 4, one by one.


---

🟢 2. while loop

Think of it like:
👉 “Do this work until a condition becomes False.”

Example:

x = 0
while x < 5:
    print(x)
    x = x + 1

➡ Output: 0 1 2 3 4
💡 It keeps running as long as x < 5.


---

🟡 Extra Tools with Loops

break → Stop the loop immediately.

continue → Skip this round, go to the next.

pass → Do nothing (just a placeholder).


Example:

for i in range(5):
    if i == 3:
        continue   # skip 3
    print(i)

➡ Output: 0 1 2 4


---

🟣 Special Feature: loop with else

In Python, you can add an else after a loop.
👉 The else runs only if the loop finished normally (not stopped by break).

Example:

for i in range(3):
    print(i)
else:
    print("Done!")

➡ Output:

0
1
2
Done!


---

🎯 Super Simple Summary:

for loop → Use when you know how many times (like numbers in a list).

while loop → Use when you don’t know how many times (repeat until condition fails).

break → Stop loop.

continue → Skip one round.

else → Runs if loop finishes normally.


