import streamlit as st
import yfinance as yf
import pandas-ta as ta
import pandas as pd

# Konfigurasi tampilan web
st.set_page_config(page_title="Alpha Private Screener", layout="centered")
st.title("📊 Alpha Private Screener")

# Input kode saham
ticker_input = st.text_input("Masukkan Kode Saham (contoh: BBCA.JK)", "BBCA.JK")

if st.button("Analisa"):
    # Mengambil data dari Yahoo Finance
    df = yf.download(ticker_input, period="6mo", interval="1d")
    
    if not df.empty:
        # Menghitung indikator teknikal
        last_close = df['Close'].iloc[-1]
        ma5 = ta.sma(df['Close'], length=5).iloc[-1]
        
        # Menampilkan data ringkas
        st.subheader(f"Data Saham: {ticker_input}")
        st.metric("Harga Terakhir", f"Rp {last_close:.0f}")
        
        # Menampilkan Trading Plan
        st.subheader("💡 Rencana Trading (Swing)")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Entry Price", f"Rp {last_close:.0f}")
            st.metric("Stop Loss", f"Rp {last_close * 0.97:.0f}")
        with col2:
            st.metric("Target Profit 1", f"Rp {last_close * 1.05:.0f}")
            st.metric("Target Profit 2", f"Rp {last_close * 1.08:.0f}")
            
        # Menampilkan grafik
        st.line_chart(df['Close'])
        
    else:
        st.error("Data tidak ditemukan. Pastikan kode saham menggunakan akhiran .JK")
