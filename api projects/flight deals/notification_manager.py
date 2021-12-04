from twilio.rest import Client
from keys import twilio_sid, twilio_auth_tokens, twilio_virtual_number, twilio_verified_number


TWILIO_SID = twilio_sid
TWILIO_AUTH_TOKENS = twilio_auth_tokens
TWILIO_VIRTUAL_NUMBER = twilio_virtual_number
TWILIO_VERIFIED_NUMBER = twilio_verified_number


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKENS)

    def send_sms(self, message):
        message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)