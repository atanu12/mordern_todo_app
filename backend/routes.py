from app import app,db
from flask import request, jsonify
from models import Todo

# get all data
@app.route('/api/todolist', methods=['GET'])
def get_all_todo():
    todos = Todo.query.filter_by(deleted=False).all()
    result = [todo.todo_json() for todo in todos]
    return jsonify(result)

# create todo data
@app.route('/api/create', methods=['POST'])
def create_todo():
    try:
        data = request.json
        task = data.get('task')
        img_url = f"https://avatar.iran.liara.run/username?username={task}"

        new_list = Todo(task=task,img_url=img_url)
        db.session.add(new_list)
        db.session.commit()
        return jsonify({'mes':'new list created successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),500

# update the task
@app.route('/api/update_todo/<int:id>', methods=['PATCH'])
def update_todo(id):
    try:
        todo = Todo.query.get(id)
        if todo is  None:
            return jsonify({'error', 'todo is not found'}),404
        data = request.json
        print(data)
        todo.task = data.get('task', todo.task)
        
        db.session.commit()
        return jsonify(todo.todo_json()),200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),500
    
# delete the task
@app.route('/api/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        todo = Todo.query.get(id)
        if todo is None:
            return jsonify({"error": "Task is not found"})
        data = request.json
        print(data)
        print(todo.todo_json())
        todo.deleted = data.get("deleted", todo.deleted)
        db.session.commit()
        return jsonify({"msg":"Task Deleted Successfully"}),200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500