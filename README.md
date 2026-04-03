# Mi Fa Volare — Progetto Drone con Arduino

## Descrizione

In questo progetto realizzeremo un **drone** che, tramite un Arduino, possa volare ed essere comandato da un controller.

**Obiettivo minimo:** far muovere le pale tramite un’app o un mini controller.

-----

## Componenti

|Quantità|Componente        |
|--------|------------------|
|4x      |Eliche            |
|1x      |sensore IMU       |
|1x      |Arduino           |
|1x      |Telaio            |
|1x      |Batteria          |   
|4x      |motori bruchhless |
|1x      |Flight controller |

-----

## Codice Arduino

```cpp
#include <Wire.h>
#include <Servo.h>

// ESC / Motori
Servo m1;
Servo m2;
Servo m3;
Servo m4;

// MPU6050
int MPU = 0x68;

// Dati sensore
float AccX, AccY, AccZ;
float angoloX, angoloY;

// Throttle base
int throttle = 1100;

void setup() {
  Wire.begin();

  // Inizializza MPU6050
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

  // Motori
  m1.attach(3);
  m2.attach(5);
  m3.attach(6);
  m4.attach(9);

  // Arm ESC
  m1.writeMicroseconds(1000);
  m2.writeMicroseconds(1000);
  m3.writeMicroseconds(1000);
  m4.writeMicroseconds(1000);

  delay(5000);
}

void loop() {
  // Lettura accelerometro
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 6, true);

  AccX = (Wire.read() << 8 | Wire.read()) / 16384.0;
  AccY = (Wire.read() << 8 | Wire.read()) / 16384.0;
  AccZ = (Wire.read() << 8 | Wire.read()) / 16384.0;

  // Calcolo inclinazione
  angoloX = atan(AccY / sqrt(AccX * AccX + AccZ * AccZ)) * 180 / PI;
  angoloY = atan(-AccX / sqrt(AccY * AccY + AccZ * AccZ)) * 180 / PI;

  // Correzioni
  int correzioneX = angoloX * 3;
  int correzioneY = angoloY * 3;

  // Mix motori
  int m1_speed = throttle + correzioneX - correzioneY;
  int m2_speed = throttle - correzioneX - correzioneY;
  int m3_speed = throttle - correzioneX + correzioneY;
  int m4_speed = throttle + correzioneX + correzioneY;

  // Limiti
  if (m1_speed < 1000) m1_speed = 1000;
  if (m2_speed < 1000) m2_speed = 1000;
  if (m3_speed < 1000) m3_speed = 1000;
  if (m4_speed < 1000) m4_speed = 1000;

  if (m1_speed > 2000) m1_speed = 2000;
  if (m2_speed > 2000) m2_speed = 2000;
  if (m3_speed > 2000) m3_speed = 2000;
  if (m4_speed > 2000) m4_speed = 2000;

  // Scrittura
  m1.writeMicroseconds(m1_speed);
  m2.writeMicroseconds(m2_speed);
  m3.writeMicroseconds(m3_speed);
  m4.writeMicroseconds(m4_speed);

  delay(10);
}

-----

## Prossimi passi

- [ ] Assemblare il telaio
- [ ] Collegare i motori brushless all’ESC
- [ ] Configurare il flight controller
- [ ] Caricare il codice sull’Arduino
- [ ] Testare il controllo via app / mini controller
- [ ] Primo volo di prova
