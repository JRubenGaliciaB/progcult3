import streamlit as st
import plotly.graph_objects as go

# Configuración de título
st.title('Evaluación de Programas Secult')

# Panel lateral para entrada de datos
st.sidebar.header('Ajusta los parámetros del programa')

# Agregar programas en una lista
if 'programas' not in st.session_state:
    st.session_state.programas = []

# Entradas de datos para el nuevo programa
programa = st.sidebar.text_input("Nombre del programa")
color_programa = st.sidebar.color_picker("Selecciona color para el programa", "#0000FF")

if st.sidebar.button("Agregar programa"):
    if programa:
        # Inicializamos los parámetros para el nuevo programa
        st.session_state.programas.append({
            "nombre": programa,
            "color": color_programa,
            "beneficiarios": 2000,
            "posicionamiento": 50,
            "percepcion": 70,
            "relevancia": 60,
            "presupuesto": 1000000,
            "cumplimiento": 75,
            "logistica": 50,
            "alcance":1,
            "artistico":50,
            "cohesion":50,
            "zmq":0,
            "economico":0
        })
        st.sidebar.write(f"Programa '{programa}' agregado con el color {color_programa}.")
    else:
        st.sidebar.write("Ingresa un nombre de programa.")

# Desplegable para seleccionar programa
programa_seleccionado = st.sidebar.selectbox(
    'Selecciona un programa',
    [p['nombre'] for p in st.session_state.programas] if st.session_state.programas else [
        "No hay programas disponibles"]
)

# Verificamos que hay programas en la lista y que el programa seleccionado existe
if programa_seleccionado != "No hay programas disponibles":
    programa_seleccionado_info = next(p for p in st.session_state.programas if p['nombre'] == programa_seleccionado)

    # Entradas de datos para el programa seleccionado

    # Subtítulo para la sección
    st.sidebar.markdown("### Sostenibilidad")
    
    programa_seleccionado_info['beneficiarios'] = st.sidebar.slider(
        'Beneficiarios',
        min_value=0,
        max_value=5000,
        value=programa_seleccionado_info['beneficiarios']
    )

    programa_seleccionado_info['presupuesto'] = st.sidebar.slider(
        'Presupuesto',
        min_value=0,
        max_value=8000000,
        step=10000,
        value=programa_seleccionado_info['presupuesto']
    )

    programa_seleccionado_info['economico'] = st.sidebar.slider(
        'Desarrollo económico',
        min_value=0,
        max_value=1,
        step=1,
        value=programa_seleccionado_info['economico']
    )
    
    # Subtítulo para la sección
    st.sidebar.markdown("### Impacto Cultural")
    
    programa_seleccionado_info['artistico'] = st.sidebar.slider(
        'Relevancia Artística',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['artistico']
    )
    
    programa_seleccionado_info['percepcion'] = st.sidebar.slider(
        'Percepción pública',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['percepcion']
    )
    
    # Subtítulo para la sección
    st.sidebar.markdown("### Impacto Social")

    programa_seleccionado_info['cohesion'] = st.sidebar.slider(
        'Cohesión Social',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['cohesion']
    )
    
    programa_seleccionado_info['zmq'] = st.sidebar.slider(
        'Descentralizado',
        min_value=0,
        max_value=1,
        step=1,
        value=programa_seleccionado_info['zmq']
    )

    programa_seleccionado_info['alcance'] = st.sidebar.slider(
        'Presencia en Municipios',
        min_value=0,
        max_value=18,
        value=programa_seleccionado_info['alcance']
    )
    
    programa_seleccionado_info['posicionamiento'] = st.sidebar.slider(
        'Posicionamiento Mediático',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['posicionamiento']
    )

    programa_seleccionado_info['relevancia'] = st.sidebar.slider(
        'Relevancia Social',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['relevancia']
    )


     # Subtítulo para la sección
    st.sidebar.markdown("### Plan Estatal de Desarrollo")
    
    programa_seleccionado_info['cumplimiento'] = st.sidebar.slider(
        'Cumplimiento de Metas PED',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['cumplimiento']
    )

    # Subtítulo para la sección
    st.sidebar.markdown("### Gestióny Operatividad")
    
    programa_seleccionado_info['logistica'] = st.sidebar.slider(
        'Recursos Logísticos',
        min_value=0,
        max_value=100,
        value=programa_seleccionado_info['logistica']
    )

    # Cálculo de métricas
    impacto = programa_seleccionado_info['posicionamiento'] + programa_seleccionado_info['percepcion'] + \
              programa_seleccionado_info['relevancia'] + programa_seleccionado_info['cumplimiento']
    rentabilidad = programa_seleccionado_info['beneficiarios'] / programa_seleccionado_info['presupuesto'] if \
    programa_seleccionado_info['presupuesto'] > 0 else 0

    # Gráfico de dispersión
    fig = go.Figure()

    # Agregar todos los programas a la gráfica
    for programa_info in st.session_state.programas:
        # Obtener los parámetros del programa
        nombre_programa = programa_info['nombre']
        color_programa = programa_info['color']
        impacto = programa_info['posicionamiento'] + programa_info['percepcion'] + programa_info['relevancia'] + \
                  programa_info['cumplimiento']
        rentabilidad = programa_info['beneficiarios'] / programa_info['presupuesto'] if programa_info[
                                                                                            'presupuesto'] > 0 else 0

        # Agregar al gráfico
        fig.add_trace(go.Scatter(
            x=[rentabilidad],
            y=[impacto],
            mode='markers+text',
            text=[nombre_programa],
            marker=dict(size=programa_info['beneficiarios'] / 200, color=color_programa),
            # Tamaño proporcional a beneficiarios
            textposition='top center'
        ))

    fig.update_layout(
        title="Impacto vs Rentabilidad",
        xaxis_title="Rentabilidad",
        yaxis_title="Impacto",
        xaxis=dict(range=[0, 0.002]),
        yaxis=dict(range=[0, 400]),
        showlegend=False
    )

    # Mostrar gráfico
    st.plotly_chart(fig)

    # Texto debajo de la gráfica
    st.markdown("### Evaluación de programas culturales bajo la metodología de David Roselló y su alineación al Plan Estatal de Desarrollo 2021-2027.")
    # Imagen
    st.image('https://github.com/JRubenGaliciaB/progcult3/blob/main/progcult.png?raw=true', use_container_width=True)

else:
    st.write("Selecciona un programa para ajustar sus parámetros.")
