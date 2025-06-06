import cv2
import mediapipe as mp
import threading
import pygame

# 🔊 Inicializa o mixer do pygame
pygame.mixer.init()

# 🔔 Caminho do som
alarme_som = 'alarm-26718.mp3'

# 🔧 Variável de controle do alarme
alarme_tocando = False

# 🔊 Função para tocar alerta sonoro
def tocar_alarme():
    global alarme_tocando
    if not alarme_tocando:
        alarme_tocando = True
        pygame.mixer.music.load(alarme_som)
        pygame.mixer.music.play(-1)  # 🔁 Repete até ser parado

# 🔊 Função para parar o alarme
def parar_alarme():
    global alarme_tocando
    if alarme_tocando:
        pygame.mixer.music.stop()
        alarme_tocando = False

# 🧍‍♂️ Inicializa MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5
)

# Utilitário de desenho
mp_drawing = mp.solutions.drawing_utils

# 🎥 Inicializa captura da câmera
cap = cv2.VideoCapture(0)

# 🔁 Loop principal
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erro na captura do vídeo.")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa pose
    results_pose = pose.process(frame_rgb)

    # Variável de controle
    person_fallen = False

    # 🚀 Verifica pessoa caída com pose
    if results_pose.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Pega posição de ombros e quadris
        left_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = results_pose.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

        # Média das posições Y (altura na tela)
        shoulder_y = (left_shoulder.y + right_shoulder.y) / 2
        hip_y = (left_hip.y + right_hip.y) / 2

        # Se ombros e quadris estão muito próximos verticalmente → possivelmente deitado
        if abs(shoulder_y - hip_y) < 0.1:
            person_fallen = True

    # 🚨 Se condição de queda for detectada
    if person_fallen:
        cv2.putText(frame, "🚨 QUEDA DETECTADA 🚨", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

        # Inicia o alarme se não estiver tocando
        if not alarme_tocando:
            threading.Thread(target=tocar_alarme).start()

    else:
        # Status normal
        cv2.putText(frame, "Status: OK", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

        # Para o alarme se não há emergência
        parar_alarme()

    # 📺 Mostra saída
    cv2.imshow('PowerGuard - Detector de Queda', frame)

    if cv2.waitKey(10) & 0xFF == 27:  # ESC
        break

# Libera recursos
cap.release()
cv2.destroyAllWindows()
