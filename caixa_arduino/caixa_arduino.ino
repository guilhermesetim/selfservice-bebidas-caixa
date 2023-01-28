// Programa : RFID - Autosserviço de bebidas - Caixa

#include <SPI.h>
#include <MFRC522.h>

 
//Servo microservo9g;
#define SS_PIN 10 // Dados
#define RST_PIN 9 // Reset
// Definicoes pino modulo RC522
MFRC522 mfrc522(SS_PIN, RST_PIN); 


void setup() 
{
  // Inicia a serial
  Serial.begin(9600);
  // Inicia  SPI bus
  SPI.begin();
  // Inicia MFRC522
  mfrc522.PCD_Init(); 
}
void loop() 
{
  
  // Aguarda a aproximacao do cartao
  if ( ! mfrc522.PICC_IsNewCardPresent()) { return; }
  // Verifica se a tag foi aproximada no sensor
  if ( ! mfrc522.PICC_ReadCardSerial()) { return; }
  
  // Mostra UID na serial
  String id= "";
  //byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     id.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : "")); 
     id.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  
  Serial.println(id);
  delay(1000);
}
