# -*- coding: utf-8 -*-

import pytest
import FuzzyRoutines


class TestBaseMethods():

    @pytest.fixture(scope='class', autouse=True)
    def init(self):
        FuzzyRoutines.FCLogger.level = 50  # Disable debug logging while test, logger CRITICAL = 50

    def test_DiapasonParser(self):
        # positive tests
        assert FuzzyRoutines.DiapasonParser("1") == [1]
        assert FuzzyRoutines.DiapasonParser("1,5") == [1, 5]
        assert FuzzyRoutines.DiapasonParser("1-5") == [1, 2, 3, 4, 5]
        assert FuzzyRoutines.DiapasonParser("8-10, 1-5, 6") == [1, 2, 3, 4, 5, 6, 8, 9, 10]
        assert FuzzyRoutines.DiapasonParser("11, 11, 12, 12, 1-5, 3-7") == [1, 2, 3, 4, 5, 6, 7, 11, 12]

        # negative tests
        assert FuzzyRoutines.DiapasonParser(12345) == []
        assert FuzzyRoutines.DiapasonParser("") == []
        assert FuzzyRoutines.DiapasonParser("-") == []
        assert FuzzyRoutines.DiapasonParser("1-") == []
        assert FuzzyRoutines.DiapasonParser(",") == []
        assert FuzzyRoutines.DiapasonParser("1,") == []

    def test_IsCorrectFuzzyNumberValue(self):
        # positive tests
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(0) is True
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(0.5) is True
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(1) is True

        # negative tests
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(-1.5) is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(1.5) is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue('0') is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(True) is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue('True') is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(False) is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue('False') is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue([]) is False
        assert FuzzyRoutines.IsCorrectFuzzyNumberValue(self) is False

    def test_FuzzyNOT(self):
        # positive tests
        assert FuzzyRoutines.FuzzyNOT(0.) == 1.
        assert FuzzyRoutines.FuzzyNOT(0.5) == 0.5
        assert FuzzyRoutines.FuzzyNOT(1.) == 0.
        assert FuzzyRoutines.FuzzyNOT(0.25, alpha=0.) == 0.25  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(0.25, alpha=0.25) == 0.25
        assert FuzzyRoutines.FuzzyNOT(0.25, alpha=0.75) == 0.9166666666666666
        assert FuzzyRoutines.FuzzyNOT(0.25, alpha=1) == 1.
        assert FuzzyRoutines.FuzzyNOT(0., alpha=0) == 0.  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(0., alpha=1) == 1.
        assert FuzzyRoutines.FuzzyNOT(1., alpha=0) == 1.  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(1., alpha=1) == 1.

        # negative tests
        assert FuzzyRoutines.FuzzyNOT(1.1) == 1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(-1.1) == -1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(1.1, alpha=0.) == 1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(1.1, alpha=0.25) == 1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(1.1, alpha=1) == 1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(-1.1, alpha=0.) == -1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(-1.1, alpha=0.25) == -1.1  # an exception (return self fuzzyNumber)
        assert FuzzyRoutines.FuzzyNOT(-1.1, alpha=1) == -1.1  # an exception (return self fuzzyNumber)

    def test_FuzzyNOTParabolic(self):
        # positive tests
        assert FuzzyRoutines.FuzzyNOTParabolic(0.) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(0.5) - 0.5 <= 0.000000001
        assert FuzzyRoutines.FuzzyNOTParabolic(1.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=0., epsilon=0.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=0., epsilon=1.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=1., epsilon=0.) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=1., epsilon=1.) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=0.25, epsilon=0.) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=0.25, epsilon=1.) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(1., alpha=0.25, epsilon=0.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(1., alpha=0.25, epsilon=1.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=0., epsilon=0.25) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=1., epsilon=0.25) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(1., alpha=0., epsilon=0.25) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(1., alpha=1., epsilon=0.25) == 0.

        # negative tests
        assert FuzzyRoutines.FuzzyNOTParabolic(-1.) == -1.
        assert FuzzyRoutines.FuzzyNOTParabolic(2.) == 2.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., alpha=-1.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(1., alpha=2.) == 1.
        assert FuzzyRoutines.FuzzyNOTParabolic(0., epsilon=-1.) == 0.
        assert FuzzyRoutines.FuzzyNOTParabolic(1., epsilon=2.) == 1.
