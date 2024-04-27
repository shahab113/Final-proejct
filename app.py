import streamlit as st
import pandas as pd


st.title("RNAseq Data Analyzer")

def read_file(file):
    if file is not None:
        df = pd.read_csv(file)
        st.write(df.head(5))
    else:
        st.write("Upload a CSV file to get started.")

def descriptive_stats():
    st.write("Description of Descriptive Stats goes here")

def normalization():
    st.write("Description of Normalization goes here")

def visualization():
    st.write("Description of Visualization goes here")

def modeling():
    st.write("Description of Modeling goes here")

with st.sidebar.container():
    st.markdown(
        """
        <style>
        .sidebar-container {
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    

    file = st.file_uploader("Upload CSV file", type="csv")
    read_file(file)

st.divider()


with st.sidebar.container(height=510):
    opt = st.selectbox("Choose an option", ["", "Descriptive stats", "Normalization", "Visualization", "Modeling"])

    if opt == "Descriptive stats":
        sub_opt = st.multiselect("Choose descriptive statistics", ['Mean', 'Mode', 'Median', 'Standard Deviation'])
        
       
        if st.sidebar.button("Apply"):
            if sub_opt:
                st.write("Applying descriptive statistics:", sub_opt)
            else:
                st.write("No descriptive statistics selected")

    elif opt == "Normalization":
        sub_opt = st.multiselect("Choose Normalization type", ['L1 Normilization', 'L2 Normalization '])

    elif opt == "Visualization":
        sub_opt = st.multiselect("Choose graphs", ['Bar', 'Line Chart', 'Histogram'])

    elif opt == "Modeling":
        sub_opt = st.multiselect("Choose ML Model", ['Linear Regression', 'K-means', 'Logistic Regression'])

    else:
        st.write("No option selected")


col1, col2 = st.columns([1, 2])

with col2:
    st.write("Result goes here")

st.divider()
