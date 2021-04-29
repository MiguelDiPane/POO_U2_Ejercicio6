import csv
import time
from claseFechaHora import FechaHora
from claseMenu import Menu

#Funcion test para verificar fechas erroneas y funciones de modificacion del reloj
def test():
    #Evaluo distintas fechas mal ingresadas
    print('TEST DE LECTURA DE FECHAS Y HORAS.')
    nombreArch = 'fechaHoraTest.csv'
    time.sleep(0.5)
    print('Lectura archivo: {}'.format(nombreArch))
    archivo = open(nombreArch)
    reader = csv.reader(archivo,delimiter=',')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            time.sleep(0.5)
            dia = int(fila[0])
            mes = int(fila[1])
            anio = int(fila[2])
            hora = int(fila[3])
            min = int(fila[4])
            seg = int(fila[5])          
            rt1 = FechaHora(dia,mes,anio,hora,min,seg)
    archivo.close()
    input('Presione ENTER para continuar...')
    print('TEST DE SUMA')
    #Testeo suma:
    print('Fecha 1: ',end='')
    rt1 = FechaHora(31,12,1999,23,59,59)
    rt1.Mostrar()
    print('Fecha 2: ',end='')
    rt2 = FechaHora(31,12,2001,23,59,59)
    print('Resultado esperado: 1/2/4002 - 23:59:58')
    print('Suma: ',end='')
    rt3 = rt1 + rt2
    rt3.Mostrar()
    print('Test finalizado.')


#Funcion para pedir los datos de la fecha y hora
def pedirDatos():
    d = int(input('Ingrese dia: '))
    m = int(input('Ingrese mes: '))
    a = int(input('Ingrese anio: '))
    h = int(input('Ingrese horas: '))
    min = int(input('Ingrese minutos: '))
    s = int(input('Ingrese segundos: '))
    return [d,m,a,h,min,s]

if __name__ == '__main__':
    menu = Menu()
    menu.define_menu(['[1]- Sumar','[2]- Restar','[3]- Mayor','[4]- Funcion test','[5]- Salir'])
    menu.showMenu()
    op = menu.selectOption()

    while op != 5:
        if op != 4:
            print('FECHA 1')
            fecha1 = pedirDatos()
            r1 = FechaHora(fecha1[0],fecha1[1],fecha1[2],fecha1[3],fecha1[4],fecha1[5])
            r1.Mostrar()
            print('FECHA 2')
            fecha2 = pedirDatos()    
            r2 = FechaHora(fecha2[0],fecha2[1],fecha2[2],fecha2[3],fecha2[4],fecha2[5])
            r2.Mostrar()
        if op == 1:
            r3 = r1 + r2
            r3.Mostrar()
            input('Presione ENTER para continuar...')
        elif op == 2:
            r3 = r1 - r2
            if r3 != None:
                r3.Mostrar()
            input('Presione ENTER para continuar...')
        elif op == 3:
            if r1 > r2:
                print('La fecha 1 es mayor a la 2')
            else:
                print('La fecha 1 NO es mayor a la 2')
            input('Presione ENTER para continuar...')
        elif op == 4:
            test()
            input('Presione ENTER para continuar...')
        menu.showMenu()
        op = menu.selectOption()

