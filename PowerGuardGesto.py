import cv2
import mediapipe as mp
import threading
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Caminho do som
alarme_som = r'C:\Users\DRT904168\Documents\pythonProject1\alarm-26718.mp3'

# Variável de controle do alarme
alarme_tocando = False

# Função para tocar alerta sonoro
def tocar_alarme():
    global alarme_tocando
    if not alarme_tocando:
        alarme_tocando = True
        pygame.mixer.music.load(alarme_som)
        pygame.mixer.music.play(-1)

# Função para parar o alarme
def parar_alarme():
    global alarme_tocando
    if alarme_tocando:
        pygame.mixer.music.stop()
        alarme_tocando = False

# Inicializa MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

# Inicializa captura da câmera
cap = cv2.VideoCapture(0)

# Loop principal
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erro na captura do vídeo.")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    gesture_detected = False
    num_hands = 0

    if results.multi_hand_landmarks:
        num_hands = len(results.multi_hand_landmarks)

        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if num_hands == 2:
            gesture_detected = True

    if gesture_detected:
        cv2.putText(frame, "EMERGENCY! HELP", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

        if not alarme_tocando:
            threading.Thread(target=tocar_alarme).start()

    else:
        cv2.putText(frame, f"Detected Hands: {num_hands}", (20, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        parar_alarme()

    cv2.imshow('PowerGuard - Detector de Gestos', frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
