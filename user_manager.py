import requests

class UserManager:
    def __init__(self, API):
        self.api = API
        self.emails = self.get_users()

    def get_users(self):
        response = requests.get(self.api)
        try:
            response.raise_for_status()
        except:
            raise "user api not working"
        data = response.json()["users"]
        data = [k["email"] for k in data]
        return data
