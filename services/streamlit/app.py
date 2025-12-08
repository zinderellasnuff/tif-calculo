import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuración de la página
st.set_page_config(
    page_title="TIF Cálculo - Análisis de Derivadas",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("🧮 Analizador de Derivadas - TIF Fase III")
st.markdown("**Aplicaciones de la Derivada con Software Libre**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Información")
    st.info("""
    **Autor:** Aron
    **Universidad:** UCSM
    **Curso:** Cálculo 2025
    **Fase:** III
    """)

    st.markdown("### 🛠️ Motores Disponibles")
    st.success("✅ Python (SymPy)")
    st.success("✅ SageMath")
    st.success("✅ GNU Octave")

    st.markdown("---")
    st.markdown("### 📖 Secciones")
    st.markdown("""
    - **Análisis:** Máximos y mínimos (3.1)
    - **Concavidad:** Puntos de inflexión (3.3)
    - **Trazo Completo:** Análisis integral (3.5)
    - **Ejemplos:** Funciones de prueba
    - **Ayuda:** Guía de sintaxis
    """)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Análisis",
    "🔄 Concavidad",
    "🎨 Trazo Completo",
    "📚 Ejemplos",
    "ℹ️ Ayuda"
])

# ==================== TAB 1: ANÁLISIS ====================
with tab1:
    st.header("Análisis de Máximos y Mínimos (Sección 3.1)")
    st.markdown("*Estudio de puntos críticos mediante el criterio de la segunda derivada*")

    col1, col2 = st.columns([2, 1])

    with col1:
        funcion_str = st.text_input(
            "Función f(x):",
            value="x**3 - 3*x**2 - 9*x + 5",
            help="Usa ** para potencias, * para multiplicación",
            key="analisis_funcion"
        )

        col_a, col_b = st.columns(2)
        with col_a:
            a = st.number_input("Límite inferior", value=-5.0, key="analisis_a")
        with col_b:
            b = st.number_input("Límite superior", value=5.0, key="analisis_b")

    with col2:
        st.markdown("### Ejemplos Rápidos")
        st.code("x**2 - 4", language="python")
        st.code("x**3 - 3*x", language="python")
        st.code("sin(x)", language="python")

    if st.button("🚀 Analizar", type="primary", key="analisis_btn"):
        try:
            x = sp.Symbol('x')
            f = sp.sympify(funcion_str)
            f_prime = sp.diff(f, x)
            f_double_prime = sp.diff(f_prime, x)

            # Mostrar derivadas
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### f(x)")
                st.latex(f"f(x) = {sp.latex(f)}")

            with col2:
                st.markdown("### f'(x)")
                st.latex(f"f'(x) = {sp.latex(f_prime)}")

            with col3:
                st.markdown("### f''(x)")
                st.latex(f"f''(x) = {sp.latex(f_double_prime)}")

            st.markdown("---")

            # Puntos críticos
            st.subheader("🎯 Puntos Críticos (f'(x) = 0)")
            critical_points = sp.solve(f_prime, x)
            critical_real = [float(p.evalf()) for p in critical_points if p.is_real]

            if critical_real:
                st.success(f"✓ Encontrados: {len(critical_real)} punto(s) crítico(s)")

                # Tabla de puntos críticos
                st.markdown("#### Tabla de Análisis")
                tabla_data = []
                for i, point in enumerate(critical_real, 1):
                    f_val = float(f.subs(x, point).evalf())
                    second = float(f_double_prime.subs(x, point).evalf())

                    if abs(second) < 1e-10:
                        tipo = "Punto de Inflexión"
                        criterio = "f''(x) = 0"
                    elif second > 0:
                        tipo = "Mínimo Local"
                        criterio = "f''(x) > 0"
                    else:
                        tipo = "Máximo Local"
                        criterio = "f''(x) < 0"

                    tabla_data.append({
                        "Punto": f"P{i}",
                        "x": f"{point:.6f}",
                        "f(x)": f"{f_val:.6f}",
                        "f'(x)": "0",
                        "f''(x)": f"{second:.6f}",
                        "Criterio": criterio,
                        "Clasificación": tipo
                    })

                st.table(tabla_data)

                # Mostrar métricas visuales
                st.markdown("#### Resumen Visual")
                cols = st.columns(len(critical_real))
                for i, point in enumerate(critical_real):
                    with cols[i]:
                        f_val = float(f.subs(x, point).evalf())
                        second = float(f_double_prime.subs(x, point).evalf())

                        if second > 0:
                            st.metric(f"Punto {i+1}", f"x = {point:.4f}",
                                     delta="Mínimo", delta_color="inverse")
                        elif second < 0:
                            st.metric(f"Punto {i+1}", f"x = {point:.4f}",
                                     delta="Máximo", delta_color="normal")
                        else:
                            st.metric(f"Punto {i+1}", f"x = {point:.4f}",
                                     delta="Inflexión", delta_color="off")
                        st.caption(f"f(x) = {f_val:.4f}")
            else:
                st.warning("⚠️ No hay puntos críticos reales en el dominio")

            st.markdown("---")

            # Gráfica
            st.subheader("📊 Visualización Gráfica")

            x_vals = np.linspace(float(a), float(b), 500)
            f_lambda = sp.lambdify(x, f, 'numpy')
            f_prime_lambda = sp.lambdify(x, f_prime, 'numpy')

            y_vals = f_lambda(x_vals)
            y_prime_vals = f_prime_lambda(x_vals)

            fig = make_subplots(
                rows=2, cols=1,
                subplot_titles=('Función f(x)', "Primera Derivada f'(x)"),
                vertical_spacing=0.15
            )

            # Plot f(x)
            fig.add_trace(
                go.Scatter(x=x_vals, y=y_vals, name='f(x)',
                          line=dict(color='blue', width=2)),
                row=1, col=1
            )

            # Marcar puntos críticos
            for point in critical_real:
                if a <= point <= b:
                    f_val = float(f.subs(x, point).evalf())
                    second = float(f_double_prime.subs(x, point).evalf())

                    if second > 0:
                        color = 'green'
                        symbol = 'triangle-down'
                        tipo = 'Mínimo'
                    elif second < 0:
                        color = 'red'
                        symbol = 'triangle-up'
                        tipo = 'Máximo'
                    else:
                        color = 'orange'
                        symbol = 'circle'
                        tipo = 'Inflexión'

                    fig.add_trace(
                        go.Scatter(x=[point], y=[f_val],
                                 mode='markers',
                                 marker=dict(size=14, color=color, symbol=symbol),
                                 name=f'{tipo}: x={point:.2f}',
                                 showlegend=True),
                        row=1, col=1
                    )

            # Plot f'(x)
            fig.add_trace(
                go.Scatter(x=x_vals, y=y_prime_vals, name="f'(x)",
                          line=dict(color='green', width=2)),
                row=2, col=1
            )

            # Línea y=0 en f'(x)
            fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)

            # Marcar puntos críticos en f'(x)
            for point in critical_real:
                if a <= point <= b:
                    fig.add_trace(
                        go.Scatter(x=[point], y=[0],
                                 mode='markers',
                                 marker=dict(size=10, color='red'),
                                 showlegend=False),
                        row=2, col=1
                    )

            fig.update_xaxes(title_text="x", row=2, col=1)
            fig.update_yaxes(title_text="y", row=1, col=1)
            fig.update_yaxes(title_text="y'", row=2, col=1)

            fig.update_layout(height=700, showlegend=True)

            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"❌ Error al procesar la función: {str(e)}")
            st.info("💡 Verifica la sintaxis de tu función. Consulta la pestaña 'Ayuda' para más información.")

