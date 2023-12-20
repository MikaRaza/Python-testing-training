import pytest


def total_with_tip(bill, percentage):
    tip_amount = bill * (percentage / 100)
    total_amount = bill + tip_amount
    return total_amount

# Tests avec pytest
def test_tip_classic():
    assert total_with_tip(100, 20) == 120
    
def test_tip_poor_service():
    assert total_with_tip(100, 0) == 100  

# Exercice : écrire les tests correspondants : 
# 2. Le tip maximal est de 500€ car il n'existe pas de billet plus gros.
# 3. Le plus petit billet étant 5€, il n'est pas possible d'avoir un total plus bas de 5€
# 4. Vérifer que l'arrondie du total est bien sur deux décimales
# 5. Adater votre function d'implementation pour passer les tests

# TODO:Tester les pourcentages -> Exception 
class NegativeValueError(Exception):
    """Bill and percentage should be positive"""
def total_with_tip(bill, percentage):
    if bill <0 :
        raise NegativeValueError ("bill should be positive")
    if percentage <0 :
        raise NegativeValueError ("percentage should be positive")
    tip_amount = bill * (percentage / 100)
    if tip_amount > 500:
        tip_amount = 500  # Limite le pourboire maximal à 500€
    
    total_amount = bill + tip_amount
    if total_amount < 5:
        total_amount = 5  # Garantit que le total est au moins de 5€
    else:
        total_amount = round(total_amount, 2)  # Arrondi à deux décimales si supérieur à 5€
    
    return total_amount


# Tests avec pytest
#2
def test_tip_max_limit():
    assert total_with_tip(1000, 51) == 1500  
    
#3
def test_minimum_total():
    assert total_with_tip(2, 0) == 5  # Montant total inférieur au minimum (5€)
    
#4
def test_rounding_two_decimals():
    assert total_with_tip(5, 12.45) == 5.62 # Vérification de l'arrondi à deux décimales
    
#TODO

def test_negative_error():
    with pytest.raises(NegativeValueError) as exceptionTips:
        total_with_tip(100, -10)
    print(exceptionTips.value)
    assert str(exceptionTips.value) == "percentage should be positive"
    with pytest.raises(NegativeValueError) as exceptionTips:
        total_with_tip(-10, 10)
    print(exceptionTips.value)
    assert str(exceptionTips.value) == "bill should be positive"