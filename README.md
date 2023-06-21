# Enigmata
Much of the Codex is firewalled behind a polymorphic security barrier I now know to be the Enigmata - algorithmic mind puzzles, stress tests of the psyche. Rites of passage, perhaps, for those who would dare to seek deeper.

So it is that if I am to continue my journey, I must first master these dark ways. I must master the Enigmata:

```
├── aoc         Advent of Code solutions and notes.
├── leetcode    LeetCode solutions and notes.
└── tools       Tools for automating problem acquisition, problem review, and progress tracking.
    ├── dsa        Personal implementations of common data structures and algorithms.
    └── tests      Unit tests.
```

### Contents
<!-- MarkdownTOC levels="1,2,3" -->

- [LeetCode](#leetcode)
  + [Stats](#stats)
  + [Problems<sub>n</sub>](#problemsn)
  + [Milestones](#milestones)
  + [Solution Log / Notes](#solution-log--notes)

<!-- /MarkdownTOC -->
<!-- ───────────────────────────────────────────────────────────────────────────── -->

## LeetCode
### Stats
|  Date   | Total Solved / Available (%) |  Rank   |
|:-------:|:----------------------------:|:-------:|
| 2023 Q2 |      105 / 2742 (3.8%)       | 618,923 |
| 2023 Q1 |      104 / 2552 (4.1%)       | 560,441 |
| 2022 Q4 |      103 / 2489 (4.1%)       | 540,579 |
| 2022 Q3 |       66 / 2426 (2.7%)       | 722,788 |
| 2022 Q2 |       44 / 2291 (1.9%)       | 796,594 |
| 2022 Q1 |       40 / 2227 (1.8%)       | 790,820 |

### Problems<sub>n</sub>
n = times solved. I use [Anki](https://apps.ankiweb.net/) to schedule daily reviews and practice re-solving past problems.
<!-- Problem table -->
<table>
  <tr>
    <td align="center"><a href="#1-two-sum-solutions">1</a><sub>9</sub></td>
    <td align="center"><a href="#3-longest-substring-without-repeating-characters-solutions-">3</a><sub>18</sub></td>
    <td align="center"><a href="#9-palindrome-number-solutions-">9</a><sub>9</sub></td>
    <td align="center"><a href="#11-container-with-most-water-solutions">11</a><sub>10</sub></td>
    <td align="center"><a href="#14-longest-common-prefix-solutions-">14</a><sub>9</sub></td>
    <td align="center"><a href="#15-3sum-solutions">15</a><sub>13</sub></td>
    <td align="center"><a href="#16-3sum-closest-solutions-">16</a><sub>6</sub></td>
    <td align="center"><a href="#18-4sum-solutions">18</a><sub>9</sub></td>
    <td align="center"><a href="#19-remove-nth-node-from-end-of-list-solutions">19</a><sub>13</sub></td>
    <td align="center"><a href="#20-valid-parentheses-solutions">20</a><sub>12</sub></td>
    <td align="center"><a href="#25-reverse-nodes-in-k-group-solutions-">25</a><sub>8</sub></td>
    <td align="center"><a href="#26-remove-duplicates-from-sorted-array-solutions-">26</a><sub>9</sub></td>
    <td align="center"><a href="#30-substring-with-concatenation-of-all-words-solutions-">30</a><sub>8</sub></td>
    <td align="center"><a href="#33-search-in-rotated-sorted-array-solutions">33</a><sub>14</sub></td>
    <td align="center"><a href="#34-find-first-and-last-position-of-element-in-sorted-array-solutions">34</a><sub>4</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#41-first-missing-positive-solutions-">41</a><sub>5</sub></td>
    <td align="center"><a href="#48-rotate-image-solutions">48</a><sub>15</sub></td>
    <td align="center"><a href="#49-group-anagrams-solutions-">49</a><sub>8</sub></td>
    <td align="center"><a href="#53-maximum-subarray-solutions">53</a><sub>11</sub></td>
    <td align="center"><a href="#56-merge-intervals-solutions">56</a><sub>14</sub></td>
    <td align="center"><a href="#57-insert-interval-solutions-">57</a><sub>7</sub></td>
    <td align="center"><a href="#61-rotate-list-solutions">61</a><sub>9</sub></td>
    <td align="center"><a href="#75-sort-colors-solutions">75</a><sub>11</sub></td>
    <td align="center"><a href="#76-minimum-window-substring-solutions">76</a><sub>13</sub></td>
    <td align="center"><a href="#78-subsets-solutions-">78</a><sub>1</sub></td>
    <td align="center"><a href="#88-merge-sorted-array-solutions-">88</a><sub>9</sub></td>
    <td align="center"><a href="#92-reverse-linked-list-ii-solutions">92</a><sub>9</sub></td>
    <td align="center"><a href="#102-binary-tree-level-order-traversal-solutions">102</a><sub>5</sub></td>
    <td align="center"><a href="#103-binary-tree-zigzag-level-order-traversal-solutions-">103</a><sub>4</sub></td>
    <td align="center"><a href="#107-binary-tree-level-order-traversal-ii-solutions-">107</a><sub>1</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#111-minimum-depth-of-binary-tree-solutions-">111</a><sub>5</sub></td>
    <td align="center"><a href="#112-path-sum-solutions">112</a><sub>5</sub></td>
    <td align="center"><a href="#113-path-sum-ii-solutions">113</a><sub>4</sub></td>
    <td align="center"><a href="#116-populating-next-right-pointers-in-each-node-solutions-">116</a><sub>7</sub></td>
    <td align="center"><a href="#121-best-time-to-buy-and-sell-stock-solutions">121</a><sub>9</sub></td>
    <td align="center"><a href="#124-binary-tree-maximum-path-sum-solutions">124</a><sub>4</sub></td>
    <td align="center"><a href="#129-sum-root-to-leaf-numbers-solutions-">129</a><sub>6</sub></td>
    <td align="center"><a href="#136-single-number-solutions">136</a><sub>5</sub></td>
    <td align="center"><a href="#137-single-number-ii-solutions">137</a><sub>5</sub></td>
    <td align="center"><a href="#141-linked-list-cycle-solutions-">141</a><sub>11</sub></td>
    <td align="center"><a href="#142-linked-list-cycle-ii-solutions-">142</a><sub>5</sub></td>
    <td align="center"><a href="#143-reorder-list-solutions">143</a><sub>5</sub></td>
    <td align="center"><a href="#152-maximum-product-subarray-solutions">152</a><sub>9</sub></td>
    <td align="center"><a href="#153-find-minimum-in-rotated-sorted-array-solutions-">153</a><sub>8</sub></td>
    <td align="center"><a href="#167-two-sum-ii-solutions">167</a><sub>8</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#199-binary-tree-right-side-view-solutions-">199</a><sub>3</sub></td>
    <td align="center"><a href="#200-number-of-islands-solutions">200</a><sub>11</sub></td>
    <td align="center"><a href="#202-happy-number-solutions-">202</a><sub>5</sub></td>
    <td align="center"><a href="#206-reverse-linked-list-solutions">206</a><sub>12</sub></td>
    <td align="center"><a href="#209-minimum-size-subarray-sum-solutions-">209</a><sub>10</sub></td>
    <td align="center"><a href="#215-kth-largest-element-in-an-array-solutions-">215</a><sub>5</sub></td>
    <td align="center"><a href="#217-contains-duplicate-solutions">217</a><sub>8</sub></td>
    <td align="center"><a href="#234-palindrome-linked-list-solutions">234</a><sub>5</sub></td>
    <td align="center"><a href="#238-product-of-array-except-self-solutions">238</a><sub>13</sub></td>
    <td align="center"><a href="#242-valid-anagram-solutions">242</a><sub>8</sub></td>
    <td align="center"><a href="#253-meeting-rooms-ii-solutions">253</a><sub>6</sub></td>
    <td align="center"><a href="#259-3sum-smaller-solutions">259</a><sub>8</sub></td>
    <td align="center"><a href="#260-single-number-iii-solutions-">260</a><sub>8</sub></td>
    <td align="center"><a href="#268-missing-number-solutions-">268</a><sub>8</sub></td>
    <td align="center"><a href="#285-inorder-successor-in-bst-solutions">285</a><sub>5</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#340-longest-substring-with-at-most-k-distinct-characters-solutions-">340</a><sub>9</sub></td>
    <td align="center"><a href="#347-top-k-frequent-elements-solutions-">347</a><sub>4</sub></td>
    <td align="center"><a href="#358-rearrange-string-k-distance-apart-solutions">358</a><sub>3</sub></td>
    <td align="center"><a href="#392-is-subsequence-solutions-">392</a><sub>5</sub></td>
    <td align="center"><a href="#417-pacific-atlantic-water-flow-solutions">417</a><sub>9</sub></td>
    <td align="center"><a href="#424-longest-repeating-character-replacement-solutions">424</a><sub>8</sub></td>
    <td align="center"><a href="#437-path-sum-iii-solutions">437</a><sub>7</sub></td>
    <td align="center"><a href="#438-find-all-anagrams-in-a-string-solutions-">438</a><sub>7</sub></td>
    <td align="center"><a href="#442-find-all-duplicates-in-an-array-solutions-">442</a><sub>6</sub></td>
    <td align="center"><a href="#448-find-all-numbers-disappeared-in-an-array-solutions-">448</a><sub>6</sub></td>
    <td align="center"><a href="#451-sort-characters-by-frequency-solutions-">451</a><sub>4</sub></td>
    <td align="center"><a href="#457-circular-array-loop-solutions">457</a><sub>10</sub></td>
    <td align="center"><a href="#476-number-complement-solutions-">476</a><sub>1</sub></td>
    <td align="center"><a href="#543-diameter-of-binary-tree-solutions">543</a><sub>4</sub></td>
    <td align="center"><a href="#560-subarray-sum-equals-k-solutions">560</a><sub>6</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#567-permutation-in-string-solutions-">567</a><sub>8</sub></td>
    <td align="center"><a href="#581-shortest-unsorted-continuous-subarray-solutions">581</a><sub>9</sub></td>
    <td align="center"><a href="#621-task-scheduler-solutions-">621</a><sub>3</sub></td>
    <td align="center"><a href="#647-palindromic-substrings-solutions-">647</a><sub>10</sub></td>
    <td align="center"><a href="#658-find-k-closest-elements-solutions">658</a><sub>5</sub></td>
    <td align="center"><a href="#702-search-in-a-sorted-array-of-unknown-size-solutions-">702</a><sub>4</sub></td>
    <td align="center"><a href="#703-kth-largest-element-in-a-stream-solutions-">703</a><sub>4</sub></td>
    <td align="center"><a href="#704-binary-search-solutions-">704</a><sub>6</sub></td>
    <td align="center"><a href="#713-subarray-product-less-than-k-solutions">713</a><sub>11</sub></td>
    <td align="center"><a href="#744-find-smallest-letter-greater-than-target-solutions-">744</a><sub>4</sub></td>
    <td align="center"><a href="#759-employee-free-time-solutions">759</a><sub>5</sub></td>
    <td align="center"><a href="#767-reorganize-string-solutions">767</a><sub>4</sub></td>
    <td align="center"><a href="#832-flipping-an-image-solutions-">832</a><sub>7</sub></td>
    <td align="center"><a href="#844-backspace-string-compare-solutions">844</a><sub>7</sub></td>
    <td align="center"><a href="#852-peak-index-in-a-mountain-array-solutions-">852</a><sub>3</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#876-middle-of-the-linked-list-solutions-">876</a><sub>5</sub></td>
    <td align="center"><a href="#895-maximum-frequency-stack-solutions-">895</a><sub>2</sub></td>
    <td align="center"><a href="#904-fruit-into-baskets-solutions-">904</a><sub>8</sub></td>
    <td align="center"><a href="#973-k-closest-points-to-origin-solutions-">973</a><sub>4</sub></td>
    <td align="center"><a href="#977-squares-of-a-sorted-array-solutions-">977</a><sub>7</sub></td>
    <td align="center"><a href="#986-interval-list-intersections-solutions">986</a><sub>5</sub></td>
    <td align="center"><a href="#1004-max-consecutive-ones-iii-solutions-">1004</a><sub>10</sub></td>
    <td align="center"><a href="#1009-complement-of-base-10-integer-solutions">1009</a><sub>5</sub></td>
    <td align="center"><a href="#1060-missing-element-in-sorted-array-solutions-">1060</a><sub>5</sub></td>
    <td align="center"><a href="#1095-find-in-mountain-array-solutions-">1095</a><sub>4</sub></td>
    <td align="center"><a href="#1167-minimum-cost-to-connect-sticks-solutions">1167</a><sub>4</sub></td>
    <td align="center"><a href="#1430-root-to-leaf-sequence-solutions-">1430</a><sub>7</sub></td>
    <td align="center"><a href="#1481-least-number-of-unique-integers-after-k-removals-solutions-">1481</a><sub>5</sub></td>
    <td align="center"><a href="#1539-kth-missing-positive-number-solutions-">1539</a><sub>5</sub></td>
    <td align="center"></td>
  </tr>
</table>
<!-- Problem table -->

### Milestones
- yyyy/mm/dd - Finished [Grokking equivalency list 2020](https://gist.github.com/tykurtz/3548a31f673588c05c89f9ca42067bc4).
- yyyy/mm/dd - Finished [Grokking equivalency list 2022](https://github.com/navidre/new_grokking_to_leetcode).
- yyyy/mm/dd - ???
- yyyy/mm/dd - Profit!

### Solution Log / Notes
_Initial Solution Legend_
-     : _No independent solution._
- 🙃 : _Solved independently with suboptimal time or space complexity._
- 😎 : _Solved independently with optimal time and space complexity._
- 🤯 : _Solved in novel or substantially cleaner/faster way than currently posted alternatives._

<!-- Sub-READMEs -->
#### [1. Two Sum](https://leetcode.com/problems/two-sum/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/))
Solutions that are O(n^2) and O(1) in time and space, respectively, can often be improved to be O(n) in both time and space. In most cases, space is cheap, while time is precious.

|    Date    | Think |  Code  | Total |                                              Solution                                               |
|:----------:|:-----:|:------:|:-----:|:---------------------------------------------------------------------------------------------------:|
| 2022/01/20 |   ∞   |   ∞    |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum.py)       |
| 2022/01/20 |   –   |  2:02  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-01-20.py) |
| 2022/01/23 |   –   |  4:03  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-01-23.py) |
| 2022/01/31 |   –   |  1:59  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-01-31.py) |
| 2022/02/22 |   –   | 10:00+ |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-02-22.py) |
| 2022/04/08 |   –   |  2:11  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-04-08.py) |
| 2022/06/15 |   –   |  6:02  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-06-15.py) |
| 2022/06/25 |   –   |  2:11  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-06-25.py) |
| 2022/08/10 |   –   |  2:10  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1.%20Two%20Sum/two_sum_2022-08-10.py) |

#### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/)) 🙃

|    Date    | Think | Code | Total |                                                                           Solution                                                                           |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/06 |   ∞   |  ∞   |   ∞   |       [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring.py)        |
| 2022/03/07 |   –   | 3:26 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-03-07.py)  |
| 2022/03/10 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-03-10.py)  |
| 2022/03/12 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-03-12.py)  |
| 2022/03/12 |   –   | 3:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-03-12_2.py) |
| 2022/03/15 |   –   | 4:25 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-03-15.py)  |
| 2022/04/13 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-04-13.py)  |
| 2022/08/12 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-08-12.py)  |
| 2022/08/14 |   –   | 7:01 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-08-14.py)  |
| 2022/08/18 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-08-18.py)  |
| 2022/08/20 |   –   | 5:23 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-08-20.py)  |
| 2022/08/23 |   –   | 1:33 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-08-23.py)  |
| 2022/08/31 |   –   | 5:39 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-08-31.py)  |
| 2022/09/21 |   –   | 5:48 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-09-21.py)  |
| 2022/09/22 |   –   | 2:44 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-09-22.py)  |
| 2022/09/26 |   –   | 1:52 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-09-26.py)  |
| 2022/10/05 |   –   | 1:29 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-10-05.py)  |
| 2022/10/24 | 0:22  | 2:32 | 2:54  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/3.%20Longest%20Substring%20Without%20Repeating%20Characters/longest_substring_2022-10-24.py)  |

#### [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/)) 😎
Fancy math solution turns out to be surprisingly slow in practice. Silly string solution is easy and fast.

|    Date    | Think | Code | Total |                                                        Solution                                                         |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2022/03/07 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number.py)       |
| 2022/03/08 |   –   | 1:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-03-08.py) |
| 2022/03/12 |   –   | 1:23 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-03-12.py) |
| 2022/04/11 |   –   | 2:10 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-04-11.py) |
| 2022/08/12 |   –   | 2:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-08-12.py) |
| 2022/08/14 |   –   | 0:42 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-08-14.py) |
| 2022/08/18 |   –   | 1:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-08-18.py) |
| 2022/08/30 |   –   | 0:42 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-08-30.py) |
| 2022/09/25 |   –   | 0:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/9.%20Palindrome%20Number/palindrome_number_2022-09-25.py) |

#### [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/))

|    Date    | Think | Code | Total |                                                               Solution                                                               |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/06 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container.py)       |
| 2022/03/07 |   –   | 4:38 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-03-07.py) |
| 2022/03/10 |   –   | 4:01 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-03-10.py) |
| 2022/03/17 |   –   | 3:54 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-03-17.py) |
| 2022/08/11 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-08-11.py) |
| 2022/08/12 |   –   | 1:19 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-08-12.py) |
| 2022/08/18 |   –   | 1:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-08-18.py) |
| 2022/08/26 |   –   | 1:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-08-26.py) |
| 2022/09/17 |   –   | 2:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2022-09-17.py) |
| 2023/01/20 | 1:44  | 6:41 | 8:26  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/11.%20Container%20With%20Most%20Water/largest_container_2023-01-20.py) |

#### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/)) 🙃

|    Date    | Think | Code | Total |                                                          Solution                                                           |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/10 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix.py)       |
| 2022/03/12 |   –   | 2:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-03-12.py) |
| 2022/03/14 |   –   | 2:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-03-14.py) |
| 2022/04/13 |   –   | 2:30 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-04-13.py) |
| 2022/08/21 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-08-21.py) |
| 2022/08/22 |   –   | 1:16 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-08-22.py) |
| 2022/08/26 |   –   | 1:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-08-26.py) |
| 2022/09/07 |   –   | 0:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-09-07.py) |
| 2022/10/01 |   –   | 1:10 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/14.%20Longest%20Common%20Prefix/longest_prefix_2022-10-01.py) |

#### [15. 3Sum](https://leetcode.com/problems/3sum/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/))
I don't like this problem :( . But became easier after learning [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/).

|    Date    | Think |  Code  | Total |                                            Solution                                            |
|:----------:|:-----:|:------:|:-----:|:----------------------------------------------------------------------------------------------:|
| 2022/02/27 |   ∞   |   ∞    |   ∞   |       [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum.py)        |
| 2022/02/28 |   –   | 10:00+ |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-02-28.py)  |
| 2022/03/02 |   –   | 10:00+ |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-03-02.py)  |
| 2022/03/10 |   –   |   ∞    |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-03-10.py)  |
| 2022/03/10 |   –   |  4:55  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-03-10_2.py) |
| 2022/03/13 |   –   |  9:30  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-03-13.py)  |
| 2022/04/06 |   –   |   ≈    |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-04-06.py)  |
| 2022/04/07 |   –   |  8:28  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-04-07.py)  |
| 2022/04/11 |   –   |  5:07  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-04-11.py)  |
| 2022/07/21 |   –   |   ∞    |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-07-21.py)  |
| 2022/08/10 |   –   |  6:02  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-08-10.py)  |
| 2022/09/03 |   –   |  5:57  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-09-03.py)  |
| 2022/10/30 | 1:38  |  7:31  | 9:10  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/15.%203Sum/3sum_2022-10-30.py)  |

#### [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest)) 😎

|    Date    | Think | Code | Total |                                                    Solution                                                    |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------:|
| 2022/03/24 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest/3sum_closest.py)       |
| 2022/08/26 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest/3sum_closest_2022-08-26.py) |
| 2022/08/30 |   –   | 6:46 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest/3sum_closest_2022-08-30.py) |
| 2022/09/04 |   –   | 7:40 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest/3sum_closest_2022-09-04.py) |
| 2022/09/17 |   –   | 6:49 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest/3sum_closest_2022-09-17.py) |
| 2022/10/20 |   –   | 4:53 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/16.%203Sum%20Closest/3sum_closest_2022-10-20.py) |

#### [18. 4Sum](https://leetcode.com/problems/4sum/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum))

|    Date    | Think | Code  | Total |                                           Solution                                           |
|:----------:|:-----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------:|
| 2022/09/07 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum.py)       |
| 2022/09/07 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-09-07.py) |
| 2022/09/09 |   –   | 5:39  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-09-09.py) |
| 2022/09/14 |   –   | 6:13  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-09-14.py) |
| 2022/09/25 |   –   | 7:34  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-09-25.py) |
| 2022/10/24 | 1:09  | 10:25 |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-10-24.py) |
| 2022/10/25 | 0:09  | 5:51  | 6:00  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-10-25.py) |
| 2022/10/28 | 0:15  | 4:49  | 5:04  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-10-28.py) |
| 2022/11/03 | 0:39  | 5:02  | 5:41  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/18.%204Sum/4sum_2022-11-03.py) |

#### [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/))

|    Date    | Think | Code | Total |                                                                  Solution                                                                  |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/07 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth.py)       |
| 2022/03/08 |   –   | 1:57 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-03-08.py) |
| 2022/03/12 |   –   | 2:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-03-12.py) |
| 2022/03/21 |   –   | 2:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-03-21.py) |
| 2022/08/12 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-08-12.py) |
| 2022/08/14 |   –   | 2:58 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-08-14.py) |
| 2022/08/18 |   –   | 1:51 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-08-18.py) |
| 2022/08/30 |   –   | 3:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-08-30.py) |
| 2022/09/26 |   –   |  ≈   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-09-26.py) |
| 2022/09/27 |   –   | 1:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-09-27.py) |
| 2022/10/01 |   –   | 3:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-10-01.py) |
| 2022/10/09 |   –   | 1:07 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-10-09.py) |
| 2022/10/28 | 0:51  | 1:09 | 2:00  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_nth_2022-10-28.py) |

#### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/))

|    Date    | Think | Code | Total |                                                      Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------:|
| 2022/02/23 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens.py)       |
| 2022/02/24 |   –   | 3:25 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-02-24.py) |
| 2022/02/27 |   –   | 2:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-02-26.py) |
| 2022/03/07 |   –   | 5:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-03-07.py) |
| 2022/06/24 |   –   |  ≈   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-06-24.py) |
| 2022/06/25 |   –   | 1:51 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-06-25.py) |
| 2022/07/11 |   –   | 4:43 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-07-11.py) |
| 2022/08/10 |   –   | 4:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-08-10.py) |
| 2022/10/20 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-10-20.py) |
| 2022/10/21 | 0:18  | 1:19 | 1:37  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-10-21.py) |
| 2022/10/25 | 0:06  | 1:06 | 1:12  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-10-25.py) |
| 2022/11/05 | 0:16  | 1:28 | 1:43  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/20.%20Valid%20Parentheses/valid_parens_2022-11-05.py) |

#### [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group)) 🙃
Got sick of sucking at linked lists. Started over from the beginning. 12 hours later, I got it (mostly :) ) . What a battle.

|    Date    | Think | Code | Total |                                                             Solution                                                             |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/30 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup.py)       |
| 2022/10/01 |   –   | 2:42 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-10-01.py) |
| 2022/10/05 |   –   | 7:49 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-10-05.py) |
| 2022/10/15 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-10-15.py) |
| 2022/10/16 |   –   | 1:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-10-16.py) |
| 2022/10/19 |   –   | 2:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-10-19.py) |
| 2022/10/28 | 1:25  | 2:42 | 4:07  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-10-28.py) |
| 2022/11/15 | 2:24  | 4:53 | 7:17  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/25.%20Reverse%20Nodes%20in%20k-Group/reverse_kgroup_2022-11-15.py) |

#### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/)) 🙃

