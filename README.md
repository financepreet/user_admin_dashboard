📄 Section 2: Task 2 - Two-Dashboard AI Feedback System
2.1 System Architecture
The application was designed as an integrated data pipeline where user input triggers an LLM "Analyst" to generate metadata, which is then persisted for administrative review.

Tech Stack: Streamlit (UI), Pandas (CSV storage), Groq/Gemini (LLM).

Data Persistence: A shared feedback_data.csv serves as the single source of truth, enabling live synchronization between the dashboards.

2.2 System Behavior & Logic
The system behavior is split across two distinct functional requirements:

A. User Dashboard (Customer Interaction)

Behavior: On submission, the system triggers three separate LLM reasoning tasks.

Response Logic: Uses a "Customer Service" persona to generate a polite reply, ensuring the user feels acknowledged immediately.

B. Admin Dashboard (Business Oversight)

Behavior: Loads data directly from the CSV and calculates real-time metrics (Average Rating, Total Submissions).

Logic: Presents the ai_summary and recommended_action in a sortable table, allowing managers to identify operational bottlenecks (e.g., repeated negative feedback regarding "slow delivery") instantly.

2.3 Deployment
Both dashboards were deployed as a single multi-page app via Streamlit Community Cloud, using GitHub as the CI/CD pipeline. Secrets Management (Streamlit Cloud Secrets) was used to store the Groq API key securely, satisfying security requirements.
