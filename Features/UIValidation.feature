Feature: UI Validation

  @skip
  Scenario: Verify that all the Tabs are present in the application

    Given : user is logged into the Application
    When : user click on the Dashboards
    Then : Dashbaords page open
    When : user click on My_portal
    Then : My_portal page opens
    When : User clicks on Infrastructure
    Then : Infrastructure page opens
    When : User click on Services Tab
    Then : Services page  open
    When : User clicks on Reports tab
    Then : Reports page opens
    When : User clicks on Config tab
    Then : Config page open
    When : user click on Syslist Tab
    Then : Syslist page opens