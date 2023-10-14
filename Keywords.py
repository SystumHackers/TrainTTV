f = open('selected_option.txt', 'r+')
a = f.readline()
print(a)
a = a.lower()

if a == 'bengali':
    s = 'bn'
elif a == 'gujarati':
    s = 'gu'
elif a == 'hindi':
    s = 'hi'
elif a == 'kannada':
    s = 'kn'
elif a == 'malayalam':
    s = 'ml'
elif a == 'marathi':
    s = 'mr'
elif a == 'tamil':
    s = 'ta'
elif a == 'telugu':
    s = 'te'
elif a == 'urdu':
    s = 'ur'

kw = s
f.close()

info = input("Enter the announcement: ")

from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Example usage
english_text = info
target_language = kw  # Change "es" to your target language code (e.g., "fr" for French)
translated_text = translate_text(english_text, target_language)
print(f"English: {english_text}")
print(f"Translated ({target_language}): {translated_text}")

# Save the translated text in a text file
output_file = open('translated_text.txt', 'w', encoding='utf-8')  # Open the file for writing
output_file.write(f"English: {english_text}\n")
output_file.write(f"Translated ({target_language}): {translated_text}\n")
output_file.close()
