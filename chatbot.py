from langchain_openai import OpenAI
from langchain.chains import LLMChain
from prompts import ice_cream_assistant_prompt_template

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct',
             temperature=0)

llm_chain = LLMChain(llm=llm, prompt=ice_cream_assistant_prompt_template)


def query_llm(question):
    print(llm_chain.invoke({'question': question})['text'])


if __name__ == '__main__':
    query_llm("Who are you?")


