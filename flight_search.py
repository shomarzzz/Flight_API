import requests
import datetime
now = datetime.datetime.now()
nowe = now.strftime(r"%d/%m/%Y")
ahead = now + datetime.timedelta(days=60)
ahead = ahead.strftime(r"%d/%m/%Y")
print(nowe, ahead)
class FlightSearch:
    def __init__(self, get_url, search_url, key, data, country, stopover, currency):
        self.curr = currency
        self.get = get_url
        self.dealer = search_url
        self.headers = {"apikey": key}
        self.data = data
        self.info = []
        self.con = country
        self.stopover = stopover
        self.deal()

    def getcode(self, data):
        param = {"limit": 10}
        for i in range(len(data)):
            print(data[i])
            param["term"] = data[i]["city"]
            response = requests.get(url=self.get, params=param, headers=self.headers)
            response.raise_for_status()
            data[i]["iataCode"] = response.json()["locations"][0]["code"]
        self.data = data

    def deal(self):
        for i in range(len(self.data)):
            param = {
                "fly_from": self.con,
                "fly_to": self.data[i]["iataCode"],
                "dateFrom": nowe,
                "dateTo": ahead,
                "limit": 50,
                "curr": self.curr,
                "max_stopovers": self.stopover
            }
            print(self.headers)
            print(self.dealer)
            response = requests.get(url=self.dealer, params=param, headers=self.headers)
            response.raise_for_status()
            # print(response.json())
            try:
                data = response.json()["data"][0]
            except IndexError:
                self.data[i]["lowestPrice"] = 9999
                continue
            self.info.append({"fly_from":data["flyFrom"],
                              "city_from":data["cityFrom"],
                              "flyto":data["flyTo"],
                              "cityto":data["cityTo"],
                              "arrival":data["route"][0]["local_arrival"],
                              })
            money = data["price"]
            self.data[i]["lowestPrice"] = money
            
