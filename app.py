import pandas as pd
import streamlit as st
import joblib 

# loading the trained model.
model = joblib.load('modelo_ML.pkl')

# carregando uma amostra dos dados.
dataset = pd.read_csv('data_plant_growth.csv') 
#classifier = pickle.load(pickle_in)


# título
st.title("Data App - Predição de crescimento de planta")

# subtítulo
st.markdown("Este é um Data App utilizado para exibir a solução de Machine Learning para o problema de predição de crescimento de planta.")



st.sidebar.subheader("Defina os atributos da planta para predição se ela vai crescer")


# mapeando dados do usuário para cada atributo
soil_type = st.sidebar.selectbox("Tipo de solo",("loam","sandy","clay"))
sunLight_hours = st.sidebar.number_input("Horas de sol")
water_frequency = st.sidebar.selectbox("Frequencia de água", ("weekly","bi-weekly","daily"))
fertilizer = st.sidebar.selectbox("Tipo de fertilizante",("chemical","organic","none"))
temperature = st.sidebar.number_input("Temperatura")
humidity = st.sidebar.number_input("Humidade")

if soil_type == "loam":
    soil_type = 1
if soil_type == "sandy":
    soil_type = 2
if soil_type == "clay":
    soil_type = 3


if water_frequency == "bi-weekly": 
    water_frequency = 1
if water_frequency == "weekly": 
    water_frequency = 2
if water_frequency == "daily": 
    water_frequency = 3

if fertilizer == "chemical": 
    fertilizer = 1
if fertilizer == "organic": 
    fertilizer = 2
if fertilizer == "none": 
    fertilizer = 3



# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Predição")

# verifica se o botão foi acionado
if btn_predict:
    data_teste = pd.DataFrame()

    data_teste["Soil_Type"] =	[soil_type]
    data_teste["Sunlight_Hours"] =	[sunLight_hours]    
    data_teste["Water_Frequency"] = [water_frequency]
    data_teste["Fertilizer_Type"] = [fertilizer]	
    data_teste["Temperature"] = [temperature]
    data_teste["Humidity"] = [humidity]
    
    #imprime os dados de teste    
    print(data_teste)

    #realiza a predição
    result = model.predict(data_teste)

    st.write(result)

    if result == 1:
        result = "Planta vai crescer"
    else:    
        result = "Planta vai morrer"
        
    
    st.write(result)

#no prompt do anaconda, ir no diretorio da api_streamlit : C:\Users\gusta\Meu Drive\Colab Notebooks\DML\api_streamlit>

#rodar o comando: streamlit run app.py

