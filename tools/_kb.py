#!/usr/bin/env python3
"""Keyboarding practice"""

from collections import Counter, defaultdict
from tools.dsa.linked_list import ListNode

# 1: 2022/10/16
class Solution1:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i
        return []


# 2: 2022/10/18
class Solution2:
    def contains_duplicate(self, nums: list[int]) -> bool:
        n_list = len(nums)
        n_set = len(set(nums))
        return n_list > n_set


# 3: 2022/10/19
class Solution3:
    def rotate(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        matrix.reverse()
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# 4: 2022/10/19
class Solution4:
    def max_profit(self, prices: list[int]) -> float:
        price_min, profit_max = float('inf'), 0
        for price in prices:
            price_min = min(price_min, price)
            profit_temp = price - price_min
            profit_max = max(profit_max, profit_temp)
        return profit_max


# 5: 2022/10/21
class Solution5:
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = [1] * n

        product_left = 1
        for i in range(n):
            products[i] *= product_left
            product_left *= nums[i]

        product_right = 1
        for i in reversed(range(n)):
            products[i] *= product_right
            product_right *= nums[i]

        return products


# 6: 2022/10/22
class Solution6:
    def max_subarray(self, nums: list[int]) -> float:
        sum_max, sum_temp = -float('inf'), 0
        for num in nums:
            sum_temp = max(sum_temp + num, num)
            sum_max = max(sum_max, sum_temp)
        return sum_max


# 7: 2022/10/23
class Solution7:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i
        return []


class Solution7_1:
    def max_product(self, nums: list[int]) -> float:
        product_min, product_max, max_final = 1, 1, -float('inf')
        for num in nums:
            x = product_min * num
            y = product_max * num
            product_min = min(num, x, y)
            product_max = max(num, x, y)
            max_final = max(max_final, product_min, product_max)
        return max_final


# 8: 2022/10/25
class Solution8:
    def contains_duplicate(self, nums: list[int]) -> bool:
        n_list = len(nums)
        n_set = len(set(nums))
        return n_list > n_set


class Solution8_1:
    def is_anagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t


# 9: 2022/10/26
# Add Start New Line shortcut as alias for Next Template Field (fix going to next line while still in live template).
# Reserve steno AE as Start New Line (I'd never use AE to split a line or move lines down, always just use Enter).
class Solution9:
    def rotate(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        matrix.reverse()
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution9_1:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m - 1
            else: return m
        return -1


# 10: 2022/10/27
class Solution10:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        l, r = 0, n - 1
        while l <= r:
            square_l, square_r = nums[l] ** 2, nums[r] ** 2
            if square_l > square_r:
                squares[r - l] = square_l
                l += 1
            else:
                squares[r - l] = square_r
                r -= 1
        return squares


# 11: 2022/10/28
class Solution11:
    def remove_dupes(self, nums: list[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1


# 12: 2022/10/30
class Solution12:
    def max_profit(self, prices: list[int]) -> float:
        price_min, profit_max = float('inf'), 0
        for price in prices:
            price_min = min(price_min, price)
            profit_temp = price - price_min
            profit_max = max(profit_max, profit_temp)
        return profit_max


class Solution12_1:
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = [1] * n

        product_left = 1
        for i in range(n):
            products[i] *= product_left
            product_left *= nums[i]

        product_right = 1
        for i in reversed(range(n)):
            products[i] *= product_right
            product_right *= nums[i]

        return products


class Solution12_2:
    def max_subarray(self, nums: list[int]) -> float:
        sum_max, sum_temp = -float('inf'), 0
        for num in nums:
            sum_temp = max(sum_temp + num, num)
            sum_max = max(sum_max, sum_temp)
        return sum_max


# 13: 2022/10/31
class Solution13:
    def max_product(self, nums: list[int]) -> float:
        min_temp, max_temp, max_final = 1, 1, -float('inf')
        for num in nums:
            x = min_temp * num
            y = max_temp * num
            min_temp = min(x, y, num)
            max_temp = max(x, y, num)
            max_final = max(max_final, min_temp, max_temp)
        return max_final


class Solution13_1:
    def threesum_closest(self, nums: list[int], target: int) -> int:
        diff_min, n, sum_closest = float('inf'), len(nums), 0
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < target: l += 1
                else: r -= 1

                diff = target - threesum
                if diff == 0: return threesum
                if abs(diff) < abs(diff_min):
                    diff_min = diff
                    sum_closest = threesum

        return sum_closest


# 14: 2022/11/02
class Solution14:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m - 1
            else: return m
        return -1


class Solution14_1:
    def is_anagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t


class Solution14_2:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        l, r = 0, n - 1
        while l <= r:
            square_l, square_r = nums[l] ** 2, nums[r] ** 2
            if square_l > square_r:
                squares[r - l] = square_l
                l += 1
            else:
                squares[r - l] = square_r
                r -= 1
        return squares


class Solution14_3:
    def threesum_smaller(self, nums: list[int], target: int) -> int:
        count, n = 0, len(nums)
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count


# 15: 2022/11/03
class Solution15:
    def remove_dupes(self, nums: list[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1


class Solution15_1:
    def subarray_product(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        count, product = 0, 1
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            count += r - l + 1
        return count


# 16: 2022/11/05
class Solution16:
    def sort_colors(self, nums: list[int]) -> None:
        p0, i, p2 = 0, 0, len(nums) - 1
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1

# 17: 2022/11/08
class Solution17:
    def threesum_closest(self, nums: list[int], target: int) -> int:
        diff_min, n, sum_closest = float('inf'), len(nums), 0
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < target: l += 1
                else: r -= 1

                diff = target - threesum
                if diff == 0: return threesum
                if abs(diff) < abs(diff_min):
                    diff_min = diff
                    sum_closest = threesum

        return sum_closest


# 18: 2022/11/11
class Solution18:
    def threesum_smaller(self, nums: list[int], target: int) -> int:
        count, n = 0, len(nums)
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count


class Solution18_1:
    def sort_colors(self, nums: list[int]) -> None:
        p0, i, p2 = 0, 0, len(nums) - 1
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1


class Solution18_2:
    def num_subarray(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        count, product = 0, 1
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            count += r - l + 1
        return count


# 19: 2022/11/11
class Solution19:
    def is_valid(self, string: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack


# 20: 2022/11/13
class Solution20:
    def is_valid(self, string: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack


class Solution20_1:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target: l += 1
            elif total > target: r -= 1
            else: return [l + 1, r + 1]
        return []


# 21: 2022/11/13
class Solution21:
    def rotate(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        matrix.reverse()
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution21_1:
    def threesum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: break
            elif i == 0 or nums[i] != nums[i - 1]:
                self._twosum(nums, i,  triplets)
        return triplets

    def _twosum(self, nums: list[int], i: int, triplets: list[list[int]]) -> None:
        l, r = i + 1, len(nums) - 1
        while l < r:
            triplet = [nums[i], nums[l], nums[r]]
            total = sum(triplet)
            if total < 0: l += 1
            elif total > 0: r -= 1
            else:
                triplets.append(triplet)
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1


# 22: 2022/11/14
class Solution22:
    def contains_dupe(self, nums: list[int]) -> bool:
        n_list = len(nums)
        n_set = len(set(nums))
        return n_list > n_set


class Solution22_1:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            anagrams[s_sorted].append(s)
        return list(anagrams.values())


# 23: 2022/11/16
class Solution23:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if not merged or i[0] > merged[-1][1]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged


# 24: 2022/11/17
class Solution24:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return[i, hashmap[complement]]
            hashmap[num] = i
        return []


class Solution24_1:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    def find_rotation_index(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[l] < nums[r]: return 0
        while l <= r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]:
                return m + 1
            elif nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1


# 25: 2022/11/19
class Solution25:
    def max_subarray(self, nums: list[int]) -> float:
        sum_max, sum_temp = -float('inf'), 0
        for num in nums:
            sum_temp = max(sum_temp + num, num)
            sum_max = max(sum_max, sum_temp)
        return sum_max


class Solution25_1:
    def is_valid(self, string: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack


# 26: 2022/12/01
class Solution26:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target: l += 1
            elif total > target: r -= 1
            else: return [l + 1, r + 1]
        return []


# 27: 2022/12/03
class Solution27:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            anagrams[s_sorted].append(s)
        anagrams = list(anagrams.values())
        return anagrams


class Solution27_1:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


class SolutionAlt27_2:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        dummy, curr = ListNode(), head
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next


# 28: 2022/12/05
class Solution28:
    def is_anagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t


# 29: 2022/12/06
class Solution29:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    def find_rotation_index(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[l] < nums[r]: return 0
        while l <= r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]: return m + 1
            elif nums[l] <= nums[m]: l = m + 1
            else: r = m - 1
        return -1


# 30: 2022/12/06
class Solution30:
    def has_cycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            # slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False


class Solution30_1:
    def has_cycle(self, head: ListNode) -> bool:
        seen, node = set(), head
        while node:
            if node in seen: return True
            seen.add(node)
            node = node.next
        return False


# 31: 2022/12/07
class Solution31:
    def find_min(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[l] < nums[r]: return nums[l]

        while l <= r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]: return nums[m + 1]
            elif nums[l] <= nums[m]: l = m + 1
            else: r = m - 1
        return -1


# 32: 2022/12/08
class Solution32:
    def max_area(self, heights: list[int]) -> int:
        area_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area_max = max(area_max, width * height)

            if heights[l] < heights[r]: l += 1
            else: r -= 1

        return area_max


# 33: 2022/12/21
class Solution33:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


class Solution33_1:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        dummy, curr = ListNode(), head
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next


class Solution33_2:
    def max_subarray(self, nums: list[int]) -> int:
        sum_max, sum_temp = -float('inf'), 0
        for num in nums:
            sum_temp = max(sum_temp + num, num)
            sum_max = max(sum_max, sum_temp)
        return sum_max

# 34: 2022/12/26
class Solution34:
    def find_min(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[l] < nums[r]: return nums[l]
        while l <= r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]: return nums[m + 1]
            elif nums[l] <= nums[m]: l = m + 1
            else: r = m - 1
        return -1


class Solution34_2:
    def is_valid(self, string: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack


# 35: 2022/12/28
class Solution35:
    def remove_dupes(self, nums: list[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1


class Solution35_1:
    def sort_squares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        l, r = 0, n - 1
        while l <= r:
            square_l, square_r = nums[l] ** 2, nums[r] ** 2
            if square_l > square_r:
                squares[r - l] = square_l
                l += 1
            else:
                squares[r - l] = square_r
                r -= 1
        return squares


# 36: 2023/01/19
class Solution36:
    def rotate(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        matrix.reverse()
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution36_1:
    def length_longest_substring(self, string: str) -> int:
        prev_use_indices, length_max = {}, 0
        l = 0
        for r, c in enumerate(string):
            if c in prev_use_indices and prev_use_indices[c] >= l:
                l = prev_use_indices[c] + 1
            else:
                length_max = max(length_max, r - l + 1)
            prev_use_indices[c] = r
        return length_max


# 37: 2023/01/19
class Solution37:
    def remove_nth_from_end(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = slow = fast = ListNode(next=head)
        for _ in range(n): fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
