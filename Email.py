"""
File: Email.py
Author: Rob Udechukwu (robinsou@netapp.com)

Description:
Simple Email script to send an alert
"""

import smtplib
import os

class Email:

    def __init__(self, server=None, from_email=None):
        if not server:
            server = "smtp.corp.netapp.com"
        self.server = server

        if not from_email:
            from_email = "boost@netapp.com"
        self.from_email = from_email

    def send_alert(self, to=None, subject=None, summary=""):
        """
        :param to: Email to
        :param subject: Email subject
        :param summary: Email summary
        """
        script_location = os.path.realpath(__file__)
        my_host = os.uname()[1]

        summary += "\nThis was ran from {} on {}".format(script_location, my_host)
        # Send an email out
        if not to:
            to = ["vishit@netapp.com"]  # must be a list

        if not subject:
            subject = "Error/Exceptions/Warnings detected on {}".format(my_host)

        content = summary

        # Prepare actual message
        message = "From: {}\n".format(self.from_email)
        message += "To: {}\n".format(", ".join(to))
        message += "Subject: {}\n".format(subject)
        message += "\n\n{}".format(content)

        # Send the mail

        server = smtplib.SMTP(self.server)
        server.sendmail(self.from_email, to, message)
        server.quit()
