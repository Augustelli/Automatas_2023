class Automata:
    def __init__(self):

        self.table = [[2, 1, 1, '', '', ''],
                      [2, '', '', '', '', ''], 
                      [2, '', '', 3, 5, 8], 
                      [4, '', '', '', '', ''], 
                      [4, '', '', '', 5, 8], 
                      [7, 6, 6, '', '', ''],
                      [7, '', '', '', '', ''],
                      [7, '', '', '', '', 8],
                      ['acepta', 'acepta', 'acepta', 'acepta', 'acepta', 'acepta']]
       
        self.state = 0
        self.number = input('Ingrese un número: ')
        for i in range(len(self.number)):
            if self.state == 0:
                if self.number[i] == '+' or self.number[i] == '-':
                    self.state = 1
                    continue
                    
                elif self.number[i].isdigit():
                    
                    self.state = 2
                    continue
                else:
                    print('No es un número')
                    return
                
            if self.state == 1:
                if self.number[i].isdigit():
                    
                    self.state = 2
                    continue
                else:
                    print('No es un número')
                    return
                
            if self.state == 2:
                if self.number[i].isdigit():
                    
                    self.state = 2
                    continue
                elif self.number[i] == '.':
                    
                    self.state = 3
                    continue
                elif self.number[i] == 'e' or self.number[i] == 'E':
                    
                    self.state = 5
                    continue
                elif self.number[i] == '$':
                    
                    self.state = 8
                    
                else:
                    print('No es un número')
                    return
                
            if self.state == 3:
                if self.number[i].isdigit():
                    
                    self.state = 4
                    continue
                else:
                    print('No es un número')
                    return
                
            if self.state == 4:
                if self.number[i].isdigit():
                    
                    self.state = 4
                    continue
                elif self.number[i] == 'e' or self.number[i] == 'E':
                    
                    self.state = 5
                    continue
                elif self.number[i] == '$':
                    
                    self.state = 8
                    
                else:
                    print('No es un número')
                    return
                
            if self.state == 5:
                if self.number[i] == '+' or self.number[i] == '-':
                    
                    self.state = 6
                    continue
                elif self.number[i].isdigit():
                    
                    self.state = 7
                    continue
                else:
                    print('No es un número')
                    return
                
            if self.state == 6:
                if self.number[i].isdigit():
                    
                    self.state = 7
                    continue
                else:
                    print('No es un número')
                    return
                
            if self.state == 7:
                if self.number[i].isdigit():
                    
                    self.state = 7
                    continue
                elif self.number[i] == '$':
                    
                    self.state = 8
                
                else:
                    print('No es un número')
                    return
          

            if self.state == 8:
                print('El número es correcto')
                return

if __name__ == '__main__':
    automata = Automata()



                   
              
