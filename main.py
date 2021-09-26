from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from user_manager import UserManager
import os

email_api = os.getenv("EMAIL")
flight_api = os.getenv("TEQUILA")
flight_deal = os.getenv("DEAL")
flight_key = os.getenv("FLIGHT_KEY")
sheety_put = os.getenv("PUT")
sheety_get = os.getenv("GET")


users = UserManager(email_api)
sheet = DataManager(sheety_put, sheety_get)
searcher = FlightSearch(flight_api, flight_deal, flight_key, sheet.data, "LON", 2)
notif = NotificationManager(users.emails, sheet.old, searcher.data, searcher.info)
notif.send_mail()
sheet.put_data(searcher.data)
