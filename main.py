from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from user_manager import UserManager

email_api = "https://api.sheety.co/9df8366ff8b44646c21a815dc791aacc/copyOfFlightDeals/users"
flight_api = "https://tequila-api.kiwi.com/locations/query"
flight_deal = "https://tequila-api.kiwi.com/v2/search"
flight_key = "4NOXDq7RbWmtNWNz5G3mmUmyrnDOIJ0I"
sheety_put = "https://api.sheety.co/9df8366ff8b44646c21a815dc791aacc/copyOfFlightDeals/prices/"
sheety_get = "https://api.sheety.co/9df8366ff8b44646c21a815dc791aacc/copyOfFlightDeals/prices"


users = UserManager(email_api)
sheet = DataManager(sheety_put, sheety_get)
searcher = FlightSearch(flight_api, flight_deal, flight_key, sheet.data, "LON", 2)
notif = NotificationManager(users.emails, sheet.old, searcher.data, searcher.info)
notif.send_mail()
sheet.put_data(searcher.data)