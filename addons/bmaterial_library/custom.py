import bpy
from bpy.types import WindowManager as wm
from bpy.props import EnumProperty

import bmaterial_library as bml
from . import consts


def load_bmatlib(cat_manager, mat_manager):
    load_cat_list(cat_manager)

    cur_cat = bpy.context.window_manager.bmatlib_cat_list
    load_mat_list(mat_manager, cur_cat)


def load_cat_list(cat_manager):
    cat_list = cat_manager.dump()
    cat_list_items = [(c.capitalize(), ) * 3 for c in cat_list]

    wm.bmatlib_cat_list = EnumProperty(name="Category List",
                                       items=cat_list_items,
                                       update=cat_list_update)

    wm.bmatlib_mat_edit_category = EnumProperty(name="Material Category",
                                                items=cat_list_items)

    wm.bmatlib_mat_save_category = EnumProperty(name="Material Category",
                                                items=cat_list_items)


def load_mat_list(mat_manager, cat_name):
    mat_list = mat_manager.list(cat_name)

    slots = bpy.context.window_manager.bmatlib_mat_list

    slots.clear()

    for mat in mat_list:
        slot = slots.add()
        slot.id = mat.id
        slot.name = mat.name
        slot.category = mat.category
        slot.description = mat.description


def load_mat_all():
    mat_items = [(m.name, ) * 3 for m in bpy.data.materials
                 if m.name != consts.BMATLIB_PREV_MAT]

    wm.bmatlib_mat_all = EnumProperty(name="All Materials",
                                      items=mat_items)


def cat_mode_update(self, context):
    mode = self.bmatlib_cat_mode

    if mode == "ADD":
        self.bmatlib_cat_name = "New Category"
    elif mode == "EDIT":
        self.bmatlib_cat_name = self.bmatlib_cat_list
    else:
        self.bmatlib_cat_name = ""


def mat_mode_update(self, context):
    mode = self.bmatlib_mat_mode

    if mode == "CLOSE":
        self.bmatlib_active_mat_index = -1
        self.bmatlib_mat_edit_name = ""
        self.bmatlib_mat_edit_description = ""
    elif mode == "EDIT":
        active_mat = self.bmatlib_active_mat

        self.bmatlib_mat_edit_name = active_mat.name
        self.bmatlib_mat_edit_category = active_mat.category.capitalize()
        self.bmatlib_mat_edit_description = active_mat.description
    else:
        self.bmatlib_mat_edit_name = ""
        self.bmatlib_mat_edit_description = ""


def mat_save_mode_update(self, context):
    mode = self.bmatlib_mat_save_mode

    if mode == "PRO":
        self.bmatlib_mat_save_name = "New Material"
        self.bmatlib_mat_save_category = self.bmatlib_cat_list
        self.bmatlib_mat_save_description = "No Description"


def cat_list_update(self, context):
    cur_cat_name = self.bmatlib_cat_list

    load_mat_list(bml.mat_manager, cur_cat_name)

    self.bmatlib_active_mat_index = -1


def mat_index_update(self, context):
    slots = self.bmatlib_mat_list
    index = self.bmatlib_active_mat_index

    if index > -1 and slots:
        wm.bmatlib_active_mat = slots[index]
    else:
        wm.bmatlib_active_mat = None

    active_mat = self.bmatlib_active_mat

    if active_mat:
        mid = active_mat.id
        load_preview(mid)

    bpy.ops.bmatlib.set_mat_mode(mode="DEFAULT")


def load_preview(mid):
    old_prev_mat = bpy.data.materials.get(consts.BMATLIB_PREV_MAT)

    if old_prev_mat:
        old_mat_id = old_prev_mat.get("id")
        if old_mat_id and old_mat_id == mid:
            return

        old_prev_mat.user_clear()
        bpy.data.materials.remove(old_prev_mat)

    new_prev_mat = bml.mat_manager.load(mid)
    new_prev_mat.name = consts.BMATLIB_PREV_MAT
    new_prev_mat["id"] = mid
