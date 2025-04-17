Feature: Login Scenario


  @Valid
  Scenario: Verify that user is able to login to the appl with Valid {username} and {password}

    Given : User is on the Login page
    When : user enters username and password
    And : Clicks on Login Button
    Then : user should be able to Log in to the application




