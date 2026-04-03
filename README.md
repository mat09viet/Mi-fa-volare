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

#include <Servo.h>

Servo motore1;
Servo motore2;
Servo motore3;
Servo motore4;

int throttle = 1000; // minimo (ESC di solito 1000-2000)

void setup() {
  motore1.attach(3);
  motore2.attach(5);
  motore3.attach(6);
  motore4.attach(9);

  // Arm ESC
  motore1.writeMicroseconds(1000);
  motore2.writeMicroseconds(1000);
  motore3.writeMicroseconds(1000);
  motore4.writeMicroseconds(1000);

  delay(5000); // tempo per armare
}

void loop() {
  // aumento graduale velocità
  for (throttle = 1000; throttle <= 1300; throttle += 5) {
    motore1.writeMicroseconds(throttle);
    motore2.writeMicroseconds(throttle);
    motore3.writeMicroseconds(throttle);
    motore4.writeMicroseconds(throttle);
    
    delay(50);
  }

  delay(3000);

  // spegnimento
  for (throttle = 1300; throttle >= 1000; throttle -= 5) {
    motore1.writeMicroseconds(throttle);
    motore2.writeMicroseconds(throttle);
    motore3.writeMicroseconds(throttle);
    motore4.writeMicroseconds(throttle);

    delay(50);
  }

  delay(5000);
}

-----

## Prossimi Passi

- [ ] Assemblare il telaio
- [ ] Collegare i motori brushless all’ESC
- [ ] Configurare il flight controller
- [ ] Caricare il codice sull’Arduino
- [ ] Testare il controllo via app / mini controller
- [ ] Primo volo di prova
