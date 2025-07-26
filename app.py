import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from utils.util_eda import show_eda
from utils.utils_clustering import show_clustering
from utils.util_model import predict_rank


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

  model = st.selectbox(
    label='Select a Machine Learning Model',
    options=['Gradient Boosting Classifier', 'Random Forest Classifier', 'Support Vector Machine'],
  )

  st.write(f'Selcted model: {model}')
  st.divider()
  st.write('Enter stand stats for analysis')
  stat_options = ['Infi','A','B','C','D','E','F']
  pwr = st.selectbox(label='Power: ', options=stat_options)
  spd = st.selectbox(label='Speed: ', options=stat_options)
  rng = st.selectbox(label='Range: ', options=stat_options)
  dev = st.selectbox(label='Development Potential: ', options=stat_options)
  per = st.selectbox(label='Power Pesistance: ', options=stat_options)
  prc = st.selectbox(label='Precision', options=stat_options)

  if st.button('Predict Rank'):
    stats = pd.DataFrame({
      'PWR': [pwr],
      'SPD': [spd],
      'RNG': [rng],
      'PER': [per],
      'PRC': [prc],
      'DEV': [dev]
    })

    encoded_map = { 'F':0, 'E':2 , 'D':4, 'C':6, 'B':8, 'A':10, 'Infi':20 }
    encoded_stats = stats.applymap(lambda x: encoded_map[x])

    class_label, rank = predict_rank(model.replace(' ', '').lower(), encoded_stats)

    if rank == 0:
      st.error(f"Stand stats suggest weak abilities and capabilities. Rank: {class_label}")
    elif rank == 1:
      st.warning(f"Stand stats suggest average abilities and capabilities. Rank: {class_label}")
    elif rank == 2:
      st.success(f"Stand stats suggest strong abilities and capabilities. Rank: {class_label}")
    else:
      st.success(f"Stand stats suggest godly abilities and capabilities. Rank: {class_label}")

elif option.lower() == 'data analysis':
  show_eda()
else:
  show_clustering()