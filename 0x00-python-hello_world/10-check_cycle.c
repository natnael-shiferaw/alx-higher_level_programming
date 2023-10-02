#include "lists.h"

/**
* check_cycle - IT CHECKS IF a linked list contains a CYCLE.
* @list: THE LINKED LIST THAT IS TO BE CHECKED.
*
* Return: 1 ON SUCCESS, 0 OTHERWISE.
*/

int check_cycle(listint_t *list)
{
	listint_t *FAST = list;
	listint_t *SLOW = list;


	if (!list)
		return (0);

	while (SLOW && FAST && FAST->next)
	{
		SLOW = SLOW->next;
		FAST = FAST->next->next;
		if (SLOW == FAST)
			return (1);
	}

	return (0);
}
