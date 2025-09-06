from marshmallow import Schema, fields

class SignupSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class ProjectCreateSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()


class TaskCreateSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str()
    assignee_id = fields.Str()
    due_date = fields.Date()   # Marshmallow will convert "2025-09-06" into a datetime.date


class TaskUpdateSchema(Schema):
    # All fields optional because it's PATCH
    title = fields.Str()
    description = fields.Str()
    assignee_id = fields.Str()
    due_date = fields.Date()
    status = fields.Str()   # TODO / IN_PROGRESS / DONE
