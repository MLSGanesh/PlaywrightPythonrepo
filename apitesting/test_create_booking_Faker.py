# -----------------------------------
# Test: Create Booking (POST request with static body)
# Request type: POST
# Data: Faker dynamic data
# -----------------------------------
from faker import Faker
from playwright.sync_api import Playwright
from datetime import datetime, timedelta


def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context=playwright.request.new_context()

    faker = Faker()

    first_name = faker.first_name()
    last_name = faker.last_name()
    total_price = faker.random_int(min=1000, max=3000)
    deposit_paid = faker.boolean()
    checkin_date = datetime.now().strftime("%Y-%m-%d")
    checkout_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
    additional_needs = faker.word()

    request_body = {
        "firstname" : first_name,
        "lastname" : last_name,
        "totalprice" : total_price,
        "depositpaid" : deposit_paid,
        "bookingdates" : {
            "checkin" : checkin_date,
            "checkout" : checkout_date
        },
    "additionalneeds" : additional_needs
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
    assert booking["firstname"]== first_name
    assert booking["lastname"]== last_name
    assert booking["totalprice"]== total_price
    assert booking["depositpaid"] is deposit_paid
    assert booking["additionalneeds"]== additional_needs

    # nested json validation
    assert booking["bookingdates"]["checkin"]== checkin_date
    assert booking["bookingdates"]["checkout"] == checkout_date

    # close the API context
    request_context.dispose()





