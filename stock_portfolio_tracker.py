import streamlit as st
import pandas as pd
import yfinance as yf
custom_css = """
<style>
body {
    background-color: lightblue;
    color: blue;
    font-family: 'Arial', sans-serif;
}
h1 {
    color: lightblue;
}
.stButton>button {
    background-color:#4682b4;
    color: white;
    border-radius: 10px;
    border: white;
}
.stButton>button:hover {
    background-color: #5a9bd6;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# Initialize the portfolio dictionary
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}

# Function to fetch stock data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")

# Function to calculate the portfolio value
def calculate_portfolio_value():
    total_value = 0.0
    for symbol, shares in st.session_state.portfolio.items():
        stock_data = get_stock_data(symbol)
        current_price = stock_data['Close'].iloc[-1]
        total_value += current_price * shares
    return total_value

# Streamlit App Layout
st.title("Stock Portfolio Tracker")
st.image("https://gifdb.com/images/file/stock-market-graph-goes-up-animation-lpfvonkh6edeih3z.gif",width=400)
st.header("Add Stock")
symbol = st.text_input("Stock Symbol (e.g., AAPL, GOOGL)", "")
shares = st.number_input("Number of Shares", min_value=1, step=1)
if st.button("Add Stock"):
    if symbol and shares > 0:
        st.session_state.portfolio[symbol] = st.session_state.portfolio.get(symbol, 0) + shares
        st.success(f"Added {shares} shares of {symbol} to the portfolio.")

# Removing stocks
st.header("Remove Stock")
remove_symbol = st.selectbox("Select Stock to Remove", options=list(st.session_state.portfolio.keys()))
remove_shares = st.number_input("Number of Shares to Remove", min_value=1, step=1)
if st.button("Remove Stock"):
    if remove_symbol in st.session_state.portfolio:
        st.session_state.portfolio[remove_symbol] -= remove_shares
        if st.session_state.portfolio[remove_symbol] <= 0:
            del st.session_state.portfolio[remove_symbol]
        st.success(f"Removed {remove_shares} shares of {remove_symbol} from the portfolio.")

# Displaying portfolio
st.header("Current Portfolio")
if st.session_state.portfolio:
    portfolio_data = []
    for symbol, shares in st.session_state.portfolio.items():
        stock_data = get_stock_data(symbol)
        current_price = stock_data['Close'].iloc[-1]
        portfolio_data.append({
            "Symbol": symbol,
            "Shares": shares,
            "Current Price": current_price,
            "Total Value": current_price * shares
        })
    portfolio_df = pd.DataFrame(portfolio_data)
    st.write(portfolio_df)
    st.write(f"Total Portfolio Value: ${calculate_portfolio_value():,.2f}")
else:
    st.write("No stocks in the portfolio.")
st.image("https://i.makeagif.com/media/5-01-2017/s7ln3_.gif",width=200)

# End of Streamlit app
