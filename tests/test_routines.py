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

    def test_IsNumber(self):
        testData = [
            # positive tests:
            [-1, True],
            [0, True],
            [1, True],
            [-2., True],
            [2., True],
            # negative tests:
            ['0', False],
            [True, False],
            [False, False],
            ['1', False],
            ['-2.', False],
            [[], False],
            [self, False],
        ]
        for test in testData:
            assert FuzzyRoutines.IsNumber(test[0]) is test[1], 'Input: [ {} ] expected output: [ {} ]'.format(test[0], test[1])

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
        # positive tests:
        testDataPositive = [
            [0., 0.5, 1.],
            [0.5, 0.5, 0.5],
            [1., 0.5, 0.],
            [0.25, 0.25, 0.25],
            [0.25, 0.75, 0.9166666666666666],
            [0.25, 1, 1.],
            [0., 1, 1.],
            [1., 1, 1.],
        ]
        for test in testDataPositive:
            assert FuzzyRoutines.FuzzyNOT(test[0], alpha=test[1]) == test[2], 'Input: [ {}, alpha={} ] expected output: [ {} ]'.format(test[0], test[1], test[2])

        # negative tests:
        testDataNegative = [
            [0., 0, None],
            [1., 0, None],
            [0.25, 0., None],
            [1.1, 0.5, None],
            [-1.1, 0.5, None],
            [1.1, 0., None],
            [1.1, 0.25, None],
            [1.1, 1, None],
            [-1.1, 0., None],
            [-1.1, 0.25, None],
            [-1.1, 1, None],
        ]
        for test in testDataNegative:
            assert FuzzyRoutines.FuzzyNOT(test[0], alpha=test[1]) is test[2], 'Input: [ {}, alpha={} ] expected output: [ {} ]'.format(test[0], test[1], test[2])

    def test_FuzzyNOTParabolic(self):
        # positive tests:
        testDataPositive = [
            [0., 0.5, 0.001, 1.],
            [0.5, 0.5, 0.001, 0.5],
            [1., 0.5, 0.001, 0.],
            [0., 1., 0., 1.],
            [0., 1., 1., 1.],
            [0., 0.25, 0., 1.],
            [0., 0.25, 1., 1.],
            [1., 0.25, 0., 0.],
            [1., 0.25, 1., 0.],
            [0., 1., 0.25, 1.],
            [1., 1., 0.25, 0.],
        ]
        for test in testDataPositive:
            assert round(FuzzyRoutines.FuzzyNOTParabolic(test[0], alpha=test[1], epsilon=test[2]), 5) == test[3], 'Input: [ {}, alpha={}, epsilon={} ] expected output: [ {} ]'.format(test[0], test[1], test[2], test[3])

        # negative tests:
        testDataNegative = [
            [1., 0., 0.25, None],
            [0., 0., 0.25, None],
            [0., 0., 0., None],
            [0., 0., 1., None],
            [-1., 0.5, 0.001, None],
            [2., 0.5, 0.001, None],
            [0., -1., 0.001, None],
            [1., 2., 0.001, None],
            [0., 0.5, -1., None],
            [1., 0.5, 2., None],
        ]
        for test in testDataNegative:
            assert FuzzyRoutines.FuzzyNOTParabolic(test[0], alpha=test[1], epsilon=test[2]) is test[3], 'Input: [ {}, alpha={}, epsilon={} ] expected output: [ {} ]'.format(test[0], test[1], test[2], test[3])

    def test_FuzzyAND(self):
        # positive tests:
        testDataPositive = [
            [0., 0., 0.],
            [0., 1., 0.],
            [1., 0., 0.],
            [1., 1., 1.],
            [0.5, 0.6, 0.5],
            [0.7, 0.5, 0.5],
            [-1., 0., -1.],
            [0., -1., -1.],
            [2., 2., 2.],
        ]
        for test in testDataPositive:
            assert FuzzyRoutines.FuzzyAND(test[0], test[1]) == test[2], 'Input: [ {}, {} ] expected output: [ {} ]'.format(test[0], test[1], test[2])

        # negative tests:
        testDataNegative = [
            [None, None, None],
            [self, 0., None],
            [[], 1., None],
            ['0.', '0.', None],
        ]
        for test in testDataNegative:
            assert FuzzyRoutines.FuzzyAND(test[0], test[1]) is test[2], 'Input: [ {}, {} ] expected output: [ {} ]'.format(test[0], test[1], test[2])

    def test_FuzzyOR(self):
        # positive tests:
        testDataPositive = [
            [0., 0., 0.],
            [0., 1., 1.],
            [1., 0., 1.],
            [1., 1., 1.],
            [0.5, 0.6, 0.6],
            [0.7, 0.5, 0.7],
            [-1., 0., 0.],
            [0., -1., 0.],
            [2., 2., 2.],
        ]
        for test in testDataPositive:
            assert FuzzyRoutines.FuzzyOR(test[0], test[1]) == test[2], 'Input: [ {}, {} ] expected output: [ {} ]'.format(test[0], test[1], test[2])

        # negative tests:
        testDataNegative = [
            [None, None, None],
            [self, 0., None],
            [[], 1., None],
            ['0.', '0.', None],
        ]
        for test in testDataNegative:
            assert FuzzyRoutines.FuzzyOR(test[0], test[1]) is test[2], 'Input: [ {}, {} ] expected output: [ {} ]'.format(test[0], test[1], test[2])
