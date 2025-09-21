from google import genai

class Agent:
    def __init__(self):
        self.agent = genai.Client()
        self.model="gemini-2.5-flash-lite"
    
    def prompt(self,content):
        response = self.agent.models.generate_content(model=self.model,contents=content)
        return response.text

if __name__ == "__main__":
    agent = Agent()
    print(agent.prompt("that's nice of you"))

# client = genai.Client()
# chat = client.chats.create(model="gemini-2.5-flash-lite")

# response = chat.send_message("I have 2 dogs in my house.")
# print(response.text)

# response = chat.send_message("How many paws are in my house?")
# print(response.text)

# for message in chat.get_history():
#     print(f'role - {message.role}',end=": ")
#     print(message.parts[0].text)