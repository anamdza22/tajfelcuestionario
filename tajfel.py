import streamlit as st

# Preguntas y respuestas
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
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué sucede durante la categorización social?",
        "opciones": ["Las personas ignoran sus grupos de pertenencia", "Las personas identifican y clasifican a otros en grupos", "Las personas se niegan a aceptar la identidad grupal"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué fenómeno describe la tendencia a favorecer al grupo propio frente a otros?",
        "opciones": ["Conformidad social", "Identificación proyectiva", "Favoritismo del endogrupo"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué estrategia puede usar una persona para mejorar su identidad social cuando su grupo tiene bajo estatus?",
        "opciones": ["Aislarse del grupo", "Rechazar toda identidad colectiva", "Buscar movilidad social o cambiar la percepción del grupo"],
        "respuesta_correcta": 2
    }
]

st.set_page_config(page_title="Quiz Teoría de Identidad Social", page_icon="🧠")

st.title("🧠 Quiz: Teoría de la Identidad Social de Tajfel")
st.write("Responde una pregunta a la vez. ¡Buena suerte!")

# Estado de la aplicación
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "respondida" not in st.session_state:
    st.session_state.respondida = False

indice = st.session_state.indice
total = len(preguntas)

if indice < total:
    pregunta_actual = preguntas[indice]
    st.subheader(f"Pregunta {indice + 1} de {total}")
    seleccion = st.radio(
        pregunta_actual["pregunta"],
        pregunta_actual["opciones"],
        key=f"pregunta_{indice}"
    )

    if st.button("Responder", key=f"boton_{indice}") and not st.session_state.respondida:
        correcta = pregunta_actual["respuesta_correcta"]
        if pregunta_actual["opciones"].index(seleccion) == correcta:
            st.success("✅ ¡Correcto!")
            st.session_state.puntaje += 1
            st.session_state.respondida = True
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es: {pregunta_actual['opciones'][correcta]}")
            st.session_state.respondida = True

    if st.session_state.respondida:
        if st.button("Siguiente"):
            st.session_state.indice += 1
            st.session_state.respondida = False
            st.rerun()

else:
    st.balloons()
    st.success(f"🎉 ¡Felicidades por completar el quiz! Obtuviste {st.session_state.puntaje} de {total} respuestas correctas.")
    if st.button("Reiniciar"):
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.respondida = False
        st.rerun()
