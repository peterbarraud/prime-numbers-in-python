# Primes
I'm writing a Python scrip to find out all `prime numbers` from `1` to `n`

**If you chance upon this, please suggest changes to make it more Pythonic and (of course) faster**

So, this is how I've built it:

For each number in the list, we're going to check if it's divisible by all previous primes.

But only upto the square root of that number (_rounded up_)

These are some timings (_on my Ubnutu_). Using **Python's** `timeit`:
|Number of primes|Time|
|:-: |:-:|
|10000|0.291s|
|20000|1.046s|
|30000|2.219s|
|40000|3.808s|
|50000|5.893s|
|60000|8.5s|
|70000|11.797s|
|80000|15.601s|
|90000|19.657s|
|100000|24.494s|