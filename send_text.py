import twilio

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC85b4505a4663f7e7caf09b462738dc65"
# Your Auth Token from twilio.com/console
auth_token  = "6b7e0e0ee5a8652d06e10f52b1a195c9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+212606639978", 
    from_="+12026013811",
    body="Hello from Python!")

print(message.sid)
