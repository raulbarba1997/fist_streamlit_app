
import streamlit
import pandas

streamlit.title("My parents new healthu diner")
streamlit.header('Menú de desayuno')
streamlit.text('Omega 3 y avena con arándanos')
streamlit.text('Batido de col rizada, espinacas y rúcula')
streamlit.text('Huevo de gallinas camperas hervidas')

#lectura del fichero csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
