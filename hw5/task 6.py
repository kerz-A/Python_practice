def bmi_info(hight, *mass):
    sum_mass = 0
    for i in mass:
        sum_mass += i

    avg_mass = sum_mass/len(mass)
    bmi = avg_mass / ((hight/100)**2)
    

    if bmi <= 18.5:
        return print(f'Your BMI: {bmi:.2f} \nIt can be classificate as Underweight \nRisk for your health is Minimal')
    
    elif 15.5 <= bmi <= 24.99:
        return print(f'Your BMI: {bmi:.2f} \nIt can be classificate as Normal \nRisk for your health is Minimal')
    
    elif 25 <= bmi <= 29.99:
        return print(f'Your BMI: {bmi:.2f} \nIt can be classificate as Overweight \nRisk for your health is Increased')

    elif 30 <= bmi <= 34.99:
        return print(f'Your BMI: {bmi:.2f} \nIt can be classificate as Obese \nRisk for your health is High')
        
    elif 35 <= bmi <= 39.99:
        return print(f'Your BMI: {bmi:.2f} \nIt can be classificate as Severely Obese \nRisk for your health is Very High')

    else:
        return print(f'Your BMI: {bmi:.2f} \nIt can be classificate as Morbidly Obese \nRisk for your health is Extremely High')


bmi_info(185, 115, 124)