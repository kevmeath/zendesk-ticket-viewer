import requests


def parse_error(response):
    """
    Print an error message appropriate for the type of error
    :param response: the response returned by a http request
    :return:
    """

    if 400 <= response.status_code < 500:  # if the response code is in the 400 range
        error = response.json()["error"]
        print("Error")

        if type(error) is dict:
            print(error["title"])
            print(error["message"])
        else:
            print(error)

    elif 500 <= response.status_code < 600:  # if the response code is in the 500 range
        print("Request failed, try again")
    else:  # if the response code is in any other range the error is unknown
        print("Unknown error")


class TicketAPI:
    def __init__(self, subdomain, email, password, token=False):  # set domain and authentication
        self.domain = "https://{subdomain}.zendesk.com".format(subdomain=subdomain)
        email = email if not token else email + "/token"
        password = password
        self.auth = (email, password)

    def get_ticket(self, ticket_id):
        """
        Get a ticket
        :param ticket_id: id of the ticket to get
        :return: the ticket
        """

        # ticket api endpoint
        url = self.domain + "/api/v2/tickets/{id}.json".format(id=ticket_id)

        # get the ticket
        ticket = self.get(url)
        return ticket

    def get_ticket_page(self, page_num, page_size=25):
        """
        Get a page of tickets given a page number and size
        :param page_num: number of the page to get
        :param page_size: the number of tickets per page
        :return: page of tickets
        """

        # ticket list api endpoint
        url = self.domain + "/api/v2/tickets.json" \
                            "?page={page_num}" \
                            "&per_page={page_size}" \
                            "&sort_by=created_at" \
                            "&sort_order=desc".format(page_num=page_num, page_size=page_size)

        # get the page
        page = self.get(url)
        return page

    def get(self, url):
        """
        Make a GET request
        :param url: URL to send the request to
        :return: json if successful, otherwise None
        """

        # get the response
        response = requests.get(url, auth=self.auth)
        if 200 <= response.status_code < 300:  # if the response is ok return the json
            return response.json()
        else:  # if the response is not ok print an appropriate error message then return None
            parse_error(response)
            return None

    def create_ticket(self, ticket):
        """
        Create a ticket
        :param ticket: the ticket to create
        :return:
        """

        # the ticket creation api endpoint
        url = self.domain + "/api/v2/tickets.json"

        # get the response
        response = requests.post(url, json=ticket, auth=self.auth)
        if 200 <= response.status_code < 300:  # if response is ok inform the user that the ticket was created
            print("\nTicket created\n")
        else:  # if the response is not ok print an appropriate error message
            parse_error(response)
