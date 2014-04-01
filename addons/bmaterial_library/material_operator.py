import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

import bmaterial_library as bml
from . import consts, custom


class BMATLIB_OP_SetMaterialMode(Operator):
    bl_idname = "bmatlib.set_mat_mode"
    bl_label = "Set Material Mode"
    bl_description = "Set material mode"
    bl_options = {"REGISTER", "INTERNAL"}

    mode = EnumProperty(name="Material Mode",
                        items=consts.BMATLIB_MATERIAL_MODE)

    def execute(self, context):
        wm = context.window_manager

        wm.bmatlib_mat_mode = self.mode

        return {"FINISHED"}


class BMATLIB_OP_SetMaterialSaveMode(Operator):
    bl_idname = "bmatlib.set_mat_save_mode"
    bl_label = "Set Material Save Mode"
    bl_description = "Set material save mode"
    bl_options = {"REGISTER", "INTERNAL"}

    mode = EnumProperty(name="Material Save Mode",
                        items=consts.BMATLIB_MATERIAL_SAVE_MODE)

    def execute(self, context):
        wm = context.window_manager

        wm.bmatlib_mat_save_mode = self.mode

        return {"FINISHED"}


class BMATLIB_OP_AppendMaterial(Operator):
    bl_idname = "bmatlib.append_mat"
    bl_label = "Append Material"
    bl_description = "Append current material to the object"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context):
        return True if context.object else False

    def execute(self, context):
        wm = context.window_manager
        active_mat = wm.bmatlib_active_mat

        bmat = bml.mat_manager.load(active_mat.id)

        context.object.data.materials.append(bmat)

        return {"FINISHED"}


class BMATLIB_OP_ReplaceMaterial(Operator):
    bl_idname = "bmatlib.replace_mat"
    bl_label = "Replace Material"
    bl_description = "Replace object's active material by current material"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context):
        return True if context.object.active_material else False

    def execute(self, context):
        wm = context.window_manager
        active_mat = wm.bmatlib_active_mat

        bmat = bml.mat_manager.load(active_mat.id)

        context.object.active_material = bmat

        return {"FINISHED"}


class BMATLIB_OP_RemoveMaterial(Operator):
    bl_idname = "bmatlib.remove_mat"
    bl_label = "Remove Material"
    bl_description = "Remove current material from library"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context):
        wm = context.window_manager
        active_mat = wm.bmatlib_active_mat

        bml.mat_manager.remove(active_mat.id)

        custom.load_mat_list(bml.mat_manager, wm.bmatlib_cat_list)

        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager

        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Are your sure to remove this material?")


class BMATLIB_OP_SaveMaterial(Operator):
    bl_idname = "bmatlib.save_mat"
    bl_label = "Save Material"
    bl_description = "Save object's active material to library"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context):
        wm = context.window_manager
        mode = wm.bmatlib_mat_save_mode
        bmat = context.object.active_material

        if mode == "DEFAULT":
            wm.bmatlib_mat_save_name = bmat.name
            wm.bmatlib_mat_save_category = wm.bmatlib_cat_list
            wm.bmatlib_mat_save_description = "No Description"

        if not wm.bmatlib_mat_save_name \
           or not wm.bmatlib_mat_save_category \
           or not wm.bmatlib_mat_save_description:
            self.report({"ERROR"}, ("Material name or description"
                                    " can not be empty"))
            return {"CANCELLED"}

        bml.mat_manager.add(bmat, wm.bmatlib_mat_save_name,
                            wm.bmatlib_mat_save_category,
                            wm.bmatlib_mat_save_description)

        if wm.bmatlib_cat_list == wm.bmatlib_mat_save_category:
            custom.load_mat_list(bml.mat_manager, wm.bmatlib_cat_list)

        return {"FINISHED"}


class BMATLIB_OP_EditMaterial(Operator):
    bl_idname = "bmatlib.edit_mat"
    bl_label = "Edit Material"
    bl_description = "Modify current material's properties"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context):
        wm = context.window_manager
        active_mat = wm.bmatlib_active_mat

        data = {
            "name": wm.bmatlib_mat_edit_name,
            "category": wm.bmatlib_mat_edit_category,
            "description": wm.bmatlib_mat_edit_description
            }

        bml.mat_manager.update(active_mat.id, data)

        custom.load_mat_list(bml.mat_manager, wm.bmatlib_cat_list)

        return {"FINISHED"}
