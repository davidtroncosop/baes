import streamlit as st

# Título de la aplicación
st.title("Visor de Archivos de Texto")

# Subir un archivo
uploaded_file = st.file_uploader("Elige un archivo de texto", type="txt")

if uploaded_file is not None:
    # Leer el archivo
    content = uploaded_file.read().decode("utf-8")
    
    # Mostrar el contenido del archivo
    st.text_area("Contenido del archivo", content, height=300)
else:
    st.write("Por favor, sube un archivo de texto para ver su contenido.")
