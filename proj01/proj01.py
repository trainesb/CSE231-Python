#input rods and convert from string to float

rods_str = input ("Input rods: ")
rods_float = float( rods_str )

#convert rods to meters, feet, miles, furlongs, and time in min to walk distance

meters = rods_float * 5.0292
feet = meters / 0.3048
miles = meters / 1609.34
furlongs = rods_float / 40
time = (miles / 3.1)*60

#print conversians

print("You input", rods_float, "rods.")
print("Conversions", "Meters:", round(meters, 3), "Feet:", round(feet,3), "Miles:", round(miles,3), "Furlongs:", round(furlongs,3), "Minutes to walk", rods_float, "rods:", round(time,3))