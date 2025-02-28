# Simple RAG App

## Overview

Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the content of a different types of cocktails placed in folder dataset. The app uses techniques to provide answers based on the content. The application leverages all-MiniLM-L6-v2, Google Gemini 2, LangChain, and FAISS for its operations.


## Features

- **Ask Questions About Cocktails:** It first processed as combination of text and stored as faiss_coktails with `index`.
- **LLM Models:** Utilizes all-MiniLM-L6-v2 and Google Gemini 2 for generating responses.
- **Efficient Document Retrieval:** Uses LangChain and FAISS for efficient retrieval and processing.

## Getting Started

### Prerequisites

- Python 3.10.5
- Required Python packages (see `requirements.txt`)
- Google gemini key is needed. It needs to be put in `.env` file as <<YourApiKey>>

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tmasmaliyev/Cocktail_Advisor_Chat.git
   cd simple-rag-app
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```bash
   python app.py
   streamlit run main.py
   ```

2. Enter your questions when prompted. Type 'exit' to quit the application.

## WIP Features

- [X] **Web UI:** A web-based user interface for easier interaction.
- [X] **Conversation Memory:** The app will remember previous interactions during runtime for better context handling. It can be preferences, favorite ingredients and etc.

## Contact

For any questions or suggestions, please open an issue in the repository.