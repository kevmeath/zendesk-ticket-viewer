import unittest
import ticket_api

email = ""
password = ""
subdomain = ""
api = ticket_api.TicketAPI(subdomain, email, password, token=True)


def get_last_ticket_id():
    """
    Get the id of the newest ticket
    :return:
    """

    page = api.get(api.domain + "/api/v2/tickets.json?page=1&per_page=1&sort_by=created_at&sort_order=desc")
    last_ticket = page["tickets"][0]
    last_id = last_ticket["id"]
    return last_id


class TestTicketAPI(unittest.TestCase):
    def test_get_ticket(self):
        """
        Test the get_ticket function
        :return:
        """

        ticket = api.get_ticket(1)
        ticket_id = ticket["ticket"]["id"]

        # the ticket returned should be the ticket with the id requested
        self.assertEqual(ticket_id, 1)

        # if an invalid id is given the ticket returned should be None
        self.assertIsNone(api.get_ticket(-1))

    def test_get_ticket_page(self):
        """
        Test the get_ticket_page function
        :return:
        """

        page = api.get_ticket_page(1)

        # if a page was returned, the json will have next_page and previous_page keys
        self.assertIn("next_page", page)
        self.assertIn("previous_page", page)

    def test_create_ticket(self):
        """
        Test the create_ticket function
        :return:
        """

        last_id = get_last_ticket_id()
        new_ticket = {
            "ticket": {
                "subject": "test subject",
                "description": "test description"
            }
        }
        api.create_ticket(new_ticket)

        # the id of the newly created ticket should be equal to the last ticket's id + 1
        self.assertEqual(get_last_ticket_id(), last_id + 1)


if __name__ == "__main__":
    unittest.main()
