from django.core.mail import EmailMessage


sender = "storeroom@company.biz"
recipients = [
    "supervisor@company.biz",
]
copy = ["tech@company.biz", "manager@company.biz"]


def reminder_email(sender, recipients, copy):
    reminder = EmailMessage(
        subject="Inventory Reminder",
        body="Weekly inventory is due NLT 0600 on Monday.",
        from_email=sender,
        to=recipients,
        cc=copy,
    )
    reminder.send()


if __name__ == "__main__":
    reminder_email(sender, recipients, copy)
