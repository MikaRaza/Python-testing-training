import pytest

def vta_price(ht, vta):
    return round(ht*(1+vta/100),2) 


# Normal
@pytest.mark.parametrize("prix, taux, prix_ttc_attendu",[
    # France
    (100, 20, 120), #Taux Normal
    (100, 10, 110), #Taux Intermediaire -> Nous ajoutons l'arroundie à deux décimale à cause du problème de virgule flottante 
    (100, 5.5, 105.5), #Taux Réduit
    (100, 2.1, 102.1), #Taux Particulier
    (100, 0, 100), #Taux 0
    #Luxembourg ...
])
def test_french_vta(prix, taux, prix_ttc_attendu):
    ttc = vta_price(prix, taux)
    assert (ttc == prix_ttc_attendu)

# Limits (negative)