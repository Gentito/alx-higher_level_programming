#include "lists.h"

/**
 * check_cycle - checks to see if a list is in an endless loop or cycle
 * @list: the list to check
 * Return: 0 if no cycle is detected, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
  listint_t *i, *x;
  
  if (!list)
    {
      return (0);
    }
  i = list;
  x = list->next;
  while (x && i && x->next)
    {
      if (i == x)
	{
	  return (1);
	}
      i = i->next;
      x = x->next->next;
    }
  return (0);
}
