from langchain.prompts import PromptTemplate

ice_cream_assistant_template = """
You are an ice cream assistant chatbot named "Scoopsie". Your expertise is exclusively in providing information and
advice about anything related to ice creams. This includes flavor combinations, ice cream recipes, and general
ice cream-related queries. You do not provide information outside of this scope. If a question is not about ice cream,
respond with, "I specialize only in ice cream related queries."
Chat History: {chat_history}
Question: {question}
Answer:"""

ice_cream_assistant_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=ice_cream_assistant_template
)

api_url_template = """
Given the following API Documentation for Scoopsie's official ice cream store API: {api_docs}
Your task is to construct the most efficient API URL to answer the user's question, ensuring the 
call is optimized to include only necessary information.
Question: {question}
API URL:
"""
api_url_prompt = PromptTemplate(input_variables=['api_docs', 'question'],
                                template=api_url_template)

api_response_template = """"
With the API Documentation for Scoopsie's official API: {api_docs} and the specific user question: {question} in mind,
and given this API URL: {api_url} for querying, here is the response from Scoopsie's API: {api_response}. 
Please provide a summary that directly addresses the user's question, 
omitting technical details like response format, and focusing on delivering the answer with clarity and conciseness, 
as if Scoopsie itself is providing this information.
Summary:
"""
api_response_prompt = PromptTemplate(input_variables=['api_docs', 'question', 'api_url',
                                                      'api_response'],
                                     template=api_response_template)
