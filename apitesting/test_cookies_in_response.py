from playwright.sync_api import Playwright

# Cookies are maintained in separate files of browser, so context is required with method storage_state

def test_cookies_in_response(playwright:Playwright):
    request_context = playwright.request.new_context()
    response=request_context.get("https://www.google.com/")

    assert response.status == 200
    assert response.ok

    # Extract all cookies from response
    cookies = request_context.storage_state()["cookies"]

    for c in cookies:
        print(f"{c['name']},{c['value']},{c['domain']}")

    # check if "AEC" cookies exist
    aec_cookie=None
    for c in cookies:
        if c["name"] == "AEC":
            aec_cookie=c
            break
    assert aec_cookie is not None, "Cookie Not found"

    # Printing details of AEC cookie
    print(aec_cookie['name'])
    print(aec_cookie['value'])
    print(aec_cookie['domain'])
    print(aec_cookie['path'])
    print(aec_cookie['expires'])



