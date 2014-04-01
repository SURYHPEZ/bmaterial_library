class LibraryError(Exception):
    def __init__(self):
        super().__init__()


class MaterialError(Exception):
    def __init__(self):
        super().__init__()


class CategoryError(Exception):
    def __init__(self, cat_name):
        super().__init__(cat_name)
        self.cat = cat_name


class NoSuchCategoryError(CategoryError):
    def __init__(self, cat_name):
        super().__init__(cat_name)

    def __str__(self):
        return "No such category: %s" % self.cat


class CategoryDuplicatedError(CategoryError):
    def __init__(self, cat_name):
        super().__init__(cat_name)

    def __str__(self):
        return "Category: %s, already exists" % self.cat
