products = {"milk": 1.02, "eggs": 0.12, "bread": 1.50, "cheese": 4.5}

services = {"printing": 0.5, "cleaning": 19.99, "delivery": 5}


def calc_taxes(tax):
    """
    Calculate taxes based on the given tax rate and return
    a lambda function to compute the tax for a given price.
    """
    return lambda price: price * tax


calc_price_products = calc_taxes(0.15)
calc_price_services = calc_taxes(0.1)

for product in products:
    print(
        f"""{product}: 
          Price with taxes {calc_price_products(products[product])}"""
    )

for service in services:
    print(
        f"""{service}: 
          Price with taxes {calc_price_services(services[service])}"""
    )

# Execute if the script is run directly
if __name__ == "__main__":
    print(calc_price_services(services["cleaning"]))
