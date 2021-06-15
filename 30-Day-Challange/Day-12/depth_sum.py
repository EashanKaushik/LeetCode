class BST:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def subtree_depth_sum(self, root):

        queue = list()
        queue.append(root)
        curr_sum = 0

        while len(queue) != 0:
            temp = queue.pop(0)

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

            curr_sum += self.find_depth_sum(temp)

        return curr_sum

    def find_depth_sum(self, root):

        depth_sum = 0
        queue1 = list()
        queue2 = list()

        queue1.append(root)
        curr_depth = 0

        while len(queue1) != 0 or len(queue2) != 0:
            if len(queue1) != 0:
                while len(queue1) != 0:
                    temp = queue1.pop(0)
                    depth_sum += curr_depth

                    if temp.left:
                        queue2.append(temp.left)

                    if temp.right:
                        queue2.append(temp.right)

                curr_depth += 1
            elif len(queue2) != 0:

                while len(queue2) != 0:
                    temp = queue2.pop(0)
                    depth_sum += curr_depth

                    if temp.left:
                        queue1.append(temp.left)

                    if temp.right:
                        queue1.append(temp.right)

                curr_depth += 1

        return depth_sum


if __name__ == '__main__':

    root = BST(1)

    root.left = BST(2)
    root.right = BST(3)

    root.left.left = BST(4)
    root.left.right = BST(5)
    root.right.left = BST(6)
    root.right.right = BST(7)

    root.left.left.left = BST(8)
    root.left.left.right = BST(9)

    s = Solution()

    print(s.subtree_depth_sum(root))
