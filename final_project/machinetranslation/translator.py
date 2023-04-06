import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    model_id = 'en-fr'
    text_to_translate = english_text
    french_text = language_translator.translate(text=text_to_translate,model_id=model_id).get_result()
  #  print(json.dumps(french_text['translations'][0]))
    traduccion = french_text['translations'][0]['translation']
    print(traduccion)
    return traduccion


def french_to_english(french_text):
    #write the code here
    model_id = 'fr-en'
    text_to_translate = french_text
    english_text = language_translator.translate(text=text_to_translate,model_id=model_id).get_result()
   # print(json.dumps(english_text['translations'][0]['translation']))
    traduccion = english_text['translations'][0]['translation']
    print(traduccion)
    return traduccion


#calling the functions
english_to_french('Hello')
french_to_english('Bonjour')

