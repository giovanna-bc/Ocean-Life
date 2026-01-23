import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials,firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase.json")
    firebase_admin.initialize_app(cred)
db= firestore.client()
# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Ocean Life – Projeto Final",
    page_icon="🌊",
    layout="centered"
)

# ===============================
# ESTILOS PERSONALIZADOS
# ===============================
st.markdown("""
    <style>
    body {
        background-color: #e3f2fd;
    }
    .titulo {
        text-align: center;
        color: #013a63;
        font-size: 50px;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #014f86;
        font-size: 26px;
        margin-bottom: 25px;
    }
    .texto {
        font-size: 19px;
        color: #012a4a;
        text-align: justify;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.12);
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# ANIMAÇÃO INICIAL
# ===============================
with st.spinner("Preparando o projeto..."):
    time.sleep(1.2)

# ===============================
# TEXTO INICIAL
# ===============================
st.markdown("<div class='titulo'>🌊 Ocean Life</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Projeto Final</div>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
O projeto <strong>Ocean Life</strong> tem como objetivo conscientizar sobre a importância da
<strong>Vida na Água</strong>, abordando a biodiversidade aquática, os impactos ambientais
e as formas de preservação dos oceanos, rios e demais ecossistemas aquáticos.<br><br>

Através deste trabalho, buscamos informar, educar e incentivar atitudes sustentáveis,
destacando como cada ação humana pode influenciar diretamente o equilíbrio da vida no planeta.
</div>
""", unsafe_allow_html=True)

# ===============================
# FORMULÁRIO
# ===============================
st.markdown("<div class='subtitulo'>📝 Formulário de Participação</div>", unsafe_allow_html=True)

with st.form("formulario_participantes"):
    nome = st.text_input("Nome completo:")
    idade = st.number_input("Idade:", min_value=0, max_value=120)
    turma = st.text_input("Turma / Série:")
    email = st.text_input("E-mail:")
    opiniao = st.selectbox(
        "Você considera importante preservar a vida na água?",
        ["Sim", "Não", "Talvez"]
    )
    comentario = st.text_area("Deixe sua opinião ou sugestão sobre o projeto:")

    enviar = st.form_submit_button("Enviar")

# ===============================
# RESPOSTA AO ENVIO
# ===============================
if enviar:
    st.success("✅ Informações enviadas com sucesso!")
    st.write("*Resumo das informações:*")
    st.write(f"👤 Nome: {nome}")
    st.write(f"🎂 Idade: {idade}")
    st.write(f"🏫 Turma: {turma}")
    st.write(f"📧 E-mail: {email}")
    st.write(f"🌊 Importância da preservação: {opiniao}")
    st.write(f"💬 Comentário: {comentario}")
    st.balloons()
    db.collection("formulario").add(
        {
            "nome":nome,
            "idade":idade,
            "turma":turma,
            "email":email,
            "opniao":opiniao,
            "comentario":comentario   
        }
    )
    
    import streamlit as st
import time

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Explorando o Oceano",
    page_icon="🌊",
    layout="centered"
)

# ===============================
# ESTILOS PERSONALIZADOS (CSS)
# ===============================
st.markdown("""
    <style>
    body {
        background-color: #e3f2fd;
    }
    .titulo {
        text-align: center;
        color: #01579b;
        font-size: 48px;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #0277bd;
        font-size: 30px;
        margin-bottom: 30px;
    }
    .texto {
        font-size: 20px;
        color: #0d47a1;
        text-align: justify;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# ANIMAÇÃO DE ENTRADA
# ===============================
with st.spinner("Mergulhando no oceano..."):
    time.sleep(1.2)

# ===============================
# CONTEÚDO PRINCIPAL
# ===============================
st.markdown("<div class='titulo'>🌊 Explorando o Oceano</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>O que é?</div>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
A <strong>Vida na Água</strong> refere-se a todos os seres vivos que habitam ambientes aquáticos,
como oceanos, mares, rios, lagos e recifes de corais. Esses ecossistemas abrigam uma enorme
diversidade de formas de vida, desde microscópicos organismos até grandes animais marinhos,
como baleias e tubarões.<br><br>

Os oceanos desempenham um papel fundamental no equilíbrio do planeta. Eles ajudam a regular
o clima, produzem grande parte do oxigênio que respiramos e são essenciais para a cadeia
alimentar global. Além disso, a vida aquática contribui diretamente para a economia,
a alimentação humana e a manutenção da biodiversidade.<br><br>

Preservar a vida na água é garantir a sobrevivência não apenas das espécies marinhas,
mas também da própria humanidade. O uso consciente dos recursos naturais e a redução da
poluição são passos essenciais para proteger esse vasto e valioso patrimônio natural.
</div>
""", unsafe_allow_html=True)

