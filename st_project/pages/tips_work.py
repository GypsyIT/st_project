import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import io


@st.cache_data  
def load_data(url):
    df = pd.read_csv(url)
    return df



file_csv = st.file_uploader('**Загрузи tips.csv**', type='csv')
df = load_data(file_csv)

st.button("Rerun")
if file_csv is None:
    st.write('Жду файл! :)')
else:
    df_original = pd.read_csv(file_csv)
    df = df_original.copy()
    st.title('Исследование по tips')
    st.write('DataFrame')
    start = pd.to_datetime('2023-01-01')
    stop = pd.to_datetime('2023-01-31')
    random = pd.to_datetime(np.random.randint(start.value, stop.value, size=len(df)))
    df['time_order'] = random.date
    df

    st.subheader('Проведенные ислледования')
    analitics = st.selectbox('**Исследование**', 
                            ['Динамика чаевых во времени', 
                                                'Связь между total_bill и tip', 
                                                'box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)', 
                                                'Графики для мужчин и женщин, показавующие связь размера счета и чаевых, дополнительно разбив по курящим/некурящим'])

    if analitics == 'Динамика чаевых во времени':
        df4 = df.groupby('time', as_index=False).agg({
        'total_bill': 'sum'})
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=df4, x='time', y='total_bill', color='orange', edgecolor='black')
        ax.set_title('Чаевые')
        save = st.pyplot(fig)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.download_button(
        label="Скачать график",
        data=buffer,
        file_name="график.png",
        mime="image/png")
    elif analitics == 'Связь между total_bill и tip':
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=df, x='total_bill', y='tip')
        save = st.pyplot(fig)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.download_button(
        label="Скачать график",
        data=buffer,
        file_name="график.png",
        mime="image/png")
    elif analitics == 'box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)':
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x='total_bill', y='day', hue='time')
        save = st.pyplot(fig)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.download_button(
        label="Скачать график",
        data=buffer,
        file_name="график.png",
        mime="image/png")
    elif analitics == 'Графики для мужчин и женщин, показавующие связь размера счета и чаевых, дополнительно разбив по курящим/некурящим':
        man = df[df['sex'] == 'Male'].iloc[:, 0:5]
        woman = df[df['sex'] == 'Female'].iloc[:, 0:5]
        st.write("График для мужчин") # не понимаю почему не скачивает разные графики
        save_man = st.scatter_chart(
            man,
            x='total_bill',
            y='tip',
            size=None,
            color='smoker',
            use_container_width=True)
        
        st.write("График для женщин")
        save_woman = st.scatter_chart(
            woman,
            x='total_bill',
            y='tip',
            size=None,
            color='smoker',
            use_container_width=True)
        