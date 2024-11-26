# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.title("Google Play Store Analysis with Data Labels")

# Upload Dataset
uploaded_file = st.file_uploader("Upload Google Play Data", type=["csv"])

if uploaded_file:
    # Load the dataset
    data = pd.read_csv(uploaded_file)
    
    # Show dataset
    if st.checkbox("Show Dataset"):
        st.dataframe(data.head())

    # 1. Distribution of Free vs Paid Apps
    st.subheader("1. Distribution of Free vs Paid Apps")
    type_counts = data['Type'].value_counts()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=type_counts.index, y=type_counts.values, palette='viridis', ax=ax1)
    ax1.set_title('Free vs Paid Apps')
    ax1.set_xlabel('Type')
    ax1.set_ylabel('Number of Apps')
    for i, v in enumerate(type_counts.values):
        ax1.text(i, v + 100, str(v), ha='center', va='bottom')  # Add labels
    st.pyplot(fig1)

    # 2. Percentage of Apps in Top 10 Categories
    st.subheader("2. Percentage of Apps in Top 10 Categories")
    category_counts = data['Category'].value_counts()
    top_10_categories = category_counts[:10]
    total_apps = len(data)
    top_10_percentage = (top_10_categories.sum() / total_apps) * 100
    fig2, ax2 = plt.subplots()
    sns.barplot(x=top_10_categories.index, y=top_10_categories.values, palette='coolwarm', ax=ax2)
    ax2.set_title(f"Top 10 Categories ({top_10_percentage:.2f}%)")
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Number of Apps')
    for i, v in enumerate(top_10_categories.values):
        ax2.text(i, v + 100, str(v), ha='center', va='bottom')  # Add labels
    st.pyplot(fig2)

    # 3. Top 10 Most Reviewed Categories
    st.subheader("3. Top 10 Most Reviewed Categories")
    category_reviews = data.groupby('Category')['Reviews'].sum().sort_values(ascending=False)
    top_10_reviewed = category_reviews[:10]
    fig3, ax3 = plt.subplots()
    sns.barplot(x=top_10_reviewed.index, y=top_10_reviewed.values, palette='magma', ax=ax3)
    ax3.set_title('Top 10 Most Reviewed Categories')
    ax3.set_xlabel('Category')
    ax3.set_ylabel('Total Reviews')
    for i, v in enumerate(top_10_reviewed.values):
        ax3.text(i, v + 100000, str(v), ha='center', va='bottom')  # Add labels
    st.pyplot(fig3)

    # 4. Average Rating by Category
    st.subheader("4. Average Rating by Category")
    avg_rating_by_category = data.groupby('Category')['Rating'].mean().sort_values(ascending=False)
    fig4, ax4 = plt.subplots()
    sns.barplot(x=avg_rating_by_category.index, y=avg_rating_by_category.values, palette='plasma', ax=ax4)
    ax4.set_title('Average Rating by Category')
    ax4.set_xlabel('Category')
    ax4.set_ylabel('Average Rating')
    for i, v in enumerate(avg_rating_by_category.values):
        ax4.text(i, v + 0.05, f"{v:.2f}", ha='center', va='bottom')  # Add labels
    st.pyplot(fig4)

    # 5. Android Version Supporting the Highest Number of Apps
    st.subheader("5. Which Android Version Supports the Highest Number of Apps?")
    android_ver_counts = data['Android Ver'].value_counts()
    fig5, ax5 = plt.subplots()
    sns.barplot(x=android_ver_counts.index[:10], y=android_ver_counts.values[:10], palette='viridis', ax=ax5)
    ax5.set_title('Top 10 Android Versions Supporting Apps')
    ax5.set_xlabel('Android Version')
    ax5.set_ylabel('Number of Apps')
    for i, v in enumerate(android_ver_counts.values[:10]):
        ax5.text(i, v + 100, str(v), ha='center', va='bottom')  # Add labels
    st.pyplot(fig5)

else:
    st.info("Please upload the dataset to see the analysis.")

