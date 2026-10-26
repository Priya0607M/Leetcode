/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* curr = head;
        int count = 0;
        while(curr!=nullptr)
        {
            count += 1;
            curr = curr->next;
        }
        int n1 = count - n + 1;
        curr = head;
        for(int i=1;i<n1-1;i++)
        {
            curr = curr -> next;
        }
        if(count==n)
        {
            return head->next;
        }
        else if(n==1)
        {
            curr->next=nullptr;
        }
        else
        {
            curr->next = curr->next->next;
        }

        return head;
    }
};