import streamlit as st
from transformers import pipeline

#1. Setup model (gune cache supaya tak load banyak kali)
@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="t5-small",
        device=-1
    )

summarizer = load_summarizer()

# 2. DEsign Interface(UI)
st.title("Mentor Ai: Text Summarizer")
st.subheader("Sila masukkan artikel yang panjang, meh aku buat ringkasan atau rumusan. Bahasa Inggeris je boleh tau.")

#Kotak input
input_text = st.text_area("Paste artikel kat sini (Min 100 patah perkataan): ", height=200)

if st.button("Ringkaskan Sekarang!"):
    if input_text:
        with st.spinner('Tengah baca... jap eh...'):
            #3. Proses summarization
            # max_length = panjang, ringkasan, min_length = pendek mana kau nak
            result = summarizer(input_text, max_length=130, min_length=30, do_sample=False)

            summary = result[0]['summary_text']

            st.success("Siap cipp!")
            st.write("Hasil Ringkasan: ")
            st.info(summary)
    else:
        st.warning("Eh, letaklah dulu baru boleh buat kerja, Ish Ish Ish")
