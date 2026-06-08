def make_car(manufacturer, model_name, **information):

    """build a dictionary about car information"""

    information['manufacturer'] = manufacturer
    information['model name'] = model_name
    return information


car = make_car(

    manufacturer='subaru',
    model_name='outback',
    color='blue',
    tow_package = True
)

print(car)