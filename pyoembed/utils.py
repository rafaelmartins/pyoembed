import os
from importlib import import_module

cwd = os.path.dirname(os.path.abspath(__file__))
import_root = os.path.join(cwd, '..')


def get_metaclass_objects(import_namespace, base_class, sort_key=None):
    import_basedir = import_namespace.replace('.', os.sep)
    import_dir = os.path.join(import_root, import_basedir)
    imported = []
    for class_file in os.listdir(import_dir):
        name, ext = os.path.splitext(class_file)
        if ext not in ['.py', '.pyc', '.pyo']:
            continue
        if name in ['__init__']:
            continue
        if name not in imported:
            import_module('%s.%s' % (import_namespace, name))
            imported.append(name)
    rv = [klass() for klass in base_class.__subclasses__()]
    rv.sort(key=sort_key)
    return rv
