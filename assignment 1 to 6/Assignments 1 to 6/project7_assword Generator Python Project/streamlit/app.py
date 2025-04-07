
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from plotly import graph_objects as go

# Function to display dataset info and perform exploratory data analysis (EDA)
def display_data(df):
    st.write(f"Number of Rows: {df.shape[0]} 📊")
    st.write(f"Number of Columns: {df.shape[1]} 🗂️")
    st.write(f"Column Names and Data Types:")
    st.write(df.dtypes)

    # Show missing data if any
    if df.isnull().sum().sum() > 0:
        st.warning('⚠️ The dataset contains missing values. Here is the count of missing values for each column:', icon="⚠️")
        st.write(df.isnull().sum().sort_values(ascending=False))
    else:
        st.success('✅ No missing values in the dataset.', icon="✅")

    # Display summary statistics
    st.subheader('Summary Statistics 📊')
    styled_summary = df.describe().style \
        .set_table_styles([{'selector': 'thead th', 'props': [('background-color', '#2D87F0'), ('color', 'white'), ('font-weight', 'bold')]},  
                           {'selector': 'tbody td', 'props': [('background-color', '#f9f9f9')]},  
                           {'selector': 'tfoot td', 'props': [('background-color', '#2D87F0'), ('color', 'white'), ('font-weight', 'bold')]}])  
    st.write(styled_summary)

    # Plot histograms for numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    if len(numeric_columns) > 0:
        st.subheader('Histogram of Numeric Columns 📈')
        for col in numeric_columns:
            st.subheader(f"Histogram for {col} 📉")
            fig, ax = plt.subplots()
            ax.hist(df[col], bins=20, edgecolor='black', alpha=0.7)
            ax.set_title(f"Distribution of {col}")
            st.pyplot(fig)

# Dataset loader with error handling
def load_dataset(dataset_name):
    try:
        df = sns.load_dataset(dataset_name)
        if df is None or df.empty:
            st.error(f"❌ Dataset '{dataset_name}' is not available or is empty.")
        return df
    except Exception as e:
        st.error(f"⚠️ Error loading dataset: {str(e)}")

# Function to upload custom CSV/Excel files
def upload_custom_dataset():
    uploaded_file = st.file_uploader('📂 Upload a custom dataset (CSV, Excel)', type=['csv', 'xlsx'])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            st.success("✅ Dataset uploaded successfully!")
            return df
        except Exception as e:
            st.error(f"⚠️ Error loading dataset: {str(e)}")
    return None

# Dynamic Correlation Heatmap creation
def create_heatmap(df):
    st.subheader('Correlation Heatmap 🔥')

    numeric_columns = df.select_dtypes(include=np.number).columns
    corr_matrix = df[numeric_columns].corr()

    heatmap_fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Cividis',
        colorbar=dict(title='Correlation'),
        zmin=-1, zmax=1,
        hoverongaps=False,
        showscale=True
    ))

    heatmap_fig.update_layout(
        title='Correlation Heatmap',
        title_x=0.5,
        xaxis_title='Features',
        yaxis_title='Features',
        template='plotly_dark'
    )

    st.plotly_chart(heatmap_fig)

# Function to create customized pairplot
def create_pairplot(df):
    st.subheader('Customized Pairplot 🔍')

    hue_column = st.selectbox('Select a column for hue in the pairplot', df.columns)
    palette = st.selectbox('Choose a color palette for the pairplot', ['Set1', 'coolwarm', 'viridis', 'cubehelix'])
    
    sns.set(style="whitegrid")
    pairplot = sns.pairplot(df, hue=hue_column, palette=palette)
    st.pyplot(pairplot)

# Function to create interactive boxplot for numeric columns
def create_boxplot(df):
    st.subheader('Boxplot for Numeric Columns 📊')

    numeric_columns = df.select_dtypes(include=[np.number]).columns
    column = st.selectbox('Select a column for boxplot', numeric_columns)
    
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=column, ax=ax)
    ax.set_title(f"Boxplot of {column}")
    st.pyplot(fig)

