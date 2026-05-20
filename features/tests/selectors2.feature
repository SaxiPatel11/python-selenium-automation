Feature: Target Cart Verification

  Scenario: Verify empty cart message
    Given User opens Target homepage
    When User clicks on the cart icon
    Then "Your cart is empty" message should be displayed