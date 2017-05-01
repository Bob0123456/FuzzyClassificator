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
