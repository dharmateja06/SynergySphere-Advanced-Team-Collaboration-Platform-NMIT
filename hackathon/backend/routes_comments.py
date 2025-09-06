from flask import Blueprint, request, jsonify
from extensions import db
from hackathon.backend.models import Comment, ProjectMember
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('comments', __name__, url_prefix='/api/projects/<project_id>/comments')

@bp.route('', methods=['GET','POST'])
@jwt_required()
def comments(project_id):
    user_id = get_jwt_identity()
    if not ProjectMember.query.filter_by(project_id=project_id, user_id=user_id).first():
        return jsonify({'error':'Forbidden'}), 403
    if request.method == 'GET':
        comments = Comment.query.filter_by(project_id=project_id).order_by(Comment.created_at.asc()).all()
        out = []
        for c in comments:
            out.append({'id': c.id, 'author_id': c.author_id, 'body': c.body, 'parent_id': c.parent_id, 'created_at': c.created_at.isoformat()})
        return jsonify(out)
    else:
        payload = request.json
        body = payload.get('body')
        if not body:
            return jsonify({'error':'body required'}), 400
        c = Comment(project_id=project_id, author_id=user_id, body=body, parent_id=payload.get('parent_id'))
        db.session.add(c)
        db.session.commit()
        return jsonify({'id': c.id, 'body': c.body, 'author_id': c.author_id}), 201
