import streamlit as st
import json
from datetime import datetime

# Función para cargar el historial
def load_history(activity_name):
    try:
        with open(f"{activity_name}_history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Función para guardar el historial
def save_history(activity_name, history):
    with open(f"{activity_name}_history.json", "w") as f:
        json.dump(history, f)

# Función para actualizar el contador
def update_count(activity_name, history, count_to_add):
    today = datetime.today().strftime('%Y-%m-%d')
    if today in history:
        history[today] += count_to_add
    else:
        history[today] = count_to_add
    return history

# Página de selección de actividad
def activity_selection():
    activities = ['Sentadillas', 'Dominadas', 'Flexiones', 'Burpees', 'Abdominales']
    activity_name = st.selectbox("Selecciona una actividad", activities)

    # Cargar historial para la actividad seleccionada
    history = load_history(activity_name)
    
    st.write(f"Repeticiones hoy: {history.get(datetime.today().strftime('%Y-%m-%d'), 0)}")

    # Botones de acción
    if st.button("Iniciar Detector"):
        st.write("Aquí iría la lógica para iniciar un detector de movimientos")
    
    if st.button("Ver Historial"):
        st.write("Historial de repeticiones:")
        for date, count in history.items():
            st.write(f"{date}: {count} repeticiones")
    
    # Botón para aumentar el contador
    if st.button("Agregar una repetición"):
        history = update_count(activity_name, history, 1)
        save_history(activity_name, history)
        st.write(f"Repeticiones hoy: {history[datetime.today().strftime('%Y-%m-%d')]}")

# Interfaz principal
def main():
    st.title("Aplicación de Actividad Física")
    
    # Mostrar pantalla de selección de actividad
    activity_selection()

if __name__ == "__main__":
    main()
