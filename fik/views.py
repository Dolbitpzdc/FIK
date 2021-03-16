from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def home(request):
    if request.method == 'POST':
        if request.POST.get("call") == "on":
            type = 'звонок'

        elif request.POST.get("message") == "on":
            type = 'Ответить на emal'

        else:
            type = 'без разницы'

        mail_content = "Имя: " + request.POST.get("service-name") + "\nEmail: " + request.POST.get("service-email") + "\nНомер телефона: " + request.POST.get("service-telephone") + "\nВид ответа (звонок\почтa): " + type


        sender_address = 'fikmarket2021@gmail.com'
        sender_pass = 'zidgaP-suffy7-humkyn'

        receiver_address = 'biwuxqpolp33.org@gmail.com'


        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Message for FIKmarket'


        message.attach(MIMEText(mail_content, 'plain'))


        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

        return render(request, 'home.html')

    else:
        return render(request, 'home.html')
