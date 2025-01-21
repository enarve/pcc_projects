from python_repos import make_request

def test_request_status_code():
    """Is response status code good?"""
    make_request()
    status_code = make_request()[1]
    assert status_code == 200
