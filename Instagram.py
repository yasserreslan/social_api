import requests
from ClientHelper import Client, Response
from Instagram_utils_ import all_fields_url, all_fields_value,User_fields
class Instagram:
    client = Client()

    def __init__(self,client_id, client_secret,redirect_uri,v) -> None:
        self.client_id =client_id
        self.client_secret =client_secret
        self.redirect_uri = redirect_uri
        self.v = v
        

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

    def get_basic_info(self,id,token):
        params = {"fields":all_fields_url(User_fields),
        "access_token":token}
        
        resp = self.client.get("https://graph.instagram.com",[self.v,id],params= params)

        return resp.body
    
    def get_user_media(self,id,token):
        params = {"access_token":token}
        resp = self.client.get("https://graph.instagram.com/",[self.v,id,"media"],params)
        return resp.body
