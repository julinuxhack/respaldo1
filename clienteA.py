# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
import zipfile, os
import socket
import logging.handlers
import paramiko
import time, shutil
from datetime import datetime
from email.MIMEBase import MIMEBase
from win32com.shell import shell, shellcon
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def envio(ARCHIVO):
    try:
        CONEXION = ("direccion ip", 9004) #(socket.gethostname(), 9003)
        cliente = socket.socket()
        cliente.connect(CONEXION)
        cliente.send(ARCHIVO)
        recibido3 = cliente.recv(10)
    #print recibido3
        if recibido3 == "libre":
              print "NO EXISTE EL ARCHIVO CONTINUANDO CON EL ENVIO"
              es="L"
	#  recibido4 = cliente.recv(10)
	#  print recibido4 
        elif recibido3 == "existe":
              print "ERROR EXISTE EL ARCHIVO"
              es="N"
        else:
              print "ERROR GRAL"
              es="G"
    except:
        print ("nada, continuamos")
    
    a=0  
    buf2=0
    if es=="L": 
	print ("exitoso vamos en if es==L")
    
		
def makeArchive(fileList, archive):
    try:
        a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)
        for f in fileList:
            print "archiving file %s" % (f)
            a.write(f)
        a.close()
        return True
    except: return False
 
def dirEntries(dir_name, subdir, *args):

    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if not args:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
        # recursively access file names in subdirectories
        elif os.path.isdir(dirfile) and subdir:
            print "Accessing directory:", dirfile
            fileList.extend(dirEntries(dirfile, subdir, *args))
    return fileList
 
if __name__ == '__main__':
 fecha =   time.strftime("%Y%m%d")
 hora = time.strftime("%H%M%S")
 
 archivo1="NOMBRE-"+"otros"+fecha+hora + ".zip"
 folder = r"RUTA1"
 makeArchive(dirEntries(folder, True), archivo1)

 archivo2="NOMBRE-"+"factura"+fecha+hora + ".zip"
 folder = r"RUTA2"
 makeArchive(dirEntries(folder, True), archivo2)
 
 archivo3="NOMBRE-"+"ISS"+fecha+hora + ".zip"
 folder = r"RUTA3"
 makeArchive(dirEntries(folder, True), archivo3)

 archivo4="NOMBRE-"+"compag12"+fecha+hora + ".zip"
 folder = r"RUTA4"
 makeArchive(dirEntries(folder, True), archivo4)

 archivo5="NOMBRE-"+"INGRESOS12"+fecha+hora + ".zip"
 folder =r"RUTA5" 
 makeArchive(dirEntries(folder, True), archivo5)

 archivo6="NOMBRE-"+"factura12"+fecha+hora + ".zip"
 folder = r"RUTA6"
 makeArchive(dirEntries(folder, True), archivo6)

 archivo7="NOMBRE-"+"escritorio12"+fecha+hora + ".zip"
 folder = r"RUTA7"
 makeArchive(dirEntries(folder, True), archivo7)

 archivo8="NOMBRE-"+"app12"+fecha+hora + ".zip"
 folder =r"RUTA8" 
 makeArchive(dirEntries(folder, True), archivo8)

 archivo9="NOMBRE-"+"EMPRESA12"+fecha+hora + ".zip"
 folder = r"RUTA9"
 makeArchive(dirEntries(folder, True), archivo9)
 
 archivo10="NOMBRE-"+"ingresos13"+fecha+hora + ".zip"
 folder = "RUTA10"
 makeArchive(dirEntries(folder, True), archivo10)

 archivo11="NOMBRE-"+"LIBRERIA"+fecha+hora + ".zip"
 folder = r"RUTA11"
 makeArchive(dirEntries(folder, True), archivo11)
 
 archivo12="NOMBRE-"+"BD"+fecha+hora + ".zip"
 folder = r"RUTA12"
 makeArchive(dirEntries(folder, True), archivo12)

 archivo13="NOMBRE-"+"ORIGINAL"+fecha+hora + ".zip"
 folder = r"RUTA13"
 makeArchive(dirEntries(folder, True), archivo13)
 
 archivo14="NOMBRE-"+"SERVIDOR"+fecha+hora + ".zip"
 folder = r"RUTA14"
 makeArchive(dirEntries(folder, True), archivo14)
 
 lista = [archivo1,archivo2,archivo3,archivo4,archivo5,archivo6,archivo7,archivo8,archivo9,archivo10,archivo11,archivo12,archivo13,archivo14]


