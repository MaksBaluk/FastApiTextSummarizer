import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


def summarize_text_OpenAI(input_text: str) -> str:
    """
    Summarizes input text using OpenAI's ChatGPT model.

    Parameters:
    - input_text (str): The text to be summarized.

    Returns:
    - str: The summarized text.
    """
    # Initialize the ChatOpenAI model with API key and parameters
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

    # Define a prompt template for the ChatOpenAI model
    prompt_template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""

    # Convert the prompt template into a PromptTemplate object
    prompt = PromptTemplate.from_template(prompt_template)

    # Load the summarization chain with the ChatOpenAI model
    summarize_chain = load_summarize_chain(llm, chain_type="stuff")

    # Create a Document object from the input text
    document = Document(page_content=input_text)

    # Invoke the summarization chain to generate the summary
    summary = summarize_chain.invoke([document])["output_text"]

    return summary


def summarize_text_Bart(input_text: str) -> str:
    """
    Summarizes input text using the BART model from Facebook's transformers library.

    Parameters:
    - input_text (str): The text to be summarized.

    Returns:
    - str: The summarized text.
    """
    # Initialize the BART summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Generate the summary using the BART model
    summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)

    # Extract and return the summary text
    return summary[0]['summary_text']
