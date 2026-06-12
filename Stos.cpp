
#define QUEUE_SIZE 5
int queue_table[QUEUE_SIZE] = { 0 };
int queue_b = 0;
int queue_e = 0;

int isQueueEmpty(void)
{
    return (queue_e == queue_b) ? 1 : 0;
}

int isQueueFull(void)
{
    return ((queue_e+1) % (QUEUE_SIZE)==queue_b) ? 1 : 0;
}

int Usun(void)
{
    int temp = 0;
    if (!isQueueEmpty())
    {
        temp=queue_table[queue_b];
        queue_b=(queue_b+1)%QUEUE_SIZE;
    }

    return temp;
}

int Odczytaj(void)
{
    if (!isQueueEmpty())
    {
        return queue_table[queue_b];
    }
    else{
        return queue_table[queue_b];
    }
}

void Wstaw(int val)
{
    if (!isQueueFull())
    {
        queue_table[queue_e] = val;
        queue_e = (queue_e+1)%QUEUE_SIZE;
    }
}
