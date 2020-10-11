from twilio.rest import Client

account_sid = 'ACc1669714d56720604633d46a1b99e30a'
auth_token = 'c2a01cb94d2204f8b789488ffb8f29db'
def send_sms(message,phno):
    client = Client(account_sid, auth_token) 
     
    message = client.messages.create( 
                                  from_='+15206368169',  
                                  body=message,
                                  to=phno
                              ) 
     
    print(message.sid)