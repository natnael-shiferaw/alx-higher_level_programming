#include "lists.h"

listint_t *REVERSED_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
* REVERSED_listint - THIS FUNCTION REVERSES THE SINGLY
*    LINKED LIST OF TYPE listint_t.
* @head: A POINTER TO THE STARTING NODE OF THE REVESED LIST.
*
* Return: A POINTER TO THE HEAD.
*/

listint_t *REVERSED_listint(listint_t **head)
{
	listint_t *NODE = *head, *next, *PREV = NULL;

	while (NODE)
	{
		next = NODE->next;
		NODE->next = PREV;
		PREV = NODE;
		NODE = next;
	}

	*head = PREV;
	return (*head);
}

/**
* is_palindrome - A FUNCTION USED TO CHECK IF A
*    SINGLY LINKED LIST IS A PALINDROME.
* @head: A POINTER TO THE HEAD OF THE LINKED LIST.
*
* Return: ON SUCCESS 1, ON FAILURE 0.
*/

int is_palindrome(listint_t **head)
{
	listint_t *TMP, *REV, *MID;
	size_t SIZE = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	TMP = *head;
	while (TMP)
	{
		SIZE++;
		TMP = TMP->next;
	}

	TMP = *head;

	for (j = 0; j < (SIZE / 2) - 1; j++)
		TMP = TMP->next;

	if ((SIZE % 2) == 0 && TMP->n != TMP->next->n)
		return (0);

	TMP = TMP->next->next;
	REV = REVERSED_listint(&TMP);
	MID = REV;

	TMP = *head;

	while (REV)
	{
		if (TMP->n != REV->n)
			return (0);
		TMP = TMP->next;
		REV = REV->next;
	}
	REVERSED_listint(&MID);

	return (1);
}
