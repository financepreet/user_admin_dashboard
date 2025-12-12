import streamlit as st
import pandas as pd
import os
from datetime import datetime
from langchain_groq import ChatGroq

# 1. Initialize LLM 
llm = ChatGroq(
    model="openai/gpt-oss-120b", 
    temperature=0.3, # Thoda variety ke liye 0.3 rakha hai
    groq_api_key="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" # Security ke liye environment variables use karein
)

DATA_FILE = "feedback_data.csv"

# 2. Shared Data Source create karna
if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=["timestamp","rating","review","ai_response","ai_summary","recommended_action"])
    df_init.to_csv(DATA_FILE, index=False)


def ai_generate(prompt: str):
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating AI response: {str(e)}"

# --- Frontend UI ---
st.set_page_config(page_title="User Feedback", page_icon="📝")
st.title("⭐ Customer Review Dashboard")
st.markdown("Aapka experience hamare liye important hai. Review likhein aur AI response payein.")

# Inputs
rating = st.select_slider("Rate your experience:", options=[1, 2, 3, 4, 5], value=5)
review = st.text_area("Write your short review:", placeholder="Ex: Food was great but delivery was late.")

# Submit Logic
if st.button("Submit Feedback"):
    if not review.strip():
        st.warning("Please provide a text review before submitting.")
    else:
        # User Submission Process Diagram visualizes what happens now
        # 
        
        with st.spinner("AI analysis processing..."):
            # A. User Dashboard requirements ke hisaab se LLM generations
            user_facing_prompt = f"Act as a customer service rep. Write a very short, polite reply to this {rating}-star review: '{review}'"
            summary_prompt = f"Act as a business analyst. Summarize this review in strictly one sentence: '{review}'"
            action_prompt = f"Act as an operational manager. Suggest one specific business improvement based on this feedback: '{review}'"

            ai_response = ai_generate(user_facing_prompt)
            ai_summary = ai_generate(summary_prompt)
            recommended_action = ai_generate(action_prompt)

        # Update CSV 
        new_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "rating": rating,
            "review": review,
            "ai_response": ai_response,
            "ai_summary": ai_summary,
            "recommended_action": recommended_action
        }

        # Data write karein 
        df_new = pd.DataFrame([new_entry])
        df_new.to_csv(DATA_FILE, mode='a', header=False, index=False)

        st.success("Submission Successful!")
        
        # User dashboard requirement: Display returned AI response
        st.markdown("---")
        st.subheader("Official Response:")

        st.info(ai_response)

