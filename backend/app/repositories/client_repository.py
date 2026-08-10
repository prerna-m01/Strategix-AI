from sqlalchemy.orm import Session

from backend.app.models.client import Client


class ClientRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Client).all()

    def get_by_id(self, client_id: int):
        return (
            self.db.query(Client)
            .filter(Client.id == client_id)
            .first()
        )

    def get_by_client_id(self, client_id: str):
        return (
            self.db.query(Client)
            .filter(Client.client_id == client_id)
            .first()
        )

    def get_by_email(self, email: str):
        return (
            self.db.query(Client)
            .filter(Client.email == email)
            .first()
        )

    def create(self, client: Client):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)

        return client

    def update(self, client: Client):
        self.db.commit()
        self.db.refresh(client)

        return client

    def delete(self, client: Client):
        self.db.delete(client)
        self.db.commit()

        return True