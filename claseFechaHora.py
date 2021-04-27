class FechaHora:
    #Atributos
    __dia = 0
    __mes = 0
    __anno = 0
    __hora = 0
    __min = 0
    __seg = 0
    __meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

    #Metodos
    def __init__(self,d=1,m=1,a=2020,h=0,mi=0,s=0):
        error = False
        if (m == 1 or m == 3 or m == 5 or m == 7 or m== 8 or m == 10 or m == 12) and (d < 1 or d > 31):
            print('Error: {} tiene 31 dias.'.format(self.__meses[m-1]))
            print('Reloj creado con parametros por defecto')
            error = True
        if (m == 4 or m == 6 or m == 9 or m == 11) and (d < 1 or d > 30):
            print('Error: {} tiene 30 dias.'.format(self.__meses[m-1]))
            print('Reloj creado con parametros por defecto')
            error = True
        if m == 2:
            esBisiesto = self.__detectarBisiesto(a)
            if esBisiesto and (d < 1 or d > 29):
                print('Error: Febrero bisiesto tiene hasta 29 dias')
                print('Reloj creado con parametros por defecto')
                error = True
            if not esBisiesto and (d < 1 or d > 28):
                print('Error: Febrero NO bisiesto tiene hasta 28 dias')
                print('Reloj creado con parametros por defecto')
                error = True
        if m < 1 or m > 12:
            print('Error: el mes debe estar entre 1 y 12.')
            print('Reloj creado con parametros por defecto')
            error = True
        if a < 0 or a > 9999:
            print('Error: el anio debe estar entre 0 y 9999.')
            print('Reloj creado con parametros por defecto')
            error = True
        if h < 0 or h >= 24:
            print('Error: las horas deben estar entre 0 y 23.')
            print('Reloj creado con parametros por defecto')
            error = True
        if mi < 0 or mi >= 60:
            print('Error: los minutos deben estar entre 0 y 59.')
            print('Reloj creado con parametros por defecto')
            error = True
        if s < 0  or s >= 60:
            print('Error: los segundos deben estar entre 0 y 59.')
            print('Reloj creado con parametros por defecto')
            error = True
        if error == False:        
            self.__dia = d
            self.__mes = m
            self.__anno = a
            self.__hora = h
            self.__min = mi
            self.__seg = s
            print('Reloj creado correctamente!')

    def Mostrar(self):
        #Formato de fecha: dd/mm/aaaa
        #Formato de hora: hh:mm:ss      
        print('Fecha: {}/{}/{}'.format(self.__dia,self.__mes,self.__anno))
        print('Hora: {}:{}:{}'.format(self.__hora,self.__min,self.__seg))

    def PonerEnHora(self,h=-1,m=-1,s=-1):
        if h >= 0 and h <= 23:
            self.__hora = h
            print('Hora modificada correctamente.')
        elif h != -1:
            print('Error: No se pudo modificar la hora.')

        if m >= 0 and m <= 59:
            self.__min = m
            print('Minutos modificados correctamente.')
        elif m != -1:
            print('Error: No se pudo modificar los minutos.')

        if s >= 0 and s <= 59: 
            self.__seg = s
            print('Segundos modificados correctamente.')
        elif s != -1:
            print('Error: No se pudo modificar los segundos.')
                     
    def AdelantarHora(self,h=0,m=0,s=0):
        anio = self.__anno
        mes = self.__mes
        dia = self.__dia
        hora = h + self.__hora
        min = m + self.__min
        seg = s + self.__seg

        valoresCorr = self.__corregirFechaHora(dia,mes,anio,hora,min,seg)
        self.__dia = valoresCorr[0]
        self.__mes = valoresCorr[1]
        self.__anno = valoresCorr[2]
        self.__hora = valoresCorr[3]
        self.__min = valoresCorr[4]
        self.__seg = valoresCorr[5]

    #Metodo para detectar anios bisiestos
    def __detectarBisiesto(self,a):
        esBisiesto = False
        if a % 4 == 0: #Resto 0 anio divisible por 4 
            if a % 100 == 0: #Si es divisible por 100 debe ser tambien por 400 
                if a % 400 == 0:
                    esBisiesto = True
            else:
                esBisiesto = True
        return esBisiesto

    #Metodo para corregir fecha que solo se utiliza al llamar al metodo AdelantarHora
    def __corregirFechaHora(self,d,m,a,h,mi,s):
        if s >= 60:
            minAdd = s // 60 #Cantidad de minutos a agregar (division entera)
            mi += minAdd
            s = s -  minAdd * 60 #Segundos que permanecen      
        if mi >= 60:
            horaAdd = mi // 60 #Cantidad de horas a agregar
            h += horaAdd
            mi = mi - horaAdd * 60
        if h >= 24:
            diaAdd = h // 24 #Cantidad de dias a agregar
            d += diaAdd
            h = h - diaAdd * 24
        #Correccion de mes, dia y anio
        mAdd = True   
        while mAdd:
            if (m == 1 or m == 3 or m == 5 or m == 7 or m== 8 or m == 10 or m == 12) and d > 31:
                m = m+1  
                d = d - 31  
            if (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
                m = m+1
                d = d - 30
            if m == 2 and self.__detectarBisiesto(a) and d > 29:
                m = m+1   
                d = d - 29
            if m == 2 and not self.__detectarBisiesto(a) and d > 28:
                m = m+1
                d = d - 28
            if m > 12:
                a += 1
                m = m - 12
            if (d <= 28) or (d == 31 and m == 1):
                mAdd = False
        return [d,m,a,h,mi,s]

    def getData(self):
        return [self.__anno,self.__mes,self.__dia,self.__hora,self.__min,self.__seg]
    
    #Sobrecarga de operadores
    def __add__(self,fechahora):
        if type(fechahora) == FechaHora:
            fecha1 = self.getData()
            fecha2 = fechahora.getData()
            fecha3 = []
            for i in range(len(fecha1)):
                fecha3.append(fecha1[i] + fecha2[i])
            fecha3 = self.__corregirFechaHora(fecha3[2],fecha3[1],fecha3[0],fecha3[3],fecha3[4],fecha3[5])
            return FechaHora(fecha3[0],fecha3[1],fecha3[2],fecha3[3],fecha3[4],fecha3[5])

    def __sub__(self,fechahora):
        if type(fechahora) == FechaHora:
            fecha1 = self.getData()
            fecha2 = fechahora.getData()
            seResta = False
            if fecha1[0] > fecha2[0]: #años no puedo restar años iguales para no tener año 0
                if fecha1[1] > fecha2[1]: #meses, idem a año
                    if fecha1[2] > fecha2[2]: #dias, idem a año
                        if fecha1[3] >= fecha2[3]: #horas, si puedo tener hora 0
                            if fecha1[4] >= fecha2[4]: #min, idem a hora
                                if fecha1[5] >= fecha2[5]: #seg, idem a hora
                                    seResta = True
            fecha3 = []
            if seResta:
                for i in range(len(fecha1)):
                    fecha3.append(fecha1[i] - fecha2[i])
                fecha = FechaHora(fecha3[2],fecha3[1],fecha3[0],fecha3[3],fecha3[4],fecha3[5])
            else:
                print('No se puede realizar la resta, se crea un objeto con parametros por defecto')
                fecha = FechaHora()
            return fecha

    def __gt__(self,fechahora):
        if type(fechahora) == FechaHora:
            fecha1 = self.getData()
            fecha2 = fechahora.getData()
            esMayor = False
            for i in range(len(fecha1)):
                if(fecha1[i] > fecha2[i]):
                    esMayor = True
                    break
            return esMayor
                