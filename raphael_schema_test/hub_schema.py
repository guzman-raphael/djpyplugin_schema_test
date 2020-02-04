from datajoint.schema import Schema
from datajoint.user_tables import Manual

target = Schema('hub')


@target
class Org(Manual):
    definition = """
    org_id: uuid
    ---
    org_name: varchar(64)
    unique index (org_name)
    """


@target
class Project(Manual):
    definition = """
    ->Org
    project_id: uuid
    ---
    project_name: varchar(64)
    database_dsn= null:varchar(64)
    unique index (org_id, project_name)
    unique index (database_dsn)
    """


@target
class User(Manual):
    definition = """
    user_id: uuid
    ---
    user_name: varchar(64)
    bio: varchar(64)
    unique index (user_name)
    """


@target
class Org_Member(Manual):
    definition = """
    -> Org
    -> User
    """
