#Python Pillow
#Importing Image module from pillow
from PIL import Image
img = Image.open("gundam.jpg")
img.show()
img = img.rotate(180)
img.show()

#Python GoogleTrans
from googletrans import Translator
translator = Translator(service_urls=[
    'translate.xyz.com'
])
langauges = {
    'e': "English",
    'n': "Nepali",
    "h": "Hindi",
    "j": "Japaneese",
    "c": "Chineese"
}
for num in range(len(langauges)):
    key = list(langauges.keys())[num]
    print(f"{num + 1}. {langauges[key]}")
from_lang_num = int(input("Enter the number of langauge you want to translate from : "))
to_lang_num = int(input("Enter the number of langauge you want to translate to : "))
keys = list(langauges.keys())
from_lang = keys[from_lang_num - 1]
to_lang = keys[to_lang_num - 1]
to_translate = input("Enter the text you want to translate : ")
translation = translator.translate(to_translate, dest=to_lang, src=from_lang)
print()
print(translation.text)