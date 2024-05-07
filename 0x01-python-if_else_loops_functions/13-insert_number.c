#include "lists.h"
/**
 * insert_node- puts number in linked list
 * @head: pointer to linked list
 * @number: number to be inserted to list
 * Return: Null if function fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_block;

	new_block = malloc(sizeof(listint_t));
	if (new_block == NULL)
		return (NULL);
	new_block->n = number;

	if (node == NULL || node->n >= number)
	{
		new_block->next = node;
		*head = new_block;
		return (new_block);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_block->next = node->next;
	node->next = new_block;

	return (new_block);
}
