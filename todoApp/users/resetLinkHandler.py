import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import url_for
from todoApp.users.views import users

class resetLink():

    @staticmethod
    def linkGenerator(receiverEmail, username,token):
        server=smtplib.SMTP('smtp.gmail.com',587)
        #adding TLS security 

        server.starttls()
        #get your app password of gmail 

        password='nmobgeeydmbaiurr'

        

        msg = MIMEMultipart()
        msg['From'] = 'd9762011436@gmail.com'   #write email id of sender
        msg['To'] = receiverEmail  #write email of receiver
        msg['Subject'] = 'Reset Link for'+ " " + username  #subject of email

        server.login(msg['From'], password)

        link = url_for('users.newPassword',email=receiverEmail, token=token, username=username,  _external=True )

        html = """<html>
                <head>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

                </head>
                <body>

                    <div style="font-family: Helvetica,Arial,sans-serif;min-width:700px;overflow:auto;line-height:2">
                    <div style="margin:20px auto;width:70%;padding:5px 0">
                        <div style="border-bottom:1px solid #eee">
                            <a href="" style="font-size:1.4em;color: #000000;text-decoration:none;font-weight:600">Todo App</a>
                        </div>
                            <p style="font-size:1.1em">Hi """+ username +""",</p>
                            <p> The Reset link for your account is """ + link + """<br>The Link is valid only for 2 minutes.</p>
                            <br>
                            <p style="font-size:0.9em;">Regards,<br />Deepak Prajapati</p>
                            <hr style="border:none;border-top:1px solid #eee" />
                        <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300" width="50px" height="50px">
                            <p>Todo App</p>
                            <p>India</p>
                        </div>
                        <br><br><br><br>
                        <div style="text-align:center;">
                            <p>The mail was issued by <a href="https://todo-app-deepspraj.herokuapp.com">https://todo-app-deepspraj.herokuapp.com</a>.<br><br><img src="https://img.icons8.com/cute-clipart/64/000000/india.png"/></p>
                        
                        </div>
                    </div>
                    </div>
                </body>
                </html>"""

        part1 = MIMEText(html, 'html')


        msg.attach(part1)


        #sending the email
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()