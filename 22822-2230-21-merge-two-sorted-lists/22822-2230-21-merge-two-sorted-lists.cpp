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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
       ListNode *head, *tail;
       head = new ListNode();
       tail = head;

       // While neither linked list is empty
       while (list1 && list2){
           if (list1->val < list2->val){
               tail->next = list1;
               list1 = list1->next;
           }
           else {
               tail->next = list2;
               list2 = list2->next;
           }
           tail = tail->next;
       }

       // One of the lists is empty
       if (list1)
            tail->next = list1;
        else
            tail->next = list2;
        
        return head->next;
    }
};