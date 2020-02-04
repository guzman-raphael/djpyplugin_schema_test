from datajoint.schema import create_virtual_module
from . import hub_schema

hub = create_virtual_module(
    'virtual_module',
    'hub',
    create_schema=True,
    create_tables=True,
    add_objects={
        'Org': hub_schema.Org,
        'Project': hub_schema.Project,
        'User': hub_schema.User,
        'Org_Member': hub_schema.Org_Member
    }
)
