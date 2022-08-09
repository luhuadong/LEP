from tests.profilers.lepvTestCase import LepvTestCase

__author__    = "Copyright (c) 2017, LEP>"
__copyright__ = "Licensed under GPLv2 or later."

import unittest

from app.modules.profilers.io.IOProfiler import IOProfiler


class StabilityTestCase(LepvTestCase):

    def setUp(self):
        pass

    def validate(self, actual):
        pass

    def test_stability(self):
        profiler = IOProfiler('www.rmlink.cn')
        self.repeated_test(profiler.get_io_top)


if __name__ =='__main__':
    unittest.main()
