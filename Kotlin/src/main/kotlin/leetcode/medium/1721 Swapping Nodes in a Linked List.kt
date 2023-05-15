package leetcode.medium
/*You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100*/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class `1721 Swapping Nodes in a Linked List` {
    fun swapNodes(head: ListNode?, k: Int): ListNode? {
        // find first node to swap
        var first = head
        for (i in 1 until k) {
            first = first?.next
        }

        // find second node to swap
        var slow = head  // slow is our second node
        var fast = first
        while (fast?.next != null) {
            slow = slow?.next
            fast = fast.next
        }

        first?.`val` = slow?.`val`.also { slow?.`val` = first?.`val`!! }!!
        return head
    }
}