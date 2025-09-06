from flask import Blueprint, request, jsonify
from extensions import db
from hackathon.backend.models import User
from marshmallow import ValidationError
from hackathon.backend.schemas import SignupSchema, LoginSchema
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = SignupSchema().load(request.json)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400

    pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    user = User(
        name=data['name'],
        email=data['email'],
        password_hash=pw_hash.decode()
    )
    db.session.add(user)
    db.session.commit()

    token = create_access_token(identity=user.id)
    return jsonify({
        'user': {'id': user.id, 'name': user.name, 'email': user.email},
        'token': token
    }), 201


@bp.route('/login', methods=['POST'])
def login():
    try:
        data = LoginSchema().load(request.json)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.checkpw(data['password'].encode(), user.password_hash.encode()):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_access_token(identity=user.id)
    return jsonify({
        'user': {'id': user.id, 'name': user.name, 'email': user.email},
        'token': token
    }), 200


@bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
