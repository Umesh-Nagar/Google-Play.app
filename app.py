{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37d548f8-e1a6-481a-9751-1e3f81560f52",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-26 11:22:31.301 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\91911\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 13\u001b[0m\n\u001b[0;32m     11\u001b[0m uploaded_file \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mfile_uploader(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgoogle_play_data\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28mtype\u001b[39m\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcsv\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[0;32m     12\u001b[0m \u001b[38;5;66;03m# Drop rows with nulls or replace them\u001b[39;00m\n\u001b[1;32m---> 13\u001b[0m data \u001b[38;5;241m=\u001b[39m data\u001b[38;5;241m.\u001b[39mdropna(subset\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRating\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mReviews\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mCategory\u001b[39m\u001b[38;5;124m'\u001b[39m])  \u001b[38;5;66;03m# Drop rows where critical columns are null\u001b[39;00m\n\u001b[0;32m     16\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m uploaded_file:\n\u001b[0;32m     17\u001b[0m     \u001b[38;5;66;03m# Load the dataset\u001b[39;00m\n\u001b[0;32m     18\u001b[0m     data \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(uploaded_file)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "# app.py\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# App Title\n",
    "st.title(\"Google Play Store Analysis\")\n",
    "\n",
    "# Upload Dataset\n",
    "uploaded_file = st.file_uploader(\"google_play_data\", type=[\"csv\"])\n",
    "\n",
    "\n",
    "if uploaded_file:\n",
    "    # Load the dataset\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "    \n",
    "\n",
    "    # Show dataset\n",
    "    if st.checkbox(\"Show Dataset\"):\n",
    "        st.dataframe(data.head())\n",
    "\n",
    "    # 1. Distribution of Free vs Paid Apps\n",
    "    st.subheader(\"1. Distribution of Free vs Paid Apps\")\n",
    "    type_counts = data['Type'].value_counts()\n",
    "    fig1, ax1 = plt.subplots()\n",
    "    sns.barplot(x=type_counts.index, y=type_counts.values, palette='viridis', ax=ax1)\n",
    "    ax1.set_title('Free vs Paid Apps')\n",
    "    ax1.set_xlabel('Type')\n",
    "    ax1.set_ylabel('Number of Apps')\n",
    "    st.pyplot(fig1)\n",
    "\n",
    "    # 2. Percentage of Apps in Top 10 Categories\n",
    "    st.subheader(\"2. Percentage of Apps in Top 10 Categories\")\n",
    "    category_counts = data['Category'].value_counts()\n",
    "    top_10_categories = category_counts[:10]\n",
    "    total_apps = len(data)\n",
    "    top_10_percentage = (top_10_categories.sum() / total_apps) * 100\n",
    "    fig2, ax2 = plt.subplots()\n",
    "    top_10_categories.plot(kind='bar', color='skyblue', ax=ax2)\n",
    "    ax2.set_title(f\"Top 10 Categories ({top_10_percentage:.2f}%)\")\n",
    "    ax2.set_xlabel('Category')\n",
    "    ax2.set_ylabel('Number of Apps')\n",
    "    st.pyplot(fig2)\n",
    "\n",
    "    # 3. Top 10 Most Reviewed Categories\n",
    "    st.subheader(\"3. Top 10 Most Reviewed Categories\")\n",
    "    category_reviews = data.groupby('Category')['Reviews'].sum().sort_values(ascending=False)\n",
    "    top_10_reviewed = category_reviews[:10]\n",
    "    fig3, ax3 = plt.subplots()\n",
    "    top_10_reviewed.plot(kind='bar', color='coral', ax=ax3)\n",
    "    ax3.set_title('Top 10 Most Reviewed Categories')\n",
    "    ax3.set_xlabel('Category')\n",
    "    ax3.set_ylabel('Total Reviews')\n",
    "    st.pyplot(fig3)\n",
    "\n",
    "    # 4. Average Rating by Category\n",
    "    st.subheader(\"4. Average Rating by Category\")\n",
    "    avg_rating_by_category = data.groupby('Category')['Rating'].mean().sort_values(ascending=False)\n",
    "    fig4, ax4 = plt.subplots()\n",
    "    avg_rating_by_category.plot(kind='bar', color='purple', ax=ax4)\n",
    "    ax4.set_title('Average Rating by Category')\n",
    "    ax4.set_xlabel('Category')\n",
    "    ax4.set_ylabel('Average Rating')\n",
    "    st.pyplot(fig4)\n",
    "\n",
    "    # 5. Android Version Supporting the Highest Number of Apps\n",
    "    st.subheader(\"5. Which Android Version Supports the Highest Number of Apps?\")\n",
    "    android_ver_counts = data['Android Ver'].value_counts()\n",
    "    fig5, ax5 = plt.subplots()\n",
    "    android_ver_counts[:10].plot(kind='bar', color='green', ax=ax5)\n",
    "    ax5.set_title('Top 10 Android Versions Supporting Apps')\n",
    "    ax5.set_xlabel('Android Version')\n",
    "    ax5.set_ylabel('Number of Apps')\n",
    "    st.pyplot(fig5)\n",
    "\n",
    "else:\n",
    "    st.info(\"Please upload the dataset to see the analysis.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "66a5d177-6db9-4b04-8406-c8dc76578658",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
