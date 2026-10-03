import streamlit as st        

st.title("LLOYD'S FIRST PYTHON PROJECT: THE TIP CALCULATOR")
st.caption("HELLO, INPUT YOUR TOTAL BILL, # OF PEOPLE, AND TIP PERCENT")

total_bill = st.number_input("Total bill")        
people = st.number_input("Number of people")        
tip_percent = st.number_input("Tip percentage")        
        
def tip_divided(tip_percent, people):    
    if tip_percent < 0 or people  == 0:    
        divided_bill = 0 
    else:    
        tip_percent_divided = tip_percent / 100     
        divided_bill = (total_bill * tip_percent_divided) / people         
    return divided_bill   
   
result = tip_divided(tip_percent, people)   
   
st.write(result)