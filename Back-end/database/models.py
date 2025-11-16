from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Animal(db.Model):
    """Modelo para animais disponíveis para adoção"""
    __tablename__ = "animals"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)  # Cachorro, Gato
    age = db.Column(db.String(50), nullable=False)  # Ex: 2 anos
    size = db.Column(db.String(50), nullable=False)  # Pequeno, Médio, Grande
    temperament = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Disponível")  # Disponível, Adotado
    image = db.Column(db.String(500), nullable=True)
    description = db.Column(db.Text, nullable=False)
    history = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    adoptions = db.relationship("Adoption", back_populates="animal", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "size": self.size,
            "temperament": self.temperament,
            "city": self.city,
            "status": self.status,
            "image": self.image,
            "description": self.description,
            "history": self.history,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class Adoption(db.Model):
    """Modelo para registros de adoção"""
    __tablename__ = "adoptions"
    
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"), nullable=False)
    adopter_name = db.Column(db.String(100), nullable=False)
    adopter_email = db.Column(db.String(100), nullable=False)
    adopter_phone = db.Column(db.String(20), nullable=True)
    address_cep = db.Column(db.String(10), nullable=False)
    address_street = db.Column(db.String(200), nullable=False)
    address_number = db.Column(db.String(20), nullable=False)
    address_complement = db.Column(db.String(200), nullable=True)
    address_neighborhood = db.Column(db.String(100), nullable=True)
    address_city = db.Column(db.String(100), nullable=False)
    address_state = db.Column(db.String(2), nullable=False)
    adoption_message = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default="Pending")  # Pending, Approved, Rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    animal = db.relationship("Animal", back_populates="adoptions")
    
    def to_dict(self):
        return {
            "id": self.id,
            "animal_id": self.animal_id,
            "animal": self.animal.to_dict() if self.animal else None,
            "adopter_name": self.adopter_name,
            "adopter_email": self.adopter_email,
            "adopter_phone": self.adopter_phone,
            "address_cep": self.address_cep,
            "address_street": self.address_street,
            "address_number": self.address_number,
            "address_complement": self.address_complement,
            "address_neighborhood": self.address_neighborhood,
            "address_city": self.address_city,
            "address_state": self.address_state,
            "adoption_message": self.adoption_message,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class Contact(db.Model):
    """Modelo para mensagens de contato"""
    __tablename__ = "contacts"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "created_at": self.created_at.isoformat()
        }


class Feedback(db.Model):
    """Modelo para feedback dos usuários"""
    __tablename__ = "feedback"
    
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "mensagem": self.mensagem,
            "created_at": self.created_at.isoformat()
        }
