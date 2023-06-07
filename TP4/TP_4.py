class Maquina_Turing:
    def __init__(self):
        self.estados = {'q0', 'q1'}
        self.alfabeto_entrada = {'x', 'y', 'B'}
        self.alfabeto_cinta = {'x', 'y', 'B'}
        self.estado_inicial = 'q0'
        self.estado_aceptacion = 'q1'
        self.estado_rechazo = 'q_rechazo'
        self.transiciones = {
            ('q0', 'x'): ('q1', 'x', 'R'),
            ('q1', 'x'): ('q1', 'x', 'R'),
            ('q1', 'y'): ('q1', 'y', 'R')
        }

    def ejecutar(self, cadena):
        cinta = list(cadena)
        cinta.append('B')
        estado_actual = self.estado_inicial
        cabeza = 0

        while estado_actual != self.estado_aceptacion and estado_actual != self.estado_rechazo:
            if (estado_actual, cinta[cabeza]) in self.transiciones:
                estado_siguiente, simbolo_escrito, movimiento = self.transiciones[(estado_actual, cinta[cabeza])]
                cinta[cabeza] = simbolo_escrito

                if movimiento == 'R':
                    cabeza += 1
                elif movimiento == 'L':
                    cabeza -= 1

                estado_actual = estado_siguiente
            else:
                estado_actual = self.estado_rechazo

        return estado_actual == self.estado_aceptacion


# Ejemplo de uso
mt = Maquina_Turing()

cadena = 'xyxyyx'
resultado = mt.ejecutar(cadena)
print(f'La cadena "{cadena}" es {"válida" if resultado else "inválida"}')




class TuringMachine:
    def __init__(self):
        self.estados = {'S', 'A', 'B', 'C', 'R'}
        self.alfabeto_cinta = {'a', 'c', '$'}
        self.estado_inicial = 'S'
        self.estados_finales = {'B', 'C'}
        self.estado_rechazo = 'R'
        self.transiciones = {
            ('S', 'c'): ('B', 'a', 'R'),
            ('S', 'a'): ('A', 'a', 'R'),
            ('A', 'c'): ('C', 'c', 'R'),
            ('B', 'a'): ('A', 'a', 'R'),
            ('B', 'c'): ('B', 'c', 'R'),
            ('C', 'c'): ('B', 'c', 'R'),
            ('C', 'a'): ('A', 'a', 'R'),
            ('S', '$'): ('R', '$', 'R')
        }
    
    def validar_cadena(self, cadena):
        cinta = list(cadena) + ['$']
        estado_actual = self.estado_inicial
        cabeza = 0
        
        while estado_actual != self.estado_rechazo and estado_actual not in self.estados_finales:
            if (estado_actual, cinta[cabeza]) in self.transiciones:
                nuevo_estado, nuevo_simbolo, movimiento = self.transiciones[(estado_actual, cinta[cabeza])]
                cinta[cabeza] = nuevo_simbolo
                
                if movimiento == 'R':
                    cabeza += 1
                elif movimiento == 'L':
                    cabeza -= 1
                
                estado_actual = nuevo_estado
            else:
                return False
        
        return estado_actual in self.estados_finales


tm = TuringMachine()
cadena = 'cac'
es_valida = tm.validar_cadena(cadena)

if es_valida:
    print(f'La cadena "{cadena}" es válida.')
else:
    print(f'La cadena "{cadena}" es inválida.')


class TuringMachine_c:
    def __init__(self):
        self.estados = {'S', 'A', 'B', 'C', 'D'}
        self.alfabeto_entrada = {'a', 'b'}
        self.alfabeto_cinta = {'a', 'b', '$'}
        self.estado_inicial = 'S'
        self.estados_finales = {'C', 'D'}
        self.transiciones = {
            ('S', 'a'): ('D', 'a', 'R'),
            ('S', 'b'): ('A', 'b', 'R'),
            ('A', 'a'): ('D', 'a', 'R'),
            ('A', 'b'): ('B', 'b', 'R'),
            ('B', 'a'): ('C', 'a', 'R'),
            ('B', 'b'): ('B', 'b', 'R'),
            ('C', 'a'): ('D', 'a', 'R'),
            ('C', 'b'): ('B', 'b', 'R'),
            ('D', 'a'): ('D', 'a', 'R'),
            ('D', 'b'): ('C', 'b', 'R')
        }
    
    def validar_cadena(self, cadena):
        cinta = list(cadena) + ['$']
        estado_actual = self.estado_inicial
        cabeza = 0
        
        while estado_actual != 'R' and estado_actual not in self.estados_finales:
            if (estado_actual, cinta[cabeza]) in self.transiciones:
                nuevo_estado, nuevo_simbolo, movimiento = self.transiciones[(estado_actual, cinta[cabeza])]
                cinta[cabeza] = nuevo_simbolo
                
                if movimiento == 'R':
                    cabeza += 1
                elif movimiento == 'L':
                    cabeza -= 1
                
                estado_actual = nuevo_estado
            else:
                return False
        
        return estado_actual in self.estados_finales


tm = TuringMachine_c()
cadena = 'abba'
es_valida = tm.validar_cadena(cadena)

if es_valida:
    print(f'La cadena "{cadena}" es válida.')
else:
    print(f'La cadena "{cadena}" es inválida.')
