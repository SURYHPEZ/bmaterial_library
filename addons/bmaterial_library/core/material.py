import bpy
import os
import shutil
import subprocess

from . import utils
from .subject import Subject
from .. import consts


class MaterialManager(Subject):
    def __init__(self, lib_path, mats_data):
        super().__init__()

        self.__path = lib_path
        self.__materials = self.__parse(mats_data)

    def __contains__(self, mid):
        return mid in self.__materials

    def __parse(self, mats_data):
        mats = [Material(mat) for mat in mats_data]
        return {mat.id: mat for mat in mats}

    def __get_mat_path(self, mat):
        return os.path.join(self.__path, mat.category, mat.id + ".blend")

    def __set_item(self, mid, mat):
        self.__materials[mid] = mat

    def __get_item(self, mid):
        mat = self.__materials.get(mid, None)

        if mat:
            return mat
        else:
            raise Exception()

    def __del_item(self, mid):
        if mid in self:
            self.__materials.pop(mid)
        else:
            raise Exception()

    def __add(self, mat, bmat):
        bpy.ops.wm.save_as_mainfile(filepath=consts.BMATLIB_TEMP_BLEND,
                                    compress=True, copy=True)

        mat_path = self.__get_mat_path(mat)

        shutil.copy(consts.BMATLIB_EMPTY_BLEND, mat_path)

        args = [bpy.app.binary_path,
                "-b", mat_path,
                "-P", consts.BMATLIB_SAVE_SCRIPT,
                "--", consts.BMATLIB_TEMP_BLEND,
                "--", bmat.name,
                "--", mat.id]

        subprocess.Popen(args)

    def load(self, mid):
        mat = self.__get_item(mid)
        mat_path = self.__get_mat_path(mat)

        mats = utils.load_blend(mat_path, "materials", mid)

        if mats:
            return mats[0]
        else:
            raise Exception()

    def add(self, bmat, name, category, descrp="No description"):
        mid = utils.random_name()
        mat_data = {
            "id": mid,
            "name": name,
            "category": category.lower(),
            "description": descrp
            }

        mat = Material(mat_data)

        self.__add(mat, bmat)

        self.__set_item(mid, mat)

        self.notify()

    def remove(self, mid):
        mat = self.__get_item(mid)

        mat_path = self.__get_mat_path(mat)
        os.remove(mat_path)

        self.__del_item(mid)

        self.notify()

    def update(self, mid, data, no_notify=False):
        mat = self.__get_item(mid)

        for key, value in data.items():
            if key != getattr(mat, key):
                if key == "category":
                    value = value.lower()
                    mat_blend = mat.id + ".blend"
                    src_cat = os.path.join(self.__path, mat.category,
                                           mat_blend)
                    dst_cat = os.path.join(self.__path, value, mat_blend)
                    shutil.move(src_cat, dst_cat)

                setattr(mat, key, value)

        if not no_notify:
            self.notify()

    def list(self, cat_name):
        cat_name = cat_name.lower()
        return [mat for mid, mat in self.__materials.items()
                if mat.category == cat_name]

    def dump(self):
        return [mat.dump() for mid, mat in self.__materials.items()]


class Material:
    def __init__(self, data):
        self.__id = data.get("id")
        self.__name = data.get("name")
        self.__category = data.get("category")
        self.__description = data.get("description")

        if not all([self.__id, self.__name,
                    self.__category, self.__description]):
            raise Exception()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_cat):
        self.__category = new_cat

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_descrip):
        self.__description = new_descrip

    def dump(self):
        return {"id": self.id, "name": self.name,
                "category": self.category, "description": self.description}
