#include "lists.h"

/**
 * reverse - reverses a list
 * @head: head of the linked list
 * Return: head
 */
listint_t *reverse(listint_t *head)
{
	listint_t *act, *prev;

	if (head == NULL)
		return (NULL);

	prev = head;
	act = head->next;

	while (act != NULL)
	{
		prev->next = act->next;
		act->next = head;
		head = act;
		act = prev->next;
	}

	return (head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: beginning of the linked list
 * Return: True if linked list is palindrome. Otherwise False.
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head, *temp = *head;

	cur = reverse(cur);

	if (!*head)
		return (1);

	while (temp)
	{
		if (cur->n != temp->n)
			return (0);

		cur = cur->next;
		temp = temp->next;
	}

	return (1);
}
