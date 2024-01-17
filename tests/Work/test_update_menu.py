import pytest
from menu import Menu

def test_update_existing_menu_item():
    menu_instance = Menu()
    menu_instance.add_menu_item("Cafe Mocha", "Coffee", "Great coffee.", 4.99)
    result = menu_instance.update_menu_item("Cafe Mocha", "Coffee", "Even better coffee.", 5.99)
    assert result == "Menu item updated for Cafe Mocha."

def test_update_non_existing_menu_item():
    menu_instance = Menu()
    result = menu_instance.update_menu_item("Cafe Mocha", "Coffee", "Even better coffee.", 5.99)
    assert result == "Menu item not found for Cafe Mocha."