import threading
import datetime as dt
import time
import smtplib
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class emailthread(threading.Thread):
    def __init__(self,timestamp,time1,user,y,z,hname1,vname1):
        threading.Thread.__init__(self)
        self.timestamp=timestamp
        self.time1=time1
        self.user=user
        self.y=y
        self.z=z
        self.hname1=hname1
        self.vname1=vname1


    def run(self):
    
        try:

           
            #time.sleep(self.timestamp-self.time1)
            v=self.timestamp
            i=0
            while(v>=time.time()):
                # print(i)
                i+=1
              

            fromaddr = "teproject69@gmail.com"
            toaddr = self.user
            
            # instance of MIMEMultipart
            msg = MIMEMultipart()
            
            # storing the senders email address  
            msg['From'] = fromaddr
            
            # storing the receivers email address 
            msg['To'] = toaddr
            
            # storing the subject 
            msg['Subject'] = "Vaccine Reminder"
            
            # string to store the body of the mail
            body = "This is a reminder of your vaccine "+ self.vname1+ " in "+ self.hname1 + " on: "+self.y+" at: "+self.z
            
            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))
            
            # open the file to be sent 
            
            
            # attach the instance 'p' to instance 'msg'
            
            
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            
            # start TLS for security
            s.starttls()
            
            # Authentication
            s.login(fromaddr, "te123456")
            
            # Converts the Multipart msg into a string
            text = msg.as_string()
            
            # sending the mail
            s.sendmail(fromaddr, toaddr, text)
            
            # terminating the session
            s.quit()
                            

        except Exception as w:
            print("Can't send email",w)


            