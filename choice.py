#!/usr/bin/env python
import sys
import csv
import webbrowser
from pygame import mixer
from collections import deque

def _process_choices(row):
    choices = []
    for choice, next_step in zip(row[::2], row[1::2] ):
        if next_step:
            item = (choice, int(next_step))
            choices.append(item)
    return choices

def _process_additional_field(field,item):
    action = field.split("#")
    item[action[0]] = action[1]

def _process_additional_fields(row,item):
    if "@" not in row: return 
    field = row.pop(0) 
    while field != "@":
        _process_additional_field(field,item)
        field = row.pop(0)

def _process_row(row):
    item = {}
    item['text'] = row.pop(0)
    _process_additional_fields(row,item)
    item['choices'] = _process_choices(row)
    return item

def load_choices(s):
    choices = {}
    with open(s,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=':')
        for row in csvreader:
            if len(row) > 1:
                choice_id = int(row.pop(0))
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

def _execute_actions(step):
   if "sound" in step:
        mixer.init()
        mixer.music.load(step['sound'])
        mixer.music.play()

   if "html" in step:
        webbrowser.open(step['html'])
   return

def _print_story(d, step_id,previous_step_id):
    step = d[step_id]
    print step['text'].replace('\\n', '\n')
    print ""
    
    _execute_actions(step)

    choice_list = {} 
    num=0
    for num,choice in enumerate(step['choices'],start=1):
       choice_list[num] = choice
    
    num+=1
    choice_list[num] = ("Go Back",previous_step_id)
    num+=1
    choice_list[num] = ("Quit", 0) 

    _print_available_choices(choice_list)

    choice_selected = _read_input("Enter Choice: ")
    return ('none',0) if choice_selected is 0 else choice_list[choice_selected]

def start_game(s):
    choice_dict = load_choices(s)
    choice_deque = deque([0])
    step_id = 1 
    previous_step_id = 0
    while(step_id != 0):
        choice_text,new_step_id = _print_story(choice_dict,step_id, previous_step_id)
        if choice_text == "Go Back" and len(choice_deque) > 1:
            choice_deque.popleft()
        else:
            choice_deque.appendleft(step_id)

        previous_step_id = choice_deque[0]
        step_id = new_step_id

    print "Goodbye"

def main(story_file):
    start_game(story_file)

if __name__ == "__main__":
    main(sys.argv[1])

