import bpy
from bpy.app.handlers import persistent
from . import custom


@persistent
def materials_update(context):
    if bpy.data.materials.is_updated:
        custom.load_mat_all()
