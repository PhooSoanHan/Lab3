import price_info

def test_total_cost_shopping():
    # Capture total cost of shopping and expected value
    total_cost = price_info.total_cost_shopping()
    expected_total_cost = 46.75  # Replace with the correct total value based on your price_list and quantity_list
    assert total_cost == expected_total_cost

def test_cost_of_fruits():
    # Test cost of 10 apples
    result = price_info.cost_of_fruits('apple', 10)
    expected_cost = 12.00  # 10 * 1.20
    assert result == expected_cost
