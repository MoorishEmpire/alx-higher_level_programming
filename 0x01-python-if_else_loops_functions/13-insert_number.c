#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list.
 * @head: pointer to head of the list
 * @number: number to be inserted
 * Return: pointer to head of the list
 */

listint_t   *insert_node(listint_t **head, int number)
{
    listint_t   *current;
    listint_t   *new;

    if (!*head && !head)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);
    new->next = NULL;
    new->n = number;
    current = *head;
    if (current->n >= number)
    {
        new->next = current;
        *head = new;
        return (*head);
    }
    while (current != NULL)
    {
        if (current->next != NULL && number >= current->n && number <= current->next->n)
        {
            new->next = current->next;
            current->next = new;
            break;
        }
        else if (current->next == NULL)
        {
            current->next = new;
            break;
        }
        current = current->next;
    }
    return (*head);
    
}