import mysql.connector
import serial

from funcoes import *
from venda import Credito
from cadastro import Cadastro


# informações para conexão com o banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", # insira a senha do banco de dados
  database = "arduino"
)
# cursor do banco de dados
mycursor = mydb.cursor()


# teste de conexão serial
try:
  portaSerial = serial.Serial('/dev/ttyUSB', 9600, timeout = 3) # no windows -> COM
  portaSerial.isOpen()
  print ("conectado")
except serial.SerialException:
  print("Porta USB não detectada")



'''
  Aguarda informações da porta serial
'''
recebeuIdTag = False
while (not recebeuIdTag):
  # recebe dados do arduino
  serialValor = str(portaSerial.readline())
  
  # tratamento de dados
  data_arduino = tratamentoDadosbd(serialValor)  


  '''
    Porta serial recebeu informação id tag
  '''
  if (data_arduino[0] != ''):
    
    # enviar para função .execute como lista
    enviarBd = list(data_arduino)
    
    # consulta da tag no banco de dados
    mycursor.execute(f"SELECT * FROM clientes WHERE id = '{enviarBd[0]}' " )
    myresult = mycursor.fetchone()

    # condição de saída do loop
    recebeuIdTag = True


'''
  Verifiacação se a tag está cadastrada
'''
print(myresult)
if (myresult == None):
  Cadastro(enviarBd[0], mycursor, mydb)
else:
  Credito(myresult, mycursor, mydb)


'''
  Fechamento da comunicação com banco de dados
'''
mycursor.close()
mydb.close()
print("Comunicação com banco de dados e arduino encerrada !")
