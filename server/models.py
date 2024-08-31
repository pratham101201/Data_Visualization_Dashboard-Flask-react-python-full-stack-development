from db import db

class ReportModel(db.Model):
    __tablename__ = 'marketinsights'
    id = db.Column(db.BigInteger, primary_key=True)
    end_year = db.Column(db.String(4))
    intensity = db.Column(db.Integer)
    sector = db.Column(db.String(50))
    topic = db.Column(db.String(50))
    insight = db.Column(db.Text)
    url = db.Column(db.Text)
    region = db.Column(db.String(50))
    start_year = db.Column(db.String(4))
    impact = db.Column(db.String(50))
    added = db.Column(db.DateTime)
    published = db.Column(db.DateTime)
    country = db.Column(db.String(50))
    relevance = db.Column(db.Integer)
    pestle = db.Column(db.String(50))
    source = db.Column(db.String(50))
    title = db.Column(db.Text)
    likelihood = db.Column(db.Integer)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
