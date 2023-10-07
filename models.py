from main import db

class Lines(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    hour = db.Column(db.Time, nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    line = db.Column(db.String(50), nullable=False)
    is_saturday = db.Column(db.Boolean, nullable=False, default=False)
    is_sunday_or_holiday = db.Column(db.Boolean, nullable=False,
                                      default=False)
    obs = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Name %r>' % self.name