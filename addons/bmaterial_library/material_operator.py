import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

from . import consts


class BMATLIB_OP_SetMaterialMode(Operator):
    bl_idname = "bmatlib.set_mat_mode"
    bl_label = "Set Material Mode"
    bl_description = "Set material mode"

    mode = EnumProperty(name = "Material Mode",
                        items = consts.BMATLIB_MATERIAL_MODE)

    def execute(self, context):
        wm = context.window_manager

        wm.bmatlib_mat_mode = self.mode

        return {"FINISHED"}


class BMATLIB_OP_SetMaterialSaveMode(Operator):
    bl_idname = "bmatlib.set_mat_save_mode"
    bl_label = "Set Material Save Mode"
    bl_description = "Set material save mode"

    mode = EnumProperty(name = "Material Save Mode",
                        items = consts.BMATLIB_MATERIAL_SAVE_MODE)

    def execute(self, context):
        wm = context.window_manager

        wm.bmatlib_mat_save_mode = self.mode

        return {"FINISHED"}


class BMATLIB_OP_AppendMaterial(Operator):
    bl_idname = "bmatlib.append_mat"
    bl_label = "Append Material"
    bl_description = "Append current material to the object"

    def execute(self, context):
        return {"FINISHED"}


class BMATLIB_OP_ReplaceMaterial(Operator):
    bl_idname = "bmatlib.replace_mat"
    bl_label = "Replace Material"
    bl_description = "Replace object's active material by current material"

    def execute(self, context):
        return {"FINISHED"}


class BMATLIB_OP_RemoveMaterial(Operator):
    bl_idname = "bmatlib.remove_mat"
    bl_label = "Remove Material"
    bl_description = "Remove current material from library"

    def execute(self, context):
        return {"FINISHED"}

    def invoke(self, context, event):
        return {"FINISHED"}

    def draw(self, context):
        pass


class BMATLIB_OP_SaveMaterial(Operator):
    bl_idname = "bmatlib.save_mat"
    bl_label = "Save Material"
    bl_description = "Save object's active material to library"

    def execute(self, context):
        return {"FINISHED"}


class BMATLIB_OP_EditMaterial(Operator):
    bl_idname = "bmatlib.edit_mat"
    bl_label = "Edit Material"
    bl_description = "Modify current material's properties"

    def execute(self, context):
        return {"FINISHED"}