# ===============================
# IMAGEM FINAL
# ===============================
st.image(
    "https://www.uninter.com/noticias/wp-content/uploads/2020/10/noticias_d0207546-gp0stpywj-1024x685.jpg",
    caption="O oceano é a base da vida no planeta",
    use_container_width=True
)

# ===============================
# ANIMAÇÃO FINAL
# ===============================

st.balloons()

import streamlit as st
import time

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Importância da Vida na Água",
    page_icon="🐠",
    layout="centered"
)

# ===============================
# ESTILOS PERSONALIZADOS
# ===============================
st.markdown("""
    <style>
    body {
        background-color: #e1f5fe;
    }
    .titulo {
        text-align: center;
        color: #01579b;
        font-size: 46px;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #0288d1;
        font-size: 28px;
        margin-bottom: 30px;
    }
    .texto {
        font-size: 19px;
        color: #0d47a1;
        text-align: justify;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.12);
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# ANIMAÇÃO INICIAL
# ===============================
with st.spinner("Carregando informações importantes..."):
    time.sleep(1.3)

# ===============================
# CONTEÚDO PRINCIPAL
# ===============================
st.markdown("<div class='titulo'>🌊 A Importância da Vida na Água</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Por que ela é tão essencial?</div>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
A <strong>Vida na Água</strong> é fundamental para a manutenção da vida no planeta Terra.
Os ecossistemas aquáticos regulam o clima, absorvem grandes quantidades de dióxido de carbono
e produzem uma parte significativa do oxigênio que respiramos.<br><br>

Além disso, os oceanos e rios são responsáveis por sustentar milhões de pessoas ao redor do mundo,
seja por meio da pesca, do turismo ou do transporte marítimo. Muitas comunidades dependem
diretamente desses ambientes para sua sobrevivência e desenvolvimento econômico.<br><br>

A biodiversidade aquática também é essencial para o equilíbrio dos ecossistemas. Cada espécie,
desde o menor organismo até os grandes predadores marinhos, possui um papel específico na
cadeia alimentar. Quando esse equilíbrio é quebrado, todo o sistema é afetado.<br><br>

Proteger a vida na água significa preservar o futuro do planeta. A conscientização,
a preservação ambiental e o uso sustentável dos recursos naturais são atitudes indispensáveis
para garantir que as próximas gerações possam continuar desfrutando da riqueza dos ecossistemas
aquáticos.
</div>
""", unsafe_allow_html=True)

# ===============================
# IMAGEM ILUSTRATIVA
# ===============================
st.image(
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b",
    caption="A vida na água sustenta o equilíbrio do planeta",
    use_container_width=True
)

# ===============================
# ANIMAÇÃO FINAL
# ===============================
st.progress(100)
st.success("🌎 Proteger a vida na água é proteger a vida na Terra!")

import streamlit as st
import time

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Preservação da Vida na Água",
    page_icon="🌱",
    layout="centered"
)

