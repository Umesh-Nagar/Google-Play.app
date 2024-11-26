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
    
    # Add data labels
    for i, v in enumerate(top_10_categories.values):
        ax2.text(i, v + 100, str(v), ha='center', va='bottom')
    
    # Rotate x-axis labels for better readability
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    
    # Adjust layout for a neat display
    plt.tight_layout()
    
    # Render the plot in Streamlit
    st.pyplot(fig2)
    
       # 3. Top 10 Most Reviewed Categories
    st.subheader("3. Top 10 Most Reviewed Categories")
    category_reviews = data.groupby('Category')['Reviews'].sum().sort_values(ascending=False)
    top_10_reviewed = category_reviews[:10]
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_10_reviewed.index, y=top_10_reviewed.values, palette='magma', ax=ax3)
    
    # Set title and axis labels
    ax3.set_title('Top 10 Most Reviewed Categories', fontsize=16)
    ax3.set_xlabel('Category', fontsize=12)
    ax3.set_ylabel('Total Reviews', fontsize=12)
    
    # Add data labels on bars with formatting
    for i, v in enumerate(top_10_reviewed.values):
        ax3.text(i, v + v * 0.02, f"{v:,}", ha='center', va='bottom', fontsize=10)
    
    # Rotate x-axis labels and adjust alignment
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right', fontsize=10)
    
    # Adjust layout for a clean look
    plt.tight_layout()
    
    # Render the plot in Streamlit
    st.pyplot(fig3)
    
       # 4. Average Rating by Category
    st.subheader("4. Average Rating by Category")
    avg_rating_by_category = data.groupby('Category')['Rating'].mean().sort_values(ascending=False)
    
    # Create figure
    fig4, ax4 = plt.subplots(figsize=(10, 10))
    sns.barplot(x=avg_rating_by_category.index, y=avg_rating_by_category.values, palette='plasma', ax=ax4)
    
    # Set titles and labels
    ax4.set_title('Average Rating by Category', fontsize=16)
    ax4.set_xlabel('Category', fontsize=12)
    ax4.set_ylabel('Average Rating', fontsize=12)
    
    # Add data labels with formatting
    for i, v in enumerate(avg_rating_by_category.values):
        ax4.text(i, v + 0.02, f"{v:.2f}", ha='center', va='bottom', fontsize=10)
    
    # Rotate x-axis labels for readability
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right', fontsize=10)
    
    # Adjust layout
    plt.tight_layout()
    
    # Render the plot in Streamlit
    st.pyplot(fig4)
    
        # 5. Android Version Supporting the Highest Number of Apps
    st.subheader("5. Which Android Version Supports the Highest Number of Apps?")
    android_ver_counts = data['Android Ver'].value_counts()
    
    # Create figure with adjusted size
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    
    # Create bar plot
    sns.barplot(x=android_ver_counts.index[:10], y=android_ver_counts.values[:10], palette='viridis', ax=ax5)
    
    # Set titles and labels
    ax5.set_title('Top 10 Android Versions Supporting Apps', fontsize=16)
    ax5.set_xlabel('Android Version', fontsize=12)
    ax5.set_ylabel('Number of Apps', fontsize=12)
    
    # Add data labels
    for i, v in enumerate(android_ver_counts.values[:10]):
        ax5.text(i, v + 50, f"{v}", ha='center', va='bottom', fontsize=10)
    
    # Rotate x-axis labels for readability
    ax5.set_xticklabels(ax5.get_xticklabels(), rotation=45, ha='right', fontsize=10)
    
    # Optimize layout
    plt.tight_layout()
    
    # Render the plot in Streamlit
    st.pyplot(fig5)

else:
    st.info("Please upload the dataset to see the analysis.")

