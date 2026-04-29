{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#comando da mettere sul terminale del PC\n",
    "pip install djitellopy opencv-python\n",
    "\n",
    "#codice iniziale per vedere lo stato del drone \n",
    "from djitellopy import Tello\n",
    "\n",
    "# 1. Inizializzazione\n",
    "drone = Tello()\n",
    "\n",
    "# 2. Connessione\n",
    "drone.connect()\n",
    "\n",
    "# 3. Controllo sicurezza (Stampa la batteria prima di partire)\n",
    "print(f\"Livello batteria: {drone.get_battery()}%\")\n",
    "\n",
    "# 4. Comandi di volo\n",
    "if drone.get_battery() > 20:\n",
    "    drone.takeoff()\n",
    "    \n",
    "    drone.move_up(50)\n",
    "    drone.rotate_clockwise(90)\n",
    "    \n",
    "    drone.land()\n",
    "else:\n",
    "    print(\"Batteria troppo bassa per decollare!\")\n",
    "\n",
    "\n",
    "#piccolo programma che fa alzare per adesso solamente il drone \n",
    "from djitellopy import Tello\n",
    "import time\n",
    "\n",
    "# Inizializza l'oggetto Tello\n",
    "drone = Tello()\n",
    "\n",
    "# Stabilisce la connessione con il drone\n",
    "drone.connect()\n",
    "\n",
    "# Controlla lo stato della batteria (sempre utile!)\n",
    "print(f\"Batteria: {drone.get_battery()}%\")\n",
    "\n",
    "# Decollo\n",
    "drone.takeoff()\n",
    "\n",
    "# Ruota di 90 gradi in senso orario\n",
    "drone.rotate_clockwise(90)\n",
    "\n",
    "# Vola avanti per 50 cm\n",
    "drone.move_forward(50)\n",
    "\n",
    "# Aspetta un secondo\n",
    "time.sleep(1)\n",
    "\n",
    "# Atterraggio\n",
    "drone.land()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
