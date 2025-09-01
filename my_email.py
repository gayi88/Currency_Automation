import smtplib
from email.mime.text import MIMEText
from logger_config import setup_logger

logger = setup_logger("EmailLogger")

def send_email(rate):
    if rate is None:
        logger.error("No rate to send. Email not sent.")
        return
    try:
        sender = "gayathri.basarahalli@gmail.com"
        receiver = "vrameshreddy.63@gmail.com"
        password = "owzu yhpb ppap uodu"  # Use App Password (for Gmail/Outlook)

        subject = "Daily EUR→SEK Exchange Rate"
        body = f"Today's EUR→SEK rate is: {rate}"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())

        logger.info("Email sent successfully.")
    except Exception as e:
        logger.error(f"Error sending email: {e}")
