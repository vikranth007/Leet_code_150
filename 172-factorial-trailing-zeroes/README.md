<h2><a href="https://leetcode.com/problems/factorial-trailing-zeroes">Factorial Trailing Zeroes</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer <code>n</code>, return <em>the number of trailing zeroes in </em><code>n!</code>.</p>

<p>Note that <code>n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 3! = 6, no trailing zero.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong> 5! = 120, one trailing zero.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you write a solution that works in logarithmic time complexity?</p>


# Solution

# 📦 Why are we counting multiples of 5?
**Because every multiple of 5 contributes at least one 5 to the prime factorization of numbers in 100!. Each of these helps create a trailing zero when paired with a 2.**


# 🧠 Think of it like this:

* `100!` is the product of all numbers from `1 to 100`.

* To find how many times `5` appears as a factor in that product, we:

* Count how many numbers are divisible by `5 → 100 // 5 = 20`

* Then how many divisible by `25 → 100 // 25 = 4`

And so on...

# 🧮 Let's trace with n = 100
# Iteration 1:

n = 100

n = n // 5 = 100 // 5 = 20

count = 0 + 20 = 20

### Interpretation:
There are 20 multiples of 5 between 1 and 100 (i.e., 5, 10, ..., 100), so at least 20 numbers contribute one 5 each.

# Iteration 2:

n = 20

n = n // 5 = 20 // 5 = 4

count = 20 + 4 = 24

`Interpretation:`
Now, we count multiples of 25 (like 25, 50, 75, 100) — each contributes an extra 5. There are 4 such numbers.

# Iteration 3:

n = 4 → loop stops (4 < 5)










