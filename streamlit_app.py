
import streamlit
import pandas
import requests


streamlit.title("My parents new healthu diner")
streamlit.header('Menú de desayuno')
streamlit.text('Omega 3 y avena con arándanos')
streamlit.text('Batido de col rizada, espinacas y rúcula')
streamlit.text('Huevo de gallinas camperas hervidas')

#lectura del fichero csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)



streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
