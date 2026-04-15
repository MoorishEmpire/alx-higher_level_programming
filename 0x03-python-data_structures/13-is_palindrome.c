#include "lists.h"

/**
 * size_list - counts size of a list
 * @head: the first of node of this list
 * Return: size of the list
 */

int         size_list(listint_t *head)
{
    int size;

    size = 0;
    while (head)
    {
        size++;
        head = head->next;
    }
    return size;
}

/**
 * add_front - add a new node to the front of the list
 * @head: the first node of this list
 * @new: the new node to add to the front
*/

void        add_front(listint_t **head, listint_t *new)
{
    new->next = *head;
    *head = new;
}

/**
 * pop_front - pop a node from the from the front
 * @head: the first node of this list
 * Return: the node poped
*/

listint_t   *pop_front(listint_t **head)
{
    listint_t   *current;

    current = *head;
    *head = current->next;
    return (current);
}

/**
 * copy_list - copies src list in dest list
 * @src: the source list
 * @dest: the destination list
*/

// void     copy_list(listint_t *src, listint_t **dest)
// {
//     while (src)
//     {
//         add_nodeint_end(dest, src->n);
//         src = src->next;
//     }
// }

/**
 * is_palindrome - check a singly linked list is a palindrome or not.
 * @head: the first node of this list
 * Return: 1 if is a palindrome, 0 if not
*/

int is_palindrome(listint_t **head)
{
    int         size;
    int         i;
    listint_t   *tmp;
    listint_t   *beta;
    listint_t   *new;

    if (!*head || !(*head)->next)
        return (1);

    size = size_list(*head);
    tmp = *head;
    beta = NULL;

    // copy_list(*head, &tmp);

    i = 0;
    while (i < size / 2)
    {
        new = pop_front(&tmp);
        add_front(&beta, new);
        i++;
    }
    if (size % 2 != 0)
        tmp = tmp->next;
    while (tmp && tmp->n == beta->n)
    {
        tmp = tmp->next;
        beta = beta->next;
    }
    if (!tmp)
        return (1);
    return 0;
}