import streamlit as st

# Funciones
def calcular_B(E, R):
    return round(E + R, 2)

def calcular_mm(R, E, D):
    if D == 0:
        return "Error: D no puede ser 0."
    e = E / D
    r = R / D
    if e < 0:
        return "Error: e debe ser mayor o igual a 0 (E/D ≥ 0)."
    if not (0 < r <= 1):
        return "Error: r debe estar entre 0 y 1 (1 incluido)."
    return round((e + 1) / (e + r), 2)

def calcular_M(R, E, D):
    if D == 0:
        return "Error: D no puede ser 0."
    e = E / D
    r = R / D
    if e < 0:
        return "Error: e debe ser mayor o igual a 0 (E/D ≥ 0)."
    if not (0 < r <= 1):
        return "Error: r debe estar entre 0 y 1 (1 incluido)."
    B = E + R
    M = ((e + 1) / (e + r)) * B
    return round(e, 2), round(r, 2), round(B, 2), round(M, 2)

# Título
st.title("Calculadora Multiplicador Monetario")

# Entradas
R = st.number_input("Reservas R:", value=20.0, step=0.1)
E = st.number_input("Efectivo E:", value=30.0, step=0.1)
D = st.number_input("Depósitos D:", value=10.0, step=0.1)

# Botones
if st.button("Calcular B"):
    st.success(f"B (Base Monetaria): {calcular_B(E, R)}")

if st.button("Calcular mm"):
    st.success(f"mm (Multiplicador Monetario): {calcular_mm(R, E, D)}")

if st.button("Calcular M"):
    res = calcular_M(R, E, D)
    if isinstance(res, str):
        st.error(res)
    else:
        e, r, B, M = res
        st.subheader("Multiplicador Monetario: Calculadora")
        st.write(f"e (E/D): {e}")
        st.write(f"r (R/D): {r}")
        st.write(f"B (Base Monetaria): {B}")
        st.write(f"M (Cantidad Nominal de Dinero): {M}")
