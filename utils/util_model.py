import joblib
import os
import streamlit as st

@st.cache_resource
def load_model(model):
  models = os.listdir('models/')
  model_path = os.path.join('models/',models[model])
  return joblib.load(model_path)

class_labels = ['weak','average','strong','god']

def predict_rank(model_name,stats):
  try:
    model_name_map = { 'gradientboostingclassifier': 0, 'randomforestclassfier': 1, 'supportvectormachine': 2 }
    model = load_model(model_name_map[model_name])
    rank = model.predict(stats)[0]
    return class_labels[rank], rank
  except Exception as e:
    st.error(f'Error in prediction: {e}')
    return 'Error', 0.0