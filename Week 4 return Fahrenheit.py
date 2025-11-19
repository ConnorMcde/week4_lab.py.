"""
week4_lab.py Python program that converts a temperature from Celsius to Fahrenheit. and returns it
"""


def celsius_to_fahrenheit(Celsius_Temp):
 Fahrenheit = (Celsius_Temp * 9/5) + 32 #formula for conversion having the celsius times by 9/5 then adding 32
 return Fahrenheit

Celsius_Temp = 25
f_temp = celsius_to_fahrenheit(Celsius_Temp)
print(f"{Celsius_Temp}C is equal to {f_temp}F")