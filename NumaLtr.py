def NumaLtr(num): #Definomos nombre de metodo en base a la operacion a realizar

    if (num < 10): #Caso base (para positivos)
        return num
    elif (num > -10): #Caso base (para negativos)
        return num
    else:
        return NumaLtr(int(num / 10)), num % 10 #Caso recursivo

NumaLtr = NumaLtr(123)
print(NumaLtr)