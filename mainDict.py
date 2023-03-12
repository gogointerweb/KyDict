import requests, os, json
from dotenv.main import load_dotenv
import pprint as pprint

load_dotenv()

#put in a function for rate limiting
#perhaps it reads a file to determine how many requests have been made
#so any request would need counted in a file also.

word = "greetings"
wordFixed = word.lower()

baseURL = os.environ["DICT_URL"]
#needs word, "?key=", api key before request send

key = os.environ["API_KEY"]

def getWord(X):
    sendURL = baseURL + X + "?key=" + key
    response = requests.get(sendURL)
    print(f"Status code: {response.status_code}")
    bytes = json.loads(response.content.decode()) #dictionary response is in bytes, UTF-8, this converts to list
    print(bytes)
    print(type(bytes))

getWord("hello")






#could also add a written file to retrain word history
#could be used in conjunction with the rate limit count mentioned above
