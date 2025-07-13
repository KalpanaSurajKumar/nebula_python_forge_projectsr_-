def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your body type is: {classify_bmi(bmi)}")

if __name__ == "__main__":
    main()