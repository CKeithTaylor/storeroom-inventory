from django.core.mail import EmailMessage
import sqlite3
from sqlite3 import Error
import pandas as pd


sender = "storeroom@company.biz"
recipients = [
    "supervisor@company.biz",
]
copy = ["tech@company.biz", "manager@company.biz"]


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn


def supply_order():
    database = "db.sqlite3"
    conn = create_connection(database)
    df = pd.read_sql(
        "SELECT * FROM inventory_inventory WHERE (reorder >= in_stock)", conn
    )
    df = df.reindex(
        columns=[
            "part",
            "description",
            "location",
            "vendor",
            "in_stock",
            "max_stock",
            "reorder",
            "reorder_amt",
            "inv_date",
        ]
    )
    header = {
        "part": "Part Number",
        "vendor": "Vendor",
        "in_stock": "On Hand",
        "max_stock": "Max Stock",
        "reorder": "Reorder Point",
        "location": "Location",
        "reorder_amt": "Reorder Amount",
        "description": "Description",
        "inv_date": "Inventory Date",
    }
    df.rename(columns=header, inplace=True)

    with pd.ExcelWriter(
        "templates/static/data/order.xlsx", engine="xlsxwriter"
    ) as writer:
        df.to_excel(writer, sheet_name="ORDER", index=False, na_rep="NaN")
        wrap_text = writer.book.add_format({"text_wrap": True})
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets["ORDER"].set_column(
                col_idx, col_idx, (column_width + 2), wrap_text
            )


def order_list_email(sender, recipients, copy):
    supply_order()
    order_email = EmailMessage(
        subject="Weekly DSO Item Order List",
        body=f"Attached is the list of DSO parts that are at or below the reorder level.",
        from_email=sender,
        to=recipients,
        cc=copy,
    )
    order_email.attach_file("templates/static/data/order.xlsx")
    order_email.send()


if __name__ == "__main__":
    order_list_email(sender, recipients, copy)
