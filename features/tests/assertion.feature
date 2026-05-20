Feature: Target Product Search

  Scenario Outline: Search for a product on Target
    Given User opens Target homepage
    When User searches for "<product>"
    Then Search results for "<product>" should be displayed

    Examples:
      | product   |
      | laptop    |
      | shoes     |
      | headphones|