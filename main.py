import Scraper.scraper as SCR
import Model.model as model
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load env variables
    load_dotenv()
    openai_key = os.getenv("openai_key")
    
    # Read prompt file
    with open("prompt.md", "r") as file:
        prompt = file.read()
    
    scraper = SCR.scraper("https://r.jina.ai/")
    
    
    ai_bot = model.Chatgpt(openai_key, "gpt-4o", prompt, 1000, [])
    
    # ai_bot.add_tools("function", scraper.fetch_reader_page, "fetch_reader_page", "Extracting information from Webpage using URL",
    # {
    #     "type": "object",
    #     "properties": {
    #         "PAGE_URL": {
    #             "type": "string",
    #             "description": "URL of the webpage"
    #         }
    #     },
    #     "required": ["PAGE_URL"]
    # })
    
    
    
    ai_bot.add_tools("function",scraper.url_extract_a,"url_extract_a","Extracting all a tag in url with mathcing pattern from Webpage",{
        "type": "object",
        "properties": {
            "PAGE_URL": {
                "type": "string",
                "description": "URL of the webpage"
            },
            "Pattern":{
                "type": "string",
                "description": "The pattern that the algorithm is gonna search from"
            }
        },
        "required": ["PAGE_URL","Pattern"]
    })
    
    for i in range(4):
        userinput = input("You: ")
        response = ai_bot.conversation(userinput)
        print("bot: " + response)
