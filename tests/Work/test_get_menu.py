import pytest
from menu import Menu

def test_get_existing_menu():
    menu_instance = Menu()
    menu_instance.add_menu_item("Cafe Mocha", "Coffee", "Great coffee.", 4.99)
    result = menu_instance.get_menu("Cafe Mocha")
    assert result == {"Coffee": {"description": "Great coffee.", "price": 4.99}}

def test_get_non_existing_menu():
    menu_instance = Menu()
    result = menu_instance.get_menu("Cafe Mocha")
    assert result == "Menu not found for Cafe Mocha."