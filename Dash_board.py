import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import ollama 
import tempfile
import base64
import os

st.set_page_config(layout="wide")
st.title("ML based analysis")
st.sidebar.header("Tool kit")

ticker = st.sidebar.text_input("Enter the name of the stock..")
start_date = st.sidebar.date_input("Enter the start date", value=pd.to_datetime("2025-05-15"))
end_date = st.sidebar.date_input("Enter the end date", value=pd.to_datetime("2025-06-04"))

if st.sidebar.button("Fetch Data"):
    st.session_state["stock_data"] = yf.download(ticker, start=start_date, end=end_date)
    st.success("Stock data loaded successfully")
    


if "stock_data" in st.session_state:
    data = st.session_state["stock_data"]
    st.write(data.columns.nlevels)
    if data.columns.nlevels >1:
        data.columns = data.columns.droplevel(1)
    
    st.write(data.columns.nlevels)
    st.write(data.head())
    
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name="Candlestick"
    )])
    st.sidebar.subheader("Technical Indicators")
    indicators = st.sidebar.multiselect("Select an indicator:", ["20 Day EMA", "20 Day Bollinger Bands"], default=["20 Day EMA"])

    def add_indicator(indicator):
        if indicator == "20 Day EMA":
            ema = data['Close'].ewm(span=20, adjust=False).mean()
            fig.add_trace(go.Scatter(x=data.index, y=ema, mode='lines', name="EMA (20)"))
        elif indicator == "20 Day Bollinger Bands":
            sma = data['Close'].rolling(window=20).mean()
            std = data['Close'].rolling(window=20).std()
            bb_upper = sma + 2 * std
            bb_lower = sma - 2 * std
            fig.add_trace(go.Scatter(x=data.index, y=bb_upper, mode='lines', name='BB Upper'))
            fig.add_trace(go.Scatter(x=data.index, y=bb_lower, mode='lines', name='BB Lower'))

    for ind in indicators:
        add_indicator(ind)

    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig)

    if st.button("Start Analysing"):
        with st.spinner("Analyzing the chart, please wait.."):
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
                fig.write_image(tmpfile.name)
                tmpfile_path = tmpfile.name
            with open(tmpfile_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')

            messages = [{
                'role': 'user',
                'content': """You are a Stock Trader specializing in Technical Analysis at a top trading firm and you analyze the stock chart's technical indicatorss and Provide a buy/hold/sell recommenditon. Base your recommmendation only on the candlestick chart and the displayed indicators and First provide the recommendation, then give you reasoning as if you are explaining it to a class of students with proper maths behind it""",
                'images': [image_data]
            }]
            response = ollama.chat(model='qwen2.5vl:3b', messages=messages)

            st.write("**AT analysis results:**")
            st.write(response["message"]["content"])

            os.remove(tmpfile_path)