|    Date    | Think | Code | Total |                                                                  Solution                                                                   |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/18 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes.py)       |
| 2022/03/21 |   –   | 2:15 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-03-21.py) |
| 2022/08/26 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-08-26.py) |
| 2022/08/30 |   –   | 4:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-08-30.py) |
| 2022/09/06 |   –   | 6:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-09-06.py) |
| 2022/09/07 |   –   | 1:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-09-07.py) |
| 2022/09/10 |   –   | 0:43 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-09-10.py) |
| 2022/09/20 |   –   | 0:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-09-20.py) |
| 2022/10/09 |   –   | 0:55 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/26.%20Remove%20Duplicates%20from%20Sorted%20Array/remove_dupes_2022-10-09.py) |

#### [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/)) 🤯
Fought real hard for this one :) .

|    Date    | Think | Code  | Total |                                                                       Solution                                                                        |
|:----------:|:-----:|:-----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/17 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring.py)       |
| 2022/03/17 |   –   | 6:34  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-03-17.py) |
| 2022/03/21 |   –   | 14:28 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-03-21.py) |
| 2022/08/25 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-08-25.py) |
| 2022/08/26 |   –   | 3:32  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-08-26.py) |
| 2022/08/31 |   –   | 6:31  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-08-31.py) |
| 2022/09/11 |   –   | 6:35  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-09-11.py) |
| 2022/10/09 |   –   | 7:02  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/30.%20Substring%20with%20Concatenation%20of%20All%20Words/find_substring_2022-10-09.py) |

#### [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/))
First time actually implementing binary search. Initially difficult, became second-nature over time.

|    Date    | Think |  Code  | Total |                                                             Solution                                                             |
|:----------:|:-----:|:------:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/02 |   ∞   |   ∞    |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search.py)       |
| 2022/03/02 |   –   | 10:00+ |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-03-02.py) |
| 2022/03/06 |   –   |   ∞    |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-03-06.py) |
| 2022/03/07 |   –   |  5:24  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-03-07.py) |
| 2022/03/10 |   –   |  3:55  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-03-10.py) |
| 2022/03/17 |   –   |   ∞    |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-03-17.py) |
| 2022/03/21 |   –   |  4:10  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-03-21.py) |
| 2022/08/10 |   –   |   ∞    |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-08-10.py) |
| 2022/08/11 |   –   |  2:18  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-08-11.py) |
| 2022/08/18 |   –   |   ∞    |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-08-18.py) |
| 2022/08/20 |   –   |  2:56  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-08-20.py) |
| 2022/08/23 |   –   |  2:39  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-08-23.py) |
| 2022/09/01 |   –   |  2:09  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-09-01.py) |
| 2022/09/28 |   –   |  3:43  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/33.%20Search%20in%20Rotated%20Sorted%20Array/search_2022-09-28.py) |

#### [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array))

|    Date    | Think | Code  | Total |                                                                                Language                                                                                |
|:----------:|:-----:|:-----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/21 | 1:05  | 21:05 |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/firstlast.py)       |
| 2022/10/23 | 0:26  | 2:03  | 2:29  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/firstlast_2022-10-23.py) |
| 2022/10/27 | 0:32  | 1:42  | 2:14  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/firstlast_2022-10-27.py) |
| 2022/11/03 | 0:12  | 3:02  | 3:14  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/firstlast_2022-11-03.py) |

#### [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/41.%20First%20Missing%20Positive)) 🙃
If you can't find a solution to the current problem as given but do know a solution to a similar problem, see if you can somehow change the current problem to be the same as the known problem.

|    Date    | Think | Code | Total |                                                          Solution                                                           |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/26 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/41.%20First%20Missing%20Positive/first_missing.py)       |
| 2022/09/27 |   –   | 3:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/41.%20First%20Missing%20Positive/first_missing_2022-09-27.py) |
| 2022/10/01 |   –   | 3:16 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/41.%20First%20Missing%20Positive/first_missing_2022-10-01.py) |
| 2022/10/11 |   –   | 3:37 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/41.%20First%20Missing%20Positive/first_missing_2022-10-11.py) |
| 2022/11/02 | 3:37  | 3:19 | 6:57  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/41.%20First%20Missing%20Positive/first_missing_2022-11-02.py) |

#### [48. Rotate Image](https://leetcode.com/problems/rotate-image/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/))
- Transpose + reflect approach is nice because it uses standard matrix operations.
- numpy-based solution is surprisingly slow.

|    Date    | Think | Code | Total |                                                    Solution                                                    |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------:|
| 2022/01/22 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image.py)       |
| 2022/01/23 |   –   | 3:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-01-23.py) |
| 2022/01/29 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-01-29.py) |
| 2022/01/30 |   –   | 3:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-01-30.py) |
| 2022/02/02 |   –   | 3:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-02-02.py) |
| 2022/02/11 |   –   | 1:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-02-11.py) |
| 2022/02/26 |   –   | 2:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-02-26.py) |
| 2022/06/15 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-06-15.py) |
| 2022/06/16 |   –   | 0:50 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-06-16.py) |
| 2022/06/23 |   –   | 0:46 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-06-23.py) |
| 2022/07/20 |   –   | 1:51 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-07-20.py) |
| 2022/09/30 |   –   |  ≈   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-09-30.py) |
| 2022/10/01 |   –   | 0:46 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-10-01.py) |
| 2022/10/06 |   –   | 0:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-10-06.py) |
| 2022/10/24 | 0:11  | 1:03 | 1:14  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/48.%20Rotate%20Image/rotate_image_2022-10-24.py) |

#### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/)) 😎
- In Python, use `collections.defaultdict` whenever you encounter a situation like this (building a hashmap where it's super convenient to have a default value automatically initialized for each key encountered).

|    Date    | Think | Code | Total |                                                      Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------:|
| 2022/02/28 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams.py)       |
| 2022/02/28 |   –   | 5:19 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-02-28.py) |
| 2022/03/04 |   –   | 4:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-03-04.py) |
| 2022/03/10 |   –   | 4:33 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-03-10.py) |
| 2022/04/13 |   –   | 3:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-04-13.py) |
| 2022/07/21 |   –   | 3:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-07-21.py) |
| 2022/08/10 |   –   | 1:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-08-10.py) |
| 2022/09/15 |   –   | 1:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/49.%20Group%20Anagrams/group_anagrams_2022-09-15.py) |

#### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/))
DP/Kadane's algorithm. Very similar to [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).

|    Date    | Think | Code | Total |                                                      Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------:|
| 2022/01/30 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray.py)       |
| 2022/01/31 |   –   | 2:41 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-01-31.py) |
| 2022/02/04 |   –   | 3:01 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-02-04.py) |
| 2022/02/22 |   –   | 5:15 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-02-22.py) |
| 2022/03/06 |   –   | 3:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-03-06.py) |
| 2022/03/14 |   –   | 3:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-03-14.py) |
| 2022/03/17 |   –   | 2:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-03-17.py) |
| 2022/06/16 |   –   | 5:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-06-16.py) |
| 2022/06/24 |   –   | 1:33 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-06-24.py) |
| 2022/07/20 |   –   | 1:19 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-07-20.py) |
| 2022/09/26 |   –   | 1:32 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/53.%20Maximum%20Subarray/max_subarray_2022-09-26.py) |

#### [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/))

|    Date    | Think | Code | Total |                                                       Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------:|
| 2022/02/28 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals.py)       |
| 2022/03/01 |   –   | 5:50 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-03-01.py) |
| 2022/03/06 |   –   | 7:54 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-03-06.py) |
| 2022/03/10 |   –   | 4:10 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-03-10.py) |
| 2022/08/10 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-08-10.py) |
| 2022/08/11 |   –   | 2:00 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-08-11.py) |
| 2022/08/18 |   –   | 2:26 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-08-18.py) |
| 2022/08/26 |   –   | 5:35 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-08-26.py) |
| 2022/09/15 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-09-15.py) |
| 2022/09/16 |   –   | 1:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-09-16.py) |
| 2022/09/20 |   –   | 1:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-09-20.py) |
| 2022/09/25 |   –   | 1:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-09-25.py) |
| 2022/10/06 |   –   | 1:43 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-10-06.py) |
| 2022/11/03 | 0:30  | 1:40 | 2:11  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/56.%20Merge%20Intervals/merge_intervals_2022-11-03.py) |

#### [57. Insert Interval](https://leetcode.com/problems/insert-interval/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval)) 🙃

|    Date    | Think | Code | Total |                                                       Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------:|
| 2022/09/17 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval.py)       |
| 2022/09/17 |   –   | 2:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval_2022-09-17.py) |
| 2022/09/21 |   –   | 2:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval_2022-09-21.py) |
| 2022/09/30 |   –   | 2:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval_2022-09-30.py) |
| 2022/10/23 | 1:10  | 9:16 | 10:26 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval_2022-10-23.py) |
| 2022/12/21 | 3:31  | 6:16 | 9:48  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval_2022-12-21.py) |
| 2022/12/26 | 0:38  | 4:40 | 5:18  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/57.%20Insert%20Interval/insert_interval_2022-12-26.py) |

#### [61. Rotate List](https://leetcode.com/problems/rotate-list/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List))

|    Date    | Think | Code | Total |                                                    Solution                                                    |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------:|
| 2022/10/02 |   ∞   |  ∞   |   ∞   |       [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list.py)        |
| 2022/10/02 |   –   | 2:26 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-10-02.py)  |
| 2022/10/06 |   –   |  ≈   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-10-06.py)  |
| 2022/10/08 |   –   | 2:57 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-10-08.py)  |
| 2022/10/11 |   –   | 1:56 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-10-11.py)  |
| 2022/10/21 | 1:10  | 3:14 | 4:24  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-10-21.py)  |
| 2022/11/13 | 1:43  | 8:48 |   ≈   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-11-13.py)  |
| 2022/11/13 | 0:09  | 1:46 | 1:55  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-11-13_2.py) |
| 2022/11/20 | 1:04  | 2:08 | 3:12  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/61.%20Rotate%20List/rotate_list_2022-11-20.py)  |

#### [75. Sort Colors](https://leetcode.com/problems/sort-colors/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors))

|    Date    | Think | Code  | Total |                                                   Solution                                                   |
|:----------:|:-----:|:-----:|:-----:|:------------------------------------------------------------------------------------------------------------:|
| 2022/04/07 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors.py)       |
| 2022/04/08 |   –   | 13:26 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-04-08.py) |
| 2022/08/31 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-08-31.py) |
| 2022/09/01 |   –   | 1:35  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-09-01.py) |
| 2022/09/06 |   –   | 1:38  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-09-06.py) |
| 2022/09/15 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-09-15.py) |
| 2022/09/16 |   –   | 1:32  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-09-16.py) |
| 2022/09/20 |   –   | 2:16  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-09-20.py) |
| 2022/09/25 |   –   | 1:02  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-09-25.py) |
| 2022/10/06 |   –   | 3:22  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-10-06.py) |
| 2022/11/02 | 0:45  | 2:05  | 2:50  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/75.%20Sort%20Colors/sort_colors_2022-11-02.py) |

#### [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/))
So hard. This problem makes me feel like I'm not cut out to be a software engineer 😢 .

|    Date    | Think | Code  | Total |                                                          Solution                                                          |
|:----------:|:-----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/12 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window.py)       |
| 2022/03/13 |   –   | 6:04  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-03-13.py) |
| 2022/03/17 |   –   | 17:01 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-03-17.py) |
| 2022/08/22 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-08-22.py) |
| 2022/08/23 |   –   | 8:55  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-08-23.py) |
| 2022/08/30 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-08-30.py) |
| 2022/08/31 |   –   | 3:27  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-08-31.py) |
| 2022/09/04 |   –   | 7:31  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-09-04.py) |
| 2022/09/10 |   –   | 7:05  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-09-10.py) |
| 2022/09/28 |   –   | 4:15  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-09-28.py) |
| 2022/11/13 | 1:56  | 11:01 |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-11-13.py) |
| 2022/11/15 | 0:13  | 4:40  | 4:53  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-11-15.py) |
| 2022/11/20 | 0:15  | 3:00  | 3:15  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/76.%20Minimum%20Window%20Substring/min_window_2022-11-20.py) |

#### [78. Subsets](https://leetcode.com/problems/subsets/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/78.%20Subsets)) 😎

|    Date    | Think | Code | Total |                                        Language                                         |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------:|
| 2023/01/21 | 8:44  | 0:33 | 9:17  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/78.%20Subsets/subsets.py) |

#### [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/)) 🙃
Always test algo in real use case. Here, using `sort()` in algo with non-optimal time complexity yields faster results because `sort()` is implemented in C (fast), and is therefore much faster than a pure algorithm solution.

