#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list.
 * @head: pointer to head of the list
 * @number: number to be inserted
 * Return: pointer to head of the list
 */

listint_t   *insert_node(listint_t **head, int number)
{
    listint_t   **current;
    listint_t   *new;

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);
    new->n = number;
    new->next = NULL;

    current = head;
    while (*current && (*current)->n < number)
        current = &(*current)->next;
    new->next = *current;
    *current = new;
    return (*head);
}