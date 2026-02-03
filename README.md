## How to use fairsharer

Fairsharer is an algorithm in which the biggest value gives a share to the left and right neighbors with each iteration.

fair_sharer([List of values], Number of Iteration)

Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

## Installation

To install fairsharer from GitHub repository, do:

```console
git clone https://github.com/libre5/fairsharer.git
cd fairsharer
python -m pip install .
# or on mac: python3 -m pip install .
```

## Documentation

Include a link to your project's full documentation here.


