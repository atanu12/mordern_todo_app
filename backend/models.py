from app import db

# declater the db setting
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000), nullable=False)
    completed_status = db.Column(db.Boolean(), default=False)
    deleted = db.Column(db.Boolean(), default=False)
    img_url = db.Column(db.String(200), nullable=False)

    # rerurn the data into json
    def todo_json(self):
        return{
        'id':self.id,
        'task':self.task,
        'completed':self.completed_status,
        'deleted':self.deleted,
        'imgUrl': self.img_url
        }