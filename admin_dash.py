import streamlit as st
import pandas as pd
import os

# --- Configuration ---
DATA_FILE = "feedback_data.csv" # Ensure this matches your User Dashboard file name

st.set_page_config(page_title="Feedback Analytics", layout="wide")
st.title("🛠️ Admin Dashboard – Feedback Overview")

# Load Data
if not os.path.exists(DATA_FILE):
    st.warning("⚠️ No feedback submitted yet! The 'data.csv' file has not been created.")
else:
    
    df = pd.read_csv(DATA_FILE)

    if df.empty:
        st.info("ℹ️ The log is currently empty.")
    else:
        
        st.subheader("📄 Recent Feedback Submissions")
        # Displaying the required columns: user Rating, Review, AI Summary, Recommended Actions
        st.dataframe(
            df[["timestamp", "rating", "review", "ai_summary", "recommended_action"]], 
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        # 2. ANALYTICS SECTION
        st.subheader("📊 Performance Analytics")

        col1, col2, col3 = st.columns(3)

        with col1:
            avg_rating = df["rating"].mean()
            st.metric("Average Star Rating", f"{round(avg_rating, 2)} ⭐️")

        with col2:
            total_feedback = len(df)
            st.metric("Total Submissions", total_feedback)
        
        with col3:
            # Simple health check: % of reviews that are 4 or 5 stars
            positive_reviews = len(df[df["rating"] >= 4])
            positive_pct = (positive_reviews / total_feedback) * 100
            st.metric("Customer Satisfaction", f"{round(positive_pct, 1)}%")

        st.markdown("---")

        # 3. VISUALIZATION
        st.subheader("📈 Rating Distribution")
        # Creating a proper count for the bar chart
        rating_counts = df["rating"].value_counts().sort_index()
        st.bar_chart(rating_counts)
