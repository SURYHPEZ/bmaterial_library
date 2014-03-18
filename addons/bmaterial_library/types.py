import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty


class BmatPropertyGroup(PropertyGroup):
    id = StringProperty(name = "Material ID")
    category = StringProperty(name = "Material Category")
    description = StringProperty(name = "Materiail Description", default = "")

bpy.utils.register_class(BmatPropertyGroup)
