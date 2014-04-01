import bpy
import sys

from bmaterial_library.core import utils


if __name__ == "__main__":
    src_blend = sys.argv[6]
    src_bmat = sys.argv[8]
    mid = sys.argv[10]

    mat = utils.load_blend(src_blend, "materials", src_bmat)[0]
    mat.name = mid
    mat.use_fake_user = True

    bpy.ops.file.pack_all()
    bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath, compress=True)
