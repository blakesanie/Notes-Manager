#!/bin/bash

function updateNotes() {
    clear
    cd /Users/blake/desktop/github/notes-manager
    python main.py
    if [ "$1" ] && [ $1 == "git" ]
    then
        git commit -m 'update' ./notes.json
        git push
    fi
}
