import cv2
import time
from djitellopy import Tello

def clip(val, min_val, max_val):
    """Limita la velocità del drone entro valori sicuri"""
    return max(min(val, max_val), min_val)

# Carichiamo il rilevatore di volti nativo di OpenCV (Haar Cascade)
# Questo file è già presente dentro la libreria OpenCV del tuo PC
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Connessione al drone Tello
print("\n=== CONNESSIONE AL RYZE TELLO ===")
tello = Tello()

try:
    tello.connect()
    print(f"-> Stato Batteria: {tello.get_battery()}%")

    # Attivazione della telecamera
    tello.streamon()
    frame_read = tello.get_frame_read()

    print("\n" + "="*40)
    print(" INSEGUIMENTO FACCIALE CON OPENCV")
    print("="*40)
    print("1. DECOLLO: Il drone partirà appena premi INVIO.")
    print("2. MOVIMENTO: Cercherà la tua faccia e girerà per seguirti.")
    print("3. ATTERRAGGIO DI EMERGENZA: Premi 'Q' sulla tastiera.")
    print("="*40)

    input("\n[SICUREZZA] Spazio libero intorno al drone? Premi INVIO per decollare... ")

    print("\n[INFO] Decollo in corso...")
    tello.takeoff()
    
    # Alziamo leggermente il drone all'altezza degli occhi
    tello.send_rc_control(0, 0, 20, 0)
    time.sleep(1.5)
    tello.send_rc_control(0, 0, 0, 0)

    # Dimensioni fisse della finestra video (leggere e veloci)
    W, H = 360, 240
    centro_schermo_x = W // 2

    print("\n[SISTEMA] Telecamera attiva. Mettiti davanti al drone!")

    while True:
        # Prendi il frame video
        img = frame_read.frame
        if img is None:
            continue
            
        # Ridimensiona l'immagine per renderla velocissima da elaborare
        img = cv2.resize(img, (W, H))
        
        # Converte in bianco e nero (OpenCV lo richiede per trovare le facce)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Cerca i volti nell'immagine
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
        
        velocita_rotazione = 0
        
        # Se trova almeno una faccia
        if len(faces) > 0:
            # Prendi le coordinate della prima faccia trovata (x, y, larghezza, altezza)
            x, y, w, h = faces[0]
            
            # Disegna il rettangolo verde intorno alla faccia
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Calcola il centro esatto della tua faccia
            centro_faccia_x = x + (w // 2)
            
            # Calcola l'errore (quanto sei distante dal centro del video)
            errore_x = centro_faccia_x - centro_schermo_x
            
            # Se ti sposti molto dal centro, attiva la rotazione del drone per seguirti
            if abs(errore_x) > 25: # Margine di tolleranza
                # Moltiplichiamo l'errore per regolare la velocità (più sei lontano, più gira veloce)
                velocita_rotazione = int(errore_x * 0.35)
                # Forza limiti di sicurezza per non farlo girare troppo bruscamente
                velocita_rotazione = clip(velocita_rotazione, -40, 40)
                
            cv2.putText(img, "FACCIA AGGANCIATA", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        else:
            cv2.putText(img, "RICERCA VOLTO...", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Invia il comando di rotazione (yaw) al Tello
        # Gli altri valori sono 0 così il drone rimane fermo sul posto e gira solo su se stesso
        tello.send_rc_control(0, 0, 0, velocita_rotazione)
        
        # Mostra il video sul PC
        cv2.imshow("OpenCV Face Tracking", img)
        
        # Se premi il tasto Q sulla tastiera, si interrompe tutto
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\n[INFO] Rilevato tasto 'Q'. Atterraggio immediato...")
            break

except Exception as e:
    print(f"\n[ERRORE] Il programma si è bloccato: {e}")

finally:
    # Sequenza di spegnimento ultra-sicura
    print("\n[SICUREZZA] Spegnimento motori e atterraggio...")
    try:
        tello.send_rc_control(0, 0, 0, 0)
        tello.land()
    except:
        pass
    
    cv2.destroyAllWindows()
    try:
        tello.streamoff()
    except:
        pass
    print("[FINE] Drone a terra in sicurezza.")