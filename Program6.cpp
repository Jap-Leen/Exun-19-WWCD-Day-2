// Reverse a linked list
// Complexity: H

void reverse()
{
      
        Node* node1= head;
        Node *node2 = NULL, *node3 = NULL;
  
        while (node1 != NULL) {
            node3= node1->next;
            node3->next = node2;
            node2= node1;
            node1= node1->next; 
        }
    
}

