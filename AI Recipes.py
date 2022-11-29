import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY");
userinput = input("Enter Ingredients and Instructions!\n")

def openAIQuery(query):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=query,
      temperature=0.8,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)

    if 'choices' in response:
              if len(response['choices']) > 0:
                  answer = response['choices'][0]['text']
              else:
              	answer = 'Change ingredients or specification verbs'
    else:
           answer = 'Change instructions to further elaborate the recipe requirements'
    return answer
        
        

openAIRecipeUnformatted = openAIQuery(userinput);
print(openAIRecipeUnformatted);