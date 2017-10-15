import os
import pytest
import choice

def test_load_choices_with_no_choice_mark():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_choices.csv"
    choices = choice.load_choices(test_file)
    expected_choices = { 1 : { 'text' : "a long time ago", 'choices' : [ ( 'yes', 2 ), ('no',3) ] }}   
    assert expected_choices == choices

def test_throws_exception_when_file_not_found():
    with pytest.raises(IOError):
        c = choice.load_choices("file_not_found.csv")

def test_start_game_exits_when_0_input_for_choice(capsys):
    
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_choices.csv"
    choice._read_input = lambda _: 0  
    choice.start_game(test_file)
    out,_ = capsys.readouterr()
    assert "Goodbye" in out

def test_load_choices_with_choice_mark_no_additional_fields():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_choices_with_choice_mark_no_additional_fields.csv"
    choices = choice.load_choices(test_file)
    expected_choices = { 1 : { 'text' : "a long time ago", 'choices' : [ ( 'yes', 2 ), ('no',3) ] }}   
    assert expected_choices == choices

def test_load_choices_with_choice_mark():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_choices_with_choice_mark.csv"
    choices = choice.load_choices(test_file)
    expected_choices = { 1 : { 'text' : "a long time ago", 'html' : 'tests/pic.png', 'sound' : 'tests/sound.mp3','choices' : [ ( 'yes', 2 ), ('no',3) ] }}   
    assert expected_choices == choices

def test_load_choices_ignores_lines_that_start_with_new_line():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_ends_with_new_lines_and_spaces.csv"
    choices = choice.load_choices(test_file)

def test_load_choices_with_choice_mark():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = test_directory + "/test_choice_with_no_choices_allowed.csv"
    choices = choice.load_choices(test_file)
