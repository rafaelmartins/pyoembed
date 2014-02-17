import mock
import unittest

from pyoembed.utils import get_metaclass_objects


class UtilsTestCase(unittest.TestCase):

    @mock.patch('pyoembed.utils.os.listdir')
    @mock.patch('pyoembed.utils.import_module')
    def test_get_metaclass_objects(self, import_module, listdir):

        class DumbBaseClass(object):
            pass

        def listdir_side_effect(d):
            if d.endswith('asd'):
                return ['bola.py', 'foo.rst', 'guda.pyc', 'qwert.pyo',
                        '__init__.py']
            return []

        listdir.side_effect = listdir_side_effect
        self.assertEqual(get_metaclass_objects('asd', DumbBaseClass), [])
        self.assertEqual(import_module.call_args_list,
                         [mock.call('asd.bola'), mock.call('asd.guda'),
                          mock.call('asd.qwert')])
