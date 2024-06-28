import streamlit as st
import pandas as pd

st.title("Kişisel Bilgi Formu")

# Ad ve Soyad
name = st.text_input("Adınız ve Soyadınız (küçük harf):", max_chars=50)

# Doğum Yılı
birth_year = st.number_input("Doğum Yılınız:", min_value=1900, max_value=2023, step=1)

# E-posta Adresi
email = st.text_input("E-posta Adresiniz:", type="email")

# Özgeçmiş Dosyası
resume = st.file_uploader("Özgeçmiş Dosyanız (maks. 3 MB):", type=["pdf", "doc", "docx"])

# Cinsiyet
gender = st.selectbox("Cinsiyetiniz:", ["Erkek", "Kadın", "Diğer"])

# Hakkında
about = st.text_area("Kendiniz Hakkında (maks. 500 karakter):", max_chars=500)

if st.button("Gönder"):
    data = {
        "Ad ve Soyad": name,
        "Doğum Yılı": birth_year,
        "E-posta": email,
        "Cinsiyet": gender,
        "Hakkında": about
    }
    df = pd.DataFrame([data])
    df.to_csv("katilimformu.csv", index=False)
    st.success("Formu başarıyla gönderdiz!")
    st.write(df)