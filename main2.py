api_key = "AIzaSyBrkEfA0TqsOzY9OghVQ_H9MUlKnhimGYA"

import google.generativeai as genai
import os

genai.configure(api_key=api_key)

text = """

"""
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Write a summary of the following text in about 200 words: " + text )
print(response.text)