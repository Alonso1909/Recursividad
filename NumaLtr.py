# Autor:: Victor Manuel Cervantes Alonso 18930195

class ConversorNumLtr:#Definomos nombre de la clase y variables a las
        # que les asignamos lo que nesecitamos, los nombres en base
        # a la operacion a realizar o a lo que almacenaran
    __tex = ['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco',
           'Seis', 'Siete', 'Ocho', 'Nueve']
    __Pos = 'Mas'
    __Neg = 'Menos'
    __auxBP = str
    __auxBN = str
    __auxRP = str
    __auxRN = str
    __ret = str

    def NumaLtr(self,num): #Definomos nombre de metodo y la varible de
        # entrada que se ocupara en todos los procesos
        if (num < 10 and num >= 0): #Caso base (para positivos)
            self.__casoBP = self.__Pos + ' : ' + self.__tex[num]
            return self.__casoBP
        elif (num > -10 and num < 0): #Caso base (para negativos)
            self.__auxBN = self.__Neg + ' : ' + self.__tex[num * -1]
            return self.__auxBN
        else:
            if num < 0: #Caso recursivo negativo
                self.__auxRN = self.NumaLtr(int(num / 10)) + ', ' + self.__tex[num % -10 * -1]
                return self.__auxRN
            else: #Caso recursivo positivo
                self.__auxRP = self.NumaLtr(int(num / 10)) + ', ' + self.__tex[num % 10]
                return self.__auxRP

NumLtr = ConversorNumLtr()
print(NumLtr.NumaLtr(123))
