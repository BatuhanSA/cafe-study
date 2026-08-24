#!/usr/bin/env python3

import sys
import traceback

import autograder.assignment
import autograder.question
import autograder.cmd.gradeassignment

import cafe.explainer
import cafe.settings

class BFS(autograder.assignment.Assignment):
    def __init__(self,  **kwargs):
        input_dir = kwargs.get('input_dir', '.')
        super().__init__(
            questions = [
                TC1(1, 'Cycle', timeout = None),
            ],
            additional_data = {"input_dir": input_dir},
            **kwargs)

class TC1(autograder.question.Question):
    def score_question(self, submission, input_dir):
        student_bfs = submission.__all__.BFS
        Node = submission.__all__.Node

        S = Node("S")
        A = Node("A")
        B = Node("B")
        C = Node("C")
        G = Node("G")

        S.neighbors.append(A)
        A.neighbors.append(S)

        S.neighbors.append(B)
        B.neighbors.append(S)

        A.neighbors.append(C)
        C.neighbors.append(A)

        B.neighbors.append(C)
        C.neighbors.append(B)

        C.neighbors.append(G)
        G.neighbors.append(C)

        try:
            submission.__all__.Queue.nodes_expanded = 0
            student_path = student_bfs(S, G)
        except NotImplementedError:
            self.fail('NotImplementedError')

        expected_expanded_count = 4
        actual_expanded_count = submission.__all__.Queue.nodes_expanded

        if (actual_expanded_count == expected_expanded_count  and student_path == ["S", "A", "C", "G"]):
            self.full_credit()
        else:
            feedback = f"Wrong number of nodes expanded.\n"

            if (cafe.settings.is_generate_feedback_enabled()):
                feedback += cafe.explainer.generate_feedback(input_dir, BFS, self, "solution_profile.json")

            self.fail(feedback)

def main():
    parser = autograder.cmd.gradeassignment._get_parser()

    group = parser.add_argument_group('CAFE Options')

    group.add_argument('--enable-cafe-feedback', dest = 'enable_cafe_feedback',
        action = 'store_true', help = 'Enables CAFE to generate feedback.'
    )

    args, _ = parser.parse_known_args()

    cafe.settings.set_generate_feedback_enabled(args.enable_cafe_feedback)

    return autograder.cmd.gradeassignment.run(args)

if (__name__ == '__main__'):
    sys.exit(main())
