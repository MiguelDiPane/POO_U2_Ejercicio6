import os
class Menu:
    __opciones = []

    def __init__(self,opciones=[]):
        self.__opciones = opciones
  
    def define_menu(self,opciones):
        self.__opciones = opciones
  
    def selectOption(self):
        op = input('--> ')
        if op.isdigit():
            op = int(op)
            if op > len(self.__opciones) or op < 0:
                input('Opcion invalida, reintente')
                op = None         
        else:
            input('Error: Opcion invalida, debe ingresar un numero entero.')
            op = None
        return op
    
    def showMenu(self):
        self.clear_screen()
        print('#-----MENU-----#')
        for opcion in self.__opciones:
            print(opcion)

    def clear_screen(self):
        os.system(['clear','cls'][os.name == 'nt'])



               
