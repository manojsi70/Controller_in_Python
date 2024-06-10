import pywhatkit

def send_whatsapp_message(phone_number, message, hour, minute):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    return "Success: WhatsApp message sent."
