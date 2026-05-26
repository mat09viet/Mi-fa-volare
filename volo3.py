import cv2
import time
from djitellopy import Tello

# Connessione al Tello
print("\n=== CONNESSIONE AL RYZE TELLO ===")
tello = Tello()

try:
    tello.connect()
    print(f"-> Stato Batteria: {tello.get_battery()}%")

    # Attivazione dello streaming video per vedere la telecamera
    tello.streamon()
    frame_read = tello.get_frame_read()

    print("\n" + "="*40)
    print(" CONTROLLO DI VOLO DA TASTIERA ACTIVATED")
    print("="*40)
    print(" Clicca sulla finestra video e premi:")
    print(" - BARRA SPAZIATRICE: Decollo (Takeoff)")
    print(" - FRECCIA SU / GIÙ: Avanza / Arretra")
    print(" - FRECCIA DESTRA / SINISTRA: Ruota a destra / sinistra")
    print(" - TASTO W / S: Sale di quota / Scende di quota")
    print(" - TASTO L: Atterraggio (Land)")
    print(" - TASTO Q: Uscita di emergenza")
    print("="*40)

    while True:
        img = frame_read.frame
        if img is None:
            continue
            
        # Ridimensiona il video per vederlo meglio
        img = cv2.resize(img, (640, 480))
        
        # Scrive la batteria sullo schermo del video
        cv2.putText(img, f"Batteria: {tello.get_battery()}%", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("Tello Keyboard Control", img)
        
        # Intercetta i tasti premuti sulla tastiera
        key = cv2.waitKey(1) & 0xFF
        
        # Velocità assi (0 di base)
        lr, fb, ud, yaw = 0, 0, 0, 0
        
        if key == ord(' '): # Barra spaziatrice per decollare
            print("[COMANDO] Decollo!")
            tello.takeoff()
        elif key == ord('l'): # Tasto L per atterrare
            print("[COMANDO] Atterraggio...")
            tello.land()
        elif key == 82: # Freccia Su (avanza)
            fb = 30
        elif key == 84: # Freccia Giù (arretra)
            fb = -30
        elif key == 83: # Freccia Destra (ruota a destra)
            yaw = 40
        elif key == 81: # Freccia Sinistra (ruota a sinistra)
            yaw = -40
        elif key == ord('w'): # Tasto W (sale)
            ud = 30
        elif key == ord('s'): # Tasto S (scende)
            ud = -30
        elif key == ord('q'): # Tasto Q per chiudere tutto
            print("[COMANDO] Emergenza! Atterraggio...")
            tello.land()
            break
            
        # Invia i comandi se stai premendo una freccia o un tasto
        if lr != 0 or fb != 0 or ud != 0 or yaw != 0:
            tello.send_rc_control(lr, fb, ud, yaw)
            time.sleep(0.1)
            tello.send_rc_control(0, 0, 0, 0) # Ferma il movimento appena lasci il tasto

except Exception as e:
    print(f"\n[ERRORE] Rilevata anomalia: {e}")
    try:
        tello.land()
    except:
        pass

finally:
    cv2.destroyAllWindows()
    try:
        tello.streamoff()
    except:
        pass
    print("\n[FINE] Programma terminato in sicurezza.")