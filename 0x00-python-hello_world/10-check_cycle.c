#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list - pointer to head of list
 * Return: 0 if the list has no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
    listint_t   *head;
    listint_t   *current;
    int         cycle;

    cycle = 0;
    head = list;
    current = head->next;
    while (current != NULL)
    {
        if (current == head)
        {
            cycle = 1;
            break;
        }
        current = current->next;
    }
    return (cycle);   
}