import pytest
from menu import Menu

def test_delete_existing_menu_item():
    menu_instance = Menu()
    menu_instance.add_menu_item("Cafe Mocha", "Coffee", "Great coffee.", 4.99)
    result = menu_instance.delete_menu_item("Cafe Mocha", "Coffee")
    assert result == "Menu item deleted for Cafe Mocha."

def test_delete_non_existing_menu_item():
    menu_instance = Menu()
    result = menu_instance.delete_menu_item("Cafe Mocha", "Coffee")
    assert result == "Menu item not found for Cafe Mocha."