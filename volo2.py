import time
from djitellopy import Tello

def mostra_comandi():
    print("\n--- COMANDI DISPONIBILI ---")
    print("decollo : Fa decollare il drone")
    print("atterra : Fa atterrare il drone")
    print("avanti  : Si muove in avanti di 100 cm")
    print("indietro: Si muove all'indietro di 100 cm")
    print("destra  : Si muove a destra di 100 cm")
    print("sinistra: Si muove a sinistra di 100 cm")
    print("batteria: Mostra la percentuale della batteria")
    print("fine    : Chiude il programma (fa atterrare il drone per sicurezza)")
    print("---------------------------\n")

def main():
    # Inizializzazione del drone
    drone = Tello()
   
    print("Connessione al Tello in corso...")
    try:
        drone.connect()
        print(f"Connessione riuscita! Batteria residua: {drone.get_battery()}%")
    except Exception as e:
        print(f"Errore di connessione: {e}")
        print("Assicurati di essere connesso al Wi-Fi del Tello!")
        return

    mostra_comandi()

    while True:
        # Legge il comando inserito dall'utente nel terminale
        comando = input("Inserisci comando >> ").lower().strip()

        if comando == "decollo":
            print("Decollo...")
            drone.takeoff()
        elif comando == "atterra":
            print("Atterraggio...")
            drone.land()
        elif comando == "avanti":
            drone.move_forward(100)
        elif comando == "indietro":
            drone.move_back(100)
        elif comando == "destra":
            drone.move_right(100)
        elif comando == "sinistra":
            drone.move_left(100)
        elif comando == "batteria":
            print(f"Batteria: {drone.get_battery()}%")
        elif comando == "fine":
            print("Chiusura del programma. Atterraggio di sicurezza...")
            drone.land()
            break
        else:
            print("Comando non riconosciuto.")
            mostra_comandi()

if __name__ == "__main__":
    main()
