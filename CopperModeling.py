import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu

def predict_status(coun,item,appli,wid,prdref,quan,cust,thick,sell_p,itmdt,itmmon,itmyr,deldt,delmon,delyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmon)
    itdy= int(itmyr)

    dydd= int(deldt)
    dydm= int(delmon)
    dydy= int(delyr)
    #modelfile of the classification
    with open(r"D:\Data Science\Python\Code\Classification_model.pkl","rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[coun,item,appli,wid,prdref,quan,cust,thick,sell_p,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(coun,stat,item,appli,wid,prdref,quan,cust,thick,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open(r"D:\Data Science\Python\Code\Regression_Model.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[coun,stat,item,appli,wid,prdref,quan,cust,thick,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred



st.set_page_config(layout="wide")
st.title(" INDUSTRIAL COPPER MODELING ")
with st.sidebar:
    option=option_menu("Main Menu",options=["Selling Price Prediction","Status Prediction"])
if option=="Status Prediction":
    st.header("Status Prediction")
    st.write(" ")
    col1,col2=st.columns(2)
    with col1:
        country=st.number_input(label="**Enter the value for COUNTRY**")
        item_type=st.number_input(label="**Enter the value for ITEM TYPE**")
        application=st.number_input(label="**Enter the value for APPLICATION**")
        width=st.number_input(label="**Enter the value for WIDTH**")
        prod_ref=st.number_input(label="**Enter the value for PRODUCT REFERENCE**")
        quantity_tons_log=st.number_input(label="**Enter the value for QUANTITY TONS**",format="%0.15f")
        customer_log=st.number_input(label="**Enter the value for CUSTOMER**",format="%0.15f")
        thickness_log=st.number_input(label="**Enter the value for THICKNESS**",format="%0.15f")

    with col2:
        selling_price_log= st.number_input(label="**Enter the value for SELLING PRICE**",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))

    button= st.button(":violet[***PREDICT THE STATUS***]",use_container_width=True)

    if button:
        status= predict_status(country,item_type,application,width,prod_ref,quantity_tons_log,
                       customer_log,thickness_log,selling_price_log,item_date_day,
                       item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                       delivery_date_year)
    
        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOST**]")


            
if option == "Selling Price Prediction":

    st.header("**Selling Price Prediction**")
    st.write(" ")
    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the value for COUNTRY**")
        status= st.number_input(label="**Enter the value for STATUS**")
        item_type= st.number_input(label="**Enter the value for ITEM TYPE**")
        application= st.number_input(label="**Enter the value for APPLICATION**")
        width= st.number_input(label="**Enter the value for WIDTH**")
        product_ref= st.number_input(label="**Enter the value for PRODUCT REFERENCE**")
        quantity_tons_log= st.number_input(label="**Enter the value for QUANTITY TONS**",format="%0.15f")
        customer_log= st.number_input(label="**Enter the value for CUSTOMER**",format="%0.15f")
    

    with col2:
        thickness_log= st.number_input(label="**Enter the value for THICKNESS**",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
    

    button= st.button(":violet[***PREDICT THE SELLING PRICE***]",use_container_width=True)
    
    if button:
        price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        
        st.write("## :green[**The Selling Price is :**]",price)



        