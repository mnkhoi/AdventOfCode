# Day 1

## Approach

I went with a very brute force approach of getting the input and just subtracting when seeing `L` prefix or adding when there is `R` prefix.
Pretty much followed the instructions given

## Errors Encountered

- I didn't account for cases where the input could go over 2 digits (3 digits)
- I went too quickly and have not thought about the case where it would result in a `curr` of negative and wrap around to 100  
My initial solution for this problem was to use `abs()` -> which is incorrect.

## Things to improve

- Slow down when reading the question
- Think through the test cases
- Think about the possible inputs and ask clarification
