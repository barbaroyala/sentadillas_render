import streamlit as st
import streamlit.components.v1 as components
from motion_detector import start_motion_detector  # Importar el detector de movimiento

# Función para mostrar la cámara
def display_camera():
    # Código HTML y JavaScript para acceder a la cámara
    html_code = """
    <html>
        <body>
            <h2>Tu Cámara Frontal</h2>
            <video id="video" width="100%" height="auto" autoplay></video>
            <script>
                const video = document.getElementById("video");
                // Solicitar acceso a la cámara frontal del dispositivo
                navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } })
                    .then(function(stream) {
                        video.srcObject = stream;
                    })
                    .catch(function(err) {
                        alert("Error al acceder a la cámara: " + err.message);
                    });
            </script>
        </body>
    </html>
    """
    # Mostrar el HTML/JS en la interfaz de Streamlit
    components.html(html_code, height=600)

# Función para iniciar el detector de movimiento
def start_detector():
    start_motion_detector()  # Llamar al detector de movimiento

# Página de selección de actividad
def activity_selection():
    activities = ['Sentadillas', 'Dominadas', 'Flexiones', 'Burpees', 'Abdominales']
    activity_name = st.selectbox("Selecciona una actividad", activities)

    # Cargar historial para la actividad seleccionada
    # history = load_history(activity_name)  # Este código lo puedes usar para gestionar historial
    history = {}

    st.write(f"Repeticiones hoy: {history.get(datetime.today().strftime('%Y-%m-%d'), 0)}")

    # Botones de acción
    if st.button("Iniciar Detección"):
        start_detector()  # Iniciar el detector de movimientos

    if st.button("Ver Historial"):
        st.write("Historial de repeticiones:")
        # Aquí también puedes mostrar el historial cargado, por ejemplo:
        # for date, count in history.items():
        #     st.write(f"{date}: {count} repeticiones")
    
    # Botón para aumentar el contador
    if st.button("Agregar una repetición"):
        # Agregar una repetición al contador
        history[datetime.today().strftime('%Y-%m-%d')] = 1
        st.write(f"Repeticiones hoy: 1")  # Actualiza el contador con la lógica que desees

# Función principal
def main():
    st.title("Aplicación de Actividad Física")

    # Mostrar cámara cuando el usuario lo solicite
    if st.button("Mostrar cámara frontal"):
        display_camera()

    # Mostrar pantalla de selección de actividad
    activity_selection()

if __name__ == "__main__":
    main()
