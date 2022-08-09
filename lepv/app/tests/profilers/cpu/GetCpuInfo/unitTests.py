"""Tests for CPU profiler method: get_processor_count"""
from tests.profilers.lepvTestCase import LepvTestCase
import unittest
from ddt import ddt, file_data

from app.modules.profilers.cpu.CPUProfiler import CPUProfiler


__author__  = "Copyright (c) 2017, LEP>"
__copyright__ = "Licensed under GPLv2 or later."


@ddt
class GetProcLoadavgTestCase(LepvTestCase):

    def setUp(self):
        self.functor = CPUProfiler('').get_processor_count

    @file_data("unittests.json")
    def test(self, kernel, os, cpu, note, lepdResult, expected, expectedMatchType):
        self.unit_test(kernel, os, cpu, note, lepdResult, expected, expectedMatchType)

if __name__ == '__main__':
    unittest.main()