print ("Respaldo completo")
print ("comenzamos envio")
conteo = len(lista)
cantidad = 0
respaldados = str("lista correctos: ")
fallidos = str("fallidos: ")
try:
    for ARCHIVO  in lista:
        print ("enviando archivo: " + ARCHIVO)
        envio(ARCHIVO)
        time.sleep(5)
        print "Envio completo"


        print ('CONECTADO AL PUERTO 9002')
        print ('Inicia el cliente ssh')
        ssh_client = paramiko.SSHClient()
    # se establecen las politicas por defecto para aceptar las claes de forma local
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # nos conectamos al servidor
        ssh_client.connect(hostname='direccion ip', port=int('22'), username='usuariossh', password='passwordssh')
    # ejecutamos unicamente un comando para ver si realmente estamos conectados
    # entrada, salida, error = ssh_client.exec_command('ls')
        sftp = ssh_client.open_sftp()

    # mostramos el contenido de salida
    #  print salida.read()
    # procedemos a enviar el archivo
        archivos = sftp.listdir()
        cantidad = 0
        print ("probando error")
        try:

        #  creamos la ruta para la descarga de los archivos de respaldo, en donde cadenas es la
        # ruta enviada anteriormente para crearse en el servidor si no existiera
            print ("conectado inicia envio")
            directorio = 'rutadedescarga' + ARCHIVO
        # entrada, salida, error = ssh_client.exec_command('chmod 7777 ' + directorio)
            print ("conectado inicia envio")
            archivozip = 'rutadedescarga' + ARCHIVO
            sftp.put(ARCHIVO, archivozip)
            print "copiado archivo %s." % ARCHIVO
            cantidad = int(cantidad) + int(1)
            respaldado = (str(cantidad) + ".- " + ARCHIVO)
            respaldados= (respaldados + ', ' + respaldado) 

        except:
            print "Fallo al intentar copiar %s. Tal vez es un directorio." % archivos2
        # cerramos el cliente sftp
            cantidad = int(cantidad) + int(1)
            fallido = (str(cantidad) + ".- " + ARCHIVO)
            fallidos= (fallidos + ', ' + fallido)             
        sftp.close()
        ssh_client.close()
    comp=2

except:
    print ("nos salimos")
    comp=1

print "Borrando Backup"
for datos in lista:
    try:
        os.remove(datos)
        print "Se ha eliminado arcivo: "+datos
    except:
        print "nada"


#envio de correo
def main():
    from_address = "correoelectornicoremitente"
    to_address = "correoelectornicodestinatario" 
    mime_message = MIMEMultipart()
    if comp is 1:
	message = "problemas de conexion, entre el servidor 204 y el de respaldos"
    else:    
	message = "RESPALDADO CON EXITO, ESTOS SON LOS ARCHIVOS RESPALDADOS: " + respaldados + "\n" + "Los fallidos son: " + fallidos
    mime_message = MIMEText(message)
    mime_message["Subject"] = "cualquiercosa"
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    smtp = smtplib.SMTP("direcciondelsmtp", 587)
   # smtp = SMTP()
    smtp.ehlo()
    smtp.starttls()
#    smtp.ehlo()
    smtp.login(from_address, "passworddelcorreo")
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()    
    
  
if __name__ == "__main__":
    main()

#vaciamos la papeleria
shell.SHEmptyRecycleBin (
                         None,
                         None,
                         shellcon.SHERB_NOCONFIRMATION
                         | shellcon.SHERB_NOPROGRESSUI
                         | shellcon.SHERB_NOSOUND
                         )
#borrado de arcivos para 64 bits
print "Borrando Backup en c:\windows"
os.remove("C:\\Windows\\SysWOW64\\" + archivo1)
print "Se ha eliminado arcivo: "+archivo1
os.remove("C:\\Windows\\SysWOW64\\" + archivo2)
print "Se ha eliminado arcivo: "+archivo2
os.remove("C:\\Windows\\SysWOW64\\" + archivo3)
print "Se ha eliminado arcivo: "+archivo3
os.remove("C:\\Windows\\SysWOW64\\" + archivo4)
print "Se ha eliminado arcivo: "+archivo4
os.remove("C:\\Windows\\SysWOW64\\" + archivo5)
print "Se ha eliminado arcivo: "+archivo5
os.remove("C:\\Windows\\SysWOW64\\" + archivo6)
print "Se ha eliminado arcivo: "+archivo6
os.remove("C:\\Windows\\SysWOW64\\" + archivo7)
print "Se ha eliminado arcivo: "+archivo7
os.remove("C:\\Windows\\SysWOW64\\" + archivo8)
print "Se ha eliminado arcivo: "+archivo8
os.remove("C:\\Windows\\SysWOW64\\" + archivo9)
print "Se ha eliminado arcivo: "+archivo9
os.remove("C:\\Windows\\SysWOW64\\" + archivo10)
print "Se ha eliminado arcivo: "+archivo10
os.remove("C:\\Windows\\SysWOW64\\" + archivo11)
print "Se ha eliminado arcivo: "+archivo11
os.remove("C:\\Windows\\SysWOW64\\" + archivo12)
print "Se ha eliminado arcivo: "+archivo12
os.remove("C:\\Windows\\SysWOW64\\" + archivo13)
print "Se ha eliminado arcivo: "+archivo13
os.remove("C:\\Windows\\SysWOW64\\" + archivo14)
print "Se ha eliminado arcivo: "+archivo14



