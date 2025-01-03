# Weight comvertion app in pyton

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds((lowercase) k or l): ")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight)}{unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is: {round(weight)}{unit}")
else:
    print(f"{unit} ::: Invalid choice")
    

if weight < 0:
    print(f"{weight} ::: Invalid choice")