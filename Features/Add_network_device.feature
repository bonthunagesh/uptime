Feature: Add System in Uptime Infrastructure Monitor

  Scenario: Add A local network device
    Given user is logged in and navigates to My Infrastructure
    When user clicks Add System and fills the necessary details
    Then the system is added successfully