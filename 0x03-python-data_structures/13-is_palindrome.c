#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		temp = slow;
		slow = slow->next;
	}
	prev->next = NULL;
	reverse_list(&slow);
	if (compare_lists(*head, slow))
	{
		reverse_list(&temp);
		prev->next = temp;
		return (1);
	}
	else
	{
		reverse_list(&temp);
		prev->next = temp;
		return (0);
	}
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first linked list
 * @list2: pointer to the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	if (list1 == NULL && list2 == NULL)
		return (1);
	return (0);
}
