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

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Análisis", "📚 Ejemplos", "ℹ️ Ayuda"])

with tab1:
    st.header("Análisis de Función")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        funcion_str = st.text_input(
            "Función f(x):",
            value="x**3 - 3*x**2 - 9*x + 5",
            help="Usa ** para potencias"
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            a = st.number_input("Límite inferior", value=-5.0)
        with col_b:
            b = st.number_input("Límite superior", value=5.0)
    
    with col2:
        st.markdown("### Ejemplos")
        st.code("x**2 - 4")
        st.code("x**3 - 3*x")
        st.code("sin(x)")
    
    if st.button("🚀 Analizar", type="primary"):
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
            st.subheader("🎯 Puntos Críticos")
            critical_points = sp.solve(f_prime, x)
            critical_real = [float(p.evalf()) for p in critical_points if p.is_real]
            
            if critical_real:
                st.success(f"Encontrados: {len(critical_real)} puntos")
                
                for i, point in enumerate(critical_real, 1):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric(f"x{i}", f"{point:.4f}")
                    
                    with col2:
                        f_val = float(f.subs(x, point).evalf())
                        st.metric(f"f(x{i})", f"{f_val:.4f}")
                    
                    with col3:
                        second = float(f_double_prime.subs(x, point).evalf())
                        if second > 0:
                            st.metric("Tipo", "Mínimo", delta="⬆️")
                        elif second < 0:
                            st.metric("Tipo", "Máximo", delta="⬇️")
                        else:
                            st.metric("Tipo", "Inflexión", delta="➡️")
            else:
                st.warning("No hay puntos críticos reales")
            
            st.markdown("---")
            
            # Gráfica
            st.subheader("📊 Gráfica")
            
            x_vals = np.linspace(float(a), float(b), 500)
            f_lambda = sp.lambdify(x, f, 'numpy')
            f_prime_lambda = sp.lambdify(x, f_prime, 'numpy')
            
            y_vals = f_lambda(x_vals)
            y_prime_vals = f_prime_lambda(x_vals)
            
            fig = make_subplots(
                rows=2, cols=1,
                subplot_titles=('f(x)', "f'(x)"),
                vertical_spacing=0.15
            )
            
            fig.add_trace(
                go.Scatter(x=x_vals, y=y_vals, name='f(x)', 
                          line=dict(color='blue', width=2)),
                row=1, col=1
            )
            
            # Marcar puntos críticos
            for point in critical_real:
                if a <= point <= b:
                    f_val = float(f.subs(x, point).evalf())
                    fig.add_trace(
                        go.Scatter(x=[point], y=[f_val], 
                                 mode='markers',
                                 marker=dict(size=12, color='red'),
                                 name=f'x={point:.2f}'),
                        row=1, col=1
                    )
            
            fig.add_trace(
                go.Scatter(x=x_vals, y=y_prime_vals, name="f'(x)", 
                          line=dict(color='green', width=2)),
                row=2, col=1
            )
            
            fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)
            
            fig.update_xaxes(title_text="x", row=2, col=1)
            fig.update_yaxes(title_text="y", row=1, col=1)
            fig.update_yaxes(title_text="y'", row=2, col=1)
            
            fig.update_layout(height=700, showlegend=True)
            
            st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

with tab2:
    st.header("📚 Ejemplos del PDF")
    
    st.markdown("""
    ### Ejemplos de funciones a probar:
    
    **Sección 3.1 - Máximos y Mínimos:**
```
    2*x**3 + x**2 + 2*x
    3*x**2 - 12*x + 5
```
    
    **Sección 3.3 - Concavidad:**
```
    3*x**4 - 4*x**3 - 12*x**2 + 5
    x**3 - 3*x**2 - 9*x + 4
```
    
    **Sección 3.5 - Trazo:**
```
    2 + 3*x - x**3
    2*x**3 - 3*x**2 - 12*x
```
    """)

with tab3:
    st.header("ℹ️ Ayuda")
    
    st.markdown("""
    ## Sintaxis de Funciones
    
    - Potencias: `x**2`, `x**3`
    - Multiplicación: `2*x` (no `2x`)
    - Funciones: `sin(x)`, `cos(x)`, `exp(x)`, `log(x)`
    
    ## Interpretación
    
    - **Puntos Críticos:** Donde f'(x) = 0
    - **Máximo Local:** f''(x) < 0
    - **Mínimo Local:** f''(x) > 0
    """)

st.markdown("---")
st.caption("TIF Cálculo Fase III - UCSM 2025")
