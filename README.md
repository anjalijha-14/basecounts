# DNA Base Counter
A simple python program that takes a DNA sequence as input and counts the number of **Adenine (A), Thymine (T), Guanine (G), and Cytosine (C)** bases present in the sequence

## Features
-Accepts DNA sequence as input.
-supports multi-line DNA sequence input.
-Converts sequence to uppercase automatically.
-Checks whether sequence contains only valid bases- 'A', 'T', 'G' and 'C'.
-Counts the number of each nucleotide.
-Provides an error message for empty or invalid input.

## How It Works
1. The user enters a DNA sequence.
2. Multiple lines can be entered, with an empty line indicating the end of the sequence.
3. The individual lines are joined together to form one sequence.
4. The sequence is converted to uppercase.
5. The program checks whether all characters are valid DNA bases.
6. If the input is valid, the program counts each base using Python's `count()` method.
7. The number of A, T, G, and C bases is displayed.

## Example
### Input
```text
ENTER THE DNA SEQUENCE (paste it, then Enter on an empty line when done.)
ATGCGATCGATCG

### Output
Number of Adenine bases in the sequence is 3.
Number of Guanine bases in the sequence is 4.
Number of Cytosine bases in the sequence is 3.
Number of Thymine bases in the sequence is 3.
