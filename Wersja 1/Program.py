import openai
import os

#Ustawia klucz API OpenAI
openai.api_key = "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"

#Funkcja odczytania pliku tekstowego
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
#Funckdja do zapisania kodu HTML do pliku
def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

#Tresc artykulu
article_content = read_file('Artykul.txt')

prompt = f"""Please create a simple HTML code for the article: {article_content} that meets the following requirements:
        -Use appropriate HTML tags to structure the content,
        -Specify places where you would insert graphics. Mark them using the <img> tag with the src="image_placeholder.jpg" attribute. Add an alt attribute to each image with an exact prompt that we can use to generate the graphic.Place captions under the graphics using the appropriate HTML tag.
        -Do not include any CSS or JavaScript code. The returned code should only contain content to be inserted between the <body> and </body> tags 
        -Do not include the <html>, <head>, or <body> tags.
        """

#Wysylanie zapytania do API OpenAI
#poprawic to na ewentualnie nowe wywolanie
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a programist assistant."},
        {"role": "user", "content":prompt}
    ],
    max_tokens=1200, 
    temperature=0.7 
)

#zapisanie wygenerowanego kodu HTML do pliku artykul.html
html_content = response.choices[0].message.content.strip()
save_to_file('artykul.html',html_content)

print("Kod HTML zostal zapisany do pliku artykul.HTML")