# Notes Manager

In college, I take handwritten notes on an iPad using [Notability](https://www.gingerlabs.com). To access my notes off-device without paying for iCloud sync/storage, I built [this website](http://www.blakesanie.com/notes) for note access through the browser.

The webpage, though, needs an updated, parsable directory of notes. Notability makes automatic backups to Google Drive. This project takes advantage of that feature.

A Python script scrapes the backup folder, organizes note documents into JSON, and optionally pushes the data to the repo for my site (or another) to query with the help of [Github Pages](https://pages.github.com).

This entire process has been built into a simple shell command, executable anywhere in the terminal.

## Use for yourself

1.  Clone the repository

```shell
$ git clone https://github.com/blakesanie/Notes-Manager.git
```

2.  In main.py, declare the folder ID where your notes are located (line 6)

```python
FOLDER_ID = "YOUR_FOLDER_ID_HERE"
```

This value can be found within the folder's url: https:<span></span>//drive.google.com/drive/u/1/folders/<span style="color: green">**FOLDER_ID**</span>

3.  In commands.sh, set the project directory's path (line 8)

```shell
cd /absolute/path/to/project/directory
```

4.  Make the shell script executable across all local directories

```shell
$ source ~/path/to/project/directory/commands.sh
```

## Run the program

In a terminal window, execute the command:

```shell
$ updateNotes
```

A JSON representation of your notes will be written to **notes.json**

Add **"git"** as a parameter if you want to commit and push changes in **notes.json**

```shell
$ updateNotes git
```

This is useful when the json file needs to be accessed across the web (make sure to enable Github Pages)

## Code Walkthrough

I'll do this later
