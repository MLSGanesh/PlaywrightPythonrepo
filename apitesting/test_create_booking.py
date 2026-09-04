# -----------------------------------
# Test: Create Booking (POST request with static body)
# Request type: POST
# Data: hard coded data inside the test
# -----------------------------------
from playwright.sync_api import Playwright


def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()

    request_body = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 1001,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-01-01",
            "checkout" : "2026-08-01"
        },
    "additionalneeds" : "Dinner"
    }

    response = request_context.post(f"{base_url}/booking",data=request_body)

    # validations
    assert response.ok
    assert response.status==200

    response_body = response.json()
    print("Response Body==",response_body)

    # field/attribute validations
    assert "bookingid" in response_body
    assert "booking" in response_body

    # data validation
    booking = response_body["booking"]
    assert booking["firstname"]=="Jim"
    assert booking["lastname"]=="Brown"
    assert booking["totalprice"]==1001
    assert booking["depositpaid"] is True
    assert booking["additionalneeds"]=="Dinner"

    # nested json validation
    assert booking["bookingdates"]["checkin"]== "2026-01-01"
    assert booking["bookingdates"]["checkout"] == "2026-08-01"

    # close the API context
    request_context.dispose()





