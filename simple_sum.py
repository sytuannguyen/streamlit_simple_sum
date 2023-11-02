import streamlit as st

def main():
    st.title("Simple Sum Calculator")
    
    num1 = st.number_input("Enter the first number", min_value=0, step=1)
    num2 = st.number_input("Enter the second number", min_value=0, step=1)
    
    result = num1 + num2
    
    st.write(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
