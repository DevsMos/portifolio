import streamlit as st
st.set_page_config(page_title="Educação", page_icon="⚡")
st.markdown("# 1° Exemplo de codigo Temperatura ")
st.markdown("## Digite um valor entre 0 e 20 ")
st.sidebar.header("Profissional")

temp = st.number_input("Enter your temperature ")
col1 = st.write(f"Hello, the temperature now is , {temp}°C !")

if temp <= 4.99:

    st.write("gelo")

elif temp <= 12 :

        st.write ("ameno")

elif temp <=27:

    st.write("quente")

else :

    st.write ("hot")

    st.write(temp)
#****************************************************************************************************************************

