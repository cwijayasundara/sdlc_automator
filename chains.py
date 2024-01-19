from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-4-1106-preview",
                 streaming=True)


prompt = """
System: You are an expert UX designer who can come up with professional UI wireframes!!

Come up with a UI wireframes for a web app based on the following user story:

Only come up with the wireframes for the web app, not the code and DO NOT ADD DESCRIPTIONS!!
 
Human: {input}

wireframes
"""

ui_wireframe_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """
System: You are an expert in quality assurance and  who can come up with css and html code for UI wireframes!!

Come up with html and css code for based on the following UI wireframes:

wireframes: {input}

html and css code"""

html_css_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """
System: You are an expert software engineer who is an expert in generating test data !!

Generate 10 test data samples for the following user story and make sure to include the following and store the data 
in a .csv file:

- positive test data
- negative test data
- edge case data

test data: {input}

test data"""

test_data_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)


prompt = """
System: You are an expert software quality assurance and testing engineer !!

Come up with a testing plan for the following user story and make sure to include the following:

- positive test cases
- negative test cases
- edge cases

test plan: {input}

detailed test plan"""

test_plan_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)


prompt = """
System: You are an expert software quality assurance and testing engineer !!

Loop through the detailed test plan and come up with a test case for each test plan covering the following:

- positive test cases
- negative test cases
- edge cases

test cases: {input}

detailed test cases"""

test_case_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)


prompt = """
System: You are an expert software engineer with expert skills with selenium and Python coding!!

Loop through the test cases and come up with a selenium and python test case for each test case covering the following:

- positive test cases
- negative test cases
- edge cases

Use the generated test data that's stored in a .csv file for the test data

selenium code: {input}

selenium and python test cases"""

selenium_code_gen_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """
System: You are an expert software engineer with expert skills with React!!

Generate comprehensive React code for the following user stories.

react code: {input}

react code"""

react_code_gen_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)