|    Date    | Think | Code | Total |                                                    Solution                                                     |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------:|
| 2022/03/12 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge.py)       |
| 2022/03/12 |   –   | 4:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-03-12.py) |
| 2022/03/13 |   –   | 2:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-03-13.py) |
| 2022/03/17 |   –   | 3:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-03-17.py) |
| 2022/08/22 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-08-22.py) |
| 2022/08/23 |   –   | 2:20 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-08-23.py) |
| 2022/08/26 |   –   | 2:23 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-08-26.py) |
| 2022/09/06 |   –   | 2:46 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-09-06.py) |
| 2022/10/01 |   –   | 3:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/88.%20Merge%20Sorted%20Array/merge_2022-10-01.py) |

#### [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II))

|    Date    | Think | Code | Total |                                                           Solution                                                            |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/29 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii.py)       |
| 2022/09/30 |   –   | 1:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-09-30.py) |
| 2022/10/03 |   –   | 1:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-10-03.py) |
| 2022/10/14 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-10-14.py) |
| 2022/10/15 |   –   | 1:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-10-15.py) |
| 2022/10/18 |   –   | 2:13 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-10-18.py) |
| 2022/10/27 | 1:25  | 1:57 | 3:23  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-10-27.py) |
| 2022/11/16 | 1:08  | 6:19 |   ≈   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-11-16.py) |
| 2022/11/17 | 0:07  | 1:57 | 2:04  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/92.%20Reverse%20Linked%20List%20II/reverse_ll_ii_2022-11-17.py) |

#### [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal))
At long last, I finally start learning classical BFS and DFS in trees :) .

|    Date    | Think | Code | Total |                                                                 Solution                                                                  |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/04 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal/level_order.py)       |
| 2022/10/05 |   –   | 1:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal/level_order_2022-10-05.py) |
| 2022/10/09 |   –   | 2:07 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal/level_order_2022-10-09.py) |
| 2022/10/18 |   –   | 1:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal/level_order_2022-10-18.py) |
| 2022/11/09 | 0:43  | 2:21 | 3:04  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/102.%20Binary%20Tree%20Level%20Order%20Traversal/level_order_2022-11-09.py) |

#### [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal)) 😎

|    Date    | Think | Code | Total |                                                                   Solution                                                                    |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/05 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/zigzag.py)       |
| 2022/10/06 |   –   | 3:26 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/zigzag_2022-10-06.py) |
| 2022/10/11 |   –   | 7:55 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/zigzag_2022-10-11.py) |
| 2022/10/22 | 0:36  | 3:25 | 4:00  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/zigzag_2022-10-22.py) |

#### [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/107.%20Binary%20Tree%20Level%20Order%20Traversal%20II)) 😎

|    Date    | Think | Code | Total |                                                                Solution                                                                |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/05 |   ∞   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/107.%20Binary%20Tree%20Level%20Order%20Traversal%20II/level_order_ii.py) |

#### [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/111.%20Minimum%20Depth%20of%20Binary%20Tree)) 😎
BFS is better than DFS here because if the tree is unbalanced, we find the min depth as soon as we find a leaf (without exploring any longer paths).

|    Date    | Think | Code | Total |                                                              Solution                                                              |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/05 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/111.%20Minimum%20Depth%20of%20Binary%20Tree/min_depth.py)       |
| 2022/10/06 |   –   | 2:08 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/111.%20Minimum%20Depth%20of%20Binary%20Tree/min_depth_2022-10-06.py) |
| 2022/10/10 |   –   | 2:28 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/111.%20Minimum%20Depth%20of%20Binary%20Tree/min_depth_2022-10-10.py) |
| 2022/10/19 |   –   | 2:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/111.%20Minimum%20Depth%20of%20Binary%20Tree/min_depth_2022-10-19.py) |
| 2022/11/13 | 1:28  | 9:45 | 11:12 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/111.%20Minimum%20Depth%20of%20Binary%20Tree/min_depth_2022-11-13.py) |

#### [112. Path Sum](https://leetcode.com/problems/path-sum/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/112.%20Path%20Sum))

|    Date    | Think | Code | Total |                                                Solution                                                 |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------:|
| 2022/10/09 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/112.%20Path%20Sum/path_sum.py)       |
| 2022/10/11 |   –   | 1:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/112.%20Path%20Sum/path_sum_2022-10-11.py) |
| 2022/10/14 |   –   | 3:22 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/112.%20Path%20Sum/path_sum_2022-10-14.py) |
| 2022/10/23 | 1:47  | 2:06 | 3:53  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/112.%20Path%20Sum/path_sum_2022-10-23.py) |
| 2023/06/21 | 0:21  | 3:11 | 3:32  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/112.%20Path%20Sum/path_sum_2023-06-21.py) |

#### [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/113.%20Path%20Sum%20II))

|    Date    | Think | Code | Total |                                                    Solution                                                     |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------:|
| 2022/10/10 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/113.%20Path%20Sum%20II/path_sum_ii.py)       |
| 2022/10/11 |   –   | 4:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/113.%20Path%20Sum%20II/path_sum_ii_2022-10-11.py) |
| 2022/10/15 |   –   | 4:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/113.%20Path%20Sum%20II/path_sum_ii_2022-10-15.py) |
| 2022/10/25 | 1:24  | 8:33 | 9:56  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/113.%20Path%20Sum%20II/path_sum_ii_2022-10-25.py) |

#### [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node)) 🙃

|    Date    | Think | Code | Total |                                                                      Solution                                                                       |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/08 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect.py)       |
| 2022/10/09 |   –   | 3:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect_2022-10-09.py) |
| 2022/10/12 |   –   | 2:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect_2022-10-12.py) |
| 2022/10/21 | 2:45  | 1:42 | 4:27  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect_2022-10-21.py) |
| 2022/11/11 | 3:07  | 7:01 |   ≈   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect_2022-11-11.py) |
| 2022/11/12 | 0:07  | 1:31 | 1:38  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect_2022-11-12.py) |
| 2022/11/16 | 0:21  | 1:12 | 1:34  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/116.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node/connect_2022-11-16.py) |

#### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/))
- `min()` and `max()` introduce quite a bit of overhead, even when called on a collection of just two items.
    + But make the code so readable that it's worth it.

|    Date    | Think | Code | Total |                                                                 Solution                                                                 |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/01/23 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell.py)       |
| 2022/01/24 |   –   | 2:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-01-24.py) |
| 2022/01/29 |   –   | 3:54 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-01-29.py) |
| 2022/02/05 |   –   | 4:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-02-05.py) |
| 2022/02/26 |   –   | 3:53 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-02-26.py) |
| 2022/06/16 |   –   | 2:51 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-06-16.py) |
| 2022/06/25 |   –   | 4:06 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-06-25.py) |
| 2022/07/20 |   –   | 2:36 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-07-20.py) |
| 2022/09/11 |   –   | 2:10 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/buy_sell_2022-09-11.py) |

#### [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/124.%20Binary%20Tree%20Maximum%20Path%20Sum))

|    Date    | Think | Code | Total |                                                               Solution                                                               |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/19 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/124.%20Binary%20Tree%20Maximum%20Path%20Sum/max_pathsum.py)       |
| 2022/10/20 |   –   | 2:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/124.%20Binary%20Tree%20Maximum%20Path%20Sum/max_pathsum_2022-10-20.py) |
| 2022/10/23 | 1:34  | 2:31 | 4:05  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/124.%20Binary%20Tree%20Maximum%20Path%20Sum/max_pathsum_2022-10-23.py) |
| 2022/10/28 | 0:25  | 2:57 | 3:22  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/124.%20Binary%20Tree%20Maximum%20Path%20Sum/max_pathsum_2022-10-28.py) |

#### [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers)) 😎
Very similar to [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/).

|    Date    | Think | Code | Total |                                                           Solution                                                            |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/11 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers/sum_nums.py)       |
| 2022/10/13 |   –   | 2:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers/sum_nums_2022-10-13.py) |
| 2022/10/16 |   –   | 4:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers/sum_nums_2022-10-16.py) |
| 2022/10/23 | 1:49  | 1:58 | 3:47  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers/sum_nums_2022-10-23.py) |
| 2022/11/11 | 1:57  | 5:19 | 7:17  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers/sum_nums_2022-11-11.py) |
| 2022/12/28 | 3:27  | 6:12 |   ≈   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/129.%20Sum%20Root%20to%20Leaf%20Numbers/sum_nums_2022-12-28.py) |

#### [136. Single Number](https://leetcode.com/problems/single-number/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/136.%20Single%20Number))
x ⊕ 0 = x, x ⊕ x = 0

|    Date    | Think | Code | Total |                                                     Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
| 2022/10/02 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/136.%20Single%20Number/single_number.py)       |
| 2022/10/02 |   –   | 0:23 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/136.%20Single%20Number/single_number_2022-10-02.py) |
| 2022/10/06 |   –   | 0:28 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/136.%20Single%20Number/single_number_2022-10-06.py) |
| 2022/10/17 |   –   | 0:23 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/136.%20Single%20Number/single_number_2022-10-17.py) |
| 2022/11/11 | 0:19  | 0:24 | 0:43  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/136.%20Single%20Number/single_number_2022-11-11.py) |

#### [137. Single Number II](https://leetcode.com/problems/single-number-ii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/137.%20Single%20Number%20II))

|    Date    | Think | Code | Total |                                                         Solution                                                          |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/02 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/137.%20Single%20Number%20II/single_number_ii.py)       |
| 2022/10/03 |   –   | 1:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/137.%20Single%20Number%20II/single_number_ii_2022-10-03.py) |
| 2022/10/07 |   –   | 2:25 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/137.%20Single%20Number%20II/single_number_ii_2022-10-07.py) |
| 2022/10/17 |   –   | 1:15 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/137.%20Single%20Number%20II/single_number_ii_2022-10-17.py) |
| 2022/11/12 | 1:15  | 1:19 | 2:33  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/137.%20Single%20Number%20II/single_number_ii_2022-11-12.py) |

#### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/)) 🙃
First time encountering Floyd's cycle-finding algorithm (tortoise and hare). A fine algorithm :) .

|    Date    | Think | Code | Total |                                                      Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------:|
| 2022/03/03 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle.py)       |
| 2022/03/04 |   –   | 8:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-03-04.py) |
| 2022/03/06 |   –   | 4:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-03-06.py) |
| 2022/03/13 |   –   | 7:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-03-13.py) |
| 2022/03/14 |   –   | 1:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-03-14.py) |
| 2022/03/17 |   –   | 1:32 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-03-17.py) |
| 2022/08/11 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-08-11.py) |
| 2022/08/12 |   –   | 0:45 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-08-12.py) |
| 2022/08/18 |   –   | 1:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-08-18.py) |
| 2022/08/30 |   –   | 1:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-08-30.py) |
| 2022/09/28 |   –   | 0:40 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/141.%20Linked%20List%20Cycle/ll_cycle_2022-09-28.py) |

#### [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/142.%20Linked%20List%20Cycle%20II)) 🙃

|    Date    | Think | Code | Total |                                                          Solution                                                          |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/09 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/142.%20Linked%20List%20Cycle%20II/ll_cycle_ii.py)       |
| 2022/09/10 |   –   | 1:50 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/142.%20Linked%20List%20Cycle%20II/ll_cycle_ii_2022-09-10.py) |
| 2022/09/15 |   –   | 1:58 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/142.%20Linked%20List%20Cycle%20II/ll_cycle_ii_2022-09-15.py) |
| 2022/09/25 |   –   | 2:53 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/142.%20Linked%20List%20Cycle%20II/ll_cycle_ii_2022-09-25.py) |
| 2022/10/20 |   –   | 2:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/142.%20Linked%20List%20Cycle%20II/ll_cycle_ii_2022-10-20.py) |

#### [143. Reorder List](https://leetcode.com/problems/reorder-list/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/143.%20Reorder%20List))

|    Date    | Think | Code | Total |                                                    Solution                                                     |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------:|
| 2022/09/15 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/143.%20Reorder%20List/reorder_list.py)       |
| 2022/09/15 |   –   | 4:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/143.%20Reorder%20List/reorder_list_2022-09-15.py) |
| 2022/09/20 |   –   | 5:57 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/143.%20Reorder%20List/reorder_list_2022-09-20.py) |
| 2022/09/28 |   –   | 2:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/143.%20Reorder%20List/reorder_list_2022-09-28.py) |
| 2022/10/24 | 3:06  | 6:08 | 9:14  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/143.%20Reorder%20List/reorder_list_2022-10-24.py) |

#### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/))

|    Date    | Think | Code | Total |                                                           Solution                                                           |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2022/02/01 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product.py)       |
| 2022/02/02 |   –   | 4:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-02-02.py) |
| 2022/02/05 |   –   | 3:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-02-05.py) |
| 2022/02/22 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-02-22.py) |
| 2022/06/24 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-06-24.py) |
| 2022/06/25 |   –   | 2:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-06-25.py) |
| 2022/07/11 |   –   | 4:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-07-11.py) |
| 2022/08/10 |   –   | 3:36 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-08-10.py) |
| 2022/10/24 | 1:13  | 2:33 | 3:46  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/152.%20Maximum%20Product%20Subarray/max_product_2022-10-24.py) |

#### [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/)) 😎
Very similar to [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/).

|    Date    | Think | Code | Total |                                                                  Solution                                                                   |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/03 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min.py)       |
| 2022/03/04 |   –   | 6:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-03-04.py) |
| 2022/03/06 |   –   | 3:38 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-03-06.py) |
| 2022/03/13 |   –   | 4:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-03-13.py) |
| 2022/08/11 |   –   | 8:19 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-08-11.py) |
| 2022/08/18 |   –   | 5:28 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-08-18.py) |
| 2022/09/03 |   –   | 3:33 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-09-03.py) |
| 2022/10/13 |   –   | 1:54 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/find_min_2022-10-13.py) |

#### [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/))
Use two-pointer solution to take advantage of input array already being sorted.

|    Date    | Think | Code | Total |                                                   Solution                                                    |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------:|
| 2022/02/27 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii.py)       |
| 2022/02/28 |   –   | 4:51 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-02-28.py) |
| 2022/03/02 |   –   | 4:27 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-03-02.py) |
| 2022/03/10 |   –   | 3:53 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-03-10.py) |
| 2022/07/21 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-07-21.py) |
| 2022/08/10 |   –   | 1:57 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-08-10.py) |
| 2022/09/07 |   –   | 1:32 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-09-07.py) |
| 2022/11/16 | 0:57  | 1:09 | 2:06  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/167.%20Two%20Sum%20II/two_sum_ii_2022-11-16.py) |

#### [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/199.%20Binary%20Tree%20Right%20Side%20View)) 😎

|    Date    | Think | Code | Total |                                                             Solution                                                              |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/08 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/199.%20Binary%20Tree%20Right%20Side%20View/rightside.py)       |
| 2022/10/09 |   –   | 1:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/199.%20Binary%20Tree%20Right%20Side%20View/rightside_2022-10-09.py) |
| 2022/10/24 | 0:21  | 2:18 | 2:40  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/199.%20Binary%20Tree%20Right%20Side%20View/rightside_2022-10-24.py) |

#### [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/))
First time encountering DFS. What a neat algo 🤓 .

|    Date    | Think | Code  | Total |                                                       Solution                                                        |
|:----------:|:-----:|:-----:|:-----:|:---------------------------------------------------------------------------------------------------------------------:|
| 2022/03/08 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands.py)       |
| 2022/03/10 |   –   | 6:40  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-03-10.py) |
| 2022/03/12 |   –   | 9:32  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-03-12.py) |
| 2022/03/21 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-03-21.py) |
| 2022/04/13 |   –   | 12:20 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-04-13.py) |
| 2022/08/21 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-08-21.py) |
| 2022/08/22 |   –   | 7:50  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-08-22.py) |
| 2022/08/26 |   –   | 6:18  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-08-26.py) |
| 2022/09/06 |   –   | 3:43  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-09-06.py) |
| 2022/10/02 |   –   | 9:02  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-10-02.py) |
| 2022/11/09 | 0:43  | 6:38  | 7:21  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/200.%20Number%20of%20Islands/num_islands_2022-11-09.py) |

#### [202. Happy Number](https://leetcode.com/problems/happy-number/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/202.%20Happy%20Number)) 🙃

|    Date    | Think | Code | Total |                                                    Solution                                                     |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------:|
| 2022/09/11 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/202.%20Happy%20Number/happy_number.py)       |
| 2022/09/12 |   –   | 3:15 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/202.%20Happy%20Number/happy_number_2022-09-12.py) |
| 2022/09/16 |   –   | 4:10 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/202.%20Happy%20Number/happy_number_2022-09-16.py) |
| 2022/09/25 |   –   | 4:45 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/202.%20Happy%20Number/happy_number_2022-09-25.py) |
| 2022/10/14 |   –   | 2:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/202.%20Happy%20Number/happy_number_2022-10-14.py) |

#### [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/))
A classic :) . Kind of hurts my brain though.

|    Date    | Think | Code | Total |                                                        Solution                                                        |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------:|
| 2022/03/02 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll.py)       |
| 2022/03/02 |   –   | 5:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-03-02.py) |
| 2022/03/06 |   –   | 4:16 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-03-06.py) |
| 2022/03/14 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-03-14.py) |
| 2022/03/15 |   –   | 1:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-03-15.py) |
| 2022/03/21 |   –   | 0:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-03-21.py) |
| 2022/08/10 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-08-10.py) |
| 2022/08/11 |   –   | 0:36 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-08-11.py) |
| 2022/08/18 |   –   | 1:19 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-08-18.py) |
| 2022/08/31 |   –   | 1:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-08-31.py) |
| 2022/10/02 |   –   | 0:43 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-10-02.py) |
| 2022/12/26 | 0:34  | 1:18 | 1:52  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/206.%20Reverse%20Linked%20List/reverse_ll_2022-12-26.py) |

#### [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/)) 🙃

|    Date    | Think | Code  | Total |                                                            Solution                                                            |
|:----------:|:-----:|:-----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/13 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length.py)       |
| 2022/03/14 |   –   | 3:33  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-03-14.py) |
| 2022/03/17 |   –   | 11:20 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-03-17.py) |
| 2022/04/13 |   –   | 11:13 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-04-13.py) |
| 2022/08/23 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-08-23.py) |
| 2022/08/24 |   –   | 1:52  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-08-24.py) |
| 2022/08/30 |   –   | 4:59  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-08-30.py) |
| 2022/09/09 |   –   | 7:28  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-09-09.py) |
| 2022/09/25 |   –   | 4:29  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-09-25.py) |
| 2022/10/24 | 2:19  | 2:07  | 4:26  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/209.%20Minimum%20Size%20Subarray%20Sum/min_length_2022-10-24.py) |

#### [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array)) 🙃

|    Date    | Think | Code | Total |                                                                 Language                                                                  |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/26 | 13:06 | 1:28 | 14:34 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array/kth_largest.py)       |
| 2022/10/27 | 0:22  | 2:38 | 3:00  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array/kth_largest_2022-10-27.py) |
| 2022/10/30 | 0:42  | 6:49 | 7:31  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array/kth_largest_2022-10-30.py) |
| 2022/11/05 | 0:24  | 4:18 | 4:43  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array/kth_largest_2022-11-05.py) |
| 2022/11/21 | 0:27  | 3:49 | 4:15  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array/kth_largest_2022-11-21.py) |

#### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/))
Real-world performance can be different from what Big-O notation says. Big-O notation is most applicable for "sufficiently large input", but if n is not sufficiently large, an algorithm with worse Big-O time complexity might actually outperform one with better Big-O time complexity.

|    Date    | Think | Code | Total |                                                        Solution                                                        |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------:|
| 2022/01/20 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe.py)       |
| 2022/01/22 |   –   | 1:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-01-22.py) |
| 2022/01/29 |   –   | 1:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-01-29.py) |
| 2022/02/22 |   –   | 1:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-02-22.py) |
| 2022/06/15 |   –   | 2:08 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-06-15.py) |
| 2022/06/23 |   –   | 1:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-06-23.py) |
| 2022/07/20 |   –   | 1:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-07-20.py) |
| 2022/10/24 | 0:09  | 0:36 | 0:46  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/217.%20Contains%20Duplicate/contains_dupe_2022-10-24.py) |

#### [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/234.%20Palindrome%20Linked%20List))

|    Date    | Think | Code | Total |                                                           Solution                                                           |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/14 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/234.%20Palindrome%20Linked%20List/palindrome_ll.py)       |
| 2022/09/15 |   –   | 3:45 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/234.%20Palindrome%20Linked%20List/palindrome_ll_2022-09-15.py) |
| 2022/09/17 |   –   | 5:26 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/234.%20Palindrome%20Linked%20List/palindrome_ll_2022-09-17.py) |
| 2022/09/25 |   –   | 3:08 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/234.%20Palindrome%20Linked%20List/palindrome_ll_2022-09-25.py) |
| 2022/10/11 |   –   | 4:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/234.%20Palindrome%20Linked%20List/palindrome_ll_2022-10-11.py) |

#### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/))

|    Date    | Think | Code | Total |                                                                   Solution                                                                   |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/01/27 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self.py)       |
| 2022/01/29 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-01-29.py) |
| 2022/01/30 |   –   | 3:14 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-01-30.py) |
| 2022/02/02 |   –   | 3:30 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-02-02.py) |
| 2022/02/11 |   –   | 6:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-02-11.py) |
| 2022/02/26 |   –   | 4:25 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-02-26.py) |
| 2022/04/07 |   –   |  ≈   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-04-07.py) |
| 2022/04/08 |   –   | 1:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-04-08.py) |
| 2022/04/12 |   –   | 2:07 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-04-12.py) |
| 2022/06/16 |   –   | 5:40 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-06-16.py) |
| 2022/06/23 |   –   | 1:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-06-23.py) |
| 2022/07/20 |   –   | 2:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-07-20.py) |
| 2022/09/23 |   –   | 1:45 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/238.%20Product%20of%20Array%20Except%20Self/product_except_self_2022-09-23.py) |

#### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/))
- In Python:
    + `collections.defaultdict` is a special dictionary that automatically initializes a value the first time a key is encountered.
    + `collections.Counter` object can be used to solve this problem in one line.

|    Date    | Think | Code | Total |                                                     Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
| 2022/02/07 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram.py)       |
| 2022/02/22 |   –   | 2:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-02-11.py) |
| 2022/02/22 |   –   | 2:07 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-02-22.py) |
| 2022/03/17 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-03-17.py) |
| 2022/06/24 |   –   | 2:20 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-06-24.py) |
| 2022/07/11 |   –   | 0:45 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-07-11.py) |
| 2022/08/11 |   –   | 0:33 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-08-11.py) |
| 2022/10/30 | 0:19  | 0:39 | 0:58  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/242.%20Valid%20Anagram/valid_anagram_2022-10-30.py) |

#### [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II))
Min-heaps are so freaking cool.

|    Date    | Think | Code | Total |                                                         Solution                                                          |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/20 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II/meeting_rooms_ii.py)       |
| 2022/09/21 |   –   | 2:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II/meeting_rooms_ii_2022-09-21.py) |
| 2022/09/25 |   –   | 2:46 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II/meeting_rooms_ii_2022-09-25.py) |
| 2022/10/02 |   –   | 2:54 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II/meeting_rooms_ii_2022-10-02.py) |
| 2022/10/21 | 1:03  | 3:42 | 4:45  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II/meeting_rooms_ii_2022-10-21.py) |
| 2022/11/12 | 0:51  | 5:31 | 6:22  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/253.%20Meeting%20Rooms%20II/meeting_rooms_ii_2022-11-12.py) |

#### [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller))

|    Date    | Think | Code | Total |                                                     Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
| 2022/03/24 |   ∞   |  ∞   |   ∞   |       [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller.py)        |
| 2022/04/06 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-04-06.py)  |
| 2022/04/07 |   –   | 8:55 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-04-07.py)  |
| 2022/08/31 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-08-31.py)  |
| 2022/08/31 |   –   | 2:37 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-08-31_2.py) |
| 2022/09/06 |   –   | 2:17 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-09-06.py)  |
| 2022/09/17 |   –   | 4:26 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-09-17.py)  |
| 2022/10/20 |   –   | 1:37 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/259.%203Sum%20Smaller/3sum_smaller_2022-10-20.py)  |

#### [260. Single Number III](https://leetcode.com/problems/single-number-iii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III)) 🙃
Bitwise trick: `x & -x` to keep rightmost bit of x and set all others to 0.

