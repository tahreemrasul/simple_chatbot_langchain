# Custom Chatbot using LangChain, OpenAI and Chainlit

You can read further [here](https://medium.com/@tahreemrasul/how-to-build-your-own-chatbot-with-langchain-and-openai-f092822b6ba6), [here](https://medium.com/@tahreemrasul/building-a-chatbot-application-with-chainlit-and-langchain-3e86da0099a6) and [here](https://medium.com/@tahreemrasul/integrating-an-external-api-with-a-chatbot-application-using-langchain-and-chainlit-b687bb1efe58).

## Overview
## Overview
This repo contains the code for Scoopsie, a custom chatbot that answers ice-cream-related questions and fetches information from a fictional ice-cream store's API. Using LangChain and OpenAI's text model, alongside a Flask web service, Scoopsie can provide users with details on flavors, toppings, and store offers. Everything is put together with Chainlit for easy web application integration.

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
   conda create -n chatbot_langchain python=3.8
* Activate the environment:
   ```bash
   conda activate chatbot_langchain

3. **Install Dependencies**
* Install the required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

4. **Set Up Your OpenAI API Key**
* Create a .env file in the root directory of the project.
* Add your OpenAI API key to the `.env` file:
   ```bash
   OPENAI_API_KEY='Your-OpenAI-API-Key-Here'

### Usage
To run the fictional store's API, execute the following command:
   ```bash
   python ice_cream_store_app.py
```
The fictional store's API will be accessible at http://localhost:5000/{endpoint_name}

Make sure the fictional store's application is running before running the chatbot. To run Scoopsie, 
simply execute the `chatbot.py` script:
   ```bash
   chainlit run chatbot.py -w --port 8000
```

To run the chatbot application, navigate to  http://localhost:8000

