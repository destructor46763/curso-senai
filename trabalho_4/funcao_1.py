def celsius_para_fahrenheit(celsius):
    F = celsius * 1.8 + 32
    return f"{celsius}° celsius são: {f}° fahrenheit."

def fahrenheit_para_celsius(fahrenheit):
    c = ( fahrenheit - 32) / 1.8
    return f"(fahrenheit)° fahrenheit são {c}° celsius."

c = int(input("Qual a sua temperatura anal em celsius: "))
f = int(input("Qua a sua temperatura sexual em farenheits: "))

c = celsius_para_fahrenheit(c)
f = fahrenheit_para_celsius(f)

print(f)
print(c)