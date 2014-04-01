bl_info = {
    'name': 'BMaterial Library',
    'author': 'SURYHPEZ',
    'blender': (2, 66, 0),
    'location': 'Material > BMaterial Library',
    'description': 'BMaterial Library',
    'warning': '',
    'tracker_url': 'https://github.com/SURYHPEZ',
    'wiki_url': 'https://github.com/SURYHPEZ',
    'category': 'Material'
    }

if "bpy" in locals():
    from imp import reload as _reload
    for val in _modules_loaded.values():
        _reload(val)

_modules = (
    'category_operator',
    'material_operator',
    'props',
    'types',
    'ui',
)

__import__(name=__name__, fromlist=_modules)
_namespace = globals()
_modules_loaded = {name: _namespace[name] for name in _modules}
del _namespace

import bpy

from .import consts, custom, handlers
from .core.library import Library


library = Library(consts.BMATLIB_DATA_PATH)
cat_manager, mat_manager = library.open()


def register():
    bpy.app.handlers.scene_update_post.append(handlers.materials_update)
    bpy.utils.register_module(__name__)

    custom.load_bmatlib(cat_manager, mat_manager)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":   
    register()
