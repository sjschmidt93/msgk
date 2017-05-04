from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb89307719aa8043871f9912452ef21c6"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12178202901", 
    from_="+2175763259",
    body="Hello from Python!")

print(message.sid)

