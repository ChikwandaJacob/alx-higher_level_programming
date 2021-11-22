#include "lists.h"

/**
 * count - counts number of elements in the list
 * @head: head of the linked list
 * Return: number of elements
 */
int count(listint_t *head)
{
	int i = 0;

	while (head)
	{
		i++;
		head = head->next;
	}

	return (i);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: beginning of the linked list
 * Return: True if linked list is palindrome. Otherwise False.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp1 = *head, *temp2 = *head;

	int arr[count(temp1)], i = 0, is_palindrome = 0;

	if (!temp1)
		return (1);

	while (temp1)
	{
		arr[i] = temp1->n;
		i++;
		temp1 = temp1->next;
	}

	i--;

	while (temp2)
	{
		if (arr[i] == temp2->n)
			is_palindrome = 1;
		else
		{
			is_palindrome = 0;
			break;
		}
		i--;
		temp2 = temp2->next;
	}

	return (is_palindrome);
}
