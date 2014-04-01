import bpy
from bpy.types import PropertyGroup
from bpy.props import EnumProperty, StringProperty


class MaterialProperties(PropertyGroup):
    id = StringProperty(name="Material ID")
    name = StringProperty(name="Material Name")
    category = StringProperty(name="Material Category")
    description = StringProperty(name="Materiail Description")

bpy.utils.register_class(MaterialProperties)
