import streamlit as st
import datetime

# Configuração da página
st.set_page_config(
    page_title="Gestão de Consultas", 
    page_icon="🏥",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
    .consulta-card {
        background: linear-gradient(135deg, #f8fff8 0%, #e8f5e8 100%);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00c851;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .consulta-normal {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left-color: #4facfe;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #00c851 0%, #00a041 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .soap-label {
        font-size: 18px;
        font-weight: bold;
        color: #4facfe;
        margin-bottom: 2px;
        margin-top: 5px;
    }
    
    .compact-info {
        background: #e3f2fd; 
        padding: 8px 15px; 
        border-radius: 8px; 
        margin-bottom: 15px;
        font-size: 14px;
    }
    
    .header-compact {
        text-align: center; 
        padding: 15px; 
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
        border-radius: 10px; 
        color: white; 
        margin-bottom: 20px;
    }
    
    /* Reduzir espaçamento entre campos do formulário */
    .stTextArea > div > div > div > div {
        margin-bottom: 0px !important;
    }
    
    .stTextArea {
        margin-bottom: 8px !important;
    }
    
    /* Reduzir padding interno das caixas de texto */
    .stTextArea textarea {
        padding: 8px !important;
        line-height: 1.2 !important;
    }
</style>
""", unsafe_allow_html=True)

# Estado da aplicação
if 'screen' not in st.session_state:
    st.session_state.screen = 1
if 'consulta_data' not in st.session_state:
    st.session_state.consulta_data = {}

# Função para mudar ecrã
def change_screen(screen_num):
    st.session_state.screen = screen_num
    st.rerun()

# Ecrã 1 - Lista de Consultas
if st.session_state.screen == 1:
    st.title("🏥 Gestão de Consultas")
    st.markdown("---")
    
    # Header com data
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="header-compact">
            <h2>Consultas de Hoje</h2>
            <p>{datetime.date.today().strftime('%A, %d de %B de %Y')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Lista de Consultas")
    
    # Próxima consulta (primeira)
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div class="consulta-card">
            <h3>🩺 Dr. João Silva - Cardiologia</h3>
            <p><strong>Paciente:</strong> Maria José Santos</p>
            <p><strong>Tipo:</strong> Consulta de rotina</p>
            <p><strong>Hora:</strong> ⏰ 09:30</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🟢 Entrar na Consulta", type="primary", key="btn1"):
            change_screen(2)
    
    # Segunda consulta
    st.markdown("""
    <div class="consulta-card consulta-normal">
        <h3>🔬 Dra. Ana Costa - Dermatologia</h3>
        <p><strong>Paciente:</strong> José Pereira</p>
        <p><strong>Tipo:</strong> Seguimento</p>
        <p><strong>Hora:</strong> ⏰ 14:00</p>
    </div>
    """, unsafe_allow_html=True)

# Ecrã 2 - Formulário SOAP
elif st.session_state.screen == 2:
    st.title("📝 Registo da Consulta")
    
    # Info da consulta atual - só paciente
    st.markdown('<div class="compact-info"><strong>👤 Paciente:</strong> Maria José Santos</div>', unsafe_allow_html=True)
    
    with st.form("soap_form"):
        st.markdown('<p class="soap-label">S - Subjetivo</p>', unsafe_allow_html=True)
        subjetivo = st.text_area(
            "",
            placeholder="Sintomas, queixas do paciente, história clínica...",
            height=68,
            key="s"
        )
        
        st.markdown('<p class="soap-label">O - Objetivo</p>', unsafe_allow_html=True)
        objetivo = st.text_area(
            "",
            placeholder="Sinais vitais, exame físico, observações...",
            height=68,
            key="o"
        )
        
        st.markdown('<p class="soap-label">A - Avaliação</p>', unsafe_allow_html=True)
        avaliacao = st.text_area(
            "",
            placeholder="Diagnóstico, impressão clínica, análise...",
            height=68,
            key="a"
        )
        
        st.markdown('<p class="soap-label">P - Plano</p>', unsafe_allow_html=True)
        plano = st.text_area(
            "",
            placeholder="Tratamento, medicação, seguimento, próximos passos...",
            height=68,
            key="p"
        )
        
        st.markdown("---")
        
        # Botões
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            voltar = st.form_submit_button("⬅️ Voltar", use_container_width=True)
        
        with col3:
            guardar = st.form_submit_button("💾 Guardar Consulta", type="primary", use_container_width=True)
        
        if voltar:
            change_screen(1)
        
        if guardar:
            if subjetivo or objetivo or avaliacao or plano:
                # Guardar dados da consulta
                st.session_state.consulta_data = {
                    'subjetivo': subjetivo,
                    'objetivo': objetivo,
                    'avaliacao': avaliacao,
                    'plano': plano,
                    'timestamp': datetime.datetime.now().strftime('%d/%m/%Y %H:%M'),
                    'paciente': 'Maria Santos',
                    'medico': 'Dr. João Silva'
                }
                
                st.success("✅ Consulta guardada com sucesso!")
                st.balloons()
                
                # Mostrar resumo
                with st.expander("📄 Resumo da Consulta Guardada"):
                    st.write(f"**Paciente:** {st.session_state.consulta_data['paciente']}")
                    st.write(f"**Médico:** {st.session_state.consulta_data['medico']}")
                    st.write(f"**Data/Hora:** {st.session_state.consulta_data['timestamp']}")
                    st.write("**S -** " + (subjetivo or "Não preenchido"))
                    st.write("**O -** " + (objetivo or "Não preenchido"))
                    st.write("**A -** " + (avaliacao or "Não preenchido"))
                    st.write("**P -** " + (plano or "Não preenchido"))
                
                # Botão para voltar
                if st.button("🔙 Voltar à Lista de Consultas"):
                    change_screen(1)
            else:
                st.error("⚠️ Preencha pelo menos um campo antes de guardar!")

# Sidebar com informações
with st.sidebar:
    st.markdown("### ℹ️ Informações")
    st.markdown("""
    **SOAP** é um método de documentação médica:
    - **S** - Subjetivo (sintomas do paciente)
    - **O** - Objetivo (exame físico)  
    - **A** - Avaliação (diagnóstico)
    - **P** - Plano (tratamento)
    """)
    
    if st.session_state.consulta_data:
        st.markdown("### 📊 Última Consulta")
        st.write(f"Paciente: {st.session_state.consulta_data.get('paciente', 'N/A')}")
        st.write(f"Guardada em: {st.session_state.consulta_data.get('timestamp', 'N/A')}")
