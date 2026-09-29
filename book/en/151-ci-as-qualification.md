# 151. CI as qualification

A commit is not the same thing as a passing test.

In M6.10 we therefore used GitHub Actions as the external qualification mechanism for the example bot. The matrix runs Python 3.11, 3.12 and 3.13, and all three must be green before the milestone receives PASS status.

This mattered in practice: the first real run exposed regressions that should not be hidden behind an assumption that the tests probably passed.

The rule is simple: **observe the result before declaring PASS**.
