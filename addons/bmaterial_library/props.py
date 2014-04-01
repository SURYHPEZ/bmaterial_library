from bpy.types import WindowManager as wm
from bpy.props import (BoolProperty, CollectionProperty, EnumProperty,
                       IntProperty, PointerProperty, StringProperty)

from . import consts, custom, types


wm.bmatlib_cat_mode = EnumProperty(
    name="Category Mode",
    items=consts.BMATLIB_CATEGORY_MODE,
    update=custom.cat_mode_update
    )
wm.bmatlib_mat_mode = EnumProperty(
    name="Material Mode",
    items=consts.BMATLIB_MATERIAL_MODE,
    update=custom.mat_mode_update
    )
wm.bmatlib_mat_save_mode = EnumProperty(
    name="Material Save Mode",
    items=consts.BMATLIB_MATERIAL_SAVE_MODE,
    update=custom.mat_save_mode_update
    )

wm.bmatlib_cat_list = EnumProperty(
    name="Category List",
    items=[],
    update=custom.cat_list_update
    )
wm.bmatlib_cat_name = StringProperty(name="Category Name")

wm.bmatlib_mat_list = CollectionProperty(type=types.MaterialProperties)
wm.bmatlib_active_mat = None
wm.bmatlib_active_mat_index = IntProperty(
    min=-1, default=-1,
    update=custom.mat_index_update
    )

wm.bmatlib_mat_save_name = StringProperty(name="Material Save Name")
wm.bmatlib_mat_save_category = EnumProperty(
    name="Material Save Category",
    items=[]
    )
wm.bmatlib_mat_save_description = StringProperty(
    name="Materiail Save Description"
    )

wm.bmatlib_mat_edit_name = StringProperty(name="Material Edit Name")
wm.bmatlib_mat_edit_category = EnumProperty(
    name="Material Edit Category",
    items=[]
    )
wm.bmatlib_mat_edit_description = StringProperty(
    name="Materiail Edit Description"
    )

wm.bmatlib_mat_all = EnumProperty(name="All Materials", items=[])
