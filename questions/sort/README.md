# Bubble Sort

A debugging task for the CAFE proto-study.
The participants are given a buggy implementation of Bubble Sort.
They debug it so that it passes the test case.

## Overview

The file [src/main.py](./src/main.py) contains an implementation of Bubble Sort over a list of integers.
It does not currently pass the test case.
Your task is to find and fix the bug so the submission passes the test case.

## Files

| File/Directory                 | Purpose                                                         |
|:------------------------------ |:--------------------------------------------------------------- |
| `src/main.py`                  | The code you edit.                                              |
| `grader.py`                    | Autograder assignment/question definitions. **Do not look.**    |
| `assignment_control.json`      | Assignment config for the control (no-CAFE) run.                |
| `assignment_experimental.json` | Assignment config for the experimental (CAFE) run.              |
| `setup.sh`                     | Generates the solution profile used by CAFE.                    |
| `grade_control.sh`             | Grades your submission without CAFE feedback.                   |
| `grade_experimental.sh`        | Grades your submission with CAFE feedback enabled.              |
| `test-submissions/`            | Reference submissions. **Do not look.**                         |

## Problem

Bubble Sort is a comparison based sorting algorithm that iterates the list and compares each pair of adjacent elements.
It swaps the adjacent elements if they are in the wrong order.
It repeats this process until the list is sorted.

Only modify the sections marked with `TODO` in the [src/main.py](./src/main.py).

## Example

The autograder uses a single small list:
```
Input:  [3, 1, 2]
Output: [1, 2, 3]
```

## Submitting an Attempt

Run all commands from this directory, inside your activated virtual environment
(see the repository root `README.md` for venv/requirements setup).
Each grading run logs a numbered attempt (submission copy + output log) under `attempts/`.

**Follow the instructions for your assigned group only.**

NOTE: To keep both implementations simple, we did not include a fail-safe for infinite loops.
If your code takes unusually long to finish after submission, it may be stuck in an infinite loop.
You can press Ctrl+C to stop it.

### Control group (without CAFE)

```bash
./grade_control.sh
```

When ever you want to submit an attempt you can run the `grade_control.sh` script.
It will grade your current `src/main.py` and print autograder feedback.

### Experimental group (with CAFE)

Before you start debugging run the `setup.sh` once, it will produce `solution_profile.json`.
CAFE will use this file later so make sure you run this command.

```bash
# Build the solution profile.
./setup.sh
```

When ever you want to submit an attempt you can run the `grade_experimental.sh` script.
It will grade your current `src/main.py` and print autograder feedback and CAFE feedback.

```bash
./grade_experimental.sh
```

Note: The experimental run will take a little longer than usual due to profiling overhead. Thank you for your patience.

## Requirements

- Python >= 3.10
- Packages from the repository-root `requirements.txt`
