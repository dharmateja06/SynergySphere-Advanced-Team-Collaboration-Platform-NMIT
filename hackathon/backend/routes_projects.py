from flask import Blueprint, request, jsonify
from extensions import db
from hackathon.backend.models import Project, ProjectMember, User, Task
from hackathon.backend.schemas import ProjectCreateSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('projects', __name__, url_prefix='/api/projects')

@bp.route('', methods=['GET'])
@jwt_required()
def list_projects():
    user_id = get_jwt_identity()
    memberships = ProjectMember.query.filter_by(user_id=user_id).all()
    project_ids = [m.project_id for m in memberships]
    projects = Project.query.filter(Project.id.in_(project_ids)).all()
    out = []
    for p in projects:
        todo = Task.query.filter_by(project_id=p.id, status='TODO').count()
        ip = Task.query.filter_by(project_id=p.id, status='IN_PROGRESS').count()
        done = Task.query.filter_by(project_id=p.id, status='DONE').count()
        out.append({'id': p.id, 'name': p.name, 'description': p.description, 'stats': {'todo': todo, 'in_progress': ip, 'done': done}})
    return jsonify(out)

@bp.route('', methods=['POST'])
@jwt_required()
def create_project():
    user_id = get_jwt_identity()
    data = ProjectCreateSchema().load(request.json)
    p = Project(name=data['name'], description=data.get('description',''), owner_id=user_id)
    db.session.add(p)
    db.session.commit()
    pm = ProjectMember(project_id=p.id, user_id=user_id, role='OWNER')
    db.session.add(pm)
    db.session.commit()
    return jsonify({'id': p.id, 'name': p.name, 'description': p.description}), 201

@bp.route('/<project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    # basic membership check
    user_id = get_jwt_identity()
    if not ProjectMember.query.filter_by(project_id=project_id, user_id=user_id).first():
        return jsonify({'error':'Forbidden'}), 403
    p = Project.query.get(project_id)
    todo = Task.query.filter_by(project_id=p.id, status='TODO').count()
    ip = Task.query.filter_by(project_id=p.id, status='IN_PROGRESS').count()
    done = Task.query.filter_by(project_id=p.id, status='DONE').count()
    return jsonify({'id': p.id, 'name': p.name, 'description': p.description, 'stats': {'todo': todo, 'in_progress': ip, 'done': done}})

@bp.route('/<project_id>/members', methods=['GET','POST'])
@jwt_required()
def project_members(project_id):
    user_id = get_jwt_identity()
    if not ProjectMember.query.filter_by(project_id=project_id, user_id=user_id).first():
        return jsonify({'error':'Forbidden'}), 403
    if request.method == 'GET':
        members = ProjectMember.query.filter_by(project_id=project_id).all()
        out = []
        for m in members:
            user = User.query.get(m.user_id)
            out.append({'id': user.id, 'name': user.name, 'email': user.email, 'role': m.role})
        return jsonify(out)
    else:
        payload = request.json
        email = payload.get('email')
        if not email:
            return jsonify({'error':'email required'}), 400
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'error':'user not found'}), 404
        if ProjectMember.query.filter_by(project_id=project_id, user_id=user.id).first():
            return jsonify({'error':'already member'}), 400
        pm = ProjectMember(project_id=project_id, user_id=user.id, role=payload.get('role','MEMBER'))
        db.session.add(pm)
        db.session.commit()
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201