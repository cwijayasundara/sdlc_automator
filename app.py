import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_core.output_parsers import StrOutputParser
from chains import (ui_wireframe_chain,
                    html_css_chain,
                    test_data_chain,
                    test_plan_chain,
                    test_case_chain,
                    selenium_code_gen_chain)

output_parser = StrOutputParser()

st.header("Gen AI for Quality Assurance Automation")
request = st.text_area('Please Detail Your User Story for QA Automation! ', height=150)
submit = st.button("submit", type="primary")

if submit and request:
    wire_frame_response = ui_wireframe_chain.run({"input": request})
    print(wire_frame_response)
    st.markdown(""" :blue[Wire Frame : ] """, unsafe_allow_html=True)
    st.write(wire_frame_response)

    html_css_response = html_css_chain.run({"input": wire_frame_response})
    print(html_css_response)
    st.markdown(""" :blue[HTML & CSS : ] """, unsafe_allow_html=True)
    st.write(html_css_response)

    test_data_chain_response = test_data_chain.run({"input": wire_frame_response})
    print(test_data_chain_response)
    st.markdown(""" :blue[Test Data : ] """, unsafe_allow_html=True)
    st.write(test_data_chain_response)

    test_plan_response = test_plan_chain.run({"input": request})
    print(test_plan_response)
    st.markdown(""" :blue[Test Plan : ] """, unsafe_allow_html=True)
    st.write(test_plan_response)

    test_case_response = test_case_chain.run({"input": test_plan_response})
    print(test_case_response)
    st.markdown(""" :blue[Test Cases : ] """, unsafe_allow_html=True)
    st.write(test_case_response)

    selenium_code_gen_response = selenium_code_gen_chain.run({"input": test_case_response})
    print(selenium_code_gen_response)
    st.markdown(""" :blue[Selenium Code : ] """, unsafe_allow_html=True)
    st.write(selenium_code_gen_response)
