Feature: Test API Response

  Scenario: API should return expected greeting
    Given the API is running
    When I send a request to "http://192.168.0.131:8083/"
    Then the response should be "Hello from Spring"
