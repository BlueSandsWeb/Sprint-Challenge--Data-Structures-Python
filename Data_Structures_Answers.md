Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method? 

    Constant runtime, O(1).  The ring buffer keeps track of it's current index and swaps the item in memory.
    
2. What is the space complexity of your ring buffer's `append` function? 

    O(1) because it only swaps in a new value to the memory that's already been allocated

3. What is the runtime complexity of your ring buffer's `get` method?

    O(n), because the function iterates over the entire array.

4. What is the space complexity of your ring buffer's `get` method?

    O(n), because it stores each item from the storage array in a new array.

5. What is the runtime complexity of the provided code in `names.py`?

    (names_1 into array)+(names_2 into array)+(outer loop)*(inner loop)+(check and append to new array)
              m         +           n        +      m     *     n      +            2
    O(m+n+(m*n)+2) =>
    ANSWER: O(m*n) or in this case because it's two arrays of the same size O(n^2)

6. What is the space complexity of the provided code in `names.py`?

    O(n+m)

7. What is the runtime complexity of your optimized code in `names.py`?

    O(n+m) => O(n)

8. What is the space complexity of your optimized code in `names.py`?

    O(n+m) => O(n)