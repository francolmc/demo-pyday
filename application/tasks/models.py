from application.extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title: str, description: str) -> None:
        super().__init__()
        self.title = title
        self.description = description

    def complete(self):
        self.completed = True

    def is_completed(self):
        return self.completed
