import yagmail


def send_alert(error_location):
    yag = yagmail.SMTP("GMAIL ADDRESS", "GMAIL PASSWORD")
    yag.send("SEND ALTERS TO@MAIL.com", "Spag borked", "Whoops, error is: " + error_location)


