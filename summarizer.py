from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_summary(text):

    llm = Ollama(model="llama3")

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
You are an intelligent research assistant.

Summarize the following YouTube transcript.

Provide:

1. 🎥 Video Title (if possible)
2. 📌 5 Key Points
3. ⏱ Important timestamps (if present)
4. 🧠 Core takeaway

Transcript:
{text}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(text=text)