import streamlit as st
import pandas as pd
import joblib

# Load model dan fitur
model = joblib.load('random_forest_attrition_model.pkl')
model_features = joblib.load('model_features.pkl')

st.title("Prediksi Attrition Karyawan dari File CSV")

# Tampilkan contoh data yang valid untuk diunggah
st.markdown("### Contoh Format CSV yang Valid")

# Ambil contoh dari file asli
example_url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/employee/employee_data.csv"
example_df = pd.read_csv(example_url)

# Hapus kolom 'Attrition' agar sesuai kebutuhan user
example_df = example_df.drop(columns=['Attrition'], errors='ignore')

# Tampilkan hanya 5 baris pertama
st.dataframe(example_df.head())

uploaded_file = st.file_uploader("Upload file CSV tanpa kolom Attrition", type=['csv'])

if uploaded_file:
    try:
        # Load data
        df = pd.read_csv(uploaded_file)
        df_original = df.copy()  # Simpan salinan asli untuk ditampilkan

        # Drop kolom yang tidak dibutuhkan
        drop_cols = ['EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours', 'Attrition']
        df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

        # One-hot encoding
        df_encoded = pd.get_dummies(df, drop_first=True)

        # Sesuaikan kolom agar sama dengan saat training
        df_encoded = df_encoded.reindex(columns=model_features, fill_value=0)

        # Prediksi
        pred = model.predict(df_encoded)
        df_original['Predicted_Attrition'] = pred

        # Tampilkan hasil
        st.success("Prediksi berhasil dilakukan!")
        st.dataframe(df_original)

        # Unduh hasil
        csv = df_original.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download hasil prediksi sebagai CSV",
            data=csv,
            file_name='predicted_attrition.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
