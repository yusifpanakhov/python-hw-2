numbers = [80, 90, 70, 60, 100]

def calculate_average(values):
    if len(values) == 0:
        return 0  
    return sum(values) / len(values)  


average = calculate_average(numbers)

print("Orta bal:", average)
