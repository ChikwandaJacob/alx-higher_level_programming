#include "lists.h"

/**
 * getLength - gets the length of the linked list.
 *
 * @head: pointer to the head of the linked list.
 * Return: the integer length of the linked list.
 */
unsigned int getLength(listint_t *head)
{
	listint_t *current = head;
	int counter = 0;

	while (current)
	{
		current = current->next;
		counter++;
	}

	return (counter);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: beginning of the linked list
 * Return: True if linked list is palindrome.
 *         Otherwise False.
 */
int is_palindrome(listint_t **head)
{
	/* Lets get the size of the linked list */
	unsigned int linked_list_len = getLength(*head);
	int is_palindrome = 1;
	unsigned int index = 0;
	unsigned int r_index = 0;

	/* Perform checks */
	if (linked_list_len == 0)
		return (1);

	/* Declare array */
	unsigned int arr[linked_list_len];

/* Loop through list and assign values to new array */
	listint_t *current = *head;

	while (current)
	{
		arr[index] = current->n;
		current = current->next;
		index++;
	}

	/* Declare array to hold reverse of arr */
	unsigned int rev_arr[linked_list_len];

	/* Assign values to reverse array */

	while (index < linked_list_len)
	{
		index--;
		rev_arr[r_index] = arr[index];
		r_index++;
	}

	/* Compare the two arrays */

	while (index < linked_list_len)
	{
		/* If the contents are not the same return 0 */
		r_index--;
		if (arr[index] != rev_arr[r_index])
			is_palindrome = 0;

		index++;
	}

	return (is_palindrome);
}
