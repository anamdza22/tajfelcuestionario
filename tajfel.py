import streamlit as st

# Configuración de la app
st.set_page_config(page_title="Quiz Teoría de Identidad Social", page_icon="🧠")

st.title("🧠 Quiz: Teoría de la Identidad Social de Tajfel")
st.write("Responde una pregunta a la vez. ¡Buena suerte!")

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cuál es el concepto central de la Teoría de la Identidad Social de Tajfel?",
        "opciones": ["La obediencia a la autoridad", "La forma en que las personas se identifican con los grupos sociales", "El aprendizaje por observación"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué busca explicar la Teoría de la Identidad Social?",
        "opciones": ["Las diferencias biológicas entre grupos", "Cómo se desarrollan los estereotipos en la infancia", "Los procesos psicológicos detrás de la pertenencia grupal y el favoritismo hacia el endogrupo"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué término se refiere al grupo al que una persona pertenece?",
        "opciones": ["Exogrupo", "Endogrupo", "Outgroup"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "Según Tajfel, ¿qué puede llevar a la discriminación entre grupos sociales?",
        "opciones": ["La personalidad autoritaria", "La simple categorización de las personas en grupos", "La falta de información objetiva"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué experimento famoso realizó Tajfel para ilustrar el favoritismo del endogrupo?",
        "opciones": ["El experimento del perro de Pavlov", "El experimento de la prisión de Stanford", "El experimento de los puntos y los grupos mínimos"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué busca una persona al mejorar su autoestima, según la teoría de la identidad social?",
        "opciones": ["Ser reconocida como individuo", "Aumentar la superioridad de su grupo frente a otros", "Aislarse de la influencia del grupo"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál de los siguientes procesos NO forma parte del desarrollo de la identidad social según Tajfel?",
        "opciones": ["Categorización social", "Comparación social", "Aprendizaje observacional"],
