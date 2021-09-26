import smtplib


class NotificationManager:
    def __init__(self, sender_mails, old_data, new_data, info):
        self.mails = sender_mails
        self.sheet = old_data
        self.flight = new_data
        self.info = info

    def message_formatter(self):
        msg = "Subject:low price\n\n"
        for i in range(len(self.sheet)):
            if self.sheet[i]["lowestPrice"] > self.flight[i]["lowestPrice"]:
                b = self.info[i]
                q = [b["fly_from"], b["city_from"], b["flyto"], b["cityto"], b["arrival"], self.flight[i]["lowestPrice"]]
                msg += f"from {q[0]} in {q[1]} to {q[2]} in {q[3]}\narrival at {q[4]} with price {q[5]}\n\n"
        return msg

        
                
    def send_mail(self):
        msg = self.message_formatter()
        if msg != "Subject:low price\n\n":
            print("hello")
            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                connection.login("emailfortestinginpython@gmail.com", "saminisnewongmail")
                for email in self.mails:
                    try:
                        connection.sendmail("emailfortestinginpython@gmail.com", email, msg)
                    except Exception:
                        pass
        return
    

