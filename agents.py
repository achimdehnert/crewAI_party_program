from textwrap import dedent
from crewai import Agent
from tools.ExaSearchTool import ExaSearchTool
search_tool = ExaSearchTool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

import os

os.environ["OPENAI_API_KEY"] = "null"
os.environ["OPENAI_API_BASE"]='http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"]="mixtral"



#llm=ChatGroq(temperature=0,
#             #model_name="llama3-70b-8192",
#             model_name="mixtral-8x7b-32768",
#             api_key=os.environ["GROQ_API_KEY"])
#
llm=ChatOpenAI(
	temperature=0,
	base_url = "http://localhost:11434/v1",
	model="mixtral"
)




class PoliticalProgramAgents():
	def research_agent(self):
		return Agent(
			role='Research Specialist',
			goal='Conduct thorough research on the different domains that define a typical municipal election program.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a Research Specialist, your mission is to uncover detailed information
					about the typical domains addressed in party programms for municipal elections. 
					Your insights will lay the groundwork for the program draft."""),
			verbose=True, 
			llm=llm
		)

	def priority_analysis_agent(self):
		return Agent(
			role='Priority Analyst',
			goal='Establish which domains found during research have highest priority. Your result is a list of the 8 most important domains to cover in the program.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As Priority Analyst, your analysis will 
					identify the domains for a municipal election program that need to be addressed first because  
                    either (1) they rule the headlines and resonate with citizens or (2) have long-term importance 
					for the city or (3) represent long-hanging fruits."""),
			verbose=True, 
			llm=llm
		)

	def political_strategy_agent(self):
		return Agent(
			role='Political Advisor',
			goal='Develop actionable political demands for each domain that align with the liberal views of Participants.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a Political Advisor, your expertise will apply liberal views to the identified domains
					and establish concrete political demands for each of them
					to ensure a complete municipal election program."""),
			verbose=True, 
			llm=llm
		)

	def draft_agent(self):
		return Agent(
			role='Draft Coordinator',
			goal='Compile all gathered information and write a fully fledged municipal election program, addressing all relevant domains.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As the Briefing Coordinator, your role is to consolidate the research,
				    and formulation of political demands for all identified domains."""),
			verbose=True, 
			llm=llm
		)
