
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv

import os
import time

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.load_local(
    "faiss_cocktails", 
    embedding_model, 
    allow_dangerous_deserialization=True
)

llm = GoogleGenerativeAI(
    model="gemini-2.0-pro-exp-02-05", 
    api_key=os.environ["GOOGLE_API_KEY"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_db.as_retriever(),
    chain_type="stuff",
    return_source_documents=True
)

user_preferences = []

def classify_input(user_input):

    prompt = f"""
    Classify this user input: "{user_input}"
    
    - If the user is sharing favorite ingredients or cocktails, return only: preference
    - If the user is asking a general question return only: query
    - If the user is asking a question based on my favorite ingredients or preferences return only: recommendation
    """
    
    response = llm.invoke(prompt)
    return response.strip().lower()

def extract_ingredients(user_input):

    prompt = f"""
    The user has mentioned their favorite cocktail ingredients or drinks in this sentence:

    "{user_input}"

    Please extract the key ingredients or cocktail names they like. If the user mentions 
    something vague (e.g., "I like refreshing drinks"), infer possible relevant ingredients 
    (e.g., "mint, lime, soda"). 

    Return a **comma-separated** list of ingredients or cocktail names. If nothing relevant is found, return 'None'.
    """

    response = llm.invoke(prompt).strip()
    

    if response.lower() == "none":
        return []
    
    return [item.strip().lower() for item in response.split(",")]

def recommend_based_on_preferences(user_input):

    if not user_preferences:
        return "You haven't shared any preferences yet! Tell me your favorite ingredients."

    preferences = " or ".join(user_preferences)

    user_input_extended = f"""
    My favorite ingredients are either {preferences} or all of them mixed.

    {user_input}
    """

    return qa_chain.invoke({"query": user_input_extended})['result']
    
def store_preference(user_input):

    ingredients = extract_ingredients(user_input)

    if ingredients:
        user_preferences.extend(ingredients)

        return f"Preferences stored: {', '.join(ingredients)}"
    
    return "No preferences found."

def chatbot_response(user_input):

    classification = classify_input(user_input)

    time.sleep(3)

    if classification == "preference":
        return store_preference(user_input)

    elif classification == 'recommendation':
        return recommend_based_on_preferences(user_input)
    
    elif classification == "query":        
        return qa_chain.invoke({"query": user_input})['result']
    
    
    return "I'm not sure how to handle that. Could you clarify?"