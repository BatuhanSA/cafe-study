# Repository for CAFE Prototype User Study

This repository contains resources for a prototype user study (proto-study) for the CAFE framework.

## Background

We created an open-source package called [CAFE](https://github.com/aiea-lab/cafe) which provides personalized profiling based feedback on coding assignments.
It integrates with the EduLinq's [Lynx Grader](https://github.com/edulinq/autograder-py) Python Interface.

## Setup

### Supported Environments

This proto-study needs a Unix-like (POSIX) command line:

- **Mac / Linux**: Use your built-in terminal.
- **Windows**: Use WSL (Windows Subsystem for Linux), not Command Prompt or PowerShell

### Python

In this proto-study, we will be using Python (version >= 3.10).
If you don't already have Python installed or need to upgrade it,
instructions for your OS can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download).

To check your already installed Python version, use:
```sh
python3 -V
```

### Virtual Environments

In this proto-study, we will be using the [standard venv tool](https://docs.python.org/3/library/venv.html) distributed with Python.
(You're welcome to use other tools, though our ability to help may be limited depending on how familiar we are with them. We'll do our best either way.)
[This guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
covers how to create an use venvs, we will reiterate the steps here.
Refer to the linked guide for the exact commands.)

Before using a venv, you must create it:
```sh
python3 -m venv env
```

(In this document, we will assume that your venv is called `env` and it is located in the same directory you are running commands in.)
Once created, a venv will be a normal directory that holds all of its information and packages.
To use your newly created venv, you will need to [activate](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment) it:

```sh
source env/bin/activate
```

If you want to stop using the venv, you can just deactivate it at any time:
```sh
deactivate
```

Your venv can be re-activated at any time in the same way as before.

### Required Packages

This repository contains a [requirements.txt](./requirements.txt) file that lists
all the required Python packages for this proto-study.

To install these packages, first make sure you are in your [virtual environment](#virtual-environments),
and then run the command:
```sh
pip3 install -r requirements.txt
```

Note that this assumes you are in the same directory as the requirements file.
Just point to the file if you are somewhere else
(e.g., use `../requirements.txt` if you are in this assignment's directory).

You may choose to use another packaging system instead of pip (like Conda),
though we can't promise the same level of help if we're not familiar with it. We'll do what we can.

## CAFE

Concrete Analysis for Explanations (CAFE) is a framework for providing personalized explanations on coding assignments by using code profiling.
It profiles both the student’s submission and a solution against the same test cases, then compares how each one behaves.
It returns the compared behavioral information to the student as feedback.
CAFE is built on top of the [autograder-py](https://github.com/edulinq/autograder-py) python package,
and uses the assignment and question objects it defines.

## Overview

The purpose of this proto-study is to assess whether a full-scale study evaluating the effectiveness of the CAFE framework would be feasible.
Participants will be asked to debug buggy code both with and without CAFE.
Each participant will complete two rounds and serves as their own baseline, meaning we will compare each person with themselves across the two rounds.
So variables that vary between people, e.g., coding skill, prior experience, and language familiarity stay constant across both rounds.
Eliminating some of these variables make observing whether CAFE helps when debugging easier.

## Study Flow

Participants will be divided into four approximately equal sized groups, each defined by the task and setup they start with.
The task is the problem they will debug (search or sort), and the setup is whether they will use CAFE (experimental) or not (control).
In the first round, participants will debug their groups assigned task with their groups given setup.
In the second round, they will switch to the opposite of both: the other task and the other setup.
Someone who starts on search without CAFE will move to sort with CAFE, and so on.

| Group |     Round 1       |     Round 2       |
|:-----:|:-----------------:|:-----------------:|
| 1     | Search & No CAFE  | Sort & CAFE       |
| 2     | Search & CAFE     | Sort & No CAFE    |
| 3     | Sort & No CAFE    | Search & CAFE     |
| 4     | Sort & CAFE       | Search & No CAFE  |


These four groups cover every permutation of starting task and starting setup.
This counterbalancing lets us account for biases such as order effects and differences in task difficulty.
We expect these biases to average out across the groups.

## Deliverables

### Quantitative

We will collect the `attempts` folder from both questions.
The `attempts` folder contains every attempt that was submitted for grading.

For each attempt, we collect:
- The logs (`output.log`)
- A copy of the code for that submission (`main.py`)
- The autograder response (`info.json`)

Zip the `attempts` folder for both questions and send it to <cafe.userstudy@gmail.com>.

- Name the sort zip `sort_attempts.zip`
- Name the search zip `search_attempts.zip`

### Qualitative

We will collect qualitative feedback via a Google Form.
Please fill out this form **after** you've sent the quantitative deliverables.

Link to the Google Form: TODO(Batu): Add the link to the survey (Google Form)

## Restrictions

To keep the results accurate, please don't use:

- **LLMs / Code Assistant Tools**:
    This includes ChatGPT, Claude, Gemini, GitHub Copilot, Cursor, or any AI Chat/Autocomplete Tool.
    *Why: We can not tell if improvement came from CAFE or the AI.*

- **Outside Resources**:
    This includes web searches, stack overflow, tutorials, or existing BFS/Bubble Sort implementations.
    *Why: Finding the answer online replaces the debugging we are measuring.*

- **External Help**:
    This includes talking with fellow participants about the questions.
    *Why: Outside help interferes with the CAFE vs. No-CAFE comparison.*

- **Solution / Test Cases Inspection**:
    This study runs on the honor system.
    If you look around the directories, you'll find the reference solutions and test cases.
    They are not hidden and they are not hard to find.
    We're treating you as a collaborator, not an adversary, so we are asking you not to use them.
    *Why: It defeats the point of the study and invalidates CAFE's feedback*

- **Editing Study Resources**:
    Edit ONLY `questions/search/src/main.py` and `questions/sort/src/main.py`.
    Within those files edit only the functions marked with `TODO(participant)`.
    Leave all other study material alone.
    *Why: It breaks CAFE and makes the rounds impossible to compare.*
