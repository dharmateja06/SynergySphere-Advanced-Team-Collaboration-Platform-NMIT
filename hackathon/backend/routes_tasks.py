from flask import Blueprint, request, jsonify
from extensions import db
from hackathon.backend.models import Task, ProjectMember
from hackathon.backend.schemas import TaskCreateSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('tasks', __name__, url_prefix='/api')

@bp.route('/projects/<project_id>/tasks', methods=['GET','POST'])
@jwt_required()
def project_tasks(project_id):
    user_id = get_jwt_identity()
    if not ProjectMember.query.filter_by(project_id=project_id, user_id=user_id).first():
        return jsonify({'error':'Forbidden'}), 403
    if request.method == 'GET':
        tasks = Task.query.filter_by(project_id=project_id).all()
        out = []
        for t in tasks:
            out.append({'id': t.id, 'title': t.title, 'description': t.description, 'assignee_id': t.assignee_id, 'status': t.status, 'due_date': t.due_date and t.due_date.isoformat()})
        return jsonify(out)
    else:
        data = TaskCreateSchema().load(request.json)
        t = Task(project_id=project_id, title=data['title'], description=data.get('description'), assignee_id=data.get('assignee_id'), due_date=data.get('due_date'), created_by=user_id)
        db.session.add(t)
        db.session.commit()
        return jsonify({'id': t.id, 'title': t.title, 'status': t.status}), 201

@bp.route('/tasks/<task_id>', methods=['PATCH','DELETE','GET'])
@jwt_required()
def single_task(task_id):
    user_id = get_jwt_identity()
    t = Task.query.get(task_id)
    if not t:
        return jsonify({'error':'not found'}), 404
    if not ProjectMember.query.filter_by(project_id=t.project_id, user_id=user_id).first():
        return jsonify({'error':'Forbidden'}), 403
    if request.method == 'GET':
        return jsonify({'id': t.id, 'title': t.title, 'description': t.description, 'assignee_id': t.assignee_id, 'status': t.status, 'due_date': t.due_date and t.due_date.isoformat()})
    if request.method == 'PATCH':
        payload = request.json
        if 'status' in payload:
            t.status = payload['status']
        if 'title' in payload:
            t.title = payload['title']
        if 'description' in payload:
            t.description = payload['description']
        if 'assignee_id' in payload:
            t.assignee_id = payload['assignee_id']
        if 'due_date' in payload:
            t.due_date = payload['due_date']
        db.session.commit()
        return jsonify({'id': t.id, 'status': t.status})
    if request.method == 'DELETE':
        db.session.delete(t)
        db.session.commit()
        return jsonify({}), 204