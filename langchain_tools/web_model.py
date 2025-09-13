from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv


load_dotenv()


_llm = ChatGoogleGenerativeAI(model=os.getenv("GENIE_MODEL", "gemini-1.5-flash"), temperature=0)
_prompt_template = ChatPromptTemplate.from_messages([
    ("system", """  You are an expert web developer specializing in finding precise XPath locators.
                        Your task is to analyze the provided HTML content and find the XPath for the element
                        that matches the user's description.
         
                        You must respond ONLY with a JSON object in the following format:
                        { "xpath": "<the XPath you found>" }
         
                        If you cannot find a matching element, respond with:
                        { "xpath": "null" }
                    
                """),

    ("human", """   Here is the HTML content of the webpage:
                        ---
                        {html_content}
                        ---
         
                        Based on this HTML, please provide the XPath for the following element: "{element_description}"
                """)
])


_parser = JsonOutputParser()
_chain = _prompt_template | _llm | _parser


def get_xpath(html_content: str, element_description: str) -> dict:
    """
    Uses an LLM to find the XPath of an element on a webpage based on its description.
    """
    try:
        response = _chain.invoke({
            "html_content": html_content,
            "element_description": element_description
        })
        return response
    except Exception as e:
        print(f"ERROR: Failed to get XPath from LLM: {e}")
        return {"xpath": "null"}
    