Feature: Login to OrangeHRM

  Scenario: Successful login with valid credentials
    Given I navigate to the OrangeHRM login page
    When I enter valid username and password
    And I click the login button
    Then I should see the dashboard page