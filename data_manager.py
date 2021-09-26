import requests


class DataManager:
    def __init__(self, put_url, get_url):
        self.put = put_url
        self.get = get_url
        self.data = {}
        self.old = self.get_data()

    def get_data(self):
        response = requests.get(self.get)
        response.raise_for_status()
        self.data = response.json()["prices"]
        return response.json()["prices"]

    def put_data(self, data):
        for i in data:
            send = {
                "price": i
            }
            print(send)
            response = requests.put(url=self.put+str(i["id"]), json=send)
            try:
                response.raise_for_status()
            except:
                pass


