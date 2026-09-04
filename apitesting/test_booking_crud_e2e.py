"""
1) Create Booking (POST) ---> booking id
2) Get Booking ID details (GET) - By ID, By Name, By Dates
3) Create Token (POST /auth)
4) Partial Update Booking (PATCH)
5) Full Update Booking (PUT)
6) Delete Booking (DELETE)
"""
import json

import pytest
from playwright.sync_api import Playwright

# Base URL
base_url = "https://restful-booker.herokuapp.com"

# Utility Function - reading json file
def read_json(file_path):
    file = open(file_path,"r")
    return json.load(file)

# Fixture: this fixture creates playwright request context
@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()

# 1) Create Booking (POST) ---> booking id
def test_create_booking(request_context):
    data=read_json("testdata/post_request_body.json")
    response=request_context.post(f"{base_url}/booking",data=data)
    assert response.ok, "POST request failed"
    assert response.status==200
    response_body = response.json()
    print("Create Booking Response:", response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking=response_body["booking"]

    assert booking["firstname"]== data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["totalprice"] == data["totalprice"]
    assert booking["depositpaid"] == data["depositpaid"]
    assert booking["bookingdates"]["checkin"]==data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]

    # we are making bookig_id as global to use it in other tests as variable in one test can't be used directly in another test
    global booking_id
    booking_id = response_body["bookingid"]
    global check_in
    check_in = booking["bookingdates"]["checkin"]
    global check_out
    check_out = booking["bookingdates"]["checkout"]



# 2) Get Booking ID details (GET) - By ID, By Name, By Dates

def test_get_booking_by_id(request_context):
    response=request_context.get(f"{base_url}/booking/{booking_id}") # https://restful-booker.herokuapp.com/booking/2634

    assert response.ok
    assert response.status==200

    response_body=response.json()
    print(f"Booking details fetched by ID {booking_id}:", response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body

def test_get_booking_by_name(request_context):
    names_params={"firstname":"Jim", "lastname":"Brown"}
    # passing query parameters
    response=request_context.get(f"{base_url}/booking/",params=names_params) # https://restful-booker.herokuapp.com/booking?firstname=MLS&lastname=Ganesh

    assert response.ok
    assert response.status==200

    response_body=response.json()
    print(f"Booking IDs fetched by names {names_params}:", response_body)
    assert len(response_body) > 0

    for item in response_body:
        assert "bookingid" in item


def test_get_booking_by_dates(request_context):
    date_params={"checkin": "2025-12-15", "checkout":"2025-12-20"}

    # passing query parameters
    # https://restful-booker.herokuapp.com/booking?checkin=2014-03-13&checkout=2014-05-21
    response=request_context.get(f"{base_url}/booking/",params=date_params)

    assert response.ok
    assert response.status==200

    response_body=response.json()
    print(f"Booking IDs fetched by Dates {date_params}:", response_body)
    assert len(response_body) >= 0

    for item in response_body:
        assert "bookingid" in item

# 3. Create token (POST/auth)

def test_create_token(request_context):
    data=read_json("testdata/token_request_body.json")
    response=request_context.post(f"{base_url}/auth",data=data)

    assert response.ok
    assert response.status == 200

    response_body=response.json()
    print("Token creation response: ",response_body)

    assert "token" in response_body
    global token

    token=response_body["token"]
    assert len(token)>5

# 4. Partial update booking (PATCH)
def test_partial_update_booking(request_context):
    data=read_json("testdata/patch_request_body.json")
    response=request_context.patch(f"{base_url}/booking/{booking_id}",data=data,headers={"Cookie":f"token={token}"})

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print("Partial update response for booking id {booking_id}:", response_body)

    for key in data.keys():
        assert key in response_body
        assert response_body[key]==data[key]

# 5) Full update booking (PUT)
def test_full_update_booking(request_context):
    data=read_json("testdata/put_request_body.json")
    response=request_context.patch(f"{base_url}/booking/{booking_id}",data=data,headers={"Cookie":f"token={token}"})

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print("Full update response for booking id {booking_id}:", response_body)

    for key in data.keys():
        assert key in response_body
        assert response_body[key]==data[key]

    assert response_body["firstname"]==data["firstname"]
    assert response_body["lastname"] == data["lastname"]
    assert response_body["totalprice"] == data["totalprice"]

# 6) Delete Booking (DELETE)
def test_delete_booking(request_context):
    response=request_context.delete(f"{base_url}/booking/{booking_id}",headers={"Cookie":f"token={token}"})

    assert response.status == 201
    print("Booking deleted Successfully for ID", booking_id)




