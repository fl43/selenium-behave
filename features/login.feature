Feature: Test the Salesforce login

Scenario: Login to Salesforce
  Given I go to the Salesforce login page
  Then the title should be "Login | Salesforce"
  When I enter my credentials
  When I click login
  Then I should see the home page
