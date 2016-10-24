import requests
import hashlib
import time
import simplejson as json
import pprintpp as pprint

#nodig voor apikey
def setup_Api():
    #api gegevens
    privKey ='0dbf711f6cbec1de65d0fb27d5c224bcf8957d47'
    publKey ='3b55fc225642ff0cc6e37e5cdf18f29f'

    #tijd in seconden voor
    ts = time.time()

    #alles wordt apikey (time + privkey + publkey
    apikey = str(ts) + privKey + publKey

    #het wordt gehashed dus naar md5 encryptie veranderd
    hash_object = hashlib.md5(apikey.encode())
    hex_dig = hash_object.hexdigest()

    #hele url met time public key en apikey
    api_url ='http://gateway.marvel.com/v1/public/characters?ts='+(str(ts)+'&apikey='+publKey+'&hash='+hex_dig)

    #url wordt gereturned
    return api_url

#deze maakt connectie met de api en api_url wordt ingelezen
def connect_Api(api_url):

    #met requests.get haal je data uit het api_url waar alles op staat
    response = requests.get(api_url)

    #alle gegevens worden opgeslagen in een json en die kan worden uitgelezen in python
    result = response.json()

    # hier wordt het resultaat gereturned
    return result

def nameCharacter(result):

    #Alleen de eerste 20 namen worden weergeven
    for character in result['data']['results']:
        print(character['name'])

def exactNameCharacter(result):
    for character in result['data']['results']:
        if character['name'] == ['Iron man']:
            print (character['id'])
            print (character['name'])
            print (character['description'])
        else:
            print('not found')
            break


api_url = setup_Api()
result = connect_Api(api_url)
#nameResult = nameCharacter(result)
nameResult2 = exactNameCharacter(result)
