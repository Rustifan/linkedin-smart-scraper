from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url

def lookup(name: str):
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their linkedin profile page. Your answer should contain only url, without explanation."""
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
        func=get_profile_url,
            description="useful for when you need get the Linkedin Page url",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    
    return agent.run(prompt_template.format_prompt(name_of_person=name))
    
