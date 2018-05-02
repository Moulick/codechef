# Chef and Array
#
# Chef has an array A[] of N elements denoted by A0, A1, ..., AN-1.
#
# He thinks about M questions of following kind: "What is the maximum element among Ai where i lies
# between min{x, y} and max{x, y} both inclusive?"
#
# You have to help Chef to find out sum of answers of all the M questions.
#
# Method of generation of values x and y for all M questions:
#
# You are given two integers x1 and y1 denoting values of x and y for the first question.
#
# For the next questions, values of xi and yi are generated in the following way:
#
# for i = 2 to M:
# 	xi = (xi-1 + 7) mod (N - 1)
# 	yi = (yi-1 + 11) mod N
# Here a mod b denotes the remainder of division of a by b.
#
# Input
# The first line contains a single integer N, denoting the number of elements in the array.
#
# The second line contains N space-separated integers, denoting A0, A1, ..., AN-1.
#
# The third line contains three space-separated integers M, x1 and y1.
#
# Output
# Output a single integer denoting the sum of the answers to the questions.
#
# Constraints and Subtasks
# 2 ≤ N ≤ 105
# 1 ≤ M ≤ 108
# 1 ≤ Ai ≤ 109
# 0 ≤ x1, y1 ≤ N-1
# Subtask 1: (20 points)
#
# N, M ≤ 103; 1 ≤ Ai ≤ 105
# Subtask 2: (50 points)
#
# N, M ≤ 105
# Subtask 3: (30 points)
#
# Original constraints
# Example
# Input:
# 3
# 1 2 3
# 3 0 1
#
# Output:
# 7
# Explanation
# The first question: x1 = 0, y1 = 1    =>    ans1 = 2
# The second question: x2 = (0 + 7) mod 2 = 1, y2 = (1 + 11) mod 3 = 0    =>    ans2 = 2
# The third question: x3 = (1 + 7) mod 2 = 0, y3 = (0 + 11) mod 3 = 2    =>    ans3 = 3
# As ans1 + ans2 + ans3 = 2 + 2 + 3 = 7. So you have to print 7


class Operation:
    def __init__(self, name, function, function_on_equal, neutral_value=0):
        self.name = name
        self.f = function
        self.f_on_equal = function_on_equal


def add_multiple(x, count):
    return x * count


def min_multiple(x, count):
    return x


def max_multiple(x, count):
    return x


sum_operation = Operation("sum", sum, add_multiple, 0)
min_operation = Operation("min", min, min_multiple, 1e9)
max_operation = Operation("max", max, max_multiple, -1e9)



class SegmentTree:
    """
    SegmentTree class. Handles an underlying array as well as available
    operations and pointer to the root of a tree.
    """

    def __init__(self,
                 array,
                 operations=[sum_operation, min_operation, max_operation]):
        """
        Builds a segment tree based on the provided `array`. Supports operations
        of class Operation provided in the operations array.
        """
        self.array = array
        if type(operations) != list:
            raise TypeError("operations must be a list")
        self.operations = {}
        for op in operations:
            self.operations[op.name] = op
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    def query(self, start, end, operation_name):
        """
        Returns the result of the operation execution with `operation_name`
        on the range from [start, end]
        """
        if self.operations.get(operation_name) == None:
            raise Exception("This operation is not available")
        return self.root._query(start, end, self.operations[operation_name])

    def summary(self):
        """
        Prints the summary for the whole array (values in the root node).
        """
        return self.root.values

    def update(self, position, value):
        """
        Updates an old value at `position` to a new `value`.
        """
        self.root._update(position, value)

    def update_range(self, start, end, value):
        """
        Updates old values old in the range [start, end], inclusively, to a new value.
        """
        self.root._update_range(start, end, value)

    def __repr__(self):
        return self.root.__repr__()


class SegmentTreeNode:
    """
    Internal SegmentTreeNode class represents a node of a segment tree. Each node
    stores the reference to the left and the right bound of a segment this
    node is responsible for.
    """

    def __init__(self, start, end, segment_tree):
        self.range = (start, end)
        self.parent_tree = segment_tree
        self.range_value = None
        self.values = {}
        self.left = None
        self.right = None
        if start == end:
            self._sync()
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2,
                                    segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end,
                                     segment_tree)
        self._sync()

    def _query(self, start, end, operation):
        if end < self.range[0] or start > self.range[1]:
            return None
        if start <= self.range[0] and self.range[1] <= end:
            return self.values[operation.name]
        self._push()
        left_res = self.left._query(start, end,
                                    operation) if self.left else None
        right_res = self.right._query(start, end,
                                      operation) if self.right else None
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return operation.f([left_res, right_res])

    def _update(self, position, value):
        if position < self.range[0] or position > self.range[1]:
            return
        if position == self.range[0] and self.range[1] == position:
            self.parent_tree.array[position] = value
            self._sync()
            return
        self._push()
        self.left._update(position, value)
        self.right._update(position, value)
        self._sync()

    def _update_range(self, start, end, value):
        if end < self.range[0] or start > self.range[1]:
            return
        if start <= self.range[0] and self.range[1] <= end:
            self.range_value = value
            self._sync()
            return
        self._push()
        self.left._update_range(start, end, value)
        self.right._update_range(start, end, value)
        self._sync()

    def _sync(self):
        if self.range[0] == self.range[1]:
            for op in self.parent_tree.operations.values():
                current_value = self.parent_tree.array[self.range[0]]
                if self.range_value is not None:
                    current_value = self.range_value
                self.values[op.name] = op.f([current_value])
        else:
            for op in self.parent_tree.operations.values():
                result = op.f(
                    [self.left.values[op.name], self.right.values[op.name]])
                if self.range_value is not None:
                    bound_length = self.range[1] - self.range[0] + 1
                    result = op.f_on_equal(self.range_value, bound_length)
                self.values[op.name] = result

    def _push(self):
        if self.range_value is None:
            return
        if self.left:
            self.left.range_value = self.range_value
            self.right.range_value = self.range_value
            self.left._sync()
            self.right._sync()
            self.range_value = None

    def __repr__(self):
        ans = "({}, {}): {}\n".format(self.range[0], self.range[1],
                                      self.values)
        if self.left:
            ans += self.left.__repr__()
        if self.right:
            ans += self.right.__repr__()
        return ans





N = int(input()) # number of elements in array
A = list(map(int, input().split())) # Array of imputs
M, a, b = map(int, input().split()) # M is number of queries, a,b are first x,y


# Create lists to store all x's and y's
x = []
y = []
sum = int()


x.append(a)
y.append(b)


seg = SegmentTree(A)




# for the first given x[0],y[0]

sum += seg.query(min(a,b), max(a,b), "max")
# print('sum: ' + str(sum))


for i in range(1, M):
    # generate x, y according to given condition
    x_new = (x[i-1] + 7) % (N - 1)
    y_new = (y[i-1] + 11) % (N)

    # add new x,y to their respective lists
    x.append(x_new)
    y.append(y_new)

    # get max and min for range of A
    mini = min(x_new, y_new)
    maxi = max(x_new, y_new)


    sum += seg.query(mini, maxi, "max")
    # print('sum: ' + str(sum))

# print('x: ' + str(x))
# print('y: ' + str(y))
print(sum)