# Function to upload images for dataset-related content
def image_uploader():
    uploaded_image = st.file_uploader('📸 Upload an image', type=['jpg', 'jpeg', 'png'])
    if uploaded_image is not None:
        img = Image.open(uploaded_image)
        st.image(img, caption='Uploaded Image', use_column_width=True)
    else:
        st.write("No image uploaded yet. 🖼️")

# Create a dynamic dropdown to select a dataset or upload a custom one
def dataset_selector():
    # Built-in datasets
    dataset_options = ['flights', 'diamonds', 'penguins', 'titanic']
    selected_dataset = st.selectbox('Select a built-in dataset 🗃️', dataset_options)
    
    if selected_dataset:
        df = load_dataset(selected_dataset)
        
        # Display a relevant image for each dataset
        if selected_dataset == 'flights':
            st.image('https://th.bing.com/th/id/R.89bcca07e2169b9eef3a5edea6ec61f3?rik=RcFYkJvY2edg%2fg&pid=ImgRaw&r=0', caption='flights Dataset Example')
        elif selected_dataset == 'titanic':  
            st.image('https://th.bing.com/th/id/R.4493b5472b103f9d699793cd58a1c97e?rik=F1L4%2fhOjhX80QQ&riu=http%3a%2f%2fpngimg.com%2fuploads%2ftitanic%2ftitanic_PNG33.png&ehk=oFdhXKu6Jewk8E1c4p1Cv1h2dRSUcku7GEcUaYHg2B8%3d&risl=&pid=ImgRaw&r=0', caption='Titanic Dataset Example')
        elif selected_dataset == 'diamonds':
            st.image('https://www.jewelryshoppingguide.com/wp-content/uploads/2019/03/list-of-diamond-shapes.jpeg', caption='Diamonds Dataset Example')
        elif selected_dataset == 'penguins':
            st.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/c0b38a3a-ac58-42a6-95c9-9ebc7541a4fc/ddh9poh-1ba73f9a-2ba0-4ff7-bf22-f832576bc582.png/v1/fill/w_1015,h_787,strp/pinguinos_01_3_colores_degradados_by_creaciones_jean_ddh9poh-pre.png', caption='Penguins Dataset Example')
        
        return df

    # Upload custom dataset if built-in selection is not chosen
    return upload_custom_dataset()

# Main Streamlit application setup
def main():
    # Display title and description
    st.title('Advanced Data Analytics Platform 📊')
    st.subheader('An advanced data analysis tool to explore datasets interactively. 🌐')
    st.write("Created by [sobiarao] 👨‍💻")
 
    # Add image uploader section for custom images
    image_uploader()

    # Select or upload a dataset
    df = dataset_selector()

    if df is not None:
        # Display dataset and allow users to interact with visualizations
        if df is not None:
            display_data(df)
            create_pairplot(df)
            create_heatmap(df)
            create_boxplot(df)

        # Feedback Section
        handle_feedback()

        # Ask Questions
        question_box()

# Feedback Section
def handle_feedback():
    st.subheader('Provide Feedback 💬')
    feedback = st.text_area('Please share your feedback or suggestions here:', '', height=200)
    if st.button('Submit Feedback'):
        if feedback:
            st.write("Thank you for your feedback! 🙏")
        else:
            st.write("Please enter your feedback before submitting. 📝")

# Question Section
def question_box():
    st.subheader('Ask a Question ❓')
    user_question = st.text_area('Please type your question here:', '', height=150)
    if st.button('Submit Question'):
        if user_question:
            st.write("Your question has been submitted! We will get back to you shortly. 📨")
        else:
            st.write("Please enter a question before submitting. ❗")

# Run the main function to execute the app
if __name__ == '__main__':
    main()
