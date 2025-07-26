import streamlit as st
from streamlit_option_menu import option_menu
import joblib
from utils.util_eda import show_eda
from utils.utils_clustering import show_clustering

st.set_page_config(page_title='JOJO Stand Poer Classifier',layout="wide")

with st.sidebar:
  option = option_menu(
    menu_title='Pages', 
    icons=["graph-up-arrow", "bar-chart-line", "diagram-3"],
    options=['Prediction', 'Data Analysis', 'Rank Clustering'],
    default_index=0
  )

if option.lower() == 'prediction':
  st.title('JOJO Stand Power Classifier')
  st.subheader("A machine model capable of guessing a stand's rank from it's stats")
  st.divider()

  st.write('Enter stand stats for analysis')
  st.text_input(label='Enter PWR', placeholder='PWR..')
  st.text_input(label='Enter SPD', placeholder='SPD..')
  st.text_input(label='Enter RNG', placeholder='RNG..')
  st.text_input(label='Enter DEV', placeholder='DEV..')
  st.text_input(label='Enter PER', placeholder='PER..')
  st.text_input(label='Enter PRC', placeholder='PRC..')
elif option.lower() == 'data analysis':
  show_eda()
else:
  show_clustering()