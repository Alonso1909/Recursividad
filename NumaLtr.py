def NumaLtr(num): #Definomos nombre de metodo en base a la operacion a realizar
    Pos = 'Mas'
    Neg = 'Menos'

    if (num < 10 and num >= 0): #Caso base (para positivos)
        return Pos , num
    elif (num > -10 and num < 0): #Caso base (para negativos)
        return Neg , num
    else:
        if num < 0:
            return NumaLtr(int(num / 10)), num % -10 #Caso recursivo
        else:
            return NumaLtr(int(num / 10)), num % 10 #Caso recursivo

NumaLtr = NumaLtr(-123)
print(NumaLtr)