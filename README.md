# codefeedback

## Introduction
The package is aim to support Imperial students to check their codes from jupyter notebook

## Magic lines
There are four essential magic lines:
- %load_ext codefeedback: load the extension from jupyter notebook
- %load_module: load necessary modules (need to be imported manually to prevent installing other packages), equivalent to codefeedback.load()
- %load_answer: load reference answer (Teachers should wrap it to .py / .csv / .txt)
- %check name: check the student answer
