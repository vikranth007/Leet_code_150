<h2><a href="https://leetcode.com/problems/palindrome-number">Palindrome Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span data-keyword="palindrome-integer"><em><strong>palindrome</strong></em></span><em>, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?











## 🧠 Step-by-step for 121:

Start:

original = 121

reversed_num = 0

## First Loop:

digit = 121 % 10 = 1 ← (last digit)

reversed_num = 0 * 10 + 1 = 1

number = 121 // 10 = 12

## Second Loop:

digit = 12 % 10 = 2

reversed_num = 1 * 10 + 2 = 12

number = 12 // 10 = 1

## Third Loop:

digit = 1 % 10 = 1

reversed_num = 12 * 10 + 1 = 121

number = 1 // 10 = 0

Compare:

reversed_num = 121

original = 121

## ✅ Equal → It’s a palindrome

