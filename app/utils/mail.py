from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

EMAIL_TX = "input_your_email"
PASSW_TX = "input_your_pw"
SMTP = ("input_email_smtp_server", 587)


def gen_mail_body(povis_id, item_name, item_remain, rnd_name, roulette_time):
    return f" {povis_id}님께,\n\n" \
           f" 안녕하세요. 사이버이공계학생교류전 준비위원회입니다.\n" \
           f" {item_name} 당첨을 축하드립니다!\n" \
           f" {povis_id}님께서는 {rnd_name} {roulette_time}에 {item_name}에 당첨되었으며, 현재 잔여 수량은 {item_remain}개 입니다. \n" \
           f" 다시 한번 당첨을 축하드리며, 수령 방법 등의 안내는 사이버이공계학생교류전 준비위원회 홍보팀장 박재완(andrew1208@postech.ac.kr)님께서 안내할 예정입니다. \n" \
           f" 사이버이공계학생교류전에 관심을 가져주셔서 감사합니다. \n" \
           f" 혹시, 본인이 행사에 참여한 것이 아닌데 본 메일을 받으셨을 경우에는 홍보팀장에게 문의해주세요. \n" \
           f" 축하드립니다. \n\n" \
           f" 사이버이공계학생교류전 준비위원회 올림."


def send_roulette_result(povis_id: str, item_name: str, item_remain: int, rnd_name: str, roulette_time: str):
    TEST_PARTICIPANTS = ["mzg00@postech.ac.kr", f"{povis_id}@postech.ac.kr"]

    smtp = smtplib.SMTP(*SMTP)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    try:
        smtp.login(EMAIL_TX, PASSW_TX)
    except smtplib.SMTPAuthenticationError:
        sys.stderr.write("Login Failed....")
        return False

    msg = MIMEMultipart()
    msg["Subject"] = "[2020 포카전 룰렛] 당첨 안내"

    msg.attach(MIMEText(gen_mail_body(povis_id, item_name, item_remain, rnd_name, roulette_time)))
    for i in TEST_PARTICIPANTS:
        msg["To"] = i
        smtp.sendmail(EMAIL_TX, i, msg.as_string())

    smtp.quit()
    return True
