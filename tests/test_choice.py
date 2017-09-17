import os
import pytest
import choice

def test_choice():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_choices.csv"
    choices = choice.load_choices(test_file)
    expected_choices = { 0 : { 'text' : "A long time ago", 'choices' : [ ( 'yes', 1 ), ('no',2) ] }}   
    assert expected_choices == choices

def test_throws_exception_when_file_not_found():
    with pytest.raises(IOError):
        c = choice.load_choices("file_not_found.csv")


