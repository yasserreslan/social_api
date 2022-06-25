import requests
from ClientHelper import Client, Response

class Instagram:
    client = Client()

    def __init__(self,client_id, client_secret,redirect_uri) -> None:
        self.client_id =client_id
        self.client_secret =client_secret
        self.redirect_uri = redirect_uri
        

    def get_short_lived_token(self,code: str):
        # code is code from oauth url 

        data = {"client_id":self.client_id,
        "client_secret":self.client_secret,
        "grant_type":"authorization_code",
        "redirect_uri":self.redirect_uri,
        "code":code}


        resp = self.client.post("https://api.instagram.com",["oauth","access_token"],body= data)

        return resp #{token, user_id}/{error}

    def get_long_lived_token(self,code:str):
        short = self.get_short_lived_token(code=code)
        try:
            access_token = short.body["access_token"]
        except KeyError:
            return short


        params = {"grant_type": "ig_exchange_token",
        "client_secret":self.client_secret,
        "access_token":access_token}

        resp = self.client.get("https://graph.instagram.com",["access_token"],params=params)

        return resp

