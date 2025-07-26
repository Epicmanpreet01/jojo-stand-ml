import streamlit as st
from PIL import Image

def augment_img(img_path):
    img = Image.open(img_path)
    return img.resize((960, 540))  # half HD for better fitting

def show_eda():
    st.title("Exploratory Data Analysis (EDA): JOJO's Bizarre Adventure Stand Stats")

    st.markdown(
        """
        Welcome to the data analysis section! Here, we explore how Stand statistics relate to their ranks,
        analyze class imbalances, check for outliers, and review feature distributions. 
        This helps build a solid foundation before any modeling.
        """
    )

    # --- Class Distribution ---
    st.subheader("Class Distribution")

    col1, col2 = st.columns(2)
    with col1:
        st.image(augment_img("figures/EDA/class-dist-bar-before.png"), caption="Before Balancing (Bar Chart)")
        st.image(augment_img("figures/EDA/class-dist-pie-before.png"), caption="Before Balancing (Pie Chart)")

    with col2:
        st.image(augment_img("figures/EDA/class-dist-bar-after.png"), caption="After Balancing (Bar Chart)")
        st.image(augment_img("figures/EDA/class-dist-pie-after.png"), caption="After Balancing (Pie Chart)")

    # --- Correlation ---
    st.subheader("Feature Correlation")
    with st.expander("View Correlation Heatmap"):
        st.image(augment_img("figures/EDA/feature-correlation.png"), caption="Correlation between Stand Stats and Rank")

    # --- Outliers ---
    st.subheader("Outlier Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.image(augment_img("figures/EDA/stat-boxplot-before.png"), caption="Boxplot Before Outlier Removal")
    with col2:
        st.image(augment_img("figures/EDA/stat-boxplot-after.png"), caption="Boxplot After Outlier Removal")

    # --- Stats Distribution ---
    st.subheader("Stats Distribution")
    col1, col2 = st.columns(2)
    with col1:
        st.image(augment_img("figures/EDA/stat-dist-before.png"), caption="Distribution Before Balancing")
    with col2:
        st.image(augment_img("figures/EDA/stat-dist-after.png"), caption="Distribution After Balancing")

    st.success("EDA Complete")
