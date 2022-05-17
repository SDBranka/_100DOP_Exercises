# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Optional:
# The 4-space rule is optional for continuation lines.
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)

# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional 
# continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

# The closing brace/bracket/parenthesis on 
# multiline constructs may either line up under 
# the first non-whitespace character of the last 
# line of list, as in:
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# or it may be lined up under the first character 
# of the line that starts the multiline construct, as in:
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# Following the tradition from mathematics usually 
# results in more readable code:
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# Imports should usually be on separate lines:
# Correct:
import os
import sys

# Wrong:
import sys, os

# It’s okay to say this though:
# Correct:
from subprocess import Popen, PIPE


