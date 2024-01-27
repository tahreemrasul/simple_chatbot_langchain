# Use-case Specific Chatbot using LangChain and OpenAI

## Overview
This repo focuses on creating a simple but use-case specific chatbot using LangChain and the text completion model from OpenAI. Scoopsie is a specialized chatbot dedicated to queries regarding ice-cream. Built using LangChain and OpenAI, it's designed to provide information and advice on ice cream flavors, recipes, and related queries. 

## Getting Started

### Prerequisites
- Python 3.8 or later
- An OpenAI API key

### Installation

1. **Clone the Repository**
   ```bash
   git clone git@github.com:tahreemrasul/simple_chatbot_langchain.git
   cd ./simple_chatbot_langchain
  
2. **Set Up a Conda Environment (Recommended)**
* If you don't have Conda, install it first.
* Create a new Conda environment:
   ```bash
   conda create -n scoopsie-env python=3.8
* Activate the environment:
   ```bash
   conda activate scoopsie-env

3. **Install Dependencies**
* Install the required packages using the requirements.txt file:
   ```bash
   pip install -r requirements.txt

4. **Set Up Your OpenAI API Key**
* Create a .env file in the root directory of the project.
* Add your OpenAI API key to the .env file:
   ```bash
   OPENAI_API_KEY='Your-OpenAI-API-Key-Here'

### Usage

To run Scoopsie, simply execute the chatbot.py script:
   ```bash
   python chatbot.py