# ===============================
# ESTILOS PERSONALIZADOS
# ===============================
st.markdown("""
    <style>
    body {
        background-color: #e0f2f1;
    }
    .titulo {
        text-align: center;
        color: #004d40;
        font-size: 46px;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #00695c;
        font-size: 28px;
        margin-bottom: 30px;
    }
    .texto {
        font-size: 19px;
        color: #00332e;
        text-align: justify;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.12);
    }
    .destaque {
        color: #00796b;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# ANIMAÇÃO INICIAL
# ===============================
with st.spinner("Carregando ações sustentáveis..."):
    time.sleep(1.3)

# ===============================
# CONTEÚDO PRINCIPAL
# ===============================
st.markdown("<div class='titulo'>🌊 Como Preservar a Vida na Água</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>O que podemos fazer?</div>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
Preservar a <strong>Vida na Água</strong> é uma responsabilidade coletiva que começa com
pequenas atitudes no dia a dia. A redução do uso de plásticos descartáveis é uma das ações
mais importantes, pois grande parte desse material acaba chegando aos oceanos e rios,
prejudicando inúmeras espécies aquáticas.<br><br>

O descarte correto do lixo, o uso consciente da água e a economia de recursos naturais
contribuem diretamente para a diminuição da poluição dos ambientes aquáticos. Além disso,
apoiar iniciativas de limpeza de praias, rios e lagos ajuda a recuperar áreas degradadas.<br><br>

Outra forma essencial de preservação é o consumo responsável de peixes e frutos do mar,
evitando espécies ameaçadas e valorizando práticas de pesca sustentável. Essas escolhas
ajudam a manter o equilíbrio dos ecossistemas aquáticos.<br><br>

A <span class="destaque">educação ambiental</span> também desempenha um papel fundamental.
Informar, conscientizar e incentivar atitudes sustentáveis garante que mais pessoas
entendam a importância de proteger a vida na água, assegurando um futuro mais equilibrado
para o planeta.
</div>
""", unsafe_allow_html=True)

# ===============================
# IMAGEM ILUSTRATIVA
# ===============================
st.image(
    "https://pt.quizur.com/_image?href=https://dev-beta.quizur.com/storage/v1/object/public//imagens//20435646/a623de47-0a5b-4c29-a70d-f50d624646e3.png&w=600&h=600&f=webp",
    caption="Pequenas atitudes geram grandes mudanças",
    use_container_width=True
)

# ===============================
# ANIMAÇÃO FINAL
# ===============================
st.success("💧 Cada ação conta para preservar a vida na água!")
st.balloons()

import streamlit as st
import time

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Conclusão – Ocean Life",
    page_icon="🌍",
    layout="centered"
)

# ===============================
# ESTILOS PERSONALIZADOS
# ===============================
st.markdown("""
    <style>
    body {
        background-color: #e3f2fd;
    }
    .titulo {
        text-align: center;
        color: #012a4a;
        font-size: 46px;
        font-weight: bold;
    }
    .subtitulo {
        text-align: center;
        color: #014f86;
        font-size: 28px;
        margin-bottom: 30px;
    }
    .texto {
        font-size: 19px;
        color: #001d3d;
        text-align: justify;
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.12);
    }
    </style>
""", unsafe_allow_html=True)

# ===============================
# ANIMAÇÃO INICIAL
# ===============================
with st.spinner("Finalizando o projeto..."):
    time.sleep(1.2)

# ===============================
# CONTEÚDO DA CONCLUSÃO
# ===============================
st.markdown("<div class='titulo'>🌊 Conclusão</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>A importância de preservar a Vida na Água</div>", unsafe_allow_html=True)

st.markdown("""
<div class='texto'>
A <strong>Vida na Água</strong> é essencial para o equilíbrio ambiental e para a manutenção da
vida no planeta. Os ecossistemas aquáticos desempenham funções fundamentais, como a regulação
do clima, a produção de oxigênio e a preservação da biodiversidade.<br><br>

Ao longo do projeto <strong>Ocean Life</strong>, foi possível compreender a importância dos
oceanos, rios e lagos, bem como os impactos negativos causados pelas ações humanas, como a
poluição e o uso inadequado dos recursos naturais. Essas atitudes comprometem diretamente
a sobrevivência de inúmeras espécies aquáticas.<br><br>

Dessa forma, torna-se evidente que a preservação da vida na água depende da conscientização
e da responsabilidade de todos. Pequenas ações no dia a dia, como o descarte correto do lixo
e o consumo consciente, contribuem para a proteção dos ecossistemas aquáticos.<br><br>

Concluir este projeto reforça a ideia de que cuidar da vida na água é cuidar do futuro do
planeta, garantindo um ambiente mais equilibrado e sustentável para as próximas gerações.
</div>
""", unsafe_allow_html=True)

# ===============================
# ANIMAÇÃO FINAL
# ===============================
st.success("🌍 Proteger a vida na água é proteger a vida na Terra.")
st.balloons()

