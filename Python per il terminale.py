import time
from djitellopy import Tello
import keyboard

# Inizializzazione del drone Tello
drone = Tello()

print("Connessione al Tello in corso...")
drone.connect()
print(  # Stats della batteria per sicurezza
    f"Connessione stabilita! Batteria residua: {drone.get_battery()}%"
)


def esegui_comando_vocale(comando):
    """Gestisce i comandi testuali/direzionali (es.

    'avanti', 'indietro').
    """
    comando = comando.lower().strip()
    spostamento = 100  # 100 cm come richiesto

    if comando == "avanti":
        print(f"Eseguo: Avanti di {spostamento}cm")
        drone.move_forward(spostamento)
    elif comando == "indietro":
        print(f"Eseguo: Indietro di {spostamento}cm")
        drone.move_back(spostamento)
    elif comando == "sinistra":
        print(f"Eseguo: Sinistra di {spostamento}cm")
        drone.move_left(spostamento)
    elif comando == "destra":
        print(f"Eseguo: Destra di {spostamento}cm")
        drone.move_right(spostamento)
    else:
        print("Comando non riconosciuto.")


def disegna_lettera(lettera):
    """Disegna le lettere dell'alfabeto nello spazio aereo."""
    lettera = lettera.upper()
    print(f"\n--- Disegno la lettera: {lettera} ---")

    # Dimensione dei tratti per il disegno della lettera
    tratto_lungo = 100
    tratto_corto = 50

    if lettera == "L":
        # Lettera L: va giù (indietro) e poi a destra
        drone.move_back(tratto_lungo)
        drone.move_right(tratto_corto)

    elif lettera == "A":
        # Lettera A semplificata: diagonale sinistra (avanti+sinistra), diagonale destra, ecc.
        # Per semplicità con movimenti ortogonali:
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)
        # Torna a metà per la sbarretta centrale
        drone.move_forward(tratto_corto)
        drone.move_left(tratto_corto)

    elif lettera == "T":
        drone.move_forward(tratto_lungo)
        drone.move_left(tratto_corto)
        drone.move_right(tratto_lungo)

    elif lettera == "H":
        drone.move_forward(tratto_lungo)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_back(tratto_lungo)

    elif lettera == "E":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_corto)

    # --- NUOVE LETTERE AGGIUNTE ---

    elif lettera == "B":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_left(tratto_corto)

    elif lettera == "C":
        drone.move_right(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)

    elif lettera == "D":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)
        drone.move_left(tratto_corto)

    elif lettera == "F":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_corto)

    elif lettera == "G":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_back(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_left(tratto_corto)

    elif lettera == "I":
        drone.move_forward(tratto_lungo)

    elif lettera == "J":
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_lungo)

    elif lettera == "K":
        drone.move_forward(tratto_lungo)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_down(tratto_corto)  # Usiamo giù/su per le diagonali simulate
        drone.move_right(tratto_corto)

    elif lettera == "M":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)

    elif lettera == "N":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)
        drone.move_forward(tratto_lungo)

    elif lettera == "O":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)
        drone.move_left(tratto_corto)

    elif lettera == "P":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_left(tratto_corto)

    elif lettera == "Q":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)
        drone.move_left(tratto_corto)
        drone.move_right(tratto_corto)
        # Piccolo trattino della Q
        drone.move_back(tratto_corto)

    elif lettera == "R":
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_corto)

    elif lettera == "S":
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_right(tratto_corto)

    elif lettera == "U":
        drone.move_forward(tratto_lungo)
        drone.move_back(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_lungo)

    elif lettera == "V":
        # Semplificata ortogonale (scende dritta, va a destra, sale dritta)
        drone.move_forward(tratto_lungo)
        drone.move_back(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_lungo)

    elif lettera == "W":
        drone.move_forward(tratto_lungo)
        drone.move_back(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_corto)
        drone.move_forward(tratto_lungo)

    elif lettera == "X":
        # Disegno a "scatola aperta" o incrocio ortogonale
        drone.move_forward(tratto_lungo)
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)
        drone.move_forward(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_right(tratto_lungo)

    elif lettera == "Y":
        drone.move_forward(tratto_corto)
        drone.move_left(tratto_corto)
        drone.move_forward(tratto_corto)
        drone.move_back(tratto_corto)
        drone.move_right(tratto_lungo)
        drone.move_forward(tratto_corto)

    elif lettera == "Z":
        drone.move_right(tratto_corto)
        drone.move_back(tratto_lungo)  # Diagonale simulata ortogonalmente
        drone.move_left(tratto_corto)
        drone.move_right(tratto_corto)

    else:
        print(
            f"La lettera {lettera} non è ancora stata programmata in questo esempio."
        )


def gestisci_tastiera(event):
    """Funzione che si attiva ogni volta che si preme un tasto."""
    tasto = event.name.upper()

    # Tasti di controllo decollo e atterraggio di sicurezza
    if tasto == "SPACE":
        print("Decollo!")
        drone.takeoff()
    elif tasto == "ESC":
        print("Atterraggio di emergenza!")
        drone.land()
        print("Programma terminato.")
        keyboard.unhook_all()
        exit()

    # Se il drone è in volo, reagisce alle lettere
    elif drone.is_flying:
        # Esempio comandi direzionali classici (frecce)
        if event.name == "up":
            esegui_comando_vocale("avanti")
        elif event.name == "down":
            esegui_comando_vocale("indietro")
        elif event.name == "left":
            esegui_comando_vocale("sinistra")
        elif event.name == "right":
            esegui_comando_vocale("destra")

        # Se premi una lettera dell'alfabeto (A-Z)
        elif len(tasto) == 1 and tasto.isalpha():
            disegna_lettera(tasto)


# --- FLUSSO PRINCIPALE ---
print("\n=== CONTROLLI ===")
print("Premere SPAZIO per decollare.")
print("Premere LE FRECCE DIREZIONALI per i movimenti da 100cm.")
print("Premere UNA LETTERA (es. L, A, T) per farla disegnare al drone.")
print("Premere ESC per atterrare e chiudere il programma.")
print("=================\n")

# Resta in ascolto degli eventi della tastiera in background
keyboard.on_press(gestisci_tastiera)

# Mantiene il programma attivo
keyboard.wait("esc")
