import openai
import os
from dotenv import load_dotenv

#Ustawia klucz API OpenAI
load_dotenv()  # Ładuje zmienne z pliku .env
openai.api_key = os.getenv("OPENAI_API_KEY")

#Funkcja odczytania pliku tekstowego
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Błąd: Plik {file_path} nie został znaleziony.")
        exit(1)
    
#Funckdja do zapisania kodu HTML do pliku
def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Plik został zapisany w {file_path}")
    
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