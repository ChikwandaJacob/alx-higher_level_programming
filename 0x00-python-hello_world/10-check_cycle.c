#include "lists.h"

/**
 * check_cycle - checks whether a singly linked list has a cycle
 * @list: linked list to be checked
 *
 * Return: Either 1 for cycle true. 0 for cycle false
 */
int check_cycle(listint_t *list)
{
	int cycle_found = 0;
	/*Store head address*/
	listint_t *head = list;

	while (list)
	{
		/*Move to lists next node*/
		list = list->next;
/*Check whether the head and current node addresses are the same*/
		if (head == list)
		{
			cycle_found = 1;
			break;
		}
	}

	return (cycle_found);
}
