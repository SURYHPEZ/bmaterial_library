import os
import shutil

from .exceptions import NoSuchCategoryError, CategoryDuplicatedError
from .subject import Subject


class CategoryManager(Subject):
    def __init__(self, lib_path, cats_data):
        super().__init__()

        self.__path = lib_path
        self.__categories = self.__parse(cats_data)

        self.__ensure_cats_exist()

    def __contains__(self, cat_name):
        return cat_name.lower() in self.__categories

    def __parse(self, cats_data):
        return {cat: Category(cat) for cat in cats_data}

    def __get_cat_path(self, cat):
        return os.path.join(self.__path, cat.name)

    def __ensure_cats_exist(self):
        for cat_name, cat in self.__categories.items():
            cat_path = self.__get_cat_path(cat)
            if not os.path.exists(cat_path):
                os.mkdir(cat_path)

    def __get_item(self, cat_name):
        cat_name = cat_name.lower()
        cat = self.__categories.get(cat_name, None)

        if cat:
            return cat
        else:
            raise NoSuchCategoryError(cat_name)

    def __set_item(self, cat_name, cat):
        self.__categories[cat_name.lower()] = cat

    def __del_item(self, cat_name):
        cat_name = cat_name.lower()
        if cat_name in self:
            self.__categories.pop(cat_name)
        else:
            raise NoSuchCategoryError(cat_name)

    def add(self, cat_name):
        cat_name = cat_name.lower()

        if cat_name not in self:
            cat = Category(cat_name)

            cat_path = self.__get_cat_path(cat)
            os.mkdir(cat_path)

            self.__set_item(cat_name, cat)

            self.notify()
        else:
            raise CategoryDuplicatedError(cat_name)

    def remove(self, cat_name):
        cat_name = cat_name.lower()
        cat = self.__get_item(cat_name)

        cat_path = self.__get_cat_path(cat)
        shutil.rmtree(cat_path)

        self.__del_item(cat_name)

        self.notify()

    def rename(self, old_name, new_name):
        old_name = old_name.lower()
        new_name = new_name.lower()

        cat = self.__get_item(old_name)

        if new_name not in self:
            old_path = os.path.join(self.__path, old_name)
            new_path = os.path.join(self.__path, new_name)

            if os.path.exists(new_path):
                shutil.rmtree(new_path)

            shutil.move(old_path, new_path)

            cat.name = new_name
            self.__set_item(new_name, cat)
            self.__del_item(old_name)

            self.notify()
        else:
            raise CategoryDuplicatedError(new_name)

    def dump(self):
        return sorted(self.__categories)


class Category:
    def __init__(self, name):
        self.__name = name.lower()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.lower()
