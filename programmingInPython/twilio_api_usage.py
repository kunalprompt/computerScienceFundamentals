from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+XXXXXXXXXXX", 
    from_="+XXXXXXXXXXX", 
    body="Hi! Welcome to Twilio."
)
