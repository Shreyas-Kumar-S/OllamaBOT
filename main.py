from langchain_ollama import OllamaLLM # type: ignore
from langchain_core.prompts import ChatPromptTemplate #type:ignore

template ="""
Answer the questions below.
Here is the conversation history: {context}

Question: {input}
Answer:
"""

model = OllamaLLM(model="llama3")
prompt=ChatPromptTemplate.from_template(template)
chain= prompt | model

def handle_conservation():
    context=""
    print("Welcome to the AI chatbot! type 'exit' to quit")
    while True:
        user_input=input("You: ")
        if(user_input.lower()=="exit"):
            break
        result = chain.invoke({"context":context,"input": user_input})
        print("Bot: ",result)
        context +=f"\nUser:{user_input}\nAI: {result}"
        
if __name__ == "__main__":
    handle_conservation()