# ==================== TAB 2: CONCAVIDAD ====================
with tab2:
    st.header("Análisis de Concavidad y Puntos de Inflexión (Sección 3.3)")
    st.markdown("*Estudio de la curvatura de la función mediante la segunda derivada*")

    col1, col2 = st.columns([2, 1])

    with col1:
        funcion_conc = st.text_input(
            "Función f(x):",
            value="x**3 - 3*x**2 - 9*x + 4",
            help="Ingresa una función para analizar su concavidad",
            key="concavidad_funcion"
        )

        col_a, col_b = st.columns(2)
        with col_a:
            a_conc = st.number_input("Límite inferior", value=-5.0, key="concavidad_a")
        with col_b:
            b_conc = st.number_input("Límite superior", value=5.0, key="concavidad_b")

    with col2:
        st.markdown("### Ejemplos")
        st.code("x**3 - 3*x**2", language="python")
        st.code("x**4 - 2*x**2", language="python")
        st.code("exp(x) - x**2", language="python")

    if st.button("🔍 Analizar Concavidad", type="primary", key="concavidad_btn"):
        try:
            x = sp.Symbol('x')
            f = sp.sympify(funcion_conc)
            f_prime = sp.diff(f, x)
            f_double_prime = sp.diff(f_prime, x)

            # Mostrar función y segunda derivada
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### f(x)")
                st.latex(f"f(x) = {sp.latex(f)}")
            with col2:
                st.markdown("### f''(x)")
                st.latex(f"f''(x) = {sp.latex(f_double_prime)}")

            st.markdown("---")

            # Puntos de inflexión (f''(x) = 0)
            st.subheader("🔄 Puntos de Inflexión (f''(x) = 0)")
            inflection_points = sp.solve(f_double_prime, x)
            inflection_real = [float(p.evalf()) for p in inflection_points if p.is_real]

            if inflection_real:
                st.success(f"✓ Encontrados: {len(inflection_real)} punto(s) de inflexión potencial(es)")

                # Verificar cambio de signo
                f_triple = sp.diff(f_double_prime, x)
                verified_inflections = []

                for point in inflection_real:
                    # Verificar cambio de signo evaluando a ambos lados
                    epsilon = 0.01
                    left = float(f_double_prime.subs(x, point - epsilon).evalf())
                    right = float(f_double_prime.subs(x, point + epsilon).evalf())

                    if left * right < 0:  # Cambio de signo
                        verified_inflections.append(point)
                        f_val = float(f.subs(x, point).evalf())
                        st.info(f"✓ x = {point:.6f}, f(x) = {f_val:.6f} (cambio de signo confirmado)")
                    else:
                        st.warning(f"⚠️ x = {point:.6f} no es punto de inflexión (no hay cambio de signo)")

                inflection_real = verified_inflections
            else:
                st.info("ℹ️ No hay puntos de inflexión")

            st.markdown("---")

            # Tabla de intervalos de concavidad
            st.subheader("📋 Tabla de Intervalos de Concavidad")

            # Determinar intervalos
            test_points = sorted(inflection_real + [float(a_conc), float(b_conc)])
            intervalos = []

            f_double_lambda = sp.lambdify(x, f_double_prime, 'numpy')

            for i in range(len(test_points) - 1):
                mid_point = (test_points[i] + test_points[i + 1]) / 2
                f_double_val = float(f_double_lambda(mid_point))

                if f_double_val > 0:
                    concavidad = "Cóncava Arriba (∪)"
                    signo = "f''(x) > 0"
                else:
                    concavidad = "Cóncava Abajo (∩)"
                    signo = "f''(x) < 0"

                intervalos.append({
                    "Intervalo": f"({test_points[i]:.2f}, {test_points[i+1]:.2f})",
                    "Punto de Prueba": f"{mid_point:.2f}",
                    "f''(x)": f"{f_double_val:.4f}",
                    "Signo": signo,
                    "Concavidad": concavidad
                })

            st.table(intervalos)

            st.markdown("---")

            # Gráfica con código de colores
            st.subheader("📊 Visualización Gráfica")

            x_vals = np.linspace(float(a_conc), float(b_conc), 1000)
            f_lambda = sp.lambdify(x, f, 'numpy')
            f_double_lambda = sp.lambdify(x, f_double_prime, 'numpy')

            y_vals = f_lambda(x_vals)
            y_double_vals = f_double_lambda(x_vals)

            fig = make_subplots(
                rows=2, cols=1,
                subplot_titles=('Función f(x) con Regiones de Concavidad',
                               "Segunda Derivada f''(x)"),
                vertical_spacing=0.15
            )

            # Graficar f(x) con código de colores por concavidad
            # Separar en regiones cóncavas arriba y abajo
            concava_arriba_x = []
            concava_arriba_y = []
            concava_abajo_x = []
            concava_abajo_y = []

            for i, (xi, yi, y_double) in enumerate(zip(x_vals, y_vals, y_double_vals)):
                if y_double > 0:
                    concava_arriba_x.append(xi)
                    concava_arriba_y.append(yi)
                else:
                    concava_abajo_x.append(xi)
                    concava_abajo_y.append(yi)

            # Plot regiones cóncavas arriba (verde)
            if concava_arriba_x:
                fig.add_trace(
                    go.Scatter(x=concava_arriba_x, y=concava_arriba_y,
                              mode='lines',
                              name='Cóncava Arriba (∪)',
                              line=dict(color='green', width=3)),
                    row=1, col=1
                )

            # Plot regiones cóncavas abajo (rojo)
            if concava_abajo_x:
                fig.add_trace(
                    go.Scatter(x=concava_abajo_x, y=concava_abajo_y,
                              mode='lines',
                              name='Cóncava Abajo (∩)',
                              line=dict(color='red', width=3)),
                    row=1, col=1
                )

            # Marcar puntos de inflexión con diamantes morados
            for point in inflection_real:
                if a_conc <= point <= b_conc:
                    f_val = float(f.subs(x, point).evalf())
                    fig.add_trace(
                        go.Scatter(x=[point], y=[f_val],
                                 mode='markers',
                                 marker=dict(size=16, color='purple',
                                           symbol='diamond',
                                           line=dict(width=2, color='white')),
                                 name=f'Inflexión: x={point:.2f}',
                                 showlegend=True),
                        row=1, col=1
                    )

            # Plot f''(x)
            fig.add_trace(
                go.Scatter(x=x_vals, y=y_double_vals, name="f''(x)",
                          line=dict(color='blue', width=2)),
                row=2, col=1
            )

            # Línea y=0 en f''(x)
            fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)

            # Marcar puntos de inflexión en f''(x)
            for point in inflection_real:
                if a_conc <= point <= b_conc:
                    fig.add_trace(
                        go.Scatter(x=[point], y=[0],
                                 mode='markers',
                                 marker=dict(size=12, color='purple', symbol='diamond'),
                                 showlegend=False),
                        row=2, col=1
                    )

            # Sombrear regiones en f''(x)
            for i in range(len(test_points) - 1):
                mid_point = (test_points[i] + test_points[i + 1]) / 2
                f_double_val = float(f_double_lambda(mid_point))

                if f_double_val > 0:
                    color = 'rgba(0, 255, 0, 0.1)'  # Verde transparente
                else:
                    color = 'rgba(255, 0, 0, 0.1)'  # Rojo transparente

                fig.add_vrect(
                    x0=test_points[i], x1=test_points[i+1],
                    fillcolor=color, layer="below",
                    line_width=0,
                    row=2, col=1
                )

            fig.update_xaxes(title_text="x", row=2, col=1)
            fig.update_yaxes(title_text="y", row=1, col=1)
            fig.update_yaxes(title_text="y''", row=2, col=1)

            fig.update_layout(height=800, showlegend=True)

            st.plotly_chart(fig, use_container_width=True)

            # Interpretación
            st.markdown("---")
            st.subheader("📖 Interpretación")
            st.markdown("""
            **Código de Colores:**
            - 🟢 **Verde:** Región cóncava hacia arriba (∪) - La función "sonríe"
            - 🔴 **Rojo:** Región cóncava hacia abajo (∩) - La función "se entristece"
            - 💜 **Diamante Morado:** Punto de inflexión (cambio de concavidad)

            **Criterio:**
            - Si f''(x) > 0 → La función es cóncava hacia arriba
            - Si f''(x) < 0 → La función es cóncava hacia abajo
            - Si f''(x) = 0 y hay cambio de signo → Punto de inflexión
            """)

        except Exception as e:
            st.error(f"❌ Error al procesar la función: {str(e)}")
            st.info("💡 Verifica la sintaxis de tu función. Consulta la pestaña 'Ayuda' para más información.")

