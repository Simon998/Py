import currency_converter

def test_currency_converter():
    # Test converting USD to CAD
    assert currency_converter.convert_currency('USD', 'CAD', 100) == 130.0
    
    # Test converting GBP to EUR
    assert currency_converter.convert_currency('GBP', 'EUR', 50) == 58.3
    
    # Test converting JPY to USD
    assert currency_converter.convert_currency('JPY', 'USD', 5000) == 45.87
    
    # Test converting EUR to GBP
    assert currency_converter.convert_currency('EUR', 'GBP', 75) == 64.26
