import pytest
from menu import Menu

def test_add_valid_menu_item():
    menu_instance = Menu()
    result = menu_instance.add_menu_item("Cafe Mocha", "Coffee", "Great coffee.", 4.99)
    assert result == "Menu item added for Cafe Mocha."

def test_add_existing_menu_item():
    menu_instance = Menu()
    menu_instance.add_menu_item("Cafe Mocha", "Coffee", "Great coffee.", 4.99)
    result = menu_instance.add_menu_item("Cafe Mocha", "Coffee", "Great coffee.", 4.99)
    assert result == "Menu item already exists."