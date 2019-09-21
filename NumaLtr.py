def NumaLtr(num): #Definomos nombre de metodo y variables a las
    # que les asignamos lo que nesecitamos, los nombres en base
    # a la operacion a realizar o a lo que almacenaran

    tex = ['Cero','Uno','Dos','Tres','Cuatro','Cinco',
           'Seis','Siete','Ocho','Nueve']
    Pos = 'Mas'
    Neg = 'Menos'

    if (num < 10 and num >= 0): #Caso base (para positivos)
        return Pos , tex[num]
    elif (num > -10 and num < 0): #Caso base (para negativos)
        return Neg , tex[num]
    else:
        if num < 0: #Caso recursivo negativo
            return NumaLtr(int(num / 10)), tex[num % -10]
        else: #Caso recursivo positivo
            return NumaLtr(int(num / 10)), tex[num % 10]

NumaLtr = NumaLtr(0)
print(NumaLtr)