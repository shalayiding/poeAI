import openai
import json

class Chatgpt:
    def __init__(self,MODEL_API_KEY,MODEL_TYPE,PROMPT,MAX_TOKEN,TOOLS):
        openai.api_key = MODEL_API_KEY
        self.model_type = MODEL_TYPE
        self.max_token = MAX_TOKEN
        self.tools = TOOLS
        self.conversation_history = []
        self.conversation_history.append({"role": "system", "content": PROMPT})
        
        
        
    def conversation(self,user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
                
                model=self.model_type,
                messages=self.conversation_history,
                max_tokens=self.max_token
            )
        response_message = response.choices[0].message['content'].strip()
        
        # Add the response to the conversation history
        self.conversation_history.append({"role": "assistant", "content": response_message})
        
        return response_message
    