import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

print(os.getcwd())
st.set_option('deprecation.showPyplotGlobalUse', False)

# Membaca file customers_dataset.csv
dataframe = pd.read_csv("Dashboard/dataframe_all.csv")

# Judul dashboard
st.title("Dashboard Submission Dicoding : Belajar Analisis Data dengan Python")

# Header pertanyaan 1
st.header("Proyek Analisis Data: E-Commerce Public Dataset")

# Subheader dan caption untuk pertanyaan 1
st.subheader("Pertanyaan 1 : Apa saja kategori produk yang paling diminati oleh customer?")
st.caption("Berdasarkan Analisis yang saya lakukan di dapat bahwa 10 kategori produk terlaris yaitu: ")

# bungkus jumlah order_id berdasarkan product_category_name_english dengan variable top_10_category_product
top_10_category_product = dataframe.groupby(by="product_category_name_english").order_id.nunique().sort_values(ascending=False).head(10)

# kemudian urutkan Secara ascending
top_10_category_product = top_10_category_product.sort_values(ascending=True)

# ambil nilai kategori produk bungkus menggunakan variable
name_category_product = top_10_category_product.index.tolist()

# Tentukan warna untuk bar plot berdasarkan nilai kategori terbesar
colors = plt.cm.viridis(top_10_category_product / float(max(top_10_category_product)))

# visualisasikan data yang di dapat ke bar diagram
plt.barh(y=name_category_product, width=top_10_category_product, color=colors)
plt.xlabel("Count of Order Product categories")
plt.ylabel("Product Category")
plt.title("Top 10 Product Categories by order product category")
plt.xlim(right=11000)

# Tampilkan visualisasi menggunakan st.pyplot()
st.pyplot()

# Subheader dan caption untuk pertanyaan 2
st.subheader("Pertanyaan 2 : dari kota mana jumlah customer terbanyak berasal?")
st.caption("Berdasarkan Analisis yang saya lakukan di dapat bahwa 10 kota asal costumers terbanyak :")

# Bungkus jumlah customer_id berdasarkan customer_city dengan vasriable top_10_customer_city
top_10_customer_city = dataframe.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).head(10)

# Kemudian urutkan secara ascending
top_10_customer_city = top_10_customer_city.sort_values(ascending=True)

# Ambil nilai nama kota dan bungkus menggunakan variable
nama_kota_terbanyak = top_10_customer_city.index.tolist()

# Tentukan warna untuk bar plot berdasarkan nilai kategori terbesar
colors = plt.cm.viridis(top_10_customer_city / float(max(top_10_customer_city)))

# Visualisasi data dengan matplotlib
plt.barh(y=nama_kota_terbanyak, width=top_10_customer_city, color=colors)
plt.ylabel("City")
plt.xlabel("Count of Customers")
plt.title("Top 10 City by Customer")

# Tampilkan visualisasi menggunakan st.pyplot()
st.pyplot()