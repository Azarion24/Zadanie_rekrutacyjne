# Zadanie_rekrutacyjne
 Zadanie rekurtacyjne na Junior AI Developer

 Program.py, artykul.html oraz Artykul.txt w obu wersjach są takie same

# Wersja 1
Zawiera 5 plików (artykul.html, Artykul.txt, podglad.html, Program.py, szablon.html). Szablon nie zwiera kodu JS. 
Plik szablon.html nie zawiera treści z pliku artykul.html.
W pliku podglad.html znajduje się treść z pliku artykul.html. 
Żeby móc sprawdzić jak wszystko działa w tym wypadku wystarczy otwotrzyć plik podglad.html w przeglądarce

# Wersja 2
Zawiera 4 pliki (artykul.html, Artykul.txt, Program.py, szablon.html). Szablon zawiera kod JS.

Żeby wszystko działało poprawnie należy: 
1. wejść w folder w którym znajdują się pliki
2. uruchomić konsole i wpisać
   ```bash
   python -m http.server
   ```
   Dzięki temu uruchomimy serwer w Pythonie.
   Domyślnie serwer uruchomi się pod adresem: http://localhost:8000.
3. Otwórz przeglądarkę i przejdź pod adres: http://localhost:8000/szablon.html.

Po wykonaniu tych akcji powinna poprawnie wczytać się strona wraz z treścią artykułu 

# Safety first
Ze względów bezpieczeństwa został stworzony plik .env który jest ignorowany. Struktura pliku .env wygląda następująco:

```bash
OPENAI_API_KEY = "sk-proj-kp..."
```
Pomiędzy "..." należy wprowadzić poprawny klucz
