"""

notes = 5

i = 1
while i <= notes:
    print(f"Current Some {i*notes}")
i = i+1

notes = 5
i = 1
while i <= notes:
    print(f"Current Some {i*10}")
    i = i+1

For Loop:
for i in range(0, 10):
    print(f"10 X {i+1} = {10*(i+1)}")


for i in range(5, 10):
    print(i)




Cost_of_items = [150, 200, 300, 400]

total_sum = 0

for i in range(0, 3):
    total_sum = total_sum + Cost_of_items[0]

print(f"Amount to be paid {total_sum}")


for i in range(1, 5):
    print("*"*i)
    
    
    
    
    
 
"""


# stations = ["Stn1", "Stn2", "Stn3", "Stn4", "Stn5"]

# current_stations = 0

# dest_station = "Stn5"

# while stations[current_stations] != dest_station:
#     print(f" Current Stn is: {stations[current_stations]}")
# print(f"My dest is: {dest_station}")
# print("Continue the journey I haven't reached the destination")
# current_stations = current_stations+1

cost_items = [100, 200, 300, 550]
total_sum = 0
for costs_var in cost_items:
    total_sum = total_sum + costs_var
print(f"Total amount to be paid {total_sum}")
