#include<stdio.h>
#include<stdlib.h>
struct node{
    int info;
    struct node *next;
};
struct node *START;
struct node* Getnode(){
    struct node *p;
    p=(struct node *)malloc(sizeof(struct node));
    return p;
}
void insbeg( struct node **START,int x){
    struct node *temp;
    temp=Getnode();
    temp->info=x;
    temp->next=(*START);
    (*START)=temp;
}
void insend(struct node **START,int x)
{
    struct node *temp;
    struct node *t;
    temp=(*START);
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    t=Getnode();
    t->info=x;
    t->next=NULL;
    temp->next=t;

}
insaft(struct node **q,int x)
{
    struct node *temp;
    temp=Getnode();
    temp->info=x;
    temp->next=(*q)->next;

    (*q)->next=temp;
}
void split(struct node **START)
{
    struct node *t;
    struct node *r;
    struct node **START2;
    t=(*START);
    r=(*START)->next;
    while( r->next!=NULL)
    {
        t=t->next;
        r=r->next;
        r=r->next;
    }
    (*START2)=t->next;
    t->next=NULL;

    Traversal(&START);
    printf("\n\n\n\n\n\n");
    Traversal(&START2);
}
Traversal(struct node **START)
{
    struct node *t;
    t=(*START);
    while (t!=NULL){
        printf("%d    ",t->info);
        t=t->next;
    }
}
void concatenate(struct node **START1,struct node **START2)
{
    struct node *p;
    p=(*START1);
    while(p->next!=NULL)
    {
        p=p->next;
    }
    p->next=(*START2);
    Traversal(&START2);
}


int main()
{
    struct node* t;
    struct node *START=NULL;
    struct node *START2;
    int y;
    insbeg(&START,9);
    insbeg(&START,11);
    insbeg(&START,200);
    insbeg(&START,300);
    insbeg(&START,407);
    insbeg(&START,509);
    insbeg(&START,600);
  /*  Traversal(&START);
    printf("\n\n\n");
    t=START;
while(t->info!=9)
    t=t->next;
insaft(&t,6);*/
split(&START);
concatenate(&START,&START2);

    return 0;
}
