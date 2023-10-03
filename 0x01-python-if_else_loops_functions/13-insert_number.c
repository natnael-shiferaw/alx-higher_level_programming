#include "lists.h"

/**
* insert_node - NUMBER IS INSERTED IN SORTED SINGLY LINKED LIST.
* @head: POINTER TO THE HEAD OF THE LINKED LIST
* @number: NUMBER TO BE INSERTED
*
* Return: POINTER TO NEW NODE, NULL ON FAILURE.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *NODE = *head;
	listint_t *NEW;

	NEW = malloc(sizeof(listint_t));

	if (NEW == NULL)
		return (NULL);
	NEW->n = number;

	if (NODE == NULL || NODE->n >= number)
	{
		NEW->next = NODE;
		*head = NEW;
		return (NEW);
	}

	while (NODE && NODE->next && NODE->next->n < number)
		NODE = NODE->next;

	NEW->next = NODE->next;
	NODE->next = NEW;

	return (NEW);
}
