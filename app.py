import warnings
import streamlit as st
from crewai import Crew
from agents import create_agents
from tasks import create_tasks
from app_utils import enter_and_set_api_keys, pretty_print_result
import traceback

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Multi-Agent Customer Campaign Automation",
    page_icon="📇",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .result-container {
        background: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .footer {
        font-size: 1rem;
        color: #666;
        text-align: center;
        margin-top: 4rem;
    }
</style>
""", unsafe_allow_html=True)


def run_crew(your_company, lead_name, industry, key_decision_maker, position, milestone):
    sales_rep_agent, lead_sales_rep_agent = create_agents(company=your_company)
    inputs = {
        "your_company": your_company,
        "lead_name": lead_name,
        "industry": industry,
        "key_decision_maker": key_decision_maker,
        "position": position,
        "milestone": milestone
    }
    lead_profiling_task, personalized_outreach_task = create_tasks(sales_rep_agent, lead_sales_rep_agent, inputs)

    crew = Crew(
        agents=[sales_rep_agent, lead_sales_rep_agent],
        tasks=[lead_profiling_task, personalized_outreach_task],
        verbose=True,
        memory=True
    )

    result = crew.kickoff(inputs=inputs)
    return result


def main():
    st.markdown('<h1 class="main-header"📇 Multi-Agent Customer Campaign Automation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Leverage multi-agent AI to identify, profile, and engage high-value leads</p>', unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        openai_api_key, serper_api_key = enter_and_set_api_keys(streamlit_mode=True)
        if not openai_api_key or not serper_api_key:
            st.error("Please enter valid API keys to continue.")
            return
        st.markdown("### 🏢 Company Context")
        company_select = st.selectbox("Select Your Company", ["CrewAI", "OpenAI", "Microsoft", "Google", "Amazon", "Custom"])
        if company_select == "Custom":
            company = st.text_input("Enter your company name:", "TechCorp Inc.")
        else:
            company = company_select
        st.markdown("### 🤖 About Agents")
        st.markdown("- Sales Rep: Identifies and profiles leads\n- Lead Sales Rep: Crafts outreach content")
        st.markdown("### 🧠 Tools Used")
        st.markdown("- File Reader\n- Web Search\n- Sentiment Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📝 Campaign Details")
        lead_name = st.text_input("Lead/Target Company Name", "Deeplearning.ai", help="Target company you're reaching out to")
        key_decision_maker = st.text_input("Key Decision Maker", "Andrew Ng", help="Name of the person to contact")
        milestone = st.text_input("Recent Milestone", "recently launched a new AI course", help="A recent event related to the company")
    with col2:
        industry = st.text_input("Industry", "AI Education", help="Industry of the target company")
        position = st.text_input("Position", "CEO", help="Job title of the decision maker")

    if st.button("🚀 Run Outreach Campaign", use_container_width=True):
        if not all([company, lead_name, industry, key_decision_maker, position, milestone]):
            st.warning("Please fill in all fields before running the campaign.")
        else:
            with st.spinner("Running CrewAI agents..."):
                try:
                    result = run_crew(company, lead_name, industry, key_decision_maker, position, milestone)
                    # Safely extract text
                    if hasattr(result, 'final_output'):
                        result_text = result.final_output
                    elif isinstance(result, str):
                        result_text = result
                    else:
                        result_text = str(result)
                    
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.markdown("### 🎯 Campaign Result")
                    st.code(result_text)
                    st.download_button("📥 Download Result", result_text, file_name="campaign_result.txt")
                    st.markdown('</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error: {e}")
                    st.text(traceback.format_exc())

    st.markdown('<h6 class="footer">Developed by Saad Toor | saadtoorx</h6>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
