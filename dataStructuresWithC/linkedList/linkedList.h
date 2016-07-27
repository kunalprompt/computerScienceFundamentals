/*
Vaiables used - 
1. node - represent the linked list node
2. node->data - represent the data to be stored in the linked list node
3. temp - represent a temporary
4. root - indicate the root of the linked list
*/

#include <stdlib.h>
#include <stdio.h>
struct node
{
	/* data */
	int data;
	struct node *next;
};
typedef struct node node;
node* insert(node *pointer, int val){
	if(pointer==NULL){//when no node exist in the list or list is empty
		node *temp = (node *)malloc(sizeof(node));
		if (temp==NULL){
			printf("%s\n", "Root can't be initialized. Memory was not allocated.");
		}
		pointer = temp;
		temp->data = val;
		temp->next=NULL;
		printf("%s to %d\n", "Root initialized", val);
		return pointer;
	}
	else{//when list is non-empty
		int choice;
		printf("\n1) Press 1 if you want to insert at root.\n2) 2 the end of the linked list.\n");
		printf("3) 3 to insert at some other index (other than root or end of the list).\n");
		scanf("%d", &choice);
		node *root = pointer, *prev=NULL;
		node *temp = (node *)malloc(sizeof(node));
		switch(choice){
			case 1://insert at root
				printf("");//statement required after a label
				//node *temp = (node *)malloc(sizeof(node));
				temp->data = val;
				temp->next=pointer;
				pointer=temp;
				printf("\n%d %s", val,"Node inserted at Root.");
				return pointer;
				break;
			case 2://insert at the end of the list
				printf("");//statement required after a label
				//node *root = pointer, *prev=NULL;
				while(pointer!=NULL){
					prev = pointer;
					pointer=pointer->next;
				}
				//node *temp = (node *)malloc(sizeof(node));
				temp->data = val;
				temp->next=NULL;
				prev->next = temp;
				printf("\n%d %s", val,"node inserted at end.");
				return root;
				break;
			case 3:
			//making a check whether the position entered by the user is valid or not (becoz the user can enter any number even more than the lenght of the linked list)
				printf("\nEnter the position where you want to insert node.\n");
				int pos;
				scanf("%d", &pos);
				int len = 0;
				//node * root = pointer, *prev=NULL;
				while(pointer!=NULL){
					len+=1;
					pointer=pointer->next;
				}
				//printf("%d\n", len);
				if (pos>0 && pos<len){
					pointer=root;
					int count = 0;
					while(count<pos){
						prev = pointer;
						pointer = pointer->next;
						count+=1;
					}
					//node *temp = (node *)malloc(sizeof(node));
					temp->data = val;
					temp->next = pointer;
					prev->next = temp;
					printf("\n%d node inserted at %d.", val, pos);
					return root;
				}
				else{
					printf("\n%s", "Invalid position entered.");
					return;
				}
				break;
		}//switch closed
	}//else block closed
}//method closed
/*to print linked list*/
void printList(node *pointer){
	if (pointer==NULL){
		printf("\n%s", "List doesn't exist. Create a new List.");
		return;
	}
	int len = 0;
	printf("******************************************\n");
	while(pointer!=NULL){
		printf("--> %d\t", pointer->data);
		pointer=pointer->next;
		len+=1;
	}
	printf("\n******************************************");
	printf("\nLength of Linked List: %d", len);
	printf("\n******************************************");
	return;
}

/*to search a node in the list */
void searchList(node *pointer){	
	if (pointer==NULL){
		printf("\n%s\n", "List doesn't exist.");
		return;
	}
	else{
		node *root=pointer, *prev=NULL;
		printf("\nEnter the value you want to search.\n");
		int val=0;
		scanf("%d", &val);
		int index = 0;
		//search is based not on the data but on pointer so as to avoid Segmentation Fault, beco'z our pointer may go NULL
		while(pointer!=NULL){
			if (pointer->data == val){
				printf("\nNode found at index - %d", index);
				return;			
			}
			pointer=pointer->next;
			index+=1;
		}
		printf("\nNode not found.");
		return;
	}//else block closed
}//method closed

/*to delete a node from the list*/
node* deleteNode(node* pointer, int val){
	if (pointer==NULL){
		printf("\n%s\n", "List doesn't exist.");
		return;
	}
	else{
		node *root=pointer, *prev=pointer;
		int index = 0;
		while(pointer!=NULL){
			// case 1 : node found at index 0
			if (index==0 && pointer->data==val){
				root = pointer->next;
				free (pointer);
				printf("\nNode found at root and deleted.");
				return root;			
			}
			//case 2: node found in the middle or at the end
			else if (index>0 && pointer->data==val){
				printf("\nNode found at index - %d", index);
				prev->next = pointer->next;
				free(pointer);
				printf("\nNode deleted from index - %d", index);
				return root;		
			}
			prev = pointer;
			pointer=pointer->next;
			index+=1;
		}
		//case 3: node not found
		printf("\nNode not found in the list.");
		return root;
	}//else block closed
}//method closed