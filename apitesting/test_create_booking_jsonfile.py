# -----------------------------------
# Test: Create Booking (POST request with static body)
# Request type: POST
# Data: External json file
# -----------------------------------
import json

from playwright.sync_api import Playwright
from pathlib import Path


def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()

    # Load data from external json file
    file = open("testdata/post_request_body.json","r")
    request_body = json.load(file)

    response = request_context.post(f"{base_url}/booking",data=request_body)

    # validations
    assert response.ok
    assert response.status==200

    response_body = response.json()
    print("Response Body==",response_body)

    # field/attribute validations
    assert "bookingid" in response_body
    assert "booking" in response_body
    id = response_body["bookingid"]
    print(id)

    # data validation
    booking = response_body["booking"]
    assert booking["firstname"]=="MLS"
    assert booking["lastname"]=="Ganesh"
    assert booking["totalprice"]==2026
    assert booking["depositpaid"] is True
    assert booking["additionalneeds"]=="Lunch"

    # nested json validation
    assert booking["bookingdates"]["checkin"]== "2026-01-04"
    assert booking["bookingdates"]["checkout"] == "2026-08-05"

    # close the API context
    request_context.dispose()





