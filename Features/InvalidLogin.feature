    @Negative
    Scenario: Verify that user is unable to login with Invalid username and password

    Given : User is on the Login page
    When : user enters invalid_username and invalid_password
    And : Clicks on Login Button
    Then : user should not be able to Log in to the application