import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

import bmaterial_library as bml
from . import consts, custom
from .core.exceptions import NoSuchCategoryError, CategoryDuplicatedError


class BMATLIB_OP_SetCategoryMode(Operator):
    bl_idname = "bmatlib.set_cat_mode"
    bl_label = "Set category mode"
    bl_description = "Set category mode"
    bl_options = {"REGISTER", "INTERNAL"}

    mode = EnumProperty(name="Category Mode",
                        items=consts.BMATLIB_CATEGORY_MODE)

    @classmethod
    def poll(self, context):
        space_type = context.space_data.type

        return space_type == "PROPERTIES"


    def execute(self, context):
        wm = context.window_manager

        wm.bmatlib_cat_mode = self.mode

        return {"FINISHED"}


class BMATLIB_OP_AddCategory(Operator):
    bl_idname = "bmatlib.add_cat"
    bl_label = "Add category"
    bl_description = "Add category"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(self, context):
        space_type = context.space_data.type

        return space_type == "PROPERTIES"

    def execute(self, context):
        wm = context.window_manager
        cat_name = wm.bmatlib_cat_name

        if cat_name:
            try:
                cat_manager = bml.cat_manager
                cat_manager.add(cat_name)

                custom.load_cat_list(cat_manager)
                wm.bmatlib_cat_list = cat_name.lower().capitalize()

                bpy.ops.bmatlib.set_cat_mode(mode="DEFAULT")
            except CategoryDuplicatedError as e:
                self.report({"ERROR"}, "%s" % e)
        else:
            self.report({"ERROR"}, "Category name can not be empty")
            return {"CANCELLED"}

        return {"FINISHED"}


class BMATLIB_OP_EditCategory(Operator):
    bl_idname = "bmatlib.edit_cat"
    bl_label = "Edit category"
    bl_description = "Edit category"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(self, context):
        space_type = context.space_data.type

        return space_type == "PROPERTIES"

    def execute(self, context):
        wm = context.window_manager
        cur_cat_name = wm.bmatlib_cat_list
        new_cat_name = wm.bmatlib_cat_name

        if new_cat_name:
            try:
                cat_manager = bml.cat_manager
                cat_manager.rename(cur_cat_name, new_cat_name)

                custom.load_cat_list(cat_manager)
                wm.bmatlib_cat_name = new_cat_name

                bpy.ops.bmatlib.set_cat_mode(mode="DEFAULT")
            except CategoryDuplicatedError as e:
                self.report({"ERROR"}, "%s" % e)
        else:
            self.report({"ERROR"}, "Category name can not be empty")
            return {"CANCELLED"}

        return {"FINISHED"}


class BMATLIB_OP_RemoveCategory(Operator):
    bl_idname = "bmatlib.remove_cat"
    bl_label = "Remove category"
    bl_description = "Remove category"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(self, context):
        space_type = context.space_data.type

        return space_type == "PROPERTIES"

    def execute(self, context):
        wm = context.window_manager
        cur_cat_name = wm.bmatlib_cat_list

        try:
            cat_manager = bml.cat_manager
            cat_manager.remove(cur_cat_name)

            custom.load_cat_list(cat_manager)
            wm.bmatlib_cat_list = wm.bmatlib_cat_list
        except Exception as e:
            self.report({"ERROR"}, "%s" % e)
            return {"CANCELLED"}

        return {"FINISHED"}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Are you sure to remove this category?")
