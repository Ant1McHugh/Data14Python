from http_class import httpPractise

test_output = httpPractise()

def status_test():
    assert test_output.status() == 200


def address_test():
    assert "B38 8AG" in test_output.find_address()