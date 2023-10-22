def calculate_bmi(weight_kg, height_cm):
    # Convert height from centimeters to meters
    height_m = height_cm / 100
    # Calculate BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)
    bmi = weight_kg / (height_m ** 2)
    return bmi

def calculate_bmi_with_age(bmi, age):
    if age < 18:
        return "BMI interpretation is not recommended for individuals under 18 years old."
    elif 18 <= age < 25:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
    elif 25 <= age < 65:
        if bmi < 22:
            return "Underweight"
        elif 22 <= bmi < 27:
            return "Normal Weight"
        elif 27 <= bmi < 32:
            return "Overweight"
        else:
            return "Obese"
    else:
        if bmi < 22:
            return "Underweight"
        elif 22 <= bmi < 27:
            return "Normal Weight"
        elif 27 <= bmi < 33:
            return "Overweight"
        else:
            return "Obese"
