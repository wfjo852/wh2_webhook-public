# -*- coding:utf-8 -*-

import smtplib

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import io
import os




def mail_send(mail_token,
              to,
              sub_text,
              msg_text="",
              html_return="",
              file_return=""):

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()  # say Hello
    mail_server.starttls()  # TLS 사용시 필요
    mail_server.login(mail_token[0],mail_token[1])

    # # 기본 메일 주소
    msg = MIMEBase('multipart','mixed')
    msg['Subject'] = sub_text
    msg['To'] = to


    #메시지
    if msg_text != "":
        text = MIMEText(msg_text)
        msg.attach(text)

    #불러온 HTML 파일 임포트
    if html_return != "":
        msg.attach(html_return)


    #미리 불러온 첨부파일 임포트
    if file_return !="":
        msg.attach(file_return)


    mail_server.sendmail(mail_token[0], to, msg.as_string())

    mail_server.quit()


def html(html_path):

    #html_메시지
    with io.open(html_path, 'r') as f:
        html_tmp = f.read()

    cont = MIMEText(html_tmp,'html','utf-8')
    return cont

def html_text(html_text):
    cont = MIMEText(html_text,'html','utf-8')
    return cont

def file(file_path):
    # 첨부파일 경로/이름 지정하기
    filename = os.path.split(file_path)[1]
    attachment = open(file_path, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    return part

