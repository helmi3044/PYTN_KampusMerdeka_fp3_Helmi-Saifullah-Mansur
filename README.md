# PYTN_KampusMerdeka_fp3_Helmi-Saifullah-Mansur

Nama : Helmi Saifullah Mansur

Kode Peserta : PYTN-KS04-010

Link Deploy : h8-fp3-ensemble.herokuapp.com

# FINAL PROJECT 3 KAMPUS MERDEKA HACKTIV8
Nama Kelompok :
- Kezario Muhammad Anaqi (PYTN-KS04-005)
- Helmi Saifullah Mansur (PYTN-KS04-010)

## 1. Overview (Perkenalan)
#### **Latar Belakang**
Penyakit kardiovaskular (CVD) merupakan salah satu penyebab kematian nomor 1 secara global, dimana mengambil sekitar 17,9 juta jiwa setiap tahun, serta menyumbang 31% dari semua kematian di seluruh dunia. Gagal jantung yaitu kejadian umum yang disebabkan oleh CVD. Pada kumpulan dataset ini berisi 12 feature yang dapat digunakan untuk memprediksi kematian akibat gagal jantung.

Sebagian besar penyakit kardiovaskular (CVD) dapat dicegah dengan mengatasi atau mengurangi faktor risiko perilaku diantaranya penggunaan tembakau, diet tidak sehat dan obesitas, kurangnya aktivitas fisik, dan penggunaan alkohol yang berbahaya menggunakan strategi di seluruh populasi.

Orang dengan penyakit kardiovaskular (CVD) atau yang berada pada risiko kardiovaskular tinggi (karena adanya satu atau lebih faktor risiko seperti hipertensi, diabetes, hiperlipidemia atau penyakit yang sudah ada) memerlukan deteksi dan manajemen dini di mana model machine learning dapat sangat membantu.

#### **Dataset**
Dataset yang digunakan pada analisis ini yaitu heart failure clinical records yang diunduh dari kaggle melalui [link berikut](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data)

Dataset ini berisikan faktor-faktor kematian oleh gagal jantung yang memiliki 13 atribut dengan 299 rows. Atribut yang menjadi target yaitu atribut Death Event/Kematian, sedangkan atribut lainnya merupakan prediktor.

#### **Objective yang Ingin Dicapai**
Objective yang ingin dicapai dalam analisis ini yaitu:

- Memahami konsep classification dengan **Ensemble Model** serta mempersiapkan data untuk digunakan dalam model **Ensemble Model**.

- Dapat mengimplementasikan **Ensemble Model** untuk membuat Prediksi keselamatan pasien dari penyakit jantung

- Mengetahui faktor-faktor yang berpengaruh signifikan dalam memPrediksi keselamatan pasien dari penyakit jantung. 

## 11. Pengambilan Kesimpulan

Dari analisis yang telah kami lakukan, diperoleh kesimpulan sebagai berikut:
- Pada Dataset terdapat 13 atribut yang diperkirakan sebagai faktor yang memprediksi keselamatan pasien dari penyakit jantung, Namun setelah dilakukan analisis kami menyimpulkan bahwa semua atribut  menjadi faktor kuat yang memprediksi keselamatan pasien dari penyakit jantung dengan atribut `Kematian` sebagai target dan atribut `Waktu`, `KreatininSerum`, `PecahanEjeksi`, `Usia`, `SodiumSerum`, `TekananDarahTinggi`, `Anaemia `, `EnzimCPK`, `Trombosit`, `Merokok`, `JenisKelamin`, dan `Diabetes` sebagai faktor yang memprediksi keselamatan pasien dari penyakit jantung
- Pada datset ini tidak terdapat adanya misssing value pada setiap atributnya
- Pada analisis ini kami juga membuat beberapa visualisasi menggunakan lineplot, boxplot, histogram, pie chart, dan matriks korelasi (heatmap) dan juga kamimelakukan beberapa contoh groupby dan query terhadap data yang ada
- Pada analisis ini variabel dependen atau target yang digunakan yaitu `Kematian` dan variabel independen yang digunakan yaitu `Waktu`, `KreatininSerum`, `PecahanEjeksi`, `Usia`, `SodiumSerum`, `TekananDarahTinggi`, `Anaemia `, `EnzimCPK`, `Trombosit`, `Merokok`, `JenisKelamin`, dan `Diabetes`
- Pada proses feature selection kami menggunakan library F regression yang memberikan score pada setiap atribut
- Pada analisis ini kami membagi data menjadi Training dan Testing dengan proporsi Training data sebesar 80% (0.80) dan Testing data sebesar 20% (0.20)
- Pada project ini kami menggunakan model ensemble method yaitu Random Forest Classifier dan Random Forest Regressor
- Untuk model Random Forest Classifier didapatkan nilai Akurasi sebesar 92% (0.916), nilai Presisi sebesar 88% (0.88), nilai Recall sebesar 83% (0.83), dan nilai F1 Score sebesar 86% (0.857)
- Untuk model Random Forest Regressor didapatkan nilai Akurasi sebesar 88% (0.88), nilai Presisi sebesar 79% (0.789), nilai Recall sebesar 83% (0.83), dan nilai F1 Score sebesar 81% (0.81)
- Hasil akurasi dengan menggunakan 2 model ensemble method diantaranya Random Forest Classifier dengan nilai akurasi 92% dan Random Forest Regressor dengan nilai akurasi 88% sama-sama baik dan bisa digunakan untuk dilakukan prediksi keselamatan pasien dari penyakit jantung.
- Pada tahap selanjutnya kami akan menggunakan kedua model tersebut dan pada hasil prediksi akan diberikan output hasil prediksi dengan 2 model tersebut

## Gambar Website
image.png
image.png
image.png