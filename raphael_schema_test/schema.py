from datajoint.schemas import VirtualModule
from . import hub_schema

hub = VirtualModule(
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
