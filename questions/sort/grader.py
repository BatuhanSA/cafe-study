#!/usr/bin/env python3

import sys
import traceback

import autograder.assignment
import autograder.question
import autograder.cmd.gradeassignment

import cafe.explainer
import cafe.settings

class BubbleSort(autograder.assignment.Assignment):
    def __init__(self,  **kwargs):
        input_dir = kwargs.get('input_dir', '.')
        super().__init__(
            questions = [
                TC1(2, 'simple', timeout=None),
            ],
            additional_data = {"input_dir": input_dir},
            **kwargs)

class TC1(autograder.question.Question):
    def score_question(self, submission, input_dir):
        arr = [1,8,3,9,4,7,1,8,3,4,8,1,2,0,1,0,2,9,4,0]
        sorted_arr = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 7, 8, 8, 8, 9, 9]

        try:
            submission.__all__.TrackedList.num_comps = 0
            tracked_arr = submission.__all__.TrackedList(arr)
            tracked_arr.bubble_sort()

            student_sorted_arr = tracked_arr.get_list()
            actual_num_comps = tracked_arr.get_num_comps()

        except NotImplementedError:
            self.fail('NotImplementedError')

        expected_num_comps = 342

        if (actual_num_comps == expected_num_comps and arr == sorted_arr):
            self.full_credit()
        else:
            feedback = ""
            if (not arr == sorted_arr):
                feedback += f"The list is not sorted.\nExpected: {sorted_arr}\nActual: {arr}\n"
            else:
                feedback = f"Wrong efficiency.\n"

            if (cafe.settings.is_generate_feedback_enabled()):
                feedback += cafe.explainer.generate_feedback(input_dir, BubbleSort, self, "solution_profile.json")

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
