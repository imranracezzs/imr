import streamlit as st
st.title("TSNPDCL")
def calculate_bill(units_consumed):
    """Calculates electricity bill based on units consumed."""

    if units_consumed <= 100:
        rate = 4.5
    elif units_consumed <= 200:
        rate = 6.0
    elif units_consumed <= 300:
        rate = 8.0
    else:
        rate = 10.0

    bill_amount = units_consumed * rate

    return bill_amount

def main():
    st.title("Electricity Bill Calculator")

    units_consumed = st.number_input("Enter units consumed:", min_value=0)

    if units_consumed:
        bill_amount = calculate_bill(units_consumed)
        st.write(f"Your electricity bill is: ₹{bill_amount:.2f}")

if __name__ == "__main__":
    main()