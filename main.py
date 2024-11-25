#lembrar de instalar a lib requests

import requests
from loguru import logger

#result = requests.get('https://api.adviceslip.com/advice')

#print(result)
#print(result.status_code)
#print(result.text)
#print(result.encoding)
#print(result.json())
#print(result.json()['slip'])
#print(result.json()['slip']['id'])
#print(result.json()['slip']['advice'])



try:
    for i in range(5):
        result = requests.get('https://api.adviceslip.com/advice')

        print(result.json())
        print(result.json()['slip'])
        print(result.json()['slip']['id'])
        print(result.json()['slip']['advice'])

except Exception as error:
    logger.exception(f'Error: {error}')







