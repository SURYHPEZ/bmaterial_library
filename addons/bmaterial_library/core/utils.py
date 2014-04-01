import bpy
import random
import datetime


def random_name(prefix="", suffix=""):
    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    rand_int = random.randint(0, 9999)

    return "%s%s%04d%s" % (prefix, time_str, rand_int, suffix)


def load_blend(filepath, datablock, name=None):
    '''
    Load data from other .blend file
    '''
    with bpy.data.libraries.load(filepath) as (from_data, to_data):
        if name:

            # If 'name' is a string list
            if isinstance(name, list) \
               and all(isinstance(x, str) for x in name):
                data = name

            # If 'name' is a string
            elif isinstance(name, str):
                data = [name]

            # Else raise TypeError
            else:
                raise TypeError('name must be a string or a string list')
            setattr(to_data, datablock, data)
        else:
            setattr(to_data, datablock, getattr(from_data, datablock))

    # Filter out None element
    not_none_filter = filter(lambda m: m is not None,
                             getattr(to_data, datablock))
    return list(not_none_filter)
