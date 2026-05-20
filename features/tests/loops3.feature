Feature: Search Results Validation

  Scenario: Verify each product has name and image on search results page
    Given User opens Target homepage
    When User searches for "shoes"
    Then Each product should have a name and an image
