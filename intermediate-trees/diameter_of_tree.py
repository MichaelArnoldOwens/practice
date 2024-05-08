# Let's define a tree's diameter as the number of nodes on the longest path between any two nodes in the tree. The longest path may or may not include the tree's root. Given a binary tree, find its diameter.
#
# In the diagrams in the examples below, the longest path is indicated by blue nodes.
#
# ### Example


# solution(t) = 6.
#
# t = {
#     "value": 1,
#     "left": null,
#     "right": {
#         "value": 2,
#         "left": {
#             "value": 3,
#             "left": null,
#             "right": {
#                 "value": 7,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": {
#             "value": 4,
#             "left": {
#                 "value": 6,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": 5,
#                 "left": null,
#                 "right": null
#             }
#         }
#     }
# }
# solution(t) = 5.

# TODO: figure out where i went wrong
def solution(t):
    # def helper(curr, level):
    #     if not curr:
    #         print('level return:', level)
    #         return level
    #     print('curr.value:', curr.value)
    #     print('current level:', level)
    #     max_left = helper(curr.left, level + 1)
    #     print('left', max_left)
    #     max_right = helper(curr.right, level + 1)
    #     print('right',max_right)
    #     print(f'final {max_right} + {max_left}:', max_right + max_left)
    #     # return max_left + max_right + 1

    def depth(node):
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter[0] = max(diameter[0], left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    diameter = [0]
    depth(t)
    return diameter[0] + 1