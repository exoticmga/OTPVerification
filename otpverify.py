import random
import smtplib

def generate_otp():
  otp = ""
  for i in range(6):
    otp += str(random.randint(0, 9))
  return otp

def send_email(email, otp):
  smtp_server = "smtp.gmail.com"
  port = 587
  username = "mgamarketingagency1@gmail.com"
  password = "mhggers"

  msg = """
Subject: OTP Verification

Your OTP is: {}

Please enter this OTP to verify your account.
""".format(otp)

  server = smtplib.SMTP(smtp_server, port)
  server.starttls()
  server.login(username, password)
  server.sendmail(username, email, msg)
  server.quit()

if __name__ == "__main__":
  email = input("Enter your email address: ")
  otp = input("Enter the OTP you received: ")

  if otp == generate_otp():
    print("OTP verified successfully!")
  else:
    print("Invalid OTP.")
