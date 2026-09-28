import streamlit as st


st.set_page_config(
    page_title="NÉVORA | Real Estate & Smart Investment",
    page_icon="💎",
    layout="wide"
)


st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1E293B;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #E2E8F0;
    }
    </style>
""", unsafe_allow_html=True)


PROPIEDADES = [
    {
        "id": 1,
        "titulo": "Urban Loft Airbnb Ready - La Carolina",
        "tipo": "Suite",
        "precio": 89000,
        "ubicacion": "La Carolina, Quito",
        "estilo_vida": "Inversión Airbnb",
        "habitaciones": 1,
        "banos": 1,
        "area": 58,
        "plusvalia_anual": 6.5,  # % estimación anual
        "imagen": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=700&q=80",
        "destacado": "Rentabilidad estimada del 9% anual en rentas cortas.",
        "whatsapp": "593999999999"
    },
    {
        "id": 2,
        "titulo": "Smart Villa Eco-Friendly - Cumbayá",
        "tipo": "Casa",
        "precio": 265000,
        "ubicacion": "Cumbayá, Quito",
        "estilo_vida": "Naturaleza & Lujo",
        "habitaciones": 3,
        "banos": 3,
        "area": 210,
        "plusvalia_anual": 8.0,
        "imagen": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=700&q=80",
        "destacado": "Paneles solares, domótica integral y piscina privada.",
        "whatsapp": "593999999999"
    },
    {
        "id": 3,
        "titulo": "Penthouse Panoramic View - Tumbaco",
        "tipo": "Departamento",
        "precio": 178000,
        "ubicacion": "Tumbaco, Quito",
        "estilo_vida": "Familia & Pet Friendly",
        "habitaciones": 3,
        "banos": 2.5,
        "area": 140,
        "plusvalia_anual": 5.8,
        "imagen": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=700&q=80",
        "destacado": "Terraza privada de 40m² con pérgola y zona de BBQ.",
        "whatsapp": "593999999999"
    }
]


st.markdown("<h1 class='main-title'>NÉVORA Smart Real Estate</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Inmuebles seleccionados con alta proyección de plusvalía y retorno de inversión</p>", unsafe_allow_html=True)


st.sidebar.header("🎯 Experiencia de Búsqueda")

estilo_seleccionado = st.sidebar.selectbox(
    "Filtrar por Estilo de Vida",
    options=["Todos", "Inversión Airbnb", "Naturaleza & Lujo", "Familia & Pet Friendly"]
)

precio_max = st.sidebar.slider("Presupuesto Máximo (USD)", 50000, 350000, 300000, step=10000)

st.sidebar.divider()
st.sidebar.subheader("🧮 Simulador Hipotecario")
entrada_porcentaje = st.sidebar.slider("Entrada Inicial (%)", 10, 50, 20)
plazo_anos = st.sidebar.selectbox("Plazo del Crédito (Años)", [10, 15, 20])
tasa_interes = 8.5  # % tasa promedio


propiedades_filtradas = [
    p for p in PROPIEDADES 
    if (estilo_seleccionado == "Todos" or p["estilo_vida"] == estilo_seleccionado) 
    and p["precio"] <= precio_max
]


st.subheader(f"Propiedades Exclusivas Encontradas ({len(propiedades_filtradas)})")

for p in propiedades_filtradas:
    with st.container(border=True):
        col_img, col_info, col_calc = st.columns([1.2, 1.5, 1.3])
        
        
        with col_img:
            st.image(p["imagen"], use_container_width=True)
            st.caption(f"🏷️ **Estilo:** {p['estilo_vida']}")
        
        
        with col_info:
            st.subheader(p["titulo"])
            st.markdown(f"### **💰 ${p['precio']:,} USD**")
            st.write(f"📍 **Ubicación:** {p['ubicacion']}")
            st.write(f"📐 **Área:** {p['area']} m² | 🛏️ {p['habitaciones']} Hab | 🚿 {p['banos']} Baños")
            st.info(f"✨ **Highlight:** {p['destacado']}")
            
            
            mensaje_wa = f"Hola NÉVORA, deseo más información sobre: {p['titulo']}"
            url_wa = f"https://wa.me/{p['whatsapp']}?text={mensaje_wa.replace(' ', '%20')}"
            st.link_button("📲 Chatear por WhatsApp", url_wa)

        
        with col_calc:
            st.markdown("#### 🚀 Proyección Financiera")
            
            
            valor_futuro = p["precio"] * ((1 + (p["plusvalia_anual"] / 100)) ** 5)
            ganancia = valor_futuro - p["precio"]
            
            
            monto_entrada = p["precio"] * (entrada_porcentaje / 100)
            monto_credito = p["precio"] - monto_entrada
            i = (tasa_interes / 100) / 12
            n = plazo_anos * 12
            cuota_mensual = monto_credito * (i * (1 + i)**n) / ((1 + i)**n - 1)

            st.metric(
                label="Plusvalía estimada en 5 años", 
                value=f"${valor_futuro:,.0f} USD", 
                delta=f"+${ganancia:,.0f} USD (+{p['plusvalia_anual']*5}%)"
            )
            
            st.markdown(f"**Cuota mensual estimada:** `${cuota_mensual:,.2f} USD/mes`")
            st.caption(f"Calculado con {entrada_porcentaje}% de entrada (${monto_entrada:,.0f} USD) a {plazo_anos} años.")


st.divider()
st.caption("© 2026 NÉVORA Smart Real Estate. Proyecciones financieras estimadas según mercado.")