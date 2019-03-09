import requests


class ConfigRequest:
    def get_method(self,host,params):
        content = requests.get(host,params=params)
        return content

    def post_method(self,host,data,headers):
        content = requests.post(host,data=data,headers=headers)
        return content