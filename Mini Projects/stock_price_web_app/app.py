import streamlit as st
import yfinance as finance


def get_ticker(name):
    company = finance.Ticker(name)  # google
    return company


# Project Details
st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")
st.sidebar.header("100DaysOfML")

company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")
company3 = get_ticker("TSLA")

# fetches the data: Open, Close, High, Low and Volume
google = finance.download("GOOGL", start="2021-10-01", end="2021-10-01")
microsoft = finance.download("MSFT", start="2021-10-01", end="2021-10-01")
tesla = finance.download("TSLA", start="2021-10-01", end="2021-10-01")

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")
data3 = company3.history(period="3mo")

# markdown syntax
st.write("""
### Google
""")

# detailed summary on Google
st.write(company1.info['longBusinessSummary'])
st.write(google)

# plots the graph
st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'])
st.write(microsoft)
st.line_chart(data2.values)

st.write("""
### Tesla
""")
st.write(company3.info['longBusinessSummary'])
st.write(tesla)
st.line_chart(data3.values)