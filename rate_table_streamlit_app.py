import pandas as pd
import streamlit as st

from rate_calculator_for_target_apr import get_quote_for_target_apr


st.title("Rate table APR calculator")

st.write("---")

st.write("Upload a CSV file with the format:")
st.write(pd.DataFrame(
    [[3, 4], [6, 4], [2, 4], [5, 4], [4, 2]],
    columns=["apr", "fee"],
))

csv = st.file_uploader(
    label="Upload CSV file here",
    type=['csv'],
)

if csv is not None:

    st.write("---")

    st.write("Input CSV data:")
    df = pd.read_csv(csv)
    st.write(df)

    aprs = df["apr"]
    fees = df["fee"]

    rates = []
    for apr, fee in zip(aprs, fees):
        rates.append(get_quote_for_target_apr(apr, fee))

    df["rate"] = rates

    st.write("Output CSV data:")
    st.write(df)

    st.write("---")

    st.download_button("Download CSV", df.to_csv(index=False), file_name="output_csv.csv")
