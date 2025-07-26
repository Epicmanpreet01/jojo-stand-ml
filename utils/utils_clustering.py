import streamlit as st
from PIL import Image
import pandas as pd

def augment_img(img_path):
    img = Image.open(img_path)
    return img.resize((960, 540))

def show_clustering():
    st.title("Rank Clustering Analysis")

    st.markdown(
        """
        This section explores how JOJO Stands are ranked using **unsupervised clustering**. 
        We used **KMeans** to identify natural groupings in Stand statistics (like Power, Speed, etc.)
        and mapped those to four custom-defined ranks.
        """
    )

    # --- Step 1: Data Preprocessing ---
    with st.expander("Step 1: Data Cleaning & Encoding"):
        st.markdown("""
        - Null values in the stats were replaced with `"F"` (considered lowest rank).
        - Each letter grade was mapped to a numeric value using:
            - A=10, B=8, C=6, D=4, E=2, F=0, Infi=20
        """)

    # --- Step 2: Normalization ---
    with st.expander("Step 2: Feature Scaling"):
        st.markdown("""
        - All numeric features were normalized using **StandardScaler** to ensure uniformity before clustering.
        """)

    # --- Step 3: KMeans Clustering ---
    with st.expander("Step 3: KMeans Clustering"):
        st.markdown("""
        - We used **KMeans with 4 clusters**.
        - The resulting cluster labels were mapped to ranks using a custom mapping:
          `Cluster {3→0, 1→1, 0→2, 2→3}` to create a meaningful rank order.
        """)

    # --- Step 4: PCA Visualization ---
    st.subheader("PCA Visualization of Clusters")
    st.image(augment_img("figures/clustering/clustering.png"), caption="PCA projection of Stands by Cluster (Rank)")

    # --- Step 5: Cluster Center Analysis ---
    st.subheader("Cluster Centroids (Decoded Back to Stats)")
    st.markdown("Each rank’s average stat profile is shown below:")

    # Show cluster centers (if you exported them as CSV)
    try:
        centroid_df = pd.read_csv("data/centroids.csv")
        st.dataframe(centroid_df.set_index("Rank"))
    except Exception as e:
        st.warning("Could not load centroid data. Make sure 'centroids.csv' exists.")

    # --- Step 6: Rank Distribution ---
    st.subheader("Rank Distribution")
    st.image(augment_img("figures/EDA/class-dist-pie-before.png"), caption="Stand Count per Clustered Rank")

    st.success("Clustering analysis completed successfully")
