import textwrap
from tabulate import tabulate


def display_page(page):
    """
    Display a page of tickets as a table
    :param page: a page of tickets
    :return:
    """

    # the table column headers
    column_headers = ["id", "status", "subject", "requester_id", "created_at"]

    # create an empty table
    table = []

    for ticket in page["tickets"]:  # add each ticket to the table
        row = []  # create an empty row
        for header in column_headers:  # add ticket properties to the row
            row.append(ticket[header])

        # add the row to the table
        table.append(row)

    # print the table
    print("\n", tabulate(table, column_headers), "\n")


def display_ticket_detail(ticket):
    """
    Display the details of a ticket
    :param ticket: the ticket to display
    :return:
    """

    print("\nTicket ID: ", ticket["id"])  # print id
    print("Status: ", ticket["status"])  # print status
    print("Priority: ", ticket["priority"], "\n")  # print priority
    print("Created by ", ticket["requester_id"], " at ", ticket["created_at"], "\n")  # print creator and time created
    print(ticket["subject"], "\n")  # print subject
    print(textwrap.fill(ticket["description"], 120, replace_whitespace=False), "\n")  # print body with 120 characters per line
