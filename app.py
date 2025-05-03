import streamlit as st
import json
import pandas as pd
from utils import load_session_data
from utils import build_prompt, analyze_user_experience, generate_recommendation
from model import generate_insight
from session_analysis import analyze_sessions


def display_page():
    st.set_page_config(page_title="Project E-Commerce Journey Analyzer", layout="wide")
    st.title("🛒 Vijay - E-Commerce Journey Analyzer")

    uploaded_file = st.file_uploader("Upload session data (JSON)", type="json")

    if uploaded_file:
        sessions = json.load(uploaded_file)
    else:
        sessions = load_session_data("data.json")

    # @st.cache_data
    # def load_session_data(file_path="data.json"):
    #     with open(file_path, "r") as f:
    #         return json.load(f)

    # sessions = load_session_data("data.json")
    # session_summaries = analyze_sessions(sessions)

    # Display each session
    session_summaries = []
    for session in sessions:
        st.markdown(f"---\n### Session ID: `{session['session_id']}`")
        with st.spinner("Analyzing with T5..."):
            prompt = build_prompt(session)
            insight = generate_insight(prompt)
            user_experience = analyze_user_experience(session)
            recommendation = generate_recommendation(session)

        st.markdown(f"**Session ID**: {session['session_id']}")
        st.markdown(f"**Device**: {session['device_type']}")
        st.markdown(f"**Country**: {session['user_attributes']['country']}")
        st.markdown(f"**Referrer**: {session['user_attributes']['referrer']}")
        st.markdown(f"**New User**: {session['user_attributes']['new_user']}")
        st.markdown(f"**Conversion**: {session['conversion']}")
        st.markdown(f"**Total Value**: ${session['total_value']}")

        st.markdown("#### * AI-Generated Insights:")
        styled_insight = f"""
        <div style="font-family: 'Courier New', monospace; font-size: 15px; white-space: pre-wrap;">
        {insight}
        </div>
        """
        st.markdown(styled_insight, unsafe_allow_html=True)
        st.markdown("#### * User Experience:")
        styled_user_experience = f"""
        <div style="font-family: 'Courier New', monospace; font-size: 15px; white-space: pre-wrap;">
        {user_experience}
        </div>
        """
        st.markdown(styled_user_experience, unsafe_allow_html=True)
        st.markdown("#### * Recommendation:")
        styled_recommendation = f"""
        <div style="font-family: 'Courier New', monospace; font-size: 15px; white-space: pre-wrap;">
        {recommendation}
        </div>
        """
        st.markdown(styled_recommendation, unsafe_allow_html=True)
        # st.markdown(recommendation)
        session_summary = {
            "Session ID": session["session_id"],
            "Device": session["device_type"],
            "Country": session["user_attributes"]["country"],
            "Conversion": session["conversion"],
            "Recommendation": recommendation
        }
        session_summaries.append(session_summary)

    # --- Display consolidated report in a table ---
    st.markdown("### Consolidated Summary Report:")

    # Convert summary to pandas DataFrame for display
    df_summary = pd.DataFrame(session_summaries)

    # Style the table to add border and dark background
    styled_df = df_summary.style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', 'darkslategray'), ('color', 'white')]},
        {'selector': 'tbody td', 'props': [('border', '1px solid black'), ('text-align', 'center')]},
        {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%')]}
    ])

    st.dataframe(styled_df)

if __name__ == "__main__":
    display_page()
