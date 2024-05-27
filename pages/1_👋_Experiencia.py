import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Experiencia", page_icon="📈")
st.markdown("# Experiência Profissional:")
st.sidebar.image('foto.jpg', caption='Profile')
col1, col2, col3, col4 = st.columns(4)
        # Profile photo section
with col1: 
            profile_pic = "https://www.modefer.com.br/uploads/banners/1680112080-g.webp"
            st.image(profile_pic, width=300
                
                     )
st.sidebar.header("")
st.markdown("""
 *  *Atua há mais de 10 anos no mercado de autopeças e agricultura em uma metalúrgica, onde adquiriu valiosa experiência em:
 *  **Impressão 3D:**
             Operação e otimização de impressoras 3D para produção de peças customizadas e prototipagem.
 *  **Corte a Laser:**
           Utilização de máquinas de corte a laser para manufatura precisa e eficiente.
 *  **Engenharia Reversa:**
             Realização de engenharia reversa de peças com o braço mecânico Romer Absolut Arm, garantindo precisão e fidelidade às peças originais.
 *  **Eletrônica:**
             Conhecimento técnico em eletrônica para desenvolvimento e reparo de equipamentos.
 *  **Softwares:**
            Proficiência em AutoCAD, modelagem digital com Siemens NX, Zbrush e Blender, demonstrando versatilidade e capacidade de trabalhar com diversas ferramentas digitais.

     **Aprende rápido:**
             Demonstra grande interesse em aprender e se manter atualizado sobre as últimas tendências tecnológicas.
 *   **Versátil:** 
            Possui experiência em diversas áreas da tecnologia, o que o torna um profissional multifacetado e capaz de se adaptar a diferentes desafios.
 *   **Proativo:**
            Busca constantemente aprimorar suas habilidades e se especializar em novas áreas, demonstrando iniciativa e proatividade.
 *   **Apaixonado por tecnologia:**
             Possui um entusiasmo contagiante por tudo que é relacionado à tecnologia, o que o motiva a buscar sempre o melhor em seu trabalho.
 *   **Objetivo:**
    *Alcançar a posição de Desenvolvedor Multiplataforma, utilizando seus conhecimentos e habilidades em tecnologia para desenvolver soluções inovadoras e impactantes.*  
""")

options = st.multiselect(
    '*Certificações que tenho por enquanto:* ',
    ['Microsoft', 'aws', 'Az-900', 'AwsCloudPratitioner'],
    ['Microsoft','aws']
)

st.markdown("""
## Habilidades e Experiências

#### Cloud e Cultura DevOps

* Entusiasta com conhecimentos práticos em diversas áreas da tecnologia, com ênfase em:
    * Infraestrutura
    * Virtualização
    * Automação
    * Metodologias DevOps

**Blockchain e Criptomoedas**

* Familiarizado com as principais tecnologias e tendências do mercado de criptoativos, buscando:
    * Aprofundar-se no tema
    * Contribuir para o desenvolvimento do setor

**Certificações**

* **AWS Cloud Practitioner:** Comprova conhecimento e habilidades em cloud computing.
* **Microcertificações do Google:** Demonstram expertise em áreas específicas da tecnologia.

**Outras Áreas de Interesse**

* Física
* Química
* Matemática
* Mercado financeiro global

**Destaques**

* Capacidade de aprendizado e adaptação a diferentes áreas do conhecimento.
* Busca constante por aprimoramento e atualização profissional.
""")

st.markdown("""
## Cursos e Conhecimentos 👀
            """)
    
col1, col2, col3, col4,col5 = st.columns(5)
        # Profile photo section

with col1: 
    st.markdown("""
* **Google**
            """)
    st.button("Google Cloud Pratitioner") 
    
with col2:
    st.markdown("""
* **Microsoft 
Azure**
            """) 
    st.button("Az900")
    st.button("Pl900")
    st.button("AI900")
    st.button("SC900")
    
    
with col3:
      st.markdown("""
* **Amazon**
            """)
      st.button("AWS Cloud Pratitioner")
      st.button("AWS Restart ")

with col4:
    st.markdown("""
* **Linguagens**
            """)
    
    st.button("Python")
    st.button("Java Script")
    st.button("Java")
with col5:
    st.markdown("""
* **Metodologias Ageis**
            """)    
    st.button("Scrum")
    st.button("Kambam")
    st.button("Ishikawa")
    
