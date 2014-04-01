import os
import pickle

from .observer import Observer
from .category import CategoryManager
from .material import MaterialManager


class Library(Observer):

    __DEFAULT_LIBRARY = {"categories": {"default"}, "materials": []}
    __INDEX_FILE = "INDEX"

    def __init__(self, lib_root):
        super().__init__()

        self.__root = lib_root
        self.__index_file = os.path.join(lib_root, Library.__INDEX_FILE)
        self.__data = None

    def __load(self):
        try:
            with open(self.__index_file, 'rb') as lib:
                self.__data = pickle.load(lib)
        except (EOFError, FileNotFoundError):
            self.__data = Library.__DEFAULT_LIBRARY
            self.save()

    def save(self):
        with open(self.__index_file, 'wb') as lib:
            pickle.dump(self.__data, lib)

    def open(self):
        self.__load()

        cats_data = self.__data.get("categories")
        mats_data = self.__data.get("materials")

        cat_manager = CategoryManager(self.__root, cats_data)
        mat_manager = MaterialManager(self.__root, mats_data)

        cat_manager.attach(self)
        mat_manager.attach(self)

        return cat_manager, mat_manager

    def update(self, subject):
        if isinstance(subject, CategoryManager):
            self.__data["categories"] = subject.dump()
        elif isinstance(subject, MaterialManager):
            self.__data["materials"] = subject.dump()
        else:
            return

        self.save()
