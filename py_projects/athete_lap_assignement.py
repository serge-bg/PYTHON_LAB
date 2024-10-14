# Exercise
'''Task: Write a Python program that uses a list of four U.S. women athletes who have competed in the 400 meters at the Olympics. Your program should do the following:
1.	Create a list called athletes with the following names:
•	Allyson Felix
•	Sanya Richards-Ross
•	Shaunae Miller-Uibo
•	Phyllis Francis
2.	Use a for loop to display each athlete's name along with the lap number they completed. The output should be in the following format:
Lap 1: Allyson Felix has completed their lap!
Lap 2: Sanya Richards-Ross has completed their lap!
Lap 3: Shaunae Miller-Uibo has completed their lap!
Lap 4: Phyllis Francis has completed their lap!
Requirements:
•	Do not use the enumerate() function.
•	Use a counter variable to keep track of the lap number.
Bonus Challenge:
•	Modify your code to display a message at the end that says: "All athletes have completed their laps!"
Submission
Please submit your code  in a file named athlete_lap_assignment.py and upload it to gihub. Make sure to test your code to ensure it produces the correct output. '''

# operation
# 1: List of U.S. women athletes
athletes = ["Allyson Felix", "Sanya Richards-Ross", "Shaunae Miller-Uibo", "Phyllis Francis"]

# Initialize a counter for the lap number
lap_number = 1

# 2: Using a for loop to display each athlete's name along with the lap number
for athlete in athletes:
    print(f"Lap {lap_number}: {athlete} has completed their lap!")
    lap_number += 1  # To increment the lap number
    
    

# Bonus Challenge: final message
print("All athletes have completed their laps!")

