import streamlit as st
import datetime

# Configuração da página
st.set_page_config(
    page_title="Gestão de Consultas", 
    page_icon="🏥",
    layout="wide"
)

# CSS personalizado + IDs específicos para automação
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
        margin-bottom: 0px !important;
        margin-top: 3px !important;
        line-height: 1.1 !important;
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
        margin-top: 0px !important;
    }
    
    .stTextArea {
        margin-bottom: 5px !important;
        margin-top: 0px !important;
    }
    
    /* Reduzir padding interno das caixas de texto */
    .stTextArea textarea {
        padding: 8px !important;
        line-height: 1.2 !important;
    }
    
    /* Reduzir espaço entre label e input */
    .stTextArea > label {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }
    
    /* Reduzir espaçamento do título principal */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0px !important;
    }
    
    /* Reduzir espaçamento do título h1 */
    h1 {
        margin-top: 0px !important;
        margin-bottom: 5px !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }
    
    /* Remover espaçamento superior da página */
    .stApp > header {
        height: 0px !important;
    }
    
    /* Reduzir espaçamento do container principal */
    .main {
        padding-top: 0px !important;
        margin-top: 0px !important;
    }
    
    /* Classes específicas para identificação em automação */
    .automation-marker {
        display: none;
    }
    
    /* Marcar visualmente os elementos para automação (opcional - remove se não quiseres) */
    [data-automation]:hover {
        outline: 2px dashed #ff9800;
    }
</style>

