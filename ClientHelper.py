import json
import requests

class Client:


    def get(self,url = "",slash_elements = [],params = {},**kwargs):
        if url == "":
            raise InvalidRequestUrl("Invalid request URL passed to GET request")

        # adding paths to url

        for elem in slash_elements:
            url += "/" + str(elem)
        
        # default get request params
        
        if params != {}:
            req = requests.get(url=url, params= params)

            return Response(status_code= req.status_code, body= req.json())


        # adding query parameters

        query_count = 1
        for key, value in kwargs.items():
            if query_count == 1:
                url += '?' + key + '=' + value
                query_count += 1
                continue
            url += "&" + key + "=" + value
            
        req = requests.get(url=url)

        
        return Response(status_code= req.status_code, body= req.json())
        
    def post(self,url = "",slash_elements = [], body:dict = {}):
        if url == "":
            raise InvalidRequestUrl("Invalid request URL passed to GET request")

        # adding paths to url

        for elem in slash_elements:
            url += "/" + str(elem)

        req = requests.post(url= url, data= body)

        return Response(status_code=req.status_code, body=req.json())
        
        


class Response:
    
    def __init__(self,body:dict = {},status_code = ''):

        if status_code == '':
            raise InvalidResponseParameters("Missing response parameter: status_code"  )

        if status_code == {}:
            raise InvalidResponseParameters("Missing response parameter: body")

        self.status_code = status_code
        self.body = body

    def response(self):
        response = {}
        response['status_code'] = self.status_code
        response['body'] = self.body

        return response

    def __repr__(self) -> str:
        return str(self.response())

    





class InvalidRequestUrl(Exception):
    pass
class InvalidParameterType(Exception):
    pass
class InvalidResponseParameters(Exception):
    pass

