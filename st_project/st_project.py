import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf


user_ticker = st.sidebar.text_input('Введите тикер акций компании')
user_start_date = st.sidebar.text_input('Введите начальную дату в формате год-месяц-день(Например: 2017-09-05)')
user_end_date = st.sidebar.text_input('Введите конечную дату в формате год-месяц-день')

if user_ticker == '':  # если пользователь не ввел в строку ничего
    ticker = 'AAPL'    # тикет по умолчание
else:
    ticker = user_ticker

if user_start_date == '':  # Тоже самое с начал. датой
    start_date = '2024-03-16' # начал. дата по умолчанию
else:
    start_date = user_start_date

if user_end_date == '':   # и тоже самое с конеч. датой
    end_date = '2025-09-23' # конеч. дата по умолчанию
else:
    end_date = user_end_date

st.title(f'Котировки {ticker} с {start_date} по {end_date}') # подставляем все данные
st.subheader('**1. Цена закрытия акции за торговый день**') 
ticker_data = yf.Ticker(ticker) # первый график
ticker_df = ticker_data.history(start=start_date, end=end_date)
st.line_chart(ticker_df.Close)
st.subheader('**2. Объем торгов**')  
st.line_chart(ticker_df.Volume)   # второй график
st.subheader('**3. Диапазон цены**')
st.line_chart(ticker_df[['High', 'Low']]) # третий график