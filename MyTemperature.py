# programa para converter temperatura...
print("qual conversão você deseja realizar")
ESCOLHA = int(imput("1. Celcius / 2. Kelvin / 3. Fahrenheit:"))
TEMPERATURA = int(imput("Digite o valor da temperatura:"))

match ESCOLHA:
    Case 1:
        KELVIN = TEMPERATURA + 273
        FAHRENHEIT = (9 / 5 * TEMPERATURA) - 32
        print(f"A Conversão de Celcius para Kelvin será {KELVIN}.")
        print(f"A Conversão de celcius para fahrenheit será {FAHRENHEIT}.")
    Case 2:
        CELCIUS = TEMPERATURA - 273
        FAHRENHEIT = 1.8 * (TEMPERATURA - 273) + 32
        print(f"A Conversão de kelvin para Celcius será {CELCIUS}.")
        print(f"A Conversão de Kelvin para fahrenheit será {FAHRENHEIT}.")
    Case 3:
        CELCIUS = 5/9 * (TEMPERATURA - 32)
        KELVIN = (TEMPERATURA - 32) / 1.8 + 273
        print(f"A Conversão de fahrenheit para Celcius será {CELCIUS}.")
        print(f"A Conversão de fahrenheit para fahrenheit será {KELVIN}.")    



print("Converter de Celsius para Kelvin e Fahrenheit...")
CELSIUS = int(input("Digitr a temperatura:"))
KELVIN = CELSIUS + 273
FAHRENHEIT = (9 / 5 * CELSIUS) + 32
print(f"A temperatura em Kelvin será {KELVIN}.")
print(f"A temperatura em fahrenheit será {FAHRENHEIT}.")

# Seria possível utilizar as estruturas condicionais if/elif/else ou match/case,
# para personalizar este programa, deforma que ele ofereça as três conversões?
# Por exempo, ele poderia perguntar ao usuário qual a unidade de medida e qual
# valor de temperatura ele quer converter e a partir daí, realir os calculos
# necessários...
