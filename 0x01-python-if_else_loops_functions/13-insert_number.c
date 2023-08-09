#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Double pointer to the head of the sorted linked list
 * @number: The number to insert into the linked list
 *
 * Return: The address of the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *previous = NULL, *current = *head, *new;

	while (current && number > current->n)
	{
		previous = current;
		current = current->next;
	}

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = current;

	if (!previous)
		*head = new;
	else
		previous->next = new;

	return (*head);
}
