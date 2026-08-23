# Breadth First Search

A debugging task for the CAFE proto-study.
The participants are given a buggy implementation of Breadth First Search (BFS).
They debug it so that it passes the test case(s).

## Overview

The file [src/main.py](./src/main.py) contains an implementation of BFS over an undirected graph.
It does not currently produce the expected result.
Your task is to find and fix the bug so the submission passes the test case(s).

## Files

| File/Directory                 | Purpose                                                         |
|:------------------------------:|:--------------------------------------------------------------- |
| `src/main.py`                  | The code you edit. Contains `Node`, `Queue`, and `BFS`.         |
| `grader.py`                    | Autograder assignment/question definitions. **Do not look.**    |
| `assignment_control.json`      | Assignment config for the control (no-CAFE) run.                |
| `assignment_experimental.json` | Assignment config for the experimental (CAFE) run.              |
| `setup.sh`                     | Generates the solution profile used by CAFE.                    |
| `grade_control.sh`             | Grades your submission without CAFE feedback.                   |
| `grade_experimental.sh`        | Grades your submission with CAFE feedback enabled.              |
| `test-submissions/`            | Reference submissions **Do not look.**                          |

## Problem

Breadth First Search (BFS) is a graph traversal algorithm that explores nodes level by level, starting from a source node.
It first visits the source, then all nodes one edge away, then all nodes two edges away, and so on.
It uses a queue (FIFO) to decide which node to expand next.

Depending on the source consulted, the definition of an expanded node can vary.
For the purposes of this proto-study, we consider a node to be expanded when it is removed from the queue and its neighbors are examined.

Because BFS expands nodes in increasing order of their distance from the source,
the first time it reaches the goal, it has found a path containing the fewest possible edges.
In an unweighted graph, this is a shortest path.
(The path itself is recovered by storing a parent pointer for each node as it is discovered,
then following those pointers back from the goal to the source.)

### Input/Output

- **Input**
  - `initial_node`: The `Node` to start the search from.
  - `goal_node`: The `Node` to search for.

- **Output**
  - A list of node **labels** describing the path from the start to the goal, inclusive of both start and end nodes.

## Submitting an Attempt

Run all commands from this directory, inside your activated virtual environment
(see the repository root `README.md` for venv/requirements setup).
Each grading run logs a numbered attempt (submission copy + output log) under `attempts/`.

**Follow the instructions for your assigned group only.**

### Control group (without CAFE)

```bash
./grade_control.sh
```

When ever you want to submit to the grader you can run the `grade_contorl.sh` script.
It will grade your current `src/main.py` and print autograder feedback.

### Experimental group (with CAFE)

Before you start debugging run the `setup.sh` once, it will produce `solution_profile.json`.
CAFE will use this file later so make sure you run this command.

```bash
# Build the solution profile.
./setup.sh
```

When ever you want to submit to the grader you can run the `grade_experimental.sh` script.
It will grade your current `src/main.py` and print autograder feedback and CAFE feedback.

```bash
./grade_experimental.sh
```

### After You're Done

- TODO(Batu): Provide a script to zip the `attempts` directory, or write manual zip instructions.
- TODO(Batu): Add the email address for participants to send the zip to.

## Requirements

- Python >= 3.10
- Packages from the repository-root `requirements.txt`
