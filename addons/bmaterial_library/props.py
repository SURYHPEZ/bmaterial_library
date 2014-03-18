import bpy
from bpy.props import (StringProperty, EnumProperty, BoolProperty,
                       CollectionProperty, IntProperty)

from . import consts, types

wm = bpy.types.WindowManager

wm.bmatlib_cat_mode = EnumProperty(name = "Category Mode",
                                   items = consts.BMATLIB_CATEGORY_MODE)
wm.bmatlib_mat_mode = EnumProperty(name = "Material Mode",
                                   items = consts.BMATLIB_MATERIAL_MODE)
wm.bmatlib_mat_save_mode = EnumProperty(name = "Material Save Mode",
                                    items = consts.BMATLIB_MATERIAL_SAVE_MODE)
wm.bmatlib_cat_list = EnumProperty(name = "Category List",
                                   items = [])
wm.bmatlib_mat_list = CollectionProperty(type = types.BmatPropertyGroup)
wm.bmatlib_active_mat_index = IntProperty(min = -1, default = -1)
wm.bmatlib_mat_name = StringProperty(name = "Material Name", default = "New")
wm.bmatlib_mat_category = EnumProperty(name = "Material Category",
                                       items = [])
wm.bmatlib_mat_description = StringProperty(name = "Material Description",
                                            default = "")
wm.bmatlib_mat_all = EnumProperty(name = "All Materials", items = [])
