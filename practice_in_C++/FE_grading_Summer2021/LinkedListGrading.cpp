#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <iostream>
#define null NULL

using namespace std;

struct node
{
    int data;
    struct node *next;
};

node *createNode(int data)
{
    node *newNode = (node *)malloc(sizeof(node));
    if (newNode == null)
    {
        printf("malloc failed :(\n");
        return null;
    }

    newNode->data = data;
    newNode->next = null;

    return newNode;
}

void destroyLinkedList(node *head)
{
    if (head == null)
        return;

    node *tmp = head;

    destroyLinkedList(head->next);

    free(tmp);
}

void destroyCircularLinkedList(node *head, node *ogHead)
{
    if (head->next == ogHead)
    {
        // this should be the last node in the linked list
        free(head);
        return;
    }

    node *tmp = head;

    destroyCircularLinkedList(head->next, ogHead);

    free(tmp);
}

void printLinkedList(node *head)
{
    if (head == null)
        return;

    printf("%d%s", head->data, head->next == null ? "\n" : " ");

    printLinkedList(head->next);
}

void printCircularLinkedList(node *head, node *ogHead)
{
    if (head->next == ogHead)
    {
        // print last element followed by the first element to indicate the cycle
        printf("%d %d\n", head->data, head->next->data);
        return;
    }

    printf("%d%s", head->data, " ");

    printCircularLinkedList(head->next, ogHead);
}

struct node *makeCirclular(struct node *head)
{
    // checks to see if head is null
    // 2 points
    if (head == NULL)
        return NULL;

    // create a new node to traverse list
    // 1 point
    struct node *helper = head;

    // advance through list until we find the end
    // 4 points
    while (helper->next != NULL)
        helper = helper->next;

    // connect the end of the list to the front
    // 2 points
    helper->next = head;

    // return the head of the list
    // 1 point
    return head;
}

struct node *studentMakeCirclular(struct node *head)
{
    if (head == NULL)
    {
        return NULL;
    }

    if (head->next == NULL)
    {
        head->next = head;
        return head;
    }

    struct node *tmp = head->next;
    while (tmp->next != NULL)
    {
        tmp = tmp->next;
    }

    tmp->next = head;

    return head;
}

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;

    node *head = createNode(120);
    node *tmp = head;

    for (int i = 1; i <= 10; i += 1)
    {
        node *newNode = createNode(i);
        tmp->next = newNode;
        tmp = tmp->next;
    }
    printLinkedList(head);

    head = studentMakeCirclular(head);
    printCircularLinkedList(head, head);

    // destroyLinkedList(head);
    destroyCircularLinkedList(head, head);

    return 0;
}
