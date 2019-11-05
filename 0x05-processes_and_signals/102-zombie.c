#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - function creates infinite loop
 *
 * Return: never returns
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
 * main - function creates zombie processes
 *
 * Return: 0 on success
 */

int main(void)
{
	int i = 0;
	pid_t pid;

	while (i++ < 5)
	{
		pid = fork();

		if (pid < 0)
		{
			perror("Fork failed");
			exit(1);
		}
		else if (pid == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			exit(0);
		}
		sleep(1);
	}
	infinite_while();
	return (0);
}
