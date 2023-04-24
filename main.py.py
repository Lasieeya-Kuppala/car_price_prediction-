import streamlit as st
import pandas as pd
import datetime
import xgboost as xgb

def main():
    html_temp="""
    <div style= "background-color:lightblue;padding: 16px">
    <h2 style="text-align:center;">Car Price Prediction</h2>
    </div>
    """
    model =xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.write('')
    st.write('')
    st.markdown("###Are you trying to sell your car###")
    st.markdown("###Please fill the below details to predict the car price###")
    st.text_input("Please enter car name")
    l1=st.number_input("What is current ex-showroom price of the car (In Dollars)",4500,250000,step=100)
    p1=l1*82
    l2= st.number_input("What is distance completed by the car in miles ?",50,10000000,step=100)
    p2=l2/0.621
    s1= st.selectbox("What is the fual type of the car?",('Petrol','Diesel','CNG'))
    
    if s1 == "Petrol":
        p3=0
    elif s1=="Diesel":
        p3=1
    elif s1=="CNG":
        p3=2
        
    s2= st.selectbox("Select the seller type",('Dealer','Individual'))
     
    if s2 == "Dealer":
         p4=0
    elif s2=="Individual":
         p4=1
     
    s3= st.selectbox("What is the transmission type?",('Manual','Automatic'))
     
    if s3 == "Manual":
         p5=0
    elif s3=="Automatic":
         p5=1 
         
    p6= st.slider("Number of owners the car previously had?",0,3)
    
    date_time= datetime.datetime.now()
    
    years= st.number_input("In which year car was purchased?",1990,date_time.year)
    p7= date_time.year -years
    
    
    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
    
},index=[0])
    try:
        if st.button('Predict'):
            pred= model.predict(data_new)
            pred_new=(pred/82)
            if pred>0:
                st.balloons()
                st.success("Predicted price for this car is ${:.2f} ".format(pred_new[0]*10000))
            else:
                st.warning("You cannot able to sell this car")
    except:
        st.warning("something Went Wrong Please Try Again")

if __name__ =='__main__':
    main()