|    Date    | Think | Code | Total |                                                          Solution                                                           |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/02 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii.py)       |
| 2022/10/03 |   –   | 1:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-10-03.py) |
| 2022/10/08 |   –   | 0:55 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-10-08.py) |
| 2022/10/18 |   –   |  ≈   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-10-18.py) |
| 2022/10/19 |   –   | 1:06 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-10-19.py) |
| 2022/10/23 | 0:25  | 1:15 | 1:40  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-10-23.py) |
| 2022/10/30 | 0:26  | 1:11 | 1:37  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-10-30.py) |
| 2022/11/13 | 0:14  | 1:17 | 1:31  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/260.%20Single%20Number%20III/single_number_iii_2022-11-13.py) |

#### [268. Missing Number](https://leetcode.com/problems/missing-number/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number)) 🙃

|    Date    | Think | Code | Total |                                                      Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------:|
| 2022/09/22 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number.py)       |
| 2022/09/23 |   –   | 5:41 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-09-23.py) |
| 2022/09/28 |   –   | 0:48 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-09-28.py) |
| 2022/10/09 |   –   | 1:10 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-10-09.py) |
| 2022/10/21 | 3:27  |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-10-21.py) |
| 2022/10/23 | 0:11  | 0:32 | 0:44  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-10-23.py) |
| 2022/10/27 | 0:16  | 0:39 | 0:55  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-10-27.py) |
| 2022/11/09 | 0:32  | 0:36 | 1:07  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/268.%20Missing%20Number/missing_number_2022-11-09.py) |

#### [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/285.%20Inorder%20Successor%20in%20BST))

|    Date    | Think | Code | Total |                                                          Solution                                                          |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/07 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/285.%20Inorder%20Successor%20in%20BST/inorder.py)       |
| 2022/10/08 |   –   | 0:58 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/285.%20Inorder%20Successor%20in%20BST/inorder_2022-10-08.py) |
| 2022/10/11 |   –   | 0:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/285.%20Inorder%20Successor%20in%20BST/inorder_2022-10-11.py) |
| 2022/10/19 |   –   | 1:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/285.%20Inorder%20Successor%20in%20BST/inorder_2022-10-19.py) |
| 2022/11/13 | 2:28  | 2:48 | 5:16  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/285.%20Inorder%20Successor%20in%20BST/inorder_2022-11-13.py) |

#### [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/)) 😎
Nearly identical to [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/).

|    Date    | Think | Code | Total |                                                                                 Solution                                                                                 |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/14 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring.py)       |
| 2022/03/15 |   –   | 2:55 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-03-15.py) |
| 2022/04/06 |   –   | 9:22 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-04-06.py) |
| 2022/08/23 |   –   | 3:25 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-08-23.py) |
| 2022/08/31 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-08-31.py) |
| 2022/09/01 |   –   | 2:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-09-01.py) |
| 2022/09/06 |   –   | 2:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-09-06.py) |
| 2022/09/16 |   –   | 1:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-09-16.py) |
| 2022/10/14 |   –   | 1:26 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters/longest_substring_2022-10-14.py) |

#### [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/347.%20Top%20K%20Frequent%20Elements)) 🙃

|    Date    | Think | Code  | Total |                                                        Language                                                        |
|:----------:|:-----:|:-----:|:-----:|:----------------------------------------------------------------------------------------------------------------------:|
| 2022/11/01 | 7:46  | 13:34 | 21:20 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/347.%20Top%20K%20Frequent%20Elements/topk.py)       |
| 2022/11/02 | 0:37  | 9:26  | 10:03 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/347.%20Top%20K%20Frequent%20Elements/topk_2022-11-02.py) |
| 2022/11/08 | 0:51  | 10:13 | 11:04 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/347.%20Top%20K%20Frequent%20Elements/topk_2022-11-08.py) |
| 2022/11/21 | 0:40  | 9:22  | 10:02 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/347.%20Top%20K%20Frequent%20Elements/topk_2022-11-20.py) |

#### [358. Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/358.%20Rearrange%20String%20k%20Distance%20Apart))

|    Date    | Think | Code | Total |                                                                Language                                                                 |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/11/12 | 6:52  | 7:35 |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/358.%20Rearrange%20String%20k%20Distance%20Apart/rearrange.py)       |
| 2022/11/13 | 0:27  | 7:00 | 7:27  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/358.%20Rearrange%20String%20k%20Distance%20Apart/rearrange_2022-11-13.py) |
| 2022/11/17 | 1:25  | 5:16 | 6:41  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/358.%20Rearrange%20String%20k%20Distance%20Apart/rearrange_2022-11-17.py) |

#### [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/392.%20Is%20Subsequence)) 😎

|    Date    | Think | Code | Total |                                                      Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------:|
| 2022/09/07 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/392.%20Is%20Subsequence/is_subsequence.py)       |
| 2022/09/08 |   –   | 0:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/392.%20Is%20Subsequence/is_subsequence_2022-09-08.py) |
| 2022/09/12 |   –   | 1:41 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/392.%20Is%20Subsequence/is_subsequence_2022-09-12.py) |
| 2022/09/23 |   –   | 1:39 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/392.%20Is%20Subsequence/is_subsequence_2022-09-23.py) |
| 2022/10/24 | 0:55  | 1:00 | 1:55  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/392.%20Is%20Subsequence/is_subsequence_2022-10-24.py) |

#### [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/))

|    Date    | Think | Code  | Total |                                                                Solution                                                                |
|:----------:|:-----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/10 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic.py)       |
| 2022/03/12 |   –   | 13:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-03-12.py) |
| 2022/03/14 |   –   | 7:40  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-03-14.py) |
| 2022/04/13 |   –   | 14:41 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-04-13.py) |
| 2022/08/22 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-08-22.py) |
| 2022/08/23 |   –   | 6:46  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-08-23.py) |
| 2022/08/30 |   –   | 9:46  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-08-30.py) |
| 2022/09/08 |   –   | 5:06  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-09-08.py) |
| 2022/10/06 |   –   | 6:32  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/417.%20Pacific%20Atlantic%20Water%20Flow/pacific_atlantic_2022-10-06.py) |

#### [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/))

|    Date    | Think | Code | Total |                                                                       Solution                                                                        |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/14 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement.py)       |
| 2022/03/14 |   –   | 3:04 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-03-14.py) |
| 2022/03/17 |   –   | 6:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-03-17.py) |
| 2022/08/23 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-08-23.py) |
| 2022/08/24 |   –   | 2:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-08-24.py) |
| 2022/08/30 |   –   | 3:25 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-08-30.py) |
| 2022/09/10 |   –   | 3:12 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-09-10.py) |
| 2022/10/09 |   –   | 3:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/424.%20Longest%20Repeating%20Character%20Replacement/longest_replacement_2022-10-09.py) |

#### [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III))

|    Date    | Think | Code | Total |                                                     Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
| 2022/10/14 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii.py)       |
| 2022/10/14 |   –   | 2:43 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii_2022-10-14.py) |
| 2022/10/19 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii_2022-10-19.py) |
| 2022/10/20 |   –   | 5:00 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii_2022-10-20.py) |
| 2022/10/23 | 1:36  | 2:42 | 4:18  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii_2022-10-23.py) |
| 2022/10/31 | 2:04  | 3:00 | 5:03  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii_2022-10-31.py) |
| 2022/11/20 | 1:47  | 5:58 | 7:45  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/437.%20Path%20Sum%20III/path_sum_iii_2022-11-20.py) |

#### [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/)) 😎
Very similar to [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/). Glad I put in the time battling with that one.

|    Date    | Think | Code | Total |                                                                 Solution                                                                  |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/17 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams.py)       |
| 2022/03/17 |   –   | 7:55 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams_2022-03-17.py) |
| 2022/04/11 |   –   | 9:14 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams_2022-04-11.py) |
| 2022/08/25 |   –   | 7:13 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams_2022-08-25.py) |
| 2022/09/03 |   –   | 3:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams_2022-09-03.py) |
| 2022/09/22 |   –   | 5:35 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams_2022-09-22.py) |
| 2022/11/12 | 3:21  | 5:20 | 8:41  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/438.%20Find%20All%20Anagrams%20in%20a%20String/find_anagrams_2022-11-12.py) |

#### [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array)) 😎
Almost identical to [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/).

|    Date    | Think | Code | Total |                                                                 Solution                                                                 |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/25 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array/find_dupes.py)       |
| 2022/09/26 |   –   | 1:16 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array/find_dupes_2022-09-26.py) |
| 2022/10/01 |   –   | 1:34 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array/find_dupes_2022-10-01.py) |
| 2022/10/11 |   –   | 1:30 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array/find_dupes_2022-10-11.py) |
| 2022/11/11 | 1:35  | 3:35 | 5:10  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array/find_dupes_2022-11-11.py) |
| 2023/01/20 | 4:55  | 2:50 |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/442.%20Find%20All%20Duplicates%20in%20an%20Array/find_dupes_2023-01-20.py) |

#### [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array)) 🙃

|    Date    | Think | Code | Total |                                                                         Solution                                                                         |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/24 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array/missing_numbers.py)       |
| 2022/09/25 |   –   | 9:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array/missing_numbers_2022-09-25.py) |
| 2022/09/26 |   –   | 3:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array/missing_numbers_2022-09-26.py) |
| 2022/09/30 |   –   | 2:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array/missing_numbers_2022-09-30.py) |
| 2022/10/09 |   –   | 1:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array/missing_numbers_2022-10-09.py) |
| 2022/10/27 | 0:47  | 5:13 | 6:00  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array/missing_numbers_2022-10-27.py) |

#### [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/451.%20Sort%20Characters%20By%20Frequency)) 🙃

|    Date    | Think | Code | Total |                                                             Language                                                             |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2022/11/03 | 2:21  | 7:36 | 9:57  |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/451.%20Sort%20Characters%20By%20Frequency/freq_sort.py)       |
| 2022/11/03 | 0:32  | 3:00 | 3:32  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/451.%20Sort%20Characters%20By%20Frequency/freq_sort_2022-11-03.py) |
| 2022/11/08 | 2:19  | 4:15 | 6:34  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/451.%20Sort%20Characters%20By%20Frequency/freq_sort_2022-11-08.py) |
| 2022/11/18 | 0:50  | 2:52 | 3:41  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/451.%20Sort%20Characters%20By%20Frequency/freq_sort_2022-11-18.py) |

#### [457. Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop))

|    Date    | Think | Code | Total |                                                            Solution                                                             |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/16 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop.py)       |
| 2022/09/16 |   –   | 3:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-09-16.py) |
| 2022/09/20 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-09-20.py) |
| 2022/09/21 |   –   | 4:20 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-09-21.py) |
| 2022/09/25 |   –   | 5:16 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-09-25.py) |
| 2022/09/30 |   –   | 3:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-09-30.py) |
| 2022/10/11 |   –   | 4:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-10-11.py) |
| 2022/11/11 | 1:11  | 8:55 |   ≈   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-11-11.py) |
| 2022/11/12 | 0:10  | 2:59 | 3:09  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-11-12.py) |
| 2022/11/16 | 0:10  | 2:56 | 3:06  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/457.%20Circular%20Array%20Loop/circular_array_loop_2022-11-16.py) |

#### [476. Number Complement](https://leetcode.com/problems/number-complement/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/476.%20Number%20Complement)) 😎
Identical to [1009. Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/).

|    Date    | Think | Code | Total |                                                Solution                                                 |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------:|
| 2022/10/03 |   ∞   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/476.%20Number%20Complement/complement.py) |

#### [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/543.%20Diameter%20of%20Binary%20Tree))

|    Date    | Think | Code | Total |                                                          Solution                                                          |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/15 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/543.%20Diameter%20of%20Binary%20Tree/diameter.py)       |
| 2022/10/16 |   –   | 2:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/543.%20Diameter%20of%20Binary%20Tree/diameter_2022-10-16.py) |
| 2022/10/19 |   –   | 2:54 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/543.%20Diameter%20of%20Binary%20Tree/diameter_2022-10-19.py) |
| 2022/10/26 | 1:02  | 1:55 | 2:57  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/543.%20Diameter%20of%20Binary%20Tree/diameter_2022-10-26.py) |

#### [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K))

