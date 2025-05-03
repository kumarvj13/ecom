from utils import build_prompt, analyze_user_experience, generate_recommendation
from model import generate_insight

def analyze_sessions(sessions):
    results = []

    for session in sessions:
        try:
            prompt = build_prompt(session)
            insight = generate_insight(prompt)
            experience = analyze_user_experience(session)
            recommendation = generate_recommendation(session)

            results.append({
                "Session ID": session.get("session_id"),
                "Device": session.get("device_type"),
                "Country": session["user_attributes"].get("country"),
                "Conversion": session.get("conversion"),
                "Insight": insight,
                "User Experience": experience,
                "Recommendation": recommendation
            })

        except Exception as e:
            results.append({
                "Session ID": session.get("session_id", "Unknown"),
                "Insight": f"Error analyzing session: {str(e)}",
                "User Experience": "N/A",
                "Recommendation": "N/A",
                "Device": "N/A",
                "Country": "N/A",
                "Conversion": False
            })

    return results
