# LAB 2
# Write a program that will ask for a user body weight in pound (Lbs) and convert it in kilogram (kg)
# Display on the screen: your body weight is: weight in lbs, and the equivalent in kgs is: weight kg . Thank you!
# (only display three digit decimal. Eg: 10.234)

# Solution

# My weight in pounds (lbs)
weight_lbs = float(input("tell your body weight in pounds (lbs): \n"))

# Weight conversion: 1 pound is approximately 0.453592 kilograms
weight_kg = weight_lbs * 0.453592

# Display the result with three decimal places
print(f"Your body weight is: {weight_lbs:.3f} lbs, and the equivalent in kgs is: {weight_kg:.3f} kg. Thank you!")
