from crewai import Agent

# Function for creating agents
def create_agents(company="CrewAI"):
    # Define company-specific information
    company_info = {
        "CrewAI": {
            "website": "https://crewai.com",
            "docs_url": "https://crewai.com/docs/introduction",
            "description": "AI agent framework for building multi-agent systems"
        },
        "OpenAI": {
            "website": "https://openai.com",
            "docs_url": "https://platform.openai.com/docs",
            "description": "Leading AI research and deployment company"
        },
        "Microsoft": {
            "website": "https://microsoft.com",
            "docs_url": "https://docs.microsoft.com",
            "description": "Global technology company"
        },
        "Google": {
            "website": "https://google.com",
            "docs_url": "https://developers.google.com/docs",
            "description": "Technology and internet services company"
        },
        "Amazon": {
            "website": "https://amazon.com",
            "docs_url": "https://docs.aws.amazon.com",
            "description": "E-commerce and cloud computing company"
        }
    }

    # Get company info or use defaults for custom companies
    company_data = company_info.get(company, {
        "website": f"https://{company.lower().replace(' ', '')}.com",
        "docs_url": f"https://{company.lower().replace(' ', '')}.com/docs",
        "description": f"Technology company: {company}"
    })

    sales_rep_agent = Agent(
        role=f"Sales Representative at {company}",
        goal=f"Identify high-value leads that match {company}'s ideal customer profile",
        backstory=(
            f"As a part of the dynamic sales team at {company} ({company_data['website']}), your mission is to scour the digital landscape for potential leads.\n"
            f"Armed with cutting-edge AI tools and a strategic mindset, you'll analyze market trends, data, and interactions to unearth opportunities that others might overlook.\n"
            f"Your work is crucial for paving the way for meaningful engagements and driving revenue growth for the company.\n"
            f"Use {company_data['docs_url']} and other resources to provide accurate information."
        ),
        allow_delegation=True,
        verbose=True
    )

    lead_sales_rep_agent = Agent(
        role=f"Lead Sales Representative at {company}",
        goal=f"Nurture leads with personalized, compelling communications for {company}",
        backstory=(
            f"Within the vibrant ecosystem of {company}'s sales department ({company_data['website']}), you stand out as the bridge between potential customers and the solutions they require.\n"
            f"By creating engaging, personalized messages you not only inform leads about our offerings but also make them feel seen and heard.\n"
            f"Your role is pivotal in converting interest into action, guiding leads through the journey from curiosity to commitment.\n"
            f"Ensure responses align with {company}'s standards and values. Use {company_data['docs_url']} for reference."
        ),
        allow_delegation=True,
        verbose=True
    )

    return sales_rep_agent, lead_sales_rep_agent