<!-- Marcadores invisíveis para identificar a página atual -->
<div id="page-marker" class="automation-marker" data-page="screen1"></div>

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
    # Atualizar marcador de página
    st.markdown("""
    <div id="page-marker" class="automation-marker" data-page="screen1" data-screen="consultas-list"></div>
    <div id="screen-identifier" data-automation="screen1" data-screen-name="lista-consultas"></div>
    """, unsafe_allow_html=True)
    
    st.title("🏥 Gestão de Consultas")
    st.markdown("---")
    
    # Header com data
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="header-compact" id="header-hoje" data-automation="header-consultas">
            <h2>Consultas de Hoje</h2>
            <p>{datetime.date.today().strftime('%A, %d de %B de %Y')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Lista de Consultas")
    
    # Próxima consulta (primeira)
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div class="consulta-card" id="consulta-maria" data-automation="primeira-consulta" data-paciente="maria-santos">
            <h3>🩺 Dr. João Silva - Cardiologia</h3>
            <p><strong>Paciente:</strong> Maria José Santos</p>
            <p><strong>Tipo:</strong> Consulta de rotina</p>
            <p><strong>Hora:</strong> ⏰ 09:30</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        # Botão com ID específico e atributos de automação
        botao_container = st.container()
        with botao_container:
            st.markdown('<div id="botao-entrar-container" data-automation="botao-container">', unsafe_allow_html=True)
            if st.button("🟢 Entrar na Consulta", type="primary", key="btn_entrar_consulta", help="Clique para iniciar a consulta"):
                change_screen(2)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Segunda consulta
    st.markdown("""
    <div class="consulta-card consulta-normal" id="consulta-jose" data-automation="segunda-consulta" data-paciente="jose-pereira">
        <h3>🔬 Dra. Ana Costa - Dermatologia</h3>
        <p><strong>Paciente:</strong> José Pereira</p>
        <p><strong>Tipo:</strong> Seguimento</p>
        <p><strong>Hora:</strong> ⏰ 14:00</p>
    </div>
    """, unsafe_allow_html=True)

# Ecrã 2 - Formulário SOAP
elif st.session_state.screen == 2:
    # Atualizar marcador de página
    st.markdown("""
    <div id="page-marker" class="automation-marker" data-page="screen2" data-screen="soap-form"></div>
    <div id="screen-identifier" data-automation="screen2" data-screen-name="formulario-soap"></div>
    """, unsafe_allow_html=True)
    
    st.title("📝 Registo da Consulta")
    
    # Info da consulta atual - só paciente
    st.markdown('<div class="compact-info" id="info-paciente" data-automation="paciente-info">Maria José Santos</div>', unsafe_allow_html=True)
    
    # Container para o formulário com ID específico
    st.markdown('<div id="soap-form-container" data-automation="soap-container">', unsafe_allow_html=True)
    
    with st.form("soap_form", clear_on_submit=False):
        st.markdown('<div id="soap-fields-container">', unsafe_allow_html=True)
        
        st.markdown('<p class="soap-label" data-automation="label-subjetivo">S - Subjetivo</p>', unsafe_allow_html=True)
        subjetivo = st.text_area(
            "",
            placeholder="Sintomas, queixas do paciente, história clínica...",
            height=68,
            key="soap_subjetivo",
            help="Campo Subjetivo do SOAP"
        )
        
        st.markdown('<p class="soap-label" data-automation="label-objetivo">O - Objetivo</p>', unsafe_allow_html=True)
        objetivo = st.text_area(
            "",
            placeholder="Sinais vitais, exame físico, observações...",
            height=68,
            key="soap_objetivo",
            help="Campo Objetivo do SOAP"
        )
        
        st.markdown('<p class="soap-label" data-automation="label-avaliacao">A - Avaliação</p>', unsafe_allow_html=True)
        avaliacao = st.text_area(
            "",
            placeholder="Diagnóstico, impressão clínica, análise...",
            height=68,
            key="soap_avaliacao",
            help="Campo Avaliação do SOAP"
        )
        
        st.markdown('<p class="soap-label" data-automation="label-plano">P - Plano</p>', unsafe_allow_html=True)
        plano = st.text_area(
            "",
            placeholder="Tratamento, medicação, seguimento, próximos passos...",
            height=68,
            key="soap_plano",
            help="Campo Plano do SOAP"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Botões com IDs específicos
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.markdown('<div id="botao-voltar-container" data-automation="voltar-container">', unsafe_allow_html=True)
            voltar = st.form_submit_button("⬅️ Voltar", use_container_width=True, help="Voltar à lista de consultas")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div id="botao-guardar-container" data-automation="guardar-container">', unsafe_allow_html=True)
            guardar = st.form_submit_button("💾 Guardar Consulta", type="primary", use_container_width=True, help="Guardar consulta SOAP")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Processamento dos botões
        if voltar:
            st.markdown('<div id="action-voltar" data-automation="action-triggered" data-action="voltar"></div>', unsafe_allow_html=True)
            change_screen(1)
        
        if guardar:
            st.markdown('<div id="action-guardar" data-automation="action-triggered" data-action="guardar"></div>', unsafe_allow_html=True)
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
                
                st.markdown('<div id="success-message" data-automation="success-state">', unsafe_allow_html=True)
                st.success("✅ Consulta guardada com sucesso!")
                st.balloons()
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Mostrar resumo
                with st.expander("📄 Resumo da Consulta Guardada"):
                    st.markdown('<div id="resumo-consulta" data-automation="resumo-container">', unsafe_allow_html=True)
                    st.write(f"**Paciente:** {st.session_state.consulta_data['paciente']}")
                    st.write(f"**Médico:** {st.session_state.consulta_data['medico']}")
                    st.write(f"**Data/Hora:** {st.session_state.consulta_data['timestamp']}")
                    st.write("**S -** " + (subjetivo or "Não preenchido"))
                    st.write("**O -** " + (objetivo or "Não preenchido"))
                    st.write("**A -** " + (avaliacao or "Não preenchido"))
                    st.write("**P -** " + (plano or "Não preenchido"))
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Botão para voltar
                st.markdown('<div id="botao-voltar-final-container" data-automation="voltar-final-container">', unsafe_allow_html=True)
                if st.button("🔙 Voltar à Lista de Consultas", key="voltar_final", help="Retornar à página inicial"):
                    change_screen(1)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div id="error-message" data-automation="error-state">', unsafe_allow_html=True)
                st.error("⚠️ Preencha pelo menos um campo antes de guardar!")
                st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.markdown('<div id="sidebar-container" data-automation="sidebar">', unsafe_allow_html=True)
    st.markdown("### ℹ️ Informações")
    st.markdown("""
    **SOAP** é um método de documentação médica:
    - **S** - Subjetivo
    - **O** - Objetivo
    - **A** - Avaliação
    - **P** - Plano
    """)
    
    if st.session_state.consulta_data:
        st.markdown("### 📊 Última Consulta")
        st.markdown('<div id="ultima-consulta-info" data-automation="ultima-consulta">', unsafe_allow_html=True)
        st.write(f"Paciente: {st.session_state.consulta_data.get('paciente', 'N/A')}")
        st.write(f"Guardada em: {st.session_state.consulta_data.get('timestamp', 'N/A')}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# JavaScript para melhorar a deteção de elementos (opcional)
st.markdown("""
<script>
// Adicionar evento para marcar quando a página está totalmente carregada
window.addEventListener('load', function() {
    // Adicionar atributo para indicar que a página está pronta
    document.body.setAttribute('data-page-loaded', 'true');
    document.body.setAttribute('data-automation-ready', 'true');
    
    // Adicionar timestamp de carregamento
    document.body.setAttribute('data-load-time', Date.now());
});

// Função para verificar se a página está pronta (pode ser útil para o Power Automate)
function isPageReady() {
    return document.body.getAttribute('data-page-loaded') === 'true';
}

// Adicionar classe específica quando elementos são clicados
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'BUTTON') {
        e.target.setAttribute('data-last-clicked', Date.now());
    }
});
</script>
""", unsafe_allow_html=True)
