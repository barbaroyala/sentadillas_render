import cv2
import numpy as np
import streamlit as st

# Función para detectar movimiento entre dos frames
def detect_motion(frame1, frame2):
    # Convertir las imágenes a escala de grises
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Calcular la diferencia entre las dos imágenes
    diff = cv2.absdiff(gray1, gray2)
    
    # Umbralizar la diferencia para obtener solo las áreas de cambio
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    # Encontrar los contornos de las áreas con movimiento
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours

# Función para iniciar el detector de movimiento
def start_motion_detector():
    # Capturar la cámara usando OpenCV
    cap = cv2.VideoCapture(0)  # 0 para usar la cámara predeterminada
    
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    
    # Contador de movimientos detectados
    motion_count = 0
    
    while ret:
        # Detectar el movimiento entre dos frames consecutivos
        contours = detect_motion(frame1, frame2)
        
        # Si hay contornos (movimiento detectado)
        if contours:
            motion_count += 1
            st.write(f"Movimiento detectado: {motion_count} repeticiones")
        
        # Mostrar el video en la interfaz
        ret, frame2 = cap.read()
        
        if ret:
            # Mostrar el video en Streamlit (usando OpenCV para convertir el frame a imagen)
            _, buffer = cv2.imencode('.jpg', frame2)
            st.image(buffer.tobytes(), channels="BGR")
    
    # Liberar la cámara al finalizar
    cap.release()
