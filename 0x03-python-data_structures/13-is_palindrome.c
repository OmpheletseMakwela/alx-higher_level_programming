#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next;
    listint_t *mid = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (is_palindrome);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    prev->next = NULL;

    while (slow != NULL)
    {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    listint_t *left = *head;
    listint_t *right = prev;

    while (right != NULL)
    {
        if (left->n != right->n)
        {
            is_palindrome = 0;
            break;
        }
        left = left->next;
        right = right->next;
    }

    if (mid != NULL)
    {
        prev = right;
        right = right->next;
        prev->next = mid;
        mid->next = right;
    }

    return (is_palindrome);
}
