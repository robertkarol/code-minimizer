# Context of the problem solved
When we are doing testing, we sometimes rely on code coverage as a measure of
how good our testing is. It has proven to me that this metric can be tricked sometimes.

# Solution description
The solution I propose takes a different approach, by asking
"How much code can I delete without changing the outcome of my tests?".
So, the algorithm created tries to mizimize the source code without breaking tests.
So, the "before vs. after" comparison will show what lines can be deleted without affecting
the tests, which mean that this can uncover false code coverages.

# Technical solution
Translating it in technical terms, we have a set of lines and we need to find the optimal subset.
So, this is a subset problem => navigating all solutions would be have a complexity of O(2^n).
Therefore, this problem is a good candidate for a genetic algorithm. 
See "code_minimizer.py" for the GA solution.
For each possible solution, we alter the source code, run tests, and check that all have passed.

# Limitations
- the algorithm is sensitive when it comes to blank lines (didn't handle it in formatting)
- the unit tests need to dynamically import the module tested and reload it at each execution
- naming conventions are assumed: test file should have the code file's name, with "_test" as suffix and
the solution's output is written in a file having the code file's name, with "sol_" suffix
- canceling the algorithm would mean that the file will need to be manually restored from
the ".backup" file created
