from openai import OpenAI
import json

class Chatgpt:
    def __init__(self,MODEL_API_KEY,MODEL_TYPE,PROMPT,MAX_TOKEN,TOOLS):
        self.client = OpenAI(api_key=MODEL_API_KEY)
        self.model_type = MODEL_TYPE
        self.max_token = MAX_TOKEN
        self.tools = TOOLS
        self.conversation_history = []
        self.conversation_history.append({"role": "system", "content": PROMPT})
        self.tool_calls = None
        self.available_functions = {}
  
        
    def conversation(self,user_input):
        if user_input:
            self.conversation_history.append({"role": "user", "content": user_input})
        
        response = self.client.chat.completions.create(
                model=self.model_type,
                messages=self.conversation_history,
                max_tokens=self.max_token,
                tools=self.tools,
                tool_choice="auto",
            )
        
        response_message = response.choices[0].message.content
        self.tool_calls = response.choices[0].message.tool_calls
        # Add the response to the conversation history
        
        if self.tool_calls:
            return self.tool_call_action()
        else :
            self.conversation_history.append({"role": "assistant", "content": response_message})
            return response_message
        
        
        
    
    # add function or tools into the set of runable functions
    def add_tools(self,type,func,func_name,func_des,parameters):
        function = {
            "name":func_name,
            "description":func_des,
            "parameters":parameters
        }
        self.available_functions[func_name] = func
        self.tools.append({"type":type,"function":function})
    
    
    # an action happend after the Chatbot decide to call any function
    def tool_call_action(self):
        for tool_call in self.tool_calls:
            function_name = tool_call.function.name
            function_to_call = self.available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                **function_args
            )
            print(function_name)
            
            self.conversation_history.append({
                "role": "function",
                "name": function_name,
                "content": function_response,
            })

        response = self.client.chat.completions.create(
            model=self.model_type,
            messages=self.conversation_history,
            max_tokens=self.max_token
        )
        response_message = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": response_message})
        return response_message
        
    
    