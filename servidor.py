import sys
import socket
import time
import smtpd, smtplib
import glob
import os
# -*- coding: utf-8 -*- 
import smtplib 


class Logger():

    def __init__(self):
              
               
        from __main__ import __dict__ as __dict
        self.__log = ''
        if '__version__' in __dict.keys():
            self.__script_vers = __dict['__version__']
        else:
            self.__script_vers = 'Unknown'
			
        self.__script_name = os.path.basename(__dict['__file__']).split('.')[0]
        
        #self.__script_name = os.path.basename(nm).split('.')[0]
        self.filename = '{0}.log'.format(self.__script_name)

    def __len__(self):
        return len(self.__log)

    def __format__(self, tit, cont, decor):

        ending = {'=':'', '_':os.linesep}[decor]
        end = {'=': '=' * 80, '_':''}[decor]
        begin = ' '.join([tit.upper(), (80 - (len(tit) + 1)) * decor]) + ending
        cont = [cont] if isinstance(cont, str) else cont
        sep = os.linesep
        self.__log += sep.join([begin, sep.join(cont), end, sep])

    def block(self, title, content):

        if content:
            self.__format__(title, content, '=')

    def list(self, title, content):

        if content:
            self.__format__(title, content, '_')

    def free(self, content):

        if isinstance(content, str):
            self.__log += content + os.linesep * 2

    def time(self, title):

        self.block(title, '{0:>80}'.format(time.strftime('%A %x, %X')))

    def header(self, url, msg):
        script = '{0} (ver. {1})'.format(self.__script_name, self.__script_vers)
        self.block('Script', [script, url, '', msg])

    def get(self):
        """Get the log content."""
        return self.__log


    def write(self, append=False):
        mode = 'ab' if append else 'wb'
        with open(self.filename, mode) as log_file:
            log_file.write(self.__log)



def conext(ruta,recibido2):
 global R
# Recibimos la longitud que envia el cliente

 recibido2 = sck.recv(1024).strip()
 recibir = recibido2.decode('utf-8') 
 if recibido2: 
  print "Recibido:", str(recibido2)
 else:
  R="NO SE RECIBIO BUFFER"


 if recibir.isdigit():		
  sck.send("OK")
  print 'ok'			
  # Inicializamos el contador que
  # guardara la cantidad de bytes recibidos
  buffer = 0

#inciooooooo
"""Main section"""
url = 'SERVICIOS Y SOLUCIONES INFORMATICAS'
head = 'LOGS DE SERVIDOR siag204'

CONEXION = ('', 9004)
servidor = socket.socket() 
servidor.bind(CONEXION)
servidor.listen(5)
while 1:
 print "Escuchando {0} en {1}".format(*CONEXION) 
 # Aceptamos conexiones
 sck, addr = servidor.accept()
 print "Conectado a: {0}:{1}".format(*addr)
 ar2=time.strftime("%Y-%m-%d")+"-"+time.strftime("%H%M%S")
 #ar2=time.strftime("%Y-%m-%d")+"-"time.strftime('%H%M%S')
 ips2="".format(*addr)
 global nm
 log = Logger()
 log.header(url, head)
 log.time('Iniciando Proceso') 
 log.free(time.strftime('%H:%M:%S')+"-"+"Escuchando {0} en {1}".format(*CONEXION)) 
 #log.free(time.strftime('%H:%M:%S')+"-"+"Conectado a: {0}:{1}".format(*addr))
 log.free(time.strftime('%H:%M:%S')+"-"+"Conectado a: {0}:{1}".format(*addr))
 recibido2 = sck.recv(1024)
 ar=recibido2.find("?")
 print "ca:   " + recibido2.rstrip("?")
 log.free(time.strftime('%H:%M:%S')+"-"+"Archivo: " + recibido2.rstrip("?"))
 if recibido2.find("NOMBRE")!= -1:
     rp="NOMBRE"
     rut = "rutadedescarga"+rp
     ruta=rut+recibido2
     
     if not os.path.exists(rut): os.makedirs(rut)
	
     os.chmod(rut, 0o777)

 print("Asignado a: "+rp)
 log.free(time.strftime('%H:%M:%S')+"-"+"Asignado a: "+rp)
 #ruta="c:\"+recibido2
 print("archivo: "+recibido2)
 #log.free(time.strftime('%H%M%S')+"-"+
 print("ruta: "+ruta)
 log.free(time.strftime('%H:%M:%S')+"-"+"ruta: "+ruta)
 file="" 
 #ruta2 = os.getcwd()
 #os.chdir(ruta)
 R=""
 for file in glob.glob(ruta):
  print "encontrado"
   
 if file !="":
   sck.send("existe")
   print "El archivo existe " +ruta
   log.free(time.strftime('%H:%M:%S')+"-"+"El archivo existe " +ruta)
   sck.send("Proceso terminado")
   R="Proceso terminado el archivo existe"
 else:
   sck.send("libre")
   print "El archivo no existe en ubicacion " +ruta
   log.free(time.strftime('%H:%M:%S')+"-"+"El archivo no existe en ubicacion" +ruta)
   conext(ruta,recibido2)  
conext(ruta)
servidor.close

 

