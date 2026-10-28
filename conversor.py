# Função que converte uma temperatura de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Função que converte uma temperatura de Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius 