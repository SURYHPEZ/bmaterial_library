import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

from . import consts


class BMATLIB_OP_SetCategoryMode(Operator):
    bl_idname = "bmatlib.set_cat_mode"
    bl_label = "Set category mode"
    bl_description = "Set category mode"

    mode = EnumProperty(name = "Category Mode",
                        items = consts.BMATLIB_CATEGORY_MODE)

    def execute(self, context):
        wm = context.window_manager

        wm.bmatlib_cat_mode = self.mode

        return {"FINISHED"}


class BMATLIB_OP_AddCategory(Operator):
    bl_idname = "bmatlib.add_cat"
    bl_label = "Add category"
    bl_description = "Add category"

    def execute(self, context):
        return {"FINISHED"}


class BMATLIB_OP_EditCategory(Operator):
    bl_idname = "bmatlib.edit_cat"
    bl_label = "Edit category"
    bl_description = "Edit category"

    def execute(self, context):
        return {"FINISHED"}


class BMATLIB_OP_RemoveCategory(Operator):
    bl_idname = "bmatlib.remove_cat"
    bl_label = "Remove category"
    bl_description = "Remove category"

    def execute(self, context):
        return {"FINISHED"}

    def invoke(self, conetxt, event):
        return {"FINISHED"}

    def draw(self, context):
        pass
