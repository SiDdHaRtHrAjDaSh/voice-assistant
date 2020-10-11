from twilio.rest import Client

account_sid = 'ACc1669714d56720604633d46a1b99e30a'
auth_token = 'c2a01cb94d2204f8b789488ffb8f29db'

def whatsappmsg(message,phno):
    phno="whatsapp:"+phno
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                                  body=message,
                                  from_='whatsapp:+14155238886',
                                  to=phno
                              )
    
    print(message.sid)