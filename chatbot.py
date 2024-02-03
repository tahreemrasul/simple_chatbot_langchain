from langchain_openai import OpenAI
from langchain.chains import LLMChain
from prompts import ice_cream_assistant_prompt_template
from langchain.memory.buffer import ConversationBufferMemory

from dotenv import load_dotenv

import chainlit as cl

load_dotenv()


@cl.on_chat_start
def quey_llm():
    llm = OpenAI(model='gpt-3.5-turbo-instruct',
                 temperature=0)
    conversation_memory = ConversationBufferMemory(memory_key="chat_history",
                                                   max_len=50,
                                                   return_messages=True,
                                                   )
    llm_chain = LLMChain(llm=llm, prompt=ice_cream_assistant_prompt_template, memory=conversation_memory)
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def query_llm(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")
    response = await llm_chain.acall(message.content,
                                     callbacks=[
                                         cl.AsyncLangchainCallbackHandler()])

    await cl.Message(response["text"]).send()