# ==================== TAB 3: TRAZO COMPLETO ====================
with tab3:
    st.header("Trazo Completo de Curvas (Sección 3.5)")
    st.markdown("*Análisis integral de funciones: dominio, simetrías, asíntotas, extremos, concavidad y gráfica*")

    col1, col2 = st.columns([2, 1])

    with col1:
        funcion_trazo = st.text_input(
            "Función f(x):",
            value="2 + 3*x - x**3",
            help="Ingresa una función para análisis completo",
            key="trazo_funcion"
        )

        col_a, col_b = st.columns(2)
        with col_a:
            a_trazo = st.number_input("Límite inferior", value=-4.0, key="trazo_a")
        with col_b:
            b_trazo = st.number_input("Límite superior", value=4.0, key="trazo_b")

    with col2:
        st.markdown("### Ejemplos")
        st.code("2 + 3*x - x**3", language="python")
        st.code("x**3 - 3*x**2", language="python")
        st.code("1/x", language="python")

    if st.button("🎨 Análisis Completo", type="primary", key="trazo_btn"):
        try:
            x = sp.Symbol('x')
            f = sp.sympify(funcion_trazo)
            f_prime = sp.diff(f, x)
            f_double_prime = sp.diff(f_prime, x)

            # Crear contenedor para el análisis en 6 pasos
            st.markdown("## 📋 Análisis en 6 Pasos")

            # ===== PASO 1: DOMINIO =====
            st.markdown("### Paso 1: Dominio")
            with st.container():
                try:
                    # Intentar encontrar restricciones del dominio
                    # Verificar denominadores
                    denominador = sp.denom(f)
                    if denominador != 1:
                        restricciones = sp.solve(denominador, x)
                        if restricciones:
                            restricciones_str = ", ".join([f"x ≠ {r}" for r in restricciones])
                            st.info(f"🔍 Dominio: ℝ - {{{restricciones_str}}}")
                            dominio_desc = f"Todos los reales excepto {restricciones_str}"
                        else:
                            st.success("🔍 Dominio: ℝ (todos los números reales)")
                            dominio_desc = "Todos los números reales"
                    else:
                        st.success("🔍 Dominio: ℝ (todos los números reales)")
                        dominio_desc = "Todos los números reales"
                except:
                    st.success("🔍 Dominio: ℝ (todos los números reales)")
                    dominio_desc = "Todos los números reales"

            st.markdown("---")

            # ===== PASO 2: SIMETRÍAS =====
            st.markdown("### Paso 2: Simetrías")
            with st.container():
                f_neg_x = f.subs(x, -x)

                # Verificar si es par: f(-x) = f(x)
                es_par = sp.simplify(f_neg_x - f) == 0

                # Verificar si es impar: f(-x) = -f(x)
                es_impar = sp.simplify(f_neg_x + f) == 0

                if es_par:
                    st.success("🔍 La función es **PAR**: f(-x) = f(x)")
                    st.info("Simétrica respecto al eje Y")
                    simetria = "Par (simétrica respecto al eje Y)"
                elif es_impar:
                    st.success("🔍 La función es **IMPAR**: f(-x) = -f(x)")
                    st.info("Simétrica respecto al origen")
                    simetria = "Impar (simétrica respecto al origen)"
                else:
                    st.info("🔍 La función **NO tiene simetría** par ni impar")
                    simetria = "Sin simetría especial"

            st.markdown("---")

            # ===== PASO 3: ASÍNTOTAS =====
            st.markdown("### Paso 3: Asíntotas")
            asintotas_vert = []
            asintotas_horiz = []

            with st.container():
                # Asíntotas verticales (donde el denominador es 0)
                denominador = sp.denom(f)
                if denominador != 1:
                    restricciones = sp.solve(denominador, x)
                    for r in restricciones:
                        try:
                            r_float = float(r.evalf())
                            if r.is_real:
                                asintotas_vert.append(r_float)
                                st.warning(f"📍 Asíntota vertical: x = {r_float:.4f}")
                        except:
                            pass

                if not asintotas_vert:
                    st.success("✓ No hay asíntotas verticales")

                # Asíntotas horizontales (límites al infinito)
                try:
                    lim_inf_pos = sp.limit(f, x, sp.oo)
                    lim_inf_neg = sp.limit(f, x, -sp.oo)

                    if lim_inf_pos.is_finite:
                        lim_val = float(lim_inf_pos.evalf())
                        asintotas_horiz.append(lim_val)
                        st.warning(f"📍 Asíntota horizontal (x→+∞): y = {lim_val:.4f}")

                    if lim_inf_neg.is_finite and lim_inf_neg != lim_inf_pos:
                        lim_val = float(lim_inf_neg.evalf())
                        if lim_val not in asintotas_horiz:
                            asintotas_horiz.append(lim_val)
                        st.warning(f"📍 Asíntota horizontal (x→-∞): y = {lim_val:.4f}")

                    if not asintotas_horiz:
                        st.success("✓ No hay asíntotas horizontales")
                except:
                    st.info("ℹ️ No se pudieron calcular asíntotas horizontales")

            st.markdown("---")

            # ===== PASO 4: EXTREMOS LOCALES =====
            st.markdown("### Paso 4: Extremos Locales (Máximos y Mínimos)")
            critical_points = sp.solve(f_prime, x)
            critical_real = [float(p.evalf()) for p in critical_points if p.is_real]

            maximos = []
            minimos = []

            with st.container():
                if critical_real:
                    for point in critical_real:
                        f_val = float(f.subs(x, point).evalf())
                        second = float(f_double_prime.subs(x, point).evalf())

                        if abs(second) < 1e-10:
                            st.info(f"🔹 x = {point:.4f}: Punto crítico indeterminado")
                        elif second > 0:
                            st.success(f"📉 **Mínimo Local:** x = {point:.4f}, f(x) = {f_val:.4f}")
                            minimos.append((point, f_val))
                        else:
                            st.error(f"📈 **Máximo Local:** x = {point:.4f}, f(x) = {f_val:.4f}")
                            maximos.append((point, f_val))
                else:
                    st.info("ℹ️ No hay extremos locales")

            st.markdown("---")

            # ===== PASO 5: CONCAVIDAD =====
            st.markdown("### Paso 5: Concavidad y Puntos de Inflexión")
            inflection_points = sp.solve(f_double_prime, x)
            inflection_real = []

            with st.container():
                if inflection_points:
                    for p in inflection_points:
                        if p.is_real:
                            point = float(p.evalf())
                            # Verificar cambio de signo
                            epsilon = 0.01
                            f_double_lambda = sp.lambdify(x, f_double_prime, 'numpy')
                            left = float(f_double_lambda(point - epsilon))
                            right = float(f_double_lambda(point + epsilon))

                            if left * right < 0:
                                f_val = float(f.subs(x, point).evalf())
                                st.warning(f"🔄 **Punto de Inflexión:** x = {point:.4f}, f(x) = {f_val:.4f}")
                                inflection_real.append((point, f_val))

                if not inflection_real:
                    st.info("ℹ️ No hay puntos de inflexión")

                # Determinar intervalos de concavidad
                st.markdown("**Intervalos de Concavidad:**")
                test_points = sorted([p for p, _ in inflection_real] + [float(a_trazo), float(b_trazo)])
                f_double_lambda = sp.lambdify(x, f_double_prime, 'numpy')

                for i in range(len(test_points) - 1):
                    mid_point = (test_points[i] + test_points[i + 1]) / 2
                    f_double_val = float(f_double_lambda(mid_point))

                    if f_double_val > 0:
                        st.success(f"🟢 ({test_points[i]:.2f}, {test_points[i+1]:.2f}): Cóncava arriba (∪)")
                    else:
                        st.error(f"🔴 ({test_points[i]:.2f}, {test_points[i+1]:.2f}): Cóncava abajo (∩)")

            st.markdown("---")

            # ===== TABLA RESUMEN ASCII =====
            st.markdown("### 📊 Tabla Resumen de Características")

            resumen = f"""
┌────────────────────────────────────────────────────────────────┐
│                    ANÁLISIS COMPLETO DE f(x)                   │
├────────────────────────────────────────────────────────────────┤
│ Función:        {str(f)[:50]:<50} │
├────────────────────────────────────────────────────────────────┤
│ 1. DOMINIO:     {dominio_desc[:50]:<50} │
├────────────────────────────────────────────────────────────────┤
│ 2. SIMETRÍA:    {simetria[:50]:<50} │
├────────────────────────────────────────────────────────────────┤
│ 3. ASÍNTOTAS:                                                  │
│    - Verticales:   {len(asintotas_vert)} asíntota(s)                                    │
│    - Horizontales: {len(asintotas_horiz)} asíntota(s)                                    │
├────────────────────────────────────────────────────────────────┤
│ 4. EXTREMOS:                                                   │
│    - Máximos:      {len(maximos)} punto(s)                                       │
│    - Mínimos:      {len(minimos)} punto(s)                                       │
├────────────────────────────────────────────────────────────────┤
│ 5. INFLEXIÓN:   {len(inflection_real)} punto(s)                                       │
└────────────────────────────────────────────────────────────────┘
            """
            st.code(resumen, language="text")

            st.markdown("---")

            # ===== PASO 6: GRÁFICA FINAL =====
            st.markdown("### Paso 6: Gráfica Final Completa")

            x_vals = np.linspace(float(a_trazo), float(b_trazo), 2000)
            f_lambda = sp.lambdify(x, f, 'numpy')
            f_double_lambda = sp.lambdify(x, f_double_prime, 'numpy')

            # Manejar posibles singularidades
            y_vals = []
            x_vals_clean = []
            y_double_vals = []

            for xi in x_vals:
                try:
                    yi = float(f_lambda(xi))
                    y_double = float(f_double_lambda(xi))
                    if not np.isnan(yi) and not np.isinf(yi) and abs(yi) < 1e6:
                        x_vals_clean.append(xi)
                        y_vals.append(yi)
                        y_double_vals.append(y_double)
                except:
                    pass

            x_vals_clean = np.array(x_vals_clean)
            y_vals = np.array(y_vals)
            y_double_vals = np.array(y_double_vals)

            # Crear gráfica
            fig = go.Figure()

            # Graficar función con código de colores por concavidad
            concava_arriba_x = []
            concava_arriba_y = []
            concava_abajo_x = []
            concava_abajo_y = []

            for xi, yi, y_double in zip(x_vals_clean, y_vals, y_double_vals):
                if y_double > 0:
                    concava_arriba_x.append(xi)
                    concava_arriba_y.append(yi)
                else:
                    concava_abajo_x.append(xi)
                    concava_abajo_y.append(yi)

            # Plot regiones
            if concava_arriba_x:
                fig.add_trace(
                    go.Scatter(x=concava_arriba_x, y=concava_arriba_y,
                              mode='lines',
                              name='Cóncava Arriba',
                              line=dict(color='green', width=3))
                )

            if concava_abajo_x:
                fig.add_trace(
                    go.Scatter(x=concava_abajo_x, y=concava_abajo_y,
                              mode='lines',
                              name='Cóncava Abajo',
                              line=dict(color='red', width=3))
                )

            # Asíntotas verticales
            for av in asintotas_vert:
                if a_trazo <= av <= b_trazo:
                    fig.add_vline(x=av, line_dash="dash", line_color="orange",
                                 annotation_text=f"AV: x={av:.2f}",
                                 annotation_position="top")

            # Asíntotas horizontales
            for ah in asintotas_horiz:
                fig.add_hline(y=ah, line_dash="dash", line_color="cyan",
                             annotation_text=f"AH: y={ah:.2f}",
                             annotation_position="right")

            # Máximos locales
            for xm, ym in maximos:
                if a_trazo <= xm <= b_trazo:
                    fig.add_trace(
                        go.Scatter(x=[xm], y=[ym],
                                 mode='markers+text',
                                 marker=dict(size=15, color='red', symbol='triangle-up'),
                                 text=[f'Máx'],
                                 textposition='top center',
                                 name=f'Máximo: ({xm:.2f}, {ym:.2f})',
                                 showlegend=True)
                    )

            # Mínimos locales
            for xm, ym in minimos:
                if a_trazo <= xm <= b_trazo:
                    fig.add_trace(
                        go.Scatter(x=[xm], y=[ym],
                                 mode='markers+text',
                                 marker=dict(size=15, color='green', symbol='triangle-down'),
                                 text=[f'Mín'],
                                 textposition='bottom center',
                                 name=f'Mínimo: ({xm:.2f}, {ym:.2f})',
                                 showlegend=True)
                    )

            # Puntos de inflexión
            for xi, yi in inflection_real:
                if a_trazo <= xi <= b_trazo:
                    fig.add_trace(
                        go.Scatter(x=[xi], y=[yi],
                                 mode='markers+text',
                                 marker=dict(size=18, color='purple', symbol='diamond',
                                           line=dict(width=2, color='white')),
                                 text=[f'Inf'],
                                 textposition='middle right',
                                 name=f'Inflexión: ({xi:.2f}, {yi:.2f})',
                                 showlegend=True)
                    )

            fig.update_layout(
                title=f"Trazo Completo: f(x) = {str(f)}",
                xaxis_title="x",
                yaxis_title="y",
                height=600,
                showlegend=True,
                hovermode='x unified'
            )

            st.plotly_chart(fig, use_container_width=True)

            # Leyenda explicativa
            st.markdown("---")
            st.subheader("📖 Leyenda de la Gráfica")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("""
                **Concavidad:**
                - 🟢 Verde: Cóncava arriba (∪)
                - 🔴 Rojo: Cóncava abajo (∩)
                """)

            with col2:
                st.markdown("""
                **Puntos Críticos:**
                - 🔺 Triángulo rojo: Máximo
                - 🔻 Triángulo verde: Mínimo
                - 💎 Diamante morado: Inflexión
                """)

            with col3:
                st.markdown("""
                **Asíntotas:**
                - 🟠 Línea naranja: Vertical
                - 🔵 Línea cyan: Horizontal
                """)

        except Exception as e:
            st.error(f"❌ Error al procesar la función: {str(e)}")
            st.info("💡 Verifica la sintaxis de tu función. Consulta la pestaña 'Ayuda' para más información.")

