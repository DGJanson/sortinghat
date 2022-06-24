Category switcher
=================

Not sure what to call this, but a small exercise to perform a kind of sorting to divide a bunch of choices as equally as possible. The reason for this exercise was a situation at work: for an activity people were given four choices, the activity had two timeslots. Everyone could choose 2 of the options. The goal was to make sure everyone got their choices and for each activity the number of participants should be the same in the first timeslot and the second timeslot.

The data is structured as follows. The input is a list of tuples. With each tuple containing, in this order:

- an id 
- first choice
- second choice

The choices are arbitrary (numbers, categories, anything), but they can never be the same (first choice != second choice). The id is irrelevant, but can be used to connect it to other data if you so desire.

Example python. There are four options (0, 1, 2, 3).

```python
list = [
    (1, 0, 1),
    (2, 1, 2),
    (3, 2, 3),
    (4, 1, 2) #etc
]
```

We can convert this to csv (and import from it as well)

```
1;0;1
2;1;2
3;2;3
4;1;2
```

The goal of this script is to make sure that the options are divided equally in the first choice and second choice columns. For example, if 10 out of 16 rows have "chosen" 0 (in first or second choice, does not matter) we want a result with 5 0's in first column and 5 0's in second column. And for the other options the same equal distribution. We cannot change the choices of rows.

Solution
--------

The solution is a simple divide and conquer approach. See [merge-sort](https://en.wikipedia.org/wiki/Merge_sort). Instead of sorting, every iteration we check if switching the choice columns improves our score. The score is based on the difference, for each option, between the first and second column. For example in one iteration we may have:

```python
('a', 0, 1)
('b', 0, 1)
```

The score is calculated by counting the options per column. First column increases the count, second column decreases the count. So in above example we would have:

- 0 has a score of 2
- 1 has a score of -2

The total score can be calculated as the **absolute** sum of the score. | 2 | + | -2 | = 4 in this case. The script then iterates over the entries and checks if the score **decreases** if you flip the columns. In the example the first row is flipped, since the score decreases by 4. The next row will not be flipped, since this will increase the score again:

```python
('a', 1, 0)
('b', 0, 1)
```

The locally 'optimized' parts are merged every round and optimized again as above, like merge sort. The eventual result is a list with an equal distribution, for each option, between the first and second column.

Results
-------

The algorithm seems to work as intended. I am not sure if it guarantees 100 % correctness. In some small sets it does not reach optimal scores, but in small sets it may also be impossible to reach an optimum, especially when there are many categories.

Performance is decent. I think similar to merge sort (n log(n)). The score calculation in a dict and the copy to check if it changes is not ideal, there is room for optimization there. Memory usage is very low, since the input list can be changed in place, no copies necessary.

Usage
=====

Simple python package. Does not depend on any libraries.

The small package has two entry points. The main entry point is simply the main:

```
python -m sortinghat -h
```

This opens the help. There are some flags you can pass, like a file to import from or some parameters for random data generation.

The other entry point is for random data generation:

```
python -m sortinghat.testdata -h
```

Will open help again. This can generate a random test file based on the above format. The ID is simply an incrementing int and the categories are ints from 0 to \[maxCategories\]. There are some options, like the number of rows and the number of categories. The distribution of categories is assigned somehwat randomly, so the 0 option may be chosen more often than the 1 option. 