# Repository for CAFE Prototype User Study

This repository contains resources for a prototype user study (proto-study) for the CAFE framework.

## Background & Context

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
If you are new to Python environments,
We recommend that you try to only have one version of Python installed on your machine at a time
(it is possible to have multiple version, but that can get pretty confusing).

To check your already installed Python version, use:
```sh
python3 -V
```

### Virtual Environments

In Python, code that is not your own or apart of the [Python standard library](https://docs.python.org/3/library/index.html)
is considered a third-party package (sometimes just shortened to "Python packages" or just "packages").
Each package can be associated with different versions and require specific versions of other packages as dependencies.
Since it can be hard (or maybe even impossible) to get a set of packages that satisfy the versions of every package needed, we use a tool called
[virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment),
or "venvs" for short.
Virtual environments lets you create as many environments as you want and install a different set of packages (or package versions) to each venv (you can even use different versions of Python).

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

Now you may notice that your shell prompt has changed, this is a sign that the venv is working.
With your venv activated, any packages you install will automatically be installed to the venv,
and any packages used/imported will come from the venv.

If you want to stop using the venv, you can just deactivate it at any time:
```sh
deactivate
```

Note that your shell prompt should have changed back.
Your venv can be re-activated at any time in the same way as before.

### Required Packages

This repository includes a `requirements.txt` file listing every package
the proto-study needs. First make sure your virtual environment is active
(step 2), then install everything in one go:
```sh
pip3 install -r requirements.txt
```

This assumes you're in the same directory as the requirements file. If
you're somewhere else, just point at it — for example `../requirements.txt`
if you're one directory down.

You can use a different environment/packaging tool (like Conda) if you
prefer, but the instructions here assume the standard venv + pip flow.

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

## Overview

The purpose of this proto-study is to assess whether a full-scale study evaluating the effectiveness of the CAFE framework would be feasible.
Participants will be asked to debug buggy code both with and without CAFE.
Each participant will complete two rounds and serves as their own baseline, meaning we will compare each person with themselves across the two rounds.
So variables that vary between people, e.g., coding skill, prior experience, and language familiarity stay constant across both rounds.
Eliminating some of these variables make observing whether CAFE helps when debugging easier.

## Study Flow

Participants will be divided into four approximately equal sized groups, each defined by the task and setup they start with.
The task is the problem they will debug (BFS or minimax), and the setup is whether they will use CAFE (experimental) or not (control).
In the first round, participants will debug their groups assigned task with their groups given setup.
In the second round, they will switch to the opposite of both: the other task and the other setup.
Someone who starts on BFS without CAFE will move to minimax with CAFE, and so on.

| Group |     Round 1       |     Round 2       |
|:-----:|:-----------------:|:-----------------:|
| 1     | BFS & No CAFE     | Minimax & CAFE    |
| 2     | BFS & CAFE        | Minimax & No CAFE |
| 3     | Minimax & No CAFE | BFS & CAFE        |
| 4     | Minimax & CAFE    | BFS & No CAFE     |


These four groups cover every permutation of starting task and starting setup.
This counterbalancing lets us account for biases such as order effects and differences in task difficulty.
We expect these biases to average out across the groups.
