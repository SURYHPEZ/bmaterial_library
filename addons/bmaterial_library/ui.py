import bpy
from bpy.types import Panel


class BMATLIB_PT_BMaterialLib(Panel):
    """
    BMaterial Library Panel
    """

    bl_label = "BMaterial Library"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        engine = context.scene.render.engine

        if engine != "CYCLES":
            row = layout.row()
            row.label(text = "Sorry, Only support cycles yet", icon = "ERROR")
        else:
            wm = context.window_manager
            self.__draw(wm, layout)

    def __draw(self, wm, layout):
        cat_mode = wm.bmatlib_cat_mode
        self.__draw_cat_block(wm, layout, cat_mode)

        self.__draw_mat_list_block(wm, layout)

        mat_mode = wm.bmatlib_mat_mode
        self.__draw_mat_detail_block(wm, layout, mat_mode)

        mat_save_mode = wm.bmatlib_mat_save_mode
        self.__draw_mat_save_block(wm, layout, mat_save_mode)

    def __draw_cat_block(self, wm, layout, cat_mode):
        row = layout.row(align = True)
        row.prop(wm, "bmatlib_cat_list", text = "Category")
        
        if cat_mode == "DEFAULT":
            row.operator("bmatlib.set_cat_mode", text = "",
                         icon = "ZOOMIN").mode = "ADD"
            row.operator("bmatlib.set_cat_mode", text = "",
                         icon = "TEXT").mode = "EDIT"
            row.operator("bmatlib.remove_cat", text = "", icon = "ZOOMOUT")
        elif cat_mode == "ADD":
            row.operator("bmatlib.add_cat", text = "", icon = "FILE_TICK")
            row.operator("bmatlib.set_cat_mode", text = "",
                         icon = "X_VEC").mode = "DEFAULT"
        elif cat_mode == "EDIT":
            row.operator("bmatlib.edit_cat", text = "", icon = "FILE_TICK")
            row.operator("bmatlib.set_cat_mode", text = "",
                         icon = "X_VEC").mode = "DEFAULT"
        else:
            pass

    def __draw_mat_list_block(self, wm, layout):
        row = layout.row(align = True)
        row.template_list("UI_UL_list", " ",
                          wm, "bmatlib_mat_list",
                          wm, "bmatlib_active_mat_index")

    def __draw_mat_detail_block(self, wm, layout, mat_mode):
        if mat_mode == "DEFAULT":
           box = layout.box()
           
           row = box.row(align = True)
           row.label(text = "Material Detail")
           row.operator("bmatlib.set_mat_mode", text = "",
                        icon = "TEXT").mode = "EDIT"
           row.operator("bmatlib.remove_mat", text = "", icon = "MESH_CYLINDER")
           row.operator("bmatlib.set_mat_mode", text = "",
                        icon = "PANEL_CLOSE").mode = "CLOSE"

           row = box.row(align = True)
           col = row.column(align = True)
           col.template_preview(bpy.data.materials.get('BMATLIB_PREV'),
                                show_buttons = False)
           col = row.column(align = True)
           col.label(text = "Name: %s" % "name")
           col.label(text = "Category: %s" % "category")
           col.label(text = "Description: %s" % "description")

           row = box.row(align = True)
           row.operator("bmatlib.append_mat", text = "Append",
                        icon = "ZOOMIN")
           row.operator("bmatlib.replace_mat", text = "Replace",
                        icon = "FILE_REFRESH")
        elif mat_mode == "EDIT":
           box = layout.box()
           
           row = box.row(align = True)
           row.label(text = "Edit Material")
           row.operator("bmatlib.set_mat_mode", text = "",
                        icon = "PANEL_CLOSE").mode = "CLOSE"

           row = box.row(align = True)
           col = row.column(align = True)
           col.template_preview(bpy.data.materials.get('BMATLIB_PREV'),
                                show_buttons = False)
           col = row.column()
           row = col.row()
           row.prop(wm, "bmatlib_mat_name", text = "Name")
           row = col.row()
           row.prop(wm, "bmatlib_mat_category", text = "Category")
           row = col.row()
           row.prop(wm, "bmatlib_mat_description", text = "Description")

           row = box.row(align = True)
           row.operator("bmatlib.edit_mat", text = "OK", icon = "FILE_TICK")
           row.operator("bmatlib.set_mat_mode", text = "Cancel",
                        icon = "X_VEC").mode = "DEFAULT"
        else:
            pass

    def __draw_mat_save_block(self, wm, layout, mat_save_mode):
        if mat_save_mode == "DEFAULT":
            row = layout.row(align = True)
            
            col = row.column(align = True)
            col.operator("bmatlib.set_mat_save_mode", text = "",
                         icon = "FULLSCREEN_ENTER").mode = "PRO"

            col = row.column(align = True)
            col.operator("bmatlib.save_mat", text = "Quick Save")
            col.enabled = True if bpy.context.object.active_materiail \
                          else False
        elif mat_save_mode == "PRO":
            box = layout.box()
            
            row = box.row(align = True)
            row.label(text = "Save Material")

            saveable = True if bpy.data.materials else False

            row = box.row(align = True)
            row.prop(wm, "bmatlib_mat_all", text = "Material")
            row.enabled = saveable

            row = box.row(align = True)
            row.prop(wm, "bmatlib_mat_name", text = "Name")
            row.enabled = saveable

            row = box.row(align = True)
            row.prop(wm, "bmatlib_mat_category", text = "Category")
            row.enabled = saveable

            row = box.row(align = True)
            row.prop(wm, "bmatlib_mat_description", text = "Description")
            row.enabled = saveable

            row = box.row(align = True)
            col = row.column(align = True)
            col.operator("bmatlib.set_mat_save_mode", text = "",
                         icon = "FULLSCREEN_EXIT").mode = "DEFAULT"
            col = row.column(align = True)
            col.operator("bmatlib.save_mat", text = "SAVE")
            col.enabled = saveable
        
        
    
