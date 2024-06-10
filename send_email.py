import smtplib

def send_bulk_email():
    recipients = ["akshatkhandelwal28@gmail.com", "parthjain.pro.2045@gmail.com"]
    for dest in recipients:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("kashifauddeen7@gmail.com", "your_email_password")
        message = "Hi, this is a bulk email."
        s.sendmail("manoj43898@gmail.com", dest, message)
        s.quit()
    return "Success: Sent bulk email."
