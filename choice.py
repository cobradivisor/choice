#!/usr/bin/env python
import sys
import csv

def _process_choices(row):
    choices = []
    for choice, next_step in zip(row[2::2], row[3::2] ):
        item = (choice, int(next_step))
        choices.append(item)
    return choices

def _process_row(row):
    item = {}
    item['text'] = row[1]
    item['choices'] = _process_choices(row)
    return item

def load_choices(s):
    choices = {}
    with open(s,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=':')
        for row in csvreader:
            choice_id = int(row[0])
            entry = _process_row(row)
            choices[choice_id] = entry
    
    return choices

def _print_available_choices(d):
    for key, choice in d.iteritems():
        answer,_ = choice
        line = str(key) + ".) " + answer
        print line

def _read_input(msg):
    return int(raw_input(msg))

def _print_story(d, step_id):
    step = d[step_id]
    print step['text'].replace('\\n', '\n')
    print ""

    choice_list = {} 
    for num,choice in enumerate(step['choices'],start=1):
       choice_list[num] = choice

    _print_available_choices(choice_list)

    choice_selected = _read_input("Enter Choice: ")
    return ('none',0) if choice_selected is 0 else choice_list[choice_selected]

def start_game(s):
    choice_dict = load_choices(s)
    step_id = 1 
    while(step_id != 0):
        _,step_id = _print_story(choice_dict,step_id)


    print "Goodbye"

def main(story_file):
    start_game(story_file)

if __name__ == "__main__":
    main(sys.argv[1])

