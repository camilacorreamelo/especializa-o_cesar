import streamlit as st
import re
from PyPDF2 import PdfReader

# Título da aplicação
st.title("Buscador de Expressões em PDFs")
st.write("Faça upload de um PDF para encontrar expressões no formato 'número x número mm balão' ou 'balão número x número mm'.")

# Upload do PDF
uploaded_file = st.file_uploader("Envie o arquivo PDF", type="pdf")

if uploaded_file is not None:
    # Leitura do PDF
    st.write("Processando o PDF...")
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()
    
    # Definir a regex
    pattern = r'\b(?:\d+\s*x\s*\d+\s*mm\s*balão|balão\s*\d+\s*x\s*\d+\s*mm)\b'
    matches = re.findall(pattern, pdf_text, re.IGNORECASE)

    # Exibir os resultados
    if matches:
        st.success("Expressões encontradas:")
        for match in matches:
            st.write(f"- {match}")
    else:
        st.warning("Nenhuma expressão encontrada no formato especificado.")
