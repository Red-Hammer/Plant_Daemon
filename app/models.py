from app import db


class Plant(db.Model):
    """The simple model of a plant and its needs"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55))
    plant_name = db.Column(db.String(255))
    last_watered = db.Column(db.Date)
    last_fed = db.Column(db.Date)


    def __repr__(self):
        return '<Plant: {}'.format(str(self.id) + ' Name: ' + str(self.name) + ' Last Watered on: '
                                     + str(self.last_watered)
                                     )
