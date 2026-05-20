Feature: Add Product to Cart

  Scenario: Add a product to cart and verify it is added
    Given User opens Target homepage
    When User searches for "laptop"
    And User selects the first product
    And User adds the product to cart
    Then Cart should contain at least 1 item