# schema is nothing but metadata, that stores the type of detail columns should store in a table
'''
pre-requisites
    pip install jsonschema
'''
from jsonschema import validate, ValidationError
from playwright.sync_api import Playwright

# Helper function to validate schema
def validate_json_schema(response_json,myschema):
    try:
        validate(instance=response_json,schema=myschema)
        print("Schema validation successfull")
        return True
    except ValidationError as e:
        print("Schema validation failed")
        return False



def test_json_validation_schema(playwright:Playwright):
    request_context = playwright.request.new_context()
    response=request_context.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status
    assert response.status_text=="OK"

    response_body=response.json()

    print(response_body)

    # schema generated from tool "https://transform.tools/json-to-json-schema"
    # here schema is hard coded where as schema detail can be called through files as per the BRD detail in projects
    schema={
      "type": "object",
        "properties": {
        "userId": {
        "type": "number"
      },
        "id": {
      "type": "number"
        },
    "title": {
      "type": "string"
        },
    "body": {
      "type": "string"
        }
        },
    "required": [
    "userId",
    "id",
    "title",
    "body"
        ]
    }

    is_valid=validate_json_schema(response_body,schema)
    assert  is_valid

    request_context.dispose()