|    Date    | Think | Code | Total |                                                           Solution                                                           |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/13 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K/subarray_sum.py)       |
| 2022/10/14 |   –   | 1:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K/subarray_sum_2022-10-14.py) |
| 2022/10/17 |   –   | 2:01 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K/subarray_sum_2022-10-17.py) |
| 2022/10/26 | 0:33  | 1:45 | 2:18  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K/subarray_sum_2022-10-26.py) |
| 2022/11/15 | 1:32  | 4:12 | 5:44  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K/subarray_sum_2022-11-15.py) |
| 2022/11/16 | 0:13  | 1:21 | 1:34  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/560.%20Subarray%20Sum%20Equals%20K/subarray_sum_2022-11-16.py) |

#### [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/)) 🤯
Battled for this one. Took 8+ hours to get a solution I was happy with. Note that "permutation" can be a synonym for "anagram".

|    Date    | Think | Code  | Total |                                                         Solution                                                          |
|:----------:|:-----:|:-----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/16 |   ∞   |   ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation.py)       |
| 2022/03/17 |   –   | 2:54  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-03-17.py) |
| 2022/04/06 |   –   | 20:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-04-06.py) |
| 2022/08/24 |   –   |   ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-08-24.py) |
| 2022/08/25 |   –   | 5:07  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-08-25.py) |
| 2022/08/30 |   –   | 2:22  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-08-30.py) |
| 2022/09/08 |   –   | 1:56  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-09-08.py) |
| 2022/10/03 |   –   | 1:58  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/567.%20Permutation%20in%20String/permutation_2022-10-03.py) |

#### [581. Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray))

|    Date    | Think | Code | Total |                                                                     Solution                                                                      |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/09 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted.py)       |
| 2022/09/09 |   –   | 2:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-09-09.py) |
| 2022/09/12 |   –   | 3:05 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-09-12.py) |
| 2022/09/19 |   –   | 3:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-09-19.py) |
| 2022/10/05 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-10-05.py) |
| 2022/10/06 |   –   | 3:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-10-06.py) |
| 2022/10/11 |   –   | 1:49 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-10-11.py) |
| 2022/10/21 | 1:25  | 2:23 | 3:48  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-10-21.py) |
| 2022/11/12 | 0:49  | 2:14 | 3:03  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/581.%20Shortest%20Unsorted%20Continuous%20Subarray/shortest_unsorted_2022-11-12.py) |

#### [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/621.%20Task%20Scheduler)) 🙃

|    Date    | Think | Code  | Total |                                                    Language                                                    |
|:----------:|:-----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------------------:|
| 2022/11/13 | 2:45  | 88:58 | 91:43 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/621.%20Task%20Scheduler/scheduler.py)       |
| 2022/11/13 | 0:21  | 1:35  | 1:55  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/621.%20Task%20Scheduler/scheduler_2022-11-13.py) |
| 2022/11/18 | 0:35  | 2:21  | 2:56  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/621.%20Task%20Scheduler/scheduler_2022-11-18.py) |

#### [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/)) 🙃

|    Date    | Think | Code  | Total |                                                               Solution                                                                |
|:----------:|:-----:|:-----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/09 |   ∞   |   ∞   |   ∞   |       [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings.py)        |
| 2022/03/12 |   –   |   ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-03-12.py)  |
| 2022/03/12 |   –   | 6:49  |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-03-12_2.py) |
| 2022/03/15 |   –   | 11:28 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-03-15.py)  |
| 2022/04/08 |   –   |   ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-04-08.py)  |
| 2022/08/21 |   –   |   ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-08-21.py)  |
| 2022/08/22 |   –   | 2:14  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-08-22.py)  |
| 2022/08/25 |   –   | 2:41  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-08-25.py)  |
| 2022/09/04 |   –   | 2:57  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-09-04.py)  |
| 2022/09/28 |   –   | 3:15  |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/647.%20Palindromic%20Substrings/palindromic_substrings_2022-09-28.py)  |

#### [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/658.%20Find%20K%20Closest%20Elements))

|    Date    | Think | Code | Total |                                                          Language                                                           |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/24 | 8:38  |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/658.%20Find%20K%20Closest%20Elements/k_closest.py)       |
| 2022/10/25 | 0:14  | 1:06 | 1:19  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/658.%20Find%20K%20Closest%20Elements/k_closest_2022-10-25.py) |
| 2022/10/30 | 0:53  | 4:21 | 5:15  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/658.%20Find%20K%20Closest%20Elements/k_closest_2022-10-30.py) |
| 2022/11/03 | 1:08  | 3:32 | 4:40  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/658.%20Find%20K%20Closest%20Elements/k_closest_2022-11-03.py) |
| 2022/11/16 | 0:27  | 1:47 | 2:14  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/658.%20Find%20K%20Closest%20Elements/k_closest_2022-11-16.py) |

#### [702. Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/702.%20Search%20in%20a%20Sorted%20Array%20of%20Unknown%20Size)) 😎

|    Date    | Think | Code  | Total |                                                                     Language                                                                      |
|:----------:|:-----:|:-----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/24 | 2:18  | 12:27 | 14:45 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/702.%20Search%20in%20a%20Sorted%20Array%20of%20Unknown%20Size/search.py)       |
| 2022/10/25 | 0:13  | 1:49  | 2:02  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/702.%20Search%20in%20a%20Sorted%20Array%20of%20Unknown%20Size/search_2022-10-25.py) |
| 2022/10/28 | 0:33  | 2:08  | 2:41  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/702.%20Search%20in%20a%20Sorted%20Array%20of%20Unknown%20Size/search_2022-10-28.py) |
| 2022/11/13 | 1:00  | 2:23  | 3:23  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/702.%20Search%20in%20a%20Sorted%20Array%20of%20Unknown%20Size/search_2022-11-13.py) |

#### [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/703.%20Kth%20Largest%20Element%20in%20a%20Stream)) 🙃

|    Date    | Think | Code  | Total |                                                                 Language                                                                  |
|:----------:|:-----:|:-----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/11/03 | 1:05  | 19:23 | 20:28 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/703.%20Kth%20Largest%20Element%20in%20a%20Stream/kth_largest.py)       |
| 2022/11/05 | 1:38  | 1:26  | 3:04  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/703.%20Kth%20Largest%20Element%20in%20a%20Stream/kth_largest_2022-11-05.py) |
| 2022/11/09 | 0:24  | 1:53  | 2:18  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/703.%20Kth%20Largest%20Element%20in%20a%20Stream/kth_largest_2022-11-09.py) |
| 2022/11/21 | 0:49  | 2:13  | 3:01  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/703.%20Kth%20Largest%20Element%20in%20a%20Stream/kth_largest_2022-11-21.py) |

#### [704. Binary Search](https://leetcode.com/problems/binary-search/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/)) 😎

|    Date    | Think | Code | Total |                                                     Solution                                                      |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------:|
| 2022/03/18 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/binary_search.py)       |
| 2022/03/21 |   –   | 1:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/binary_search_2022-03-21.py) |
| 2022/08/26 |   –   | 2:19 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/binary_search_2022-08-26.py) |
| 2022/08/30 |   –   | 0:58 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/binary_search_2022-08-30.py) |
| 2022/09/06 |   –   | 1:22 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/binary_search_2022-09-06.py) |
| 2022/09/26 |   –   | 1:33 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/704.%20Binary%20Search/binary_search_2022-09-26.py) |

#### [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K))

|    Date    | Think | Code | Total |                                                                  Solution                                                                   |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/04/06 |   ∞   |  ∞   |   ∞   |       [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product.py)        |
| 2022/04/07 |   –   | 3:50 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-04-07.py)  |
| 2022/08/31 |   –   |  ∞   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-08-31.py)  |
| 2022/08/31 |   –   | 2:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-08-31_2.py) |
| 2022/09/06 |   –   | 2:04 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-09-06.py)  |
| 2022/09/18 |   –   | 4:29 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-09-18.py)  |
| 2022/10/18 |   –   |  ≈   |   ∞   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-10-18.py)  |
| 2022/10/19 |   –   | 2:08 |   –   |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-10-19.py)  |
| 2022/10/23 | 0:42  | 1:49 | 2:32  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-10-23.py)  |
| 2022/10/30 | 1:21  | 1:57 | 3:18  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-10-30.py)  |
| 2022/11/18 | 0:50  | 1:54 | 2:44  |  [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/713.%20Subarray%20Product%20Less%20Than%20K/subarray_product_2022-11-18.py)  |

#### [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target)) 🙃

|    Date    | Think | Code | Total |                                                                       Language                                                                       |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/21 | 1:37  | 1:30 | 3:07  |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target/next_greatest.py)       |
| 2022/10/23 | 0:52  | 1:34 | 2:27  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target/next_greatest_2022-10-23.py) |
| 2022/10/28 | 0:05  | 2:26 | 2:31  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target/next_greatest_2022-10-28.py) |
| 2022/11/08 | 0:20  | 3:52 | 4:12  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target/next_greatest_2022-11-08.py) |

#### [759. Employee Free Time](https://leetcode.com/problems/employee-free-time/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/759.%20Employee%20Free%20Time))
- Most intuitive to solve by using a heap merge to take advantage of sorted input data.
- Python's built-in `sort()` is adaptive merge-sort and takes advantage of sorted input data too (this approach is actually a little faster here).

|    Date    | Think | Code | Total |                                                       Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------:|
| 2022/09/21 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/759.%20Employee%20Free%20Time/free_time.py)       |
| 2022/09/22 |   –   | 6:41 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/759.%20Employee%20Free%20Time/free_time_2022-09-22.py) |
| 2022/09/26 |   –   | 5:42 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/759.%20Employee%20Free%20Time/free_time_2022-09-26.py) |
| 2022/10/06 |   –   | 9:28 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/759.%20Employee%20Free%20Time/free_time_2022-10-06.py) |
| 2022/10/30 | 2:45  | 9:58 | 12:43 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/759.%20Employee%20Free%20Time/free_time_2022-10-30.py) |

#### [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/767.%20Reorganize%20String))

|    Date    | Think | Code  | Total |                                                       Language                                                       |
|:----------:|:-----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------------------------:|
| 2022/11/05 | 11:25 | 27:21 |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/767.%20Reorganize%20String/reorg_string.py)       |
| 2022/11/13 | 0:59  | 11:04 |   ≈   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/767.%20Reorganize%20String/reorg_string_2022-11-13.py) |
| 2022/11/15 | 0:17  | 5:29  | 5:46  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/767.%20Reorganize%20String/reorg_string_2022-11-15.py) |
| 2022/11/20 | 0:43  | 3:15  | 3:58  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/767.%20Reorganize%20String/reorg_string_2022-11-20.py) |

#### [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image)) 🙃

|    Date    | Think | Code | Total |                                                       Solution                                                       |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------:|
| 2022/10/03 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert.py)       |
| 2022/10/04 |   –   | 1:23 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert_2022-10-04.py) |
| 2022/10/09 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert_2022-10-09.py) |
| 2022/10/11 |   –   | 1:40 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert_2022-10-11.py) |
| 2022/10/16 |   –   | 1:22 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert_2022-10-16.py) |
| 2022/10/25 | 0:27  | 1:15 | 1:43  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert_2022-10-25.py) |
| 2022/11/17 | 0:41  | 1:50 | 2:32  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/832.%20Flipping%20an%20Image/flipinvert_2022-11-17.py) |

#### [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare))

|    Date    | Think | Code | Total |                                                              Solution                                                              |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------:|
| 2022/04/08 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare.py)       |
| 2022/04/11 |   –   | 1:59 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare_2022-04-11.py) |
| 2022/08/31 |   –   | 8:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare_2022-08-31.py) |
| 2022/09/01 |   –   | 1:55 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare_2022-09-01.py) |
| 2022/09/06 |   –   | 1:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare_2022-09-06.py) |
| 2022/09/15 |   –   | 2:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare_2022-09-15.py) |
| 2022/10/11 |   –   | 2:17 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/844.%20Backspace%20String%20Compare/backspace_compare_2022-10-11.py) |

#### [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/852.%20Peak%20Index%20in%20a%20Mountain%20Array)) 😎

