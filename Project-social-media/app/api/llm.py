import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from model_names_repo import llm_model_names
from prompts import llm_prompt_template


class llmclass:
    def __init__(self):
        
        load_dotenv()
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        
        self.llm_model = llm_model_names[5]
        self.create_chain()


    def change_model_name(self, model_name):
        if model_name in [model for model in llm_model_names]:
            self.llm_model = model_name
            self.create_chain()
        else:
            raise ValueError("Model name not found in available models.")
        
        
    def create_chain(self):
        self.llm = ChatGroq(groq_api_key=self.groq_api_key, model=self.llm_model)
        self.chain = llm_prompt_template | self.llm
        
            
    def generate_content(self, input_data):
        if not hasattr(self, 'chain'):
            self.create_chain()
        output = self.chain.invoke(input_data)
        return output.content


