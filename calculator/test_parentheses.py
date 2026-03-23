#!/usr/bin/env python3
"""Test parentheses support in calculator."""

from pkg.calculator import Calculator

def test_parentheses():
    calc = Calculator()
    
    # Test that parentheses are handled correctly
    # (2 + 3) * 4 should be 20, not 14
    result = calc.evaluate("( 2 + 3 ) * 4")
    assert result == 20, f"Expected 20, got {result}"
    
    # Nested parentheses
    result = calc.evaluate("( ( 2 + 3 ) * 4 ) - 5")
    assert result == 15, f"Expected 15, got {result}"
    
    print("All parentheses tests passed!")

if __name__ == "__main__":
    test_parentheses()
