class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if restaurant_name not in self.menu_items:
            self.menu_items[restaurant_name] = {}
        if item_name in self.menu_items[restaurant_name]:
            return "Menu item already exists."
        self.menu_items[restaurant_name][item_name] = {'description': description, 'price': price}
        return f"Menu item added for {restaurant_name}."

    def get_menu(self, restaurant_name):
        if restaurant_name in self.menu_items:
            return self.menu_items[restaurant_name]
        else:
            return "Menu not found for {}.".format(restaurant_name)

    def update_menu_item(self, restaurant_name, item_name, new_description, new_price):
        if restaurant_name in self.menu_items and item_name in self.menu_items[restaurant_name]:
            self.menu_items[restaurant_name][item_name]['description'] = new_description
            self.menu_items[restaurant_name][item_name]['price'] = new_price
            return "Menu item updated for {}.".format(restaurant_name)
        else:
            return "Menu item not found for {}.".format(restaurant_name)

    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name in self.menu_items and item_name in self.menu_items[restaurant_name]:
            del self.menu_items[restaurant_name][item_name]
            return "Menu item deleted for {}.".format(restaurant_name)
        else:
            return "Menu item not found for {}.".format(restaurant_name)
