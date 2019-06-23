#!/bin/bash

function updateNotes() {
    clear
    python main.py
    if [ "$1" ] && [ $1 == "git" ]
    then
        cd /Users/blake/desktop/github/notes-manager
        git commit -m 'update' ./notes.json
        git push
    fi
}
