Feature: License information

  Scenario Outline: Verify authentication test with different credentials
    Given : user is logged in and navigates to Test Configuration
    When User enters valid "<username>" and "<password>"
    Then Success is seen with message "<expected_message>"

    Examples:
      | username | password   | expected_message |
      | nagesh   | Alpha122 | Authentication Status for user 'nagesh' using method Database:  Passed. |

      | admin    | password   | Skipping test, the admin user is always authenticated against the Uptime Data Store |

