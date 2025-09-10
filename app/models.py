from app import db

ingredientes_galletas = db.Table('ingredientes_galletas',db.Column('galleta_id',db.Integer, db.ForeignKey('galleta_id'),primary_key=True),db.Column('ingrediente_id',db.Integer, db.ForeignKey('ingrediente_id'),primary_key=True))

class Ingrediente(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    nombre = db.Colum(db.String(80), nullable=False)
    costo = db.Colum(db.Float,nullabe=False)

def to_dict(self):
    return {
        'id':self.id,
        'nombre':self.nombre,
        'costo':self.costo,
    }


class Ingrediente(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    nombre = db.Colum(db.String(80), nullable=False)
    sabor = db.Column(db.String(80), nullable=False)
    precio = db.Colum(db.Float,nullabe=False)
    Ingredientes = db.relationship('ingrediente', secondary=ingredientes_galletas)


def to_dict(self):
    return {
        'id':self.id,
        'nombre':self.nombre,
        'sabor':self.sabor,
        'precio':self.precio,
        'ingrediente':[ingrediente.to_dict() for Ingrediente in self.ingredientes]

    }