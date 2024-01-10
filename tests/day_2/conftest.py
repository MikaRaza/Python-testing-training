import pytest
from restaurant_reviews import RestaurantReviews

# Fixture : Définition d'un scério réutilisable dans les tests
@pytest.fixture
def restaurant_reviews_with_two_restaurants():
    rr = RestaurantReviews()
    # Ajout des restaurants pour mes scénario
    rr.add_review("Cafe Mocha", "Great Coffe.", 4)
    rr.add_review("Cafe Burger", "Good Burger", 3)
    return rr

# Cours : nous avons vu ensemble comment utiliser les fixture dans le test_fixture_review_get.py
# Exercice : Créer et écrire les tests add/update/delete en utilisant le/la fixture
