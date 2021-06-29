from app.models import Plant


def plant_getter(plant_name):
    """
    Takes a page name and queries itself to get all the content associated with that page.
    Then it takes the content_name attr and converts it to a lower-snakecased version of itself.
    Then it passes those vars into a dict.
    It returns that dict.
    :return:
    """
    plants = Plant.query.filter_by(name=str(plant_name)).all()
    plant_dict = {}
    for plant in plants:
        # Take each obj and push its content into a variable as described above
        # Then push into a dict
        name = str(plant.name)
        plant_name = str(plant.plant_name)
        last_watered = str(plant.last_watered)
        last_fed = str(plant.last_fed)
        plant_dict.update({'name': name, 'plant_name': plant_name, 'last_watered': last_watered, 'last_fed': last_fed})
    return plant_dict