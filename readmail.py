# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 02:33:26 2020

@author: SIDDHARTH RAJ DASH
"""

import imaplib
import email
from email.header import decode_header
import webbrowser
import os

def readmymail():
    # account credentials
    username = "siddhu.dash@gmail.com"
    password = "65477412"
    
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
    
    status, messages = imap.select("INBOX")
    # number of top emails to fetch
    N = 1
    # total number of emails
    messages = int(messages[0])
    
    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
    
                msg = email.message_from_bytes(response[1])
                
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                
                    subject = subject.decode()
                
                from_ = msg.get("From")
                print("Subject:", subject)
                print("From:", from_)
                
                if msg.is_multipart():
                    
                    for part in msg.walk():
                        
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                        
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(body)
                        elif "attachment" in content_disposition:
                            print("you have an an attachment which has been downloaded")
                            filename = part.get_filename()
                            if filename:
                                if not os.path.isdir(subject):
                                    os.mkdir(subject)
                                filepath = os.path.join(subject, filename)
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)
    imap.close()
    imap.logout()