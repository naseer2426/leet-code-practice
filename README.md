# Common patterns

## Prefix sum

When we want to calculate sum of a sub array, we can optimize it using prefix
sum array

```
psa[i] = sum of all elements until i
```

we can find sum of all elements between i and j by

```
psa[j] - psa[i-1]
```

## 2 Pointers

Sometimes some sub array problems can be solved with this, where we scan the
array with pointers starting at the end and coming towards each other or start
at the middle and go away from each other, choosing which pointer to move based
on a condition that optimizes what we need

- container_with_most_water
- longest palindrome sub array
- longest sub str no repeats
- palindrome
- 3sum
- 3sum_closest
- 4sum
- remove_nth_from_end

## Sliding window

When we need to find subarray that optimizes some quantity, and calculations
between 2 arrays that differ in only 1 element are very linked, then we can use
sliding window to calculate the quantity for each sub array instead of
calculating each sub array independently

## Binary search

When any list with a sortable value can be optimally searched in logn time by
dividing the list into chunks

## BFS

When a graph is searched from root, level by level till we reach the leaf nodes.
Usually use a queue for implementing

- open_lock
- coin_change
- combination_sum

## DFS

When a graph is searched path by path all the way till leaf nodes, usually use
stack to implement

## Backtracking

Essentially same as DFS but more broadly when we have to find the best choice
along a decision tree and we calculate till the end and find the outcome and
backtrack

- letter_combinations

## Priority Queue

Most top k problems should use this pattern, usually use a min or max heap to
implement solutions

## Dynamic Programming

I am yet to find someone who understands this crap. Basically if can break down
the solution of step n as some combination of solution of steps (n-k), (n-m) ...
terms. There are 2 approaches top down and bottom up. Top down is when we start
from what we need to compute and find it by slowly computing its sub problems
till the end. Bottom up is when we start from the most basic sub problem and
build up to what we want. There is also a concept of memoizing the computation
for a particular step so we dont need to redo it if its involved in the solution
of multiple sub steps. I hate this.

- coin_change

## Follow the instructions problems

I dont consider these problems coding problems because time/space complexity is
not the bottleneck of solving the problem, its just the weird egde cases with
the requirements.

- integer_to_roman
- string_to_int
- reverse_int

## Cant place them into any patterns

These are the problems that just have some elegant solution that I cant really
place it into any pattern

- lexocographically_smallest_array
