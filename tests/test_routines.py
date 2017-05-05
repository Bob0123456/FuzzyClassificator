# -*- coding: utf-8 -*-

import pytest
import FuzzyRoutines


class TestBaseMethods():

    @pytest.fixture(scope='class', autouse=True)
    def init(self):
        FuzzyRoutines.FCLogger.level = 50  # Disable debug logging while test, logger CRITICAL = 50

    def test_DiapasonParser(self):
        testData = [
            # positive tests:
            ["1", [1]],
            ["1,5", [1, 5]],
            ["1-5", [1, 2, 3, 4, 5]],
            ["8-10, 1-5, 6", [1, 2, 3, 4, 5, 6, 8, 9, 10]],
            ["11, 11, 12, 12, 1-5, 3-7", [1, 2, 3, 4, 5, 6, 7, 11, 12]],
            # negative tests:
            [12345, []],
            ["", []],
            ["-", []],
            ["1-", []],
            [",", []],
            ["1,", []],
        ]
        for test in testData:
            assert FuzzyRoutines.DiapasonParser(test[0]) == test[1], 'Input: [ {} ] expected output: [ {} ]'.format(test[0], test[1])

    def test_IsCorrectFuzzyNumberValue(self):
        testData = [
            # positive tests:
            [0, True],
            [0.5, True],
            [1, True],
            # negative tests:
            [-1.5, False],
            [1.5, False],
            ['0', False],
            [True, False],
            ['True', False],
            [False, False],
            ['False', False],
            [[], False],
            [self, False],
        ]
        for test in testData:
            assert FuzzyRoutines.IsCorrectFuzzyNumberValue(test[0]) is test[1], 'Input: [ {} ] expected output: [ {} ]'.format(test[0], test[1])

    def test_FuzzyNOT(self):
        testData = [
            # positive tests:
            [0., 0.5, 1.],
            [0.5, 0.5, 0.5],
            [1., 0.5, 0.],
            [0.25, 0., 0.25],
            [0.25, 0.25, 0.25],
            [0.25, 0.75, 0.9166666666666666],
            [0.25, 1, 1.],
            [0., 0, 0.],
            [0., 1, 1.],
            [1., 0, 1.],
            [1., 1, 1.],
            # negative tests:
            [1.1, 0.5, 1.1],
            [-1.1, 0.5, -1.1],
            [1.1, 0., 1.1],
            [1.1, 0.25, 1.1],
            [1.1, 1, 1.1],
            [-1.1, 0., -1.1],
            [-1.1, 0.25, -1.1],
            [-1.1, 1, -1.1],
        ]
        for test in testData:
            assert FuzzyRoutines.FuzzyNOT(test[0], alpha=test[1]) == test[2], 'Input: [ {}, alpha={} ] expected output: [ {} ]'.format(test[0], test[1], test[2])

    def test_FuzzyNOTParabolic(self):
        testData = [
            # positive tests:
            [0., 0.5, 0.001, 1.],
            [0.5, 0.5, 0.001, 0.5],
            [1., 0.5, 0.001, 0.],
            [0., 0., 0., 0.],
            [0., 0., 1., 0.],
            [0., 1., 0., 1.],
            [0., 1., 1., 1.],
            [0., 0.25, 0., 1.],
            [0., 0.25, 1., 1.],
            [1., 0.25, 0., 0.],
            [1., 0.25, 1., 0.],
            [0., 0., 0.25, 0.],
            [0., 1., 0.25, 1.],
            [1., 0., 0.25, 1.],
            [1., 1., 0.25, 0.],
            # negative tests:
            [-1., 0.5, 0.001, -1.],
            [2., 0.5, 0.001, 2.],
            [0., -1., 0.001, 0.],
            [1., 2., 0.001, 1.],
            [0., 0.5, -1., 0.],
            [1., 0.5, 2., 1.],
        ]
        for test in testData:
            assert round(FuzzyRoutines.FuzzyNOTParabolic(test[0], alpha=test[1], epsilon=test[2]), 5) == test[3], 'Input: [ {}, alpha={}, epsilon={} ] expected output: [ {} ]'.format(test[0], test[1], test[2], test[3])

    def test_FuzzyAND(self):
        testData = [
            # positive tests:
            [0., 0., 0.],
            [0., 1., 0.],
            [1., 0., 0.],
            [1., 1., 1.],
            [0.5, 0.6, 0.5],
            [0.7, 0.5, 0.5],
            # negative tests:
            [None, None, 0.],
            [self, 0., 0.],
            [-1., 0., 0.],
            [0., -1., 0.],
            [2., 2., 0.],
            ['0.', '0.', 0.],
        ]
        for test in testData:
            assert FuzzyRoutines.FuzzyAND(test[0], test[1]) == test[2], 'Input: [ {}, {} ] expected output: [ {} ]'.format(test[0], test[1], test[2])
