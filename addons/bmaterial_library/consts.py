import bpy
import inspect
import os.path

BMATLIB_PATH = os.path.split(inspect.getfile(inspect.currentframe()))[0]
BMATLIB_DATA_PATH = os.path.join(BMATLIB_PATH, "data")
BMATLIB_DATA_INDEX_PATH = os.path.join(BMATLIB_DATA_PATH, "INDEX")
BMATLIB_TEMP_PATH = bpy.app.tempdir
BMATLIB_TEMP_BLEND = os.path.join(BMATLIB_TEMP_PATH, "bmatlib_tmp.blend")


BMATLIB_MATERIAL_MODE = [("DEFAULT", ) * 3, ("EDIT", ) * 3,
                         ("CLOSE", ) * 3, ("ADD", ) * 3]
BMATLIB_CATEGORY_MODE = [("DEFAULT", ) * 3, ("ADD", ) * 3, ("EDIT", ) * 3]
BMATLIB_MATERIAL_SAVE_MODE = [("DEFAULT", ) * 3, ("PRO", ) * 3]
