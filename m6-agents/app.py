import streamlit as st

# Page config
st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.title("📄 AI Resume Optimizer & Job Matcher")

st.write("Paste your Resume and Job Description below.")

# Two columns layout
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "📝 Enter Resume Text",
        height=300,
        placeholder="Paste your full resume text here..."
    )

with col2:
    job_description = st.text_area(
        "💼 Enter Job Description",
        height=300,
        placeholder="Paste job description here..."
    )

# Button
if st.button("🔍 Analyze Match"):
    if resume_text and job_description:
        st.success("Processing...")

        # 🔥 Replace this with your agent function
        # result = run_agent(resume_text, job_description)

        result = f"""
        ✅ Analysis Complete!

        Resume Length: {len(resume_text.split())} words  
        Job Description Length: {len(job_description.split())} words  

        (Connect this to your LLM agent for real optimization)
        """

        st.markdown(result)

    else:
        st.warning("Please fill both fields before analyzing.")