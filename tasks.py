from crewai import Task
from tools import agents_tools

def create_tasks(sales_rep_agent, lead_sales_rep_agent, inputs):
    tools = agents_tools()
    directory_read_tool = tools["directory_read_tool"]
    file_read_tool = tools["file_read_tool"]
    search_tool = tools["search_tool"]
    sentiment_analysis_tool = tools["sentiment_analysis_tool"]

    lead_profiling_task = Task(
        description=(
            f"Conduct an in-depth analysis of {inputs['lead_name']}, a company in the {inputs['industry']} sector "
            "that recently showed interest in our solutions. Utilize all the available data sources "
            "to compile a detailed profile, focusing on key decision-makers, recent business developments, "
            "and potential needs that align with our offerings. This task is crucial for tailoring "
            "our engagement strategy effectively.\n"
            "Do not make assumptions and only use information you are absolutely sure about."
        ),
        expected_output=(
            f"A comprehensive report on {inputs['lead_name']}, including company background, key personnel, "
            "recent milestones, and identified needs.\n"
            "Highlight potential areas where our solutions can provide value and suggest personalized "
            "engagement strategies based on the analysis."
        ),
        tools=[directory_read_tool, file_read_tool, search_tool],
        agent=sales_rep_agent
    )

    personalized_outreach_task = Task(
        description=(
            f"Using the insights gathered from the lead profiling report on {inputs['lead_name']}, craft a personalized outreach campaign aimed at {inputs['key_decision_maker']}, the {inputs['position']} of {inputs['lead_name']}.\n"
            f"The campaign should address their recent {inputs['milestone']} and how our solutions can support their goals.\n"
            f"Your communication must resonate with {inputs['lead_name']}'s company culture and values, demonstrating a deep understanding of their business and needs.\n"
            "Don't make assumptions and only use information you are absolutely sure about."
        ),
        expected_output=(
            f"A series of personalized email drafts tailored to {inputs['lead_name']}, specifically targeting {inputs['key_decision_maker']}.\n"
            "Each draft should include a compelling narrative that connects our solutions with their recent achievements and future goals.\n"
            f"Ensure the tone is engaging, professional, and aligned with {inputs['lead_name']}'s corporate identity."
        ),
        tools=[sentiment_analysis_tool, search_tool],
        agent=lead_sales_rep_agent,
    )

    return lead_profiling_task, personalized_outreach_task