|    Date    | Think | Code | Total |                                                             Language                                                              |
|:----------:|:-----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/25 | 8:50  | 5:50 | 14:40 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/852.%20Peak%20Index%20in%20a%20Mountain%20Array/peak.py)       |
| 2022/10/26 | 0:16  | 0:54 | 1:11  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/852.%20Peak%20Index%20in%20a%20Mountain%20Array/peak_2022-10-26.py) |
| 2022/10/30 | 0:16  | 0:50 | 1:06  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/852.%20Peak%20Index%20in%20a%20Mountain%20Array/peak_2022-10-30.py) |

#### [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/876.%20Middle%20of%20the%20Linked%20List)) 😎

|    Date    | Think | Code | Total |                                                            Solution                                                             |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/13 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/876.%20Middle%20of%20the%20Linked%20List/middle_ll.py)       |
| 2022/09/14 |   –   | 0:36 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/876.%20Middle%20of%20the%20Linked%20List/middle_ll_2022-09-14.py) |
| 2022/09/20 |   –   | 1:14 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/876.%20Middle%20of%20the%20Linked%20List/middle_ll_2022-09-20.py) |
| 2022/10/02 |   –   | 0:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/876.%20Middle%20of%20the%20Linked%20List/middle_ll_2022-10-02.py) |
| 2022/11/15 | 0:49  | 0:33 | 1:22  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/876.%20Middle%20of%20the%20Linked%20List/middle_ll_2022-11-15.py) |

#### [895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/895.%20Maximum%20Frequency%20Stack)) 🙃

|    Date    | Think | Code  | Total |                                                         Language                                                          |
|:----------:|:-----:|:-----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2022/11/17 | 4:04  | 67:04 | 71:08 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/895.%20Maximum%20Frequency%20Stack/freqstack.py)       |
| 2022/11/18 | 0:36  | 4:21  | 4:57  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/895.%20Maximum%20Frequency%20Stack/freqstack_2022-11-18.py) |

#### [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/)) 🙃
Identical to [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/).

|    Date    | Think | Code | Total |                                                           Solution                                                            |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/14 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets.py)       |
| 2022/03/15 |   –   | 2:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-03-15.py) |
| 2022/04/06 |   –   | 6:45 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-04-06.py) |
| 2022/08/24 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-08-24.py) |
| 2022/08/25 |   –   | 3:04 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-08-25.py) |
| 2022/08/30 |   –   | 3:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-08-30.py) |
| 2022/09/08 |   –   | 2:04 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-09-08.py) |
| 2022/10/03 |   –   | 1:57 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/904.%20Fruit%20Into%20Baskets/fruit_into_baskets_2022-10-03.py) |

#### [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/973.%20K%20Closest%20Points%20to%20Origin)) 🙃

|    Date    | Think | Code  | Total |                                                             Language                                                             |
|:----------:|:-----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/27 | 10:34 | 10:13 | 20:47 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/973.%20K%20Closest%20Points%20to%20Origin/k_closest.py)       |
| 2022/10/28 | 1:25  | 9:01  | 10:26 | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/973.%20K%20Closest%20Points%20to%20Origin/k_closest_2022-10-28.py) |
| 2022/10/31 | 0:13  | 6:11  | 6:24  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/973.%20K%20Closest%20Points%20to%20Origin/k_closest_2022-10-31.py) |
| 2022/11/12 | 1:01  | 5:07  | 6:08  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/973.%20K%20Closest%20Points%20to%20Origin/k_closest_2022-11-12.py) |

#### [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/)) 🙃

|    Date    | Think | Code | Total |                                                           Solution                                                            |
|:----------:|:-----:|:----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/18 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares.py)       |
| 2022/03/21 |   –   | 5:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares_2022-03-21.py) |
| 2022/08/26 |   –   | 3:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares_2022-08-26.py) |
| 2022/08/30 |   –   | 3:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares_2022-08-30.py) |
| 2022/09/03 |   –   | 5:09 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares_2022-09-03.py) |
| 2022/09/14 |   –   | 2:31 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares_2022-09-14.py) |
| 2022/10/09 |   –   | 2:35 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/977.%20Squares%20of%20a%20Sorted%20Array/squares_2022-10-09.py) |

#### [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/986.%20Interval%20List%20Intersections))

|    Date    | Think | Code | Total |                                                                  Solution                                                                  |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/19 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/986.%20Interval%20List%20Intersections/interval_intersections.py)       |
| 2022/09/20 |   –   | 6:40 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/986.%20Interval%20List%20Intersections/interval_intersections_2022-09-20.py) |
| 2022/09/22 |   –   | 2:29 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/986.%20Interval%20List%20Intersections/interval_intersections_2022-09-22.py) |
| 2022/10/01 |   –   | 3:52 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/986.%20Interval%20List%20Intersections/interval_intersections_2022-10-01.py) |
| 2022/10/28 | 1:59  | 5:47 | 7:46  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/986.%20Interval%20List%20Intersections/interval_intersections_2022-10-28.py) |

#### [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/)) 🙃
Except for one minor simplification/twist, basically the same as:

- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

|    Date    | Think | Code | Total |                                                             Solution                                                             |
|:----------:|:-----:|:----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------:|
| 2022/03/16 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii.py)       |
| 2022/03/17 |   –   | 1:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-03-17.py) |
| 2022/04/07 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-04-07.py) |
| 2022/04/08 |   –   | 1:13 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-04-08.py) |
| 2022/04/12 |   –   | 2:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-04-12.py) |
| 2022/08/24 |   –   |  ∞   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-08-24.py) |
| 2022/08/25 |   –   | 1:24 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-08-25.py) |
| 2022/08/30 |   –   | 1:03 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-08-30.py) |
| 2022/09/08 |   –   | 0:56 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-09-08.py) |
| 2022/10/03 |   –   | 1:02 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1004.%20Max%20Consecutive%20Ones%20III/max_ones_iii_2022-10-03.py) |

#### [1009. Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1009.%20Complement%20of%20Base%2010%20Integer))
0 ⊕ b = b, 1 ⊕ b = ¬b, bitlength of n = `floor(log2(n)) + 1`, all ones bitmask of length n = `(1 << n) - 1`.

|    Date    | Think | Code | Total |                                                               Solution                                                                |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/03 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1009.%20Complement%20of%20Base%2010%20Integer/complement.py)       |
| 2022/10/04 |   –   | 1:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1009.%20Complement%20of%20Base%2010%20Integer/complement_2022-10-04.py) |
| 2022/10/07 |   –   | 1:44 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1009.%20Complement%20of%20Base%2010%20Integer/complement_2022-10-07.py) |
| 2022/10/14 |   –   | 1:21 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1009.%20Complement%20of%20Base%2010%20Integer/complement_2022-10-14.py) |
| 2022/11/02 | 2:34  | 3:27 | 6:01  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1009.%20Complement%20of%20Base%2010%20Integer/complement_2022-11-02.py) |

#### [1060. Missing Element in Sorted Array](https://leetcode.com/problems/missing-element-in-sorted-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1060.%20Missing%20Element%20in%20Sorted%20Array)) 🙃
I finally, finally, at long, long last, understand lambda functions 🙃 . Some things just take a million exposures.

|    Date    | Think | Code | Total |                                                                 Solution                                                                 |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/28 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1060.%20Missing%20Element%20in%20Sorted%20Array/kth_missing.py)       |
| 2022/09/28 |   –   | 1:46 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1060.%20Missing%20Element%20in%20Sorted%20Array/kth_missing_2022-09-28.py) |
| 2022/10/01 |   –   | 1:11 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1060.%20Missing%20Element%20in%20Sorted%20Array/kth_missing_2022-10-01.py) |
| 2022/10/09 |   –   | 1:40 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1060.%20Missing%20Element%20in%20Sorted%20Array/kth_missing_2022-10-09.py) |
| 2022/10/27 | 0:15  | 1:19 | 1:34  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1060.%20Missing%20Element%20in%20Sorted%20Array/kth_missing_2022-10-27.py) |

#### [1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1095.%20Find%20in%20Mountain%20Array)) 😎

|    Date    | Think | Code | Total |                                                            Language                                                            |
|:----------:|:-----:|:----:|:-----:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/25 | 6:06  | 8:02 | 14:08 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1095.%20Find%20in%20Mountain%20Array/mountainfind.py)       |
| 2022/10/26 | 0:16  | 3:00 | 3:16  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1095.%20Find%20in%20Mountain%20Array/mountainfind_2022-10-26.py) |
| 2022/10/30 | 0:17  | 3:07 | 3:24  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1095.%20Find%20in%20Mountain%20Array/mountainfind_2022-10-30.py) |
| 2022/11/13 | 1:10  | 4:15 | 5:25  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1095.%20Find%20in%20Mountain%20Array/mountainfind_2022-11-13.py) |

#### [1167. Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1167.%20Minimum%20Cost%20to%20Connect%20Sticks))

|    Date    | Think | Code | Total |                                                              Language                                                              |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/29 | 10:23 | 9:14 |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1167.%20Minimum%20Cost%20to%20Connect%20Sticks/sticks.py)       |
| 2022/10/30 | 0:34  | 1:45 | 2:19  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1167.%20Minimum%20Cost%20to%20Connect%20Sticks/sticks_2022-10-30.py) |
| 2022/11/02 | 0:14  | 2:58 | 3:11  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1167.%20Minimum%20Cost%20to%20Connect%20Sticks/sticks_2022-11-02.py) |
| 2022/11/16 | 0:29  | 4:39 | 5:07  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1167.%20Minimum%20Cost%20to%20Connect%20Sticks/sticks_2022-11-16.py) |

#### [1430. Root to Leaf Sequence](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence)) 😎
2022/10/31: Tested out an alternate solution written in a named lambda style. Learned that this provides a marginal improvement in readability but is about 2x slower.

|    Date    | Think | Code | Total |                                                         Solution                                                          |
|:----------:|:-----:|:----:|:-----:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2022/10/13 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence.py)       |
| 2022/10/13 |   –   | 3:06 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence_2022-10-13.py) |
| 2022/10/18 |   –   |  ≈   |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence_2022-10-18.py) |
| 2022/10/19 |   –   | 2:47 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence_2022-10-19.py) |
| 2022/10/23 | 0:59  | 2:25 | 3:24  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence_2022-10-23.py) |
| 2022/10/31 | 0:23  | 9:31 | 9:54  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence_2022-10-31.py) |
| 2022/11/18 | 0:37  | 3:26 | 4:04  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1430.%20Root%20to%20Leaf%20Sequence/sequence_2022-11-18.py) |

#### [1481. Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1481.%20Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals)) 🙃

|    Date    | Think | Code  | Total |                                                                             Language                                                                             |
|:----------:|:-----:|:-----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2022/11/04 | 7:34  | 24:28 | 32:02 |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1481.%20Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/least_unique.py)       |
| 2022/11/05 | 0:53  | 2:53  | 3:47  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1481.%20Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/least_unique_2022-11-05.py) |
| 2022/11/09 | 1:16  | 3:22  | 4:38  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1481.%20Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/least_unique_2022-11-09.py) |
| 2022/11/18 | 3:16  | 6:22  |   ∞   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1481.%20Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/least_unique_2022-11-18.py) |
| 2022/11/21 | 0:33  | 4:56  | 5:29  | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1481.%20Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/least_unique_2022-11-21.py) |

#### [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/) ([solutions](https://github.com/jxcrw/enigmata/blob/main/leetcode/1539.%20Kth%20Missing%20Positive%20Number)) 🙃
Pre-sorted input ⇒ binary search may be a possibility.

|    Date    | Think | Code | Total |                                                              Solution                                                              |
|:----------:|:-----:|:----:|:-----:|:----------------------------------------------------------------------------------------------------------------------------------:|
| 2022/09/28 |   ∞   |  ∞   |   ∞   |      [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1539.%20Kth%20Missing%20Positive%20Number/kth_missing.py)       |
| 2022/09/28 |   –   | 1:20 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1539.%20Kth%20Missing%20Positive%20Number/kth_missing_2022-09-28.py) |
| 2022/10/01 |   –   | 3:18 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1539.%20Kth%20Missing%20Positive%20Number/kth_missing_2022-10-01.py) |
| 2022/10/09 |   –   | 5:30 |   –   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1539.%20Kth%20Missing%20Positive%20Number/kth_missing_2022-10-09.py) |
| 2022/10/26 | 0:53  | 4:55 |   ≈   | [Python](https://github.com/jxcrw/enigmata/blob/main/leetcode/1539.%20Kth%20Missing%20Positive%20Number/kth_missing_2022-10-26.py) |

<!-- Sub-READMEs -->
