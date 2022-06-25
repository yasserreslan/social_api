import requests
from ClientHelper import Response, Client

c =  Client()

# cr = c.get(url = "https://graph.instagram.com",slash_elements=['v13.0',17841453319434075],fields = 'id,username,media_count',access_token ="IGQVJWZAVdOXzdiUlctaW1pdnNJanMzeTVZAYUFKc2RoVG56b0tWVDg2VkR1WGhjSWJqanlyTHdGUDhSUjAzTkVjblB1S2pDdVpHaEdXZAE82ODhSU25wNWpGNGhhRXFBNERRaEgycndB")

par = {'fields' : 'id,username,media_count',
'access_token' :"IGQVJWZAVdOXzdiUlctaW1pdnNJanMzeTVZAYUFKc2RoVG56b0tWVDg2VkR1WGhjSWJqanlyTHdGUDhSUjAzTkVjblB1S2pDdVpHaEdXZAE82ODhSU25wNWpGNGhhRXFBNERRaEgycndB"}

# cp = c.get(url = "https://graph.instagram.com",slash_elements=['v13.0',17841453319434075], params= par)

# print(cp.response())

# cp2 = c.post(url="https://httpbin.org", slash_elements=["post"])



