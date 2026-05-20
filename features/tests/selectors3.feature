Feature: Target Sign In Navigation

  Scenario: Verify logged out user can navigate to Sign In
    Given User opens Target homepage
    When User clicks on Sign In button
    And User clicks Sign In from right side navigation menu
    Then Sign In form should be displayed