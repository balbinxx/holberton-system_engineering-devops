#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zb;

	for (i = 0; i < 5; i++)
	{
		zb = fork();
		if (!zb)
			return (0);
		printf("Zombie process created, PID: %d\n", zb);
	}

	infinite_while();
	return (0);
}
