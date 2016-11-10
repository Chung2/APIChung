import requests
import hashlib
import time
import random

#lijst met de helden
def helden():
    #1008368
    lijstHelden = [1009368,1009351,1009220,1009610,1009718,1009697,1009664,1009262,1009619]
    return lijstHelden

#nodig voor apikey
def setup_Api(rawLijstHelden):
    #api gegevens
    privKey ='0dbf711f6cbec1de65d0fb27d5c224bcf8957d47'
    publKey ='3b55fc225642ff0cc6e37e5cdf18f29f'

    lijstLinkjes =[]
    #tijd in seconden voor
    ts = time.time()

    #alles wordt apikey (time + privkey + publkey
    apikey = str(ts) + privKey + publKey

    #het wordt gehashed dus naar md5 encryptie veranderd
    hash_object = hashlib.md5(apikey.encode())
    hex_dig = hash_object.hexdigest()

    #hele url met time public key en apikey
    #api_url ='http://gateway.marvel.com/v1/public/characters?ts='+(str(ts)+'&apikey='+publKey+'&hash='+hex_dig)

    #door gebruik te maken van een character id kan je specifiek een character eruit halen in een lijst
    for i in rawLijstHelden:
        api_url = 'http://gateway.marvel.com/v1/public/characters/'+str(i)+'?ts='+(str(ts)+'&apikey='+publKey+'&hash='+hex_dig)
        lijstLinkjes.append(api_url)

    #url wordt gereturned
    return lijstLinkjes

#deze maakt connectie met de api en api_url wordt ingelezen
def connect_Api(lijstLinkjes):
    resultHelden = []

    #met requests.get haal je data uit het api_url waar alles op staat
    for s in lijstLinkjes:
        response = requests.get(s)
        resultApi = response.json()
        resultHelden.append(resultApi['data']['results'][0])

    #alle gegevens worden opgeslagen in een json en die kan worden uitgelezen in python
    return resultHelden

    # hier wordt het resultaat gereturned

#Alle namen weergeven uit API, naam, id en description
def nameCharacter(result):
    #Alleen de eerste 20 namen worden weergeven

    for i in range(len(result)):
        print(result[i]['id'])
        print(result[i]['name'])
        print(result[i]['description'])

#functie specifiek character selecteren uit Marvel API en print id, naam en description
def exactNameCharacter(result):

    for i in range(len(result)):
       if result[i].get('id') == 1009697:
           print(result[i].get('id'))
           print(result[i].get('name'))
           print(result[i].get('description'))

def Selectrandomhero(result):

    random.shuffle(result)
    #print(result[0].get('id'))
    #print(result[0].get('name'))
    #print(result[0].get('description'))


heroes = helden()
lijst = setup_Api(heroes)
result = connect_Api(lijst)
#nameResult = nameCharacter(result)
#nameResult2 = exactNameCharacter(result)
randomHero = Selectrandomhero(result)

