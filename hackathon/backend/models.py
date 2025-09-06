from datetime import datetime
import enum
import uuid
from extensions import db

class TaskStatus(enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    projects = db.relationship('Project', backref='owner', lazy=True)
    tasks = db.relationship('Task', backref='assignee', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)


class Project(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.String, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    members = db.relationship('ProjectMember', backref='project', lazy=True)
    tasks = db.relationship('Task', backref='project', lazy=True)
    comments = db.relationship('Comment', backref='project', lazy=True)


class ProjectMember(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = db.Column(db.String, db.ForeignKey('project.id'), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(20), default='MEMBER')

    # relationship
    user = db.relationship('User', backref='project_memberships')


class Task(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = db.Column(db.String, db.ForeignKey('project.id'), nullable=False)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    assignee_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=True)
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.TODO)
    due_date = db.Column(db.Date)
    created_by = db.Column(db.String, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = db.Column(db.String, db.ForeignKey('project.id'), nullable=False)
    author_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    parent_id = db.Column(db.String, db.ForeignKey('comment.id'), nullable=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # self-referencing relationship (for threaded comments)
    replies = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]))
