#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head node of the linked list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed;
	int is_palindrome = 1;

	if (!head || !*head)
		return (1);

	reversed = reverse_list(*head);
	if (!reversed)
		return (0);

	while (*head && reversed)
	{
		if ((*head)->n != reversed->n)
		{
			is_palindrome = 0;
			break;
		}

		(*head) = (*head)->next;
		reversed = reversed->next;
	}

	free_listint(reversed);
	return (is_palindrome);
}

/**
 * reverse_list - Reverses a linked list and returns a new list.
 * @head: Pointer to the head node of the original linked list.
 *
 * Return: Pointer to the head node of the newly created reversed list,
 *         or NULL if memory allocation fails.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *reversed = NULL, *current = head, *new;

	while (current)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
		{
			free_listint(reversed);
			return (NULL);
		}

		new->n = current->n;
		new->next = reversed;
		reversed = new;
		current = current->next;
	}

	return (reversed);
}
