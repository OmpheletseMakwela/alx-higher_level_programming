#include "lists.h"
#include <stdio.h>

listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

int compare_lists(listint_t *list1, listint_t *list2) {
    while (list1 != NULL && list2 != NULL) {
        if (list1->n != list2->n) {
            return 0;
        }
        list1 = list1->next;
        list2 = list2->next;
    }

    if (list1 == NULL && list2 == NULL) {
        return 1;
    }

    return 0;
}

int is_palindrome(listint_t **head) {
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half;
    listint_t *prev_slow = *head;
    listint_t *mid = NULL;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL) {
        return is_pal;
    }

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    second_half = reverse_list(slow);
    is_pal = compare_lists(*head, second_half);
    second_half = reverse_list(second_half);

    if (mid != NULL) {
        prev_slow->next = mid;
        mid->next = second_half;
    } else {
        prev_slow->next = second_half;
    }

    return is_pal;
}

int main() {
    listint_t *head = NULL;

    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 1);

    int result = is_palindrome(&head);

    if (result == 1) {
        printf("The list is a palindrome.\n");
    } else {
        printf("The list is not a palindrome.\n");
    }

    return 0;
}

