# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh negeri. Sebagai perusahaan yang berkembang pesat, Jaya Jaya Maju menghadapi tantangan dalam **pengelolaan karyawan**, yang berdampak langsung pada **attrition rate** yang tinggi, yaitu lebih dari **10%**.  

Untuk mengatasi masalah ini, manajer departemen HR ingin memahami **faktor-faktor utama yang mempengaruhi attrition** agar perusahaan dapat mengambil langkah-langkah strategis untuk meningkatkan **retensi karyawan** dan mengurangi turnover.  

### Permasalahan Bisnis

Terdapat beberapa permasalahan utama yang ingin diselesaikan melalui proyek ini:  
- **Tingginya attrition rate** (lebih dari 10%), yang dapat berdampak pada efektivitas operasional perusahaan.  
- **Kurangnya pemahaman tentang faktor-faktor penyebab attrition**, sehingga sulit bagi manajemen untuk mengambil tindakan yang tepat.  
- **Minimnya sistem pemantauan faktor-faktor karyawan**, menyebabkan keputusan yang kurang berbasis data dalam strategi retensi.  

### Cakupan Proyek

Dalam proyek ini, beberapa cakupan utama meliputi:  
- **Analisis faktor-faktor yang mempengaruhi attrition rate**, menggunakan pendekatan data-driven dengan model prediktif seperti **RandomForestClassifier**.  
- **Pembuatan business dashboard** untuk memberikan wawasan tentang aspek-aspek yang berdampak pada attrition rate dan memudahkan pemantauan tren attrition.  
- **Menyusun rekomendasi strategis** bagi perusahaan berdasarkan analisis data, seperti peningkatan work-life balance, optimasi paket kompensasi, dan strategi retensi karyawan yang lebih efektif.  
- **Pengembangan aplikasi Streamlit sederhana** yang memungkinkan perusahaan melakukan **prediksi berbasis file CSV tanpa label**, sehingga dapat digunakan untuk mengidentifikasi tren attrition secara lebih fleksibel tanpa perlu data historis yang lengkap.  

### Persiapan

Sumber data: ....

Setup environment:

Jika Anda menggunakan **Laragon** (Windows) sebagai local web development suite, maka berikut adalah langkah-langkah menjalankan aplikasi Streamlit:

1. **Buka Terminal di Laragon** → `Menu > Terminal`

2. **Aktifkan Virtual Environment (opsional, jika dibuat):**

   ```bash
   venv\Scripts\activate
   ```

3. **Install dependensi dari `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit:**

   ```bash
   streamlit run app.py
   ```

5. **Akses aplikasi di browser:**
   Biasanya tersedia di `http://localhost:8501`

## Business Dashboard

Dashboard bisnis ini dirancang untuk memberikan analisis mendalam mengenai tingkat attrition atau perputaran karyawan dalam perusahaan. Dengan visualisasi yang jelas dan informatif, dashboard ini membantu manajemen dalam mengidentifikasi pola, faktor penyebab, dan strategi yang dapat diterapkan untuk meningkatkan retensi karyawan.

### **Fitur Utama:**
- **Ringkasan Attrition**: Menampilkan total jumlah karyawan, jumlah yang mengalami attrition, dan persentase turnover.
- **Analisis Demografis**: Mengevaluasi attrition berdasarkan usia, masa kerja, dan bidang pendidikan karyawan.
- **Distribusi Berdasarkan Departemen & Peran**: Memetakan tingkat attrition di berbagai departemen dan posisi pekerjaan untuk mengidentifikasi area dengan tingkat keluar tinggi.
- **Faktor-Faktor Pendukung**: Menyelidiki hubungan antara penghasilan, overtime, dan kepuasan kerja dengan tingkat attrition.
- **Kepuasan Hubungan Interpersonal**: Menggambarkan bagaimana tingkat kepuasan sosial berpengaruh terhadap retensi karyawan.

Dashboard ini memberikan wawasan mengenai attrition karyawan dan faktor-faktor yang mempengaruhinya.  
Akses langsung: [Klik di sini]([https://contoh-dashboard.com](https://public.tableau.com/views/SubmissionPertamaMenyelesaikanPermasalahanHumanResources/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link))

## Conclusion

Berdasarkan hasil **feature importance** dari model **RandomForestClassifier(random_state=42)**, dapat disimpulkan bahwa **faktor finansial dan keseimbangan kerja** memiliki peran penting dalam memprediksi attrition karyawan.  
- **MonthlyIncome, MonthlyRate, dan DailyRate** menjadi fitur dengan pengaruh terbesar, menunjukkan bahwa **aspek kompensasi** sangat berpengaruh dalam keputusan karyawan untuk tetap bertahan atau meninggalkan perusahaan.  
- **OverTime_Yes dan DistanceFromHome** juga memiliki kontribusi besar, mengindikasikan bahwa **beban kerja dan jarak tempuh** berpengaruh terhadap kepuasan kerja dan retensi karyawan.  
- **TotalWorkingYears, YearsAtCompany, dan YearsWithCurrManager** menguatkan bahwa **lama bekerja dan pengalaman** dalam perusahaan juga menjadi faktor yang perlu diperhatikan.  

Kesimpulannya, strategi retensi karyawan perlu mempertimbangkan aspek **keuangan, keseimbangan kerja, serta faktor pengalaman dan stabilitas** dalam pekerjaan.

### Rekomendasi Action Items (Optional)

Untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan, berikut beberapa langkah yang dapat diambil perusahaan:

**Action Item 1 – Optimalisasi Paket Kompensasi**  
- Lakukan **review terhadap sistem penggajian**, terutama untuk peran yang memiliki tingkat attrition tinggi.  
- **Sesuaikan gaji berdasarkan pengalaman kerja**, tidak hanya berdasarkan standar industri, tetapi juga mempertimbangkan perbedaan internal.  
- Pertimbangkan **insentif berbasis performa** untuk meningkatkan kepuasan dan loyalitas karyawan.  

**Action Item 2 – Peningkatan Work-Life Balance dan Fleksibilitas Kerja**  
- **Evaluasi kebijakan lembur** dan pastikan bahwa kompensasi lembur sesuai dengan beban kerja.  
- Perkenalkan **fleksibilitas jam kerja atau opsi kerja hybrid** untuk mengurangi beban karyawan.  
- Jika memungkinkan, **optimalkan penempatan lokasi kerja** bagi karyawan yang memiliki perjalanan jauh, atau berikan fasilitas transportasi yang lebih mendukung.  

Langkah-langkah ini akan membantu perusahaan dalam **mengurangi turnover, meningkatkan kepuasan kerja, dan mempertahankan karyawan berbakat** dalam jangka panjang!
