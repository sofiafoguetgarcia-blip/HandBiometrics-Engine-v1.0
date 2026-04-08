import math
import cv2
import mediapipe as mp
import numpy as np

# Inicialización de MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def distancia_px(a, b, ancho, alto):
    ax, ay = int(a.x * ancho), int(a.y * alto)
    bx, by = int(b.x * ancho), int(b.y * alto)
    return math.hypot(bx - ax, by - ay)

def punto_px(p, ancho, alto):
    return int(p.x * ancho), int(p.y * alto)

def medir_mano(landmarks, ancho, alto):
    medidas = {
        "Palma Ancho": distancia_px(landmarks[5], landmarks[17], ancho, alto),
        "Palma Alto": distancia_px(landmarks[0], landmarks[9], ancho, alto),
        "Pulgar": distancia_px(landmarks[2], landmarks[4], ancho, alto),
        "Indice": distancia_px(landmarks[5], landmarks[8], ancho, alto),
        "Medio": distancia_px(landmarks[9], landmarks[12], ancho, alto),
        "Anular": distancia_px(landmarks[13], landmarks[16], ancho, alto),
        "Menique": distancia_px(landmarks[17], landmarks[20], ancho, alto),
    }
    # Ratios para estimación de género (Proporciones de Manning)
    ancho_palma = max(medidas["Palma Ancho"], 1.0)
    medidas["ratio_2D4D"] = medidas["Indice"] / max(medidas["Anular"], 1.0)
    medidas["robustez"] = ancho_palma / max(medidas["Palma Alto"], 1.0)
    return medidas

def estimar_genero(medidas):
    # Lógica biométrica: los hombres suelen tener el anular más largo que el índice (ratio < 1)
    # y palmas proporcionalmente más anchas.
    score_masculino = 0
    if medidas["ratio_2D4D"] < 0.96: score_masculino += 1
    if medidas["robustez"] > 0.85: score_masculino += 1
    
    if score_masculino >= 1:
        return "Masculino", (255, 100, 0) # Azul
    else:
        return "Femenino", (150, 0, 255) # Rosa/Morado

def dibujar_panel(frame, medidas, genero, color_genero):
    # Lista de todas las distancias calculadas
    lineas = [f"{k}: {v:.1f}px" for k, v in medidas.items() if "ratio" not in k and "robustez" not in k]
    
    # Dibujar fondo del panel (ajustado al tamaño de la lista)
    cv2.rectangle(frame, (5, 5), (280, 260), (0, 0, 0), -1)
    cv2.rectangle(frame, (5, 5), (280, 260), color_genero, 2)

    # Título de Género
    cv2.putText(frame, f"GENERO: {genero}", (15, 30), cv2.FONT_HERSHEY_TRIPLEX, 0.7, color_genero, 2)
    
    # Mostrar todas las distancias
    for i, texto in enumerate(lineas):
        cv2.putText(frame, texto, (15, 65 + i * 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

def main():
    cap = cv2.VideoCapture(0)
    
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        while True:
            ok, frame = cap.read()
            if not ok: break

            frame = cv2.flip(frame, 1)
            alto, ancho = frame.shape[:2]
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                medidas = medir_mano(hand_landmarks.landmark, ancho, alto)
                genero, color = estimar_genero(medidas)
                dibujar_panel(frame, medidas, genero, color)
                
                # Dibujar contorno de la mano (Hull)
                puntos = np.array([punto_px(p, ancho, alto) for p in hand_landmarks.landmark], dtype=np.int32)
                hull = cv2.convexHull(puntos)
                cv2.polylines(frame, [hull], True, color, 2)
            else:
                cv2.putText(frame, "BUSCANDO MANO...", (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            cv2.imshow("Analisis Biometrico de Mano", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()