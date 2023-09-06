from typing import Tuple
from dotenv import load_dotenv
load_dotenv()
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import get_img_url_from_linkedin_data, scrape_linkedin_profile
from output_parsers import PersonIntel, person_intel_parser
import json
def find_info(name: str)->Tuple[PersonIntel, str]:
    summary_template = """
    Response should be in Croatian language.
    given the information {information} about this person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    3. A topic that may interest them
    4. 2 creative Ice breakers to open a conversation with them
    
    \n {format_instructions}
    """    
    linkedin_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_url)
    img_url = get_img_url_from_linkedin_data(linkedin_data)

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template, partial_variables={
        "format_instructions": person_intel_parser.get_format_instructions()
    })
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.run(information=json.dumps(linkedin_data)[:3000])

    return person_intel_parser.parse(result), img_url

if __name__ == "__main__":
    print(find_info("Ivica Hrg kompare"))    

if __name__ == "1__main__":
    pass
    