# ==================== TAB 4: EJEMPLOS ====================
with tab4:
    st.header("📚 Ejemplos Organizados por Sección")
    st.markdown("*Funciones de prueba organizadas según las secciones del curso*")

    # Sección 3.1
    st.markdown("## 📈 Sección 3.1: Máximos y Mínimos")
    st.markdown("*Funciones para practicar el criterio de la primera y segunda derivada*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Ejemplos Básicos")
        st.code("x**2 - 4*x + 3", language="python")
        st.caption("Parábola simple con un mínimo")

        st.code("2*x**3 + x**2 + 2*x", language="python")
        st.caption("Función cúbica con puntos críticos")

        st.code("-x**2 + 6*x - 5", language="python")
        st.caption("Parábola invertida con un máximo")

    with col2:
        st.markdown("### Ejemplos Avanzados")
        st.code("x**3 - 3*x**2 - 9*x + 5", language="python")
        st.caption("Función cúbica con máximo y mínimo")

        st.code("x**4 - 4*x**3 + 4*x**2", language="python")
        st.caption("Función de cuarto grado")

        st.code("x**3 - 12*x + 1", language="python")
        st.caption("Cúbica con dos extremos locales")

    st.markdown("---")

    # Sección 3.3
    st.markdown("## 🔄 Sección 3.3: Concavidad y Puntos de Inflexión")
    st.markdown("*Funciones para estudiar la segunda derivada y curvatura*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Ejemplos Básicos")
        st.code("x**3", language="python")
        st.caption("Función cúbica simple con inflexión en origen")

        st.code("x**3 - 3*x**2", language="python")
        st.caption("Cúbica con punto de inflexión")

        st.code("x**4 - 6*x**2", language="python")
        st.caption("Función de cuarto grado")

    with col2:
        st.markdown("### Ejemplos Avanzados")
        st.code("3*x**4 - 4*x**3 - 12*x**2 + 5", language="python")
        st.caption("Cuarto grado con múltiples inflexiones")

        st.code("x**3 - 3*x**2 - 9*x + 4", language="python")
        st.caption("Cúbica compleja")

        st.code("x**5 - 5*x**3 + 4*x", language="python")
        st.caption("Quinto grado con varios puntos de inflexión")

    st.markdown("---")

    # Sección 3.5
    st.markdown("## 🎨 Sección 3.5: Trazo de Curvas")
    st.markdown("*Funciones completas para análisis integral*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Polinomios")
        st.code("2 + 3*x - x**3", language="python")
        st.caption("Cúbica con término constante")

        st.code("2*x**3 - 3*x**2 - 12*x", language="python")
        st.caption("Cúbica sin término independiente")

        st.code("x**4 - 2*x**2 + 1", language="python")
        st.caption("Función de cuarto grado simétrica")

    with col2:
        st.markdown("### Funciones Especiales")
        st.code("1/x", language="python")
        st.caption("Hipérbola con asíntotas")

        st.code("x + 1/x", language="python")
        st.caption("Combinación lineal-hiperbólica")

        st.code("exp(-x**2)", language="python")
        st.caption("Campana de Gauss")

    st.markdown("---")

    # Funciones trigonométricas
    st.markdown("## 〰️ Funciones Trigonométricas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.code("sin(x)", language="python")
        st.caption("Seno básico")

        st.code("cos(x)", language="python")
        st.caption("Coseno básico")

    with col2:
        st.code("sin(x) + cos(x)", language="python")
        st.caption("Suma trigonométrica")

        st.code("x*sin(x)", language="python")
        st.caption("Producto con seno")

    with col3:
        st.code("sin(x)/x", language="python")
        st.caption("Función sinc")

        st.code("exp(x)*sin(x)", language="python")
        st.caption("Exponencial-trigonométrica")

    st.markdown("---")

    # Tips
    st.info("""
    **💡 Consejos para usar los ejemplos:**

    1. Copia el código y pégalo en el campo de entrada de cualquier pestaña
    2. Ajusta los límites del intervalo según la función
    3. Para funciones con asíntotas (como 1/x), evita incluir el punto singular
    4. Funciones trigonométricas: usa intervalos como [-2*pi, 2*pi] o [-6.28, 6.28]
    5. Experimenta modificando coeficientes para ver cómo cambia el comportamiento
    """)

# ==================== TAB 5: AYUDA ====================
with tab5:
    st.header("ℹ️ Guía de Uso y Sintaxis")

    # Sintaxis básica
    st.markdown("## 📝 Sintaxis de Funciones")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Operaciones Básicas")
        sintaxis_basica = """
        ✓ Suma:            x + 2
        ✓ Resta:           x - 3
        ✓ Multiplicación:  2*x  (NO usar 2x)
        ✓ División:        x/2
        ✓ Potencias:       x**2, x**3
        ✓ Raíz cuadrada:   sqrt(x)
        ✓ Valor absoluto:  Abs(x)
        """
        st.code(sintaxis_basica, language="text")

    with col2:
        st.markdown("### Funciones Matemáticas")
        funciones = """
        ✓ Exponencial:     exp(x)
        ✓ Logaritmo:       log(x)    [ln(x)]
        ✓ Logaritmo base 10: log(x, 10)
        ✓ Seno:            sin(x)
        ✓ Coseno:          cos(x)
        ✓ Tangente:        tan(x)
        ✓ Arcoseno:        asin(x)
        ✓ Arcocoseno:      acos(x)
        ✓ Arcotangente:    atan(x)
        """
        st.code(funciones, language="text")

    st.markdown("---")

    # Ejemplos de sintaxis
    st.markdown("## 💡 Ejemplos de Sintaxis Correcta vs Incorrecta")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ **CORRECTO**")
        ejemplos_correctos = """
        2*x + 3           # Multiplicación explícita
        x**2 - 4*x + 3    # Potencias con **
        sin(x)*cos(x)     # Funciones trigonométricas
        (x + 1)/(x - 1)   # División con paréntesis
        exp(-x**2)        # Exponencial de potencia
        sqrt(x**2 + 1)    # Raíz cuadrada
        3*x**3 - 2*x      # Polinomio
        1/x + x           # Suma de términos
        """
        st.code(ejemplos_correctos, language="python")

    with col2:
        st.error("❌ **INCORRECTO**")
        ejemplos_incorrectos = """
        2x + 3            # Falta *
        x^2 - 4x + 3      # Usar ^ en vez de **
        sen(x)*cos(x)     # 'sen' no existe, usar 'sin'
        (x + 1)/(x - 1    # Falta paréntesis
        e^(-x^2)          # Usar exp() y **
        √(x^2 + 1)        # Usar sqrt()
        3x³ - 2x          # Símbolos unicode
        1/x + x)          # Paréntesis desbalanceado
        """
        st.code(ejemplos_incorrectos, language="python")

    st.markdown("---")

    # Casos especiales
    st.markdown("## 🔧 Casos Especiales")

    st.markdown("### Constantes Matemáticas")
    col1, col2 = st.columns(2)

    with col1:
        st.code("pi          # π ≈ 3.14159", language="python")
        st.code("E           # e ≈ 2.71828", language="python")

    with col2:
        st.code("sin(pi/2)   # = 1", language="python")
        st.code("exp(1)      # = e", language="python")

    st.markdown("### Funciones Racionales")
    st.code("1/x                    # Hipérbola (asíntota en x=0)", language="python")
    st.code("(x**2 - 1)/(x - 1)     # Simplificable a x+1 (discontinuidad removible)", language="python")
    st.code("1/(x**2 + 1)           # Sin asíntotas verticales", language="python")

    st.markdown("### Funciones Compuestas")
    st.code("sin(x**2)              # Seno de x cuadrado", language="python")
    st.code("exp(sin(x))            # e elevado a seno de x", language="python")
    st.code("log(x**2 + 1)          # Logaritmo de un polinomio", language="python")

    st.markdown("---")

    # Troubleshooting
    st.markdown("## 🔍 Solución de Problemas (Troubleshooting)")

    with st.expander("⚠️ Error: 'name X is not defined'"):
        st.markdown("""
        **Causa:** Uso de variable no reconocida o sintaxis incorrecta.

        **Solución:**
        - Usa solo la variable `x` (minúscula)
        - Verifica que todas las funciones estén escritas correctamente
        - Ejemplo: `sin(x)` no `sen(x)`, `exp(x)` no `e^x`
        """)

    with st.expander("⚠️ Error: 'unexpected character after line continuation'"):
        st.markdown("""
        **Causa:** Uso de caracteres especiales o símbolos no válidos.

        **Solución:**
        - No uses símbolos unicode (√, ², ³, π)
        - Reemplaza √ por sqrt()
        - Reemplaza ² por **2
        - Reemplaza π por pi
        """)

    with st.expander("⚠️ La gráfica no se muestra correctamente"):
        st.markdown("""
        **Posibles causas y soluciones:**

        1. **Asíntotas verticales en el intervalo:**
           - Ajusta los límites para evitar puntos singulares
           - Ejemplo: para f(x) = 1/x, evita incluir x = 0

        2. **Valores muy grandes o muy pequeños:**
           - Reduce el intervalo de graficación
           - Ajusta el rango de visualización

        3. **Función muy compleja:**
           - Simplifica la expresión si es posible
           - Aumenta el intervalo para ver el comportamiento global
        """)

    with st.expander("⚠️ No encuentra puntos críticos"):
        st.markdown("""
        **Posibles razones:**

        1. La función realmente no tiene puntos críticos en ℝ
           - Ejemplo: f(x) = exp(x) no tiene extremos

        2. Los puntos críticos son complejos
           - La app solo muestra puntos reales

        3. La función es constante
           - f'(x) = 0 en todo el dominio
        """)

    with st.expander("⚠️ División por cero o asíntotas"):
        st.markdown("""
        **Manejo de asíntotas:**

        1. **Asíntotas verticales:**
           - La app las detecta automáticamente
           - Se muestran como líneas punteadas naranjas
           - Evita incluir estos puntos en el intervalo

        2. **Asíntotas horizontales:**
           - Se calculan mediante límites al infinito
           - Se muestran como líneas punteadas cyan

        **Ejemplos:**
        - `1/x`: Asíntota vertical en x=0, horizontal en y=0
        - `(x**2)/(x**2+1)`: Asíntota horizontal en y=1
        """)

    st.markdown("---")

    # Tips avanzados
    st.markdown("## 🎓 Consejos Avanzados")

    st.info("""
    **Para análisis de máximos y mínimos:**
    - Usa intervalos que incluyan varios períodos si es una función periódica
    - Para polinomios, el intervalo debe ser ~2 veces el rango de raíces esperadas
    - Verifica siempre el criterio de la segunda derivada

    **Para análisis de concavidad:**
    - Busca puntos donde f''(x) cambie de signo
    - Los puntos de inflexión son cruciales para el trazo de curvas
    - Observa cómo la concavidad afecta la forma de la gráfica

    **Para trazo completo:**
    - Sigue los 6 pasos en orden para un análisis sistemático
    - Presta atención a todas las características (simetrías, asíntotas, etc.)
    - La gráfica final debe reflejar TODAS las características encontradas

    **Recomendaciones generales:**
    - Comienza con funciones simples y aumenta la complejidad
    - Compara los resultados numéricos con la gráfica visual
    - Usa la tabla resumen ASCII para tener una visión global
    - Experimenta cambiando coeficientes para entender el comportamiento
    """)

    st.markdown("---")

    # Rangos recomendados
    st.markdown("## 📏 Rangos Recomendados por Tipo de Función")

    rangos_tabla = [
        {"Tipo de Función": "Polinomio grado 2-3", "Intervalo Sugerido": "[-5, 5]", "Ejemplo": "x**3 - 3*x"},
        {"Tipo de Función": "Polinomio grado 4-5", "Intervalo Sugerido": "[-3, 3]", "Ejemplo": "x**4 - 2*x**2"},
        {"Tipo de Función": "Función racional", "Intervalo Sugerido": "[-10, 10]", "Ejemplo": "1/x"},
        {"Tipo de Función": "Trigonométrica", "Intervalo Sugerido": "[-2*pi, 2*pi] ≈ [-6.28, 6.28]", "Ejemplo": "sin(x)"},
        {"Tipo de Función": "Exponencial", "Intervalo Sugerido": "[-3, 3]", "Ejemplo": "exp(x)"},
        {"Tipo de Función": "Logarítmica", "Intervalo Sugerido": "[0.1, 10]", "Ejemplo": "log(x)"},
    ]

    st.table(rangos_tabla)

    st.markdown("---")

    # Referencias
    st.markdown("## 📚 Referencias y Recursos")

    st.markdown("""
    **Documentación de SymPy:**
    - [SymPy Documentation](https://docs.sympy.org/)
    - [SymPy Tutorial](https://docs.sympy.org/latest/tutorial/index.html)

    **Recursos de Cálculo:**
    - Sección 3.1: Máximos y Mínimos Locales
    - Sección 3.3: Concavidad y Puntos de Inflexión
    - Sección 3.5: Trazo de Curvas

    **Herramientas Relacionadas:**
    - Wolfram Alpha (verificación de resultados)
    - Desmos (visualización gráfica)
    - GeoGebra (geometría dinámica)
    """)

# Footer
st.markdown("---")
st.caption("🧮 TIF Cálculo Fase III - UCSM 2025 | Desarrollado con Streamlit + SymPy + Plotly")
st.caption("Autor: Aron | Versión 2.0 - Análisis Completo de Derivadas")
