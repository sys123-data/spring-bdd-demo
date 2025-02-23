import requests
from behave import given, when, then

@given("the API is running")
def step_api_running(context):
    pass  # Assume API is running

@when('I send a request to "{url}"')
def step_send_request(context, url):
    context.response = requests.get(url)

@then('the response should be "{expected_response}"')
def step_check_response(context, expected_response):
    assert context.response.text.strip() == expected_response, \
        f"Expected '{expected_response}', but got '{context.response.text.strip()}'"
