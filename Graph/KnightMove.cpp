#include <iostream.h>
#include <vector>

class cell
{
public:
	int xPosition;
	int yPosition;
};

std::vector<cell*> FindNextCellList(cell* c);
void printAllCell(std::vector<cell*> list);
void  GetPossibleRoutine(cell* start, cell* end, std::vector<cell*> arranged);
bool TargetInList(std::vector<cell*> list, cell* target);
int minSteps=10000;

int main()
{
	cell* c=new cell;
	c->xPosition=1;
	c->yPosition=1;
	cell* targetCell=new cell;
	targetCell->xPosition=8;
	targetCell->yPosition=8;
	
	std::vector<cell*> arranged;
	GetPossibleRoutine(c, targetCell, arranged);
	std::cout<<"To get from A to B takes "<<minSteps<<" knight moves.";
	//printAllCell(possibleRoutine);
	//std::cout<<possibleRoutine.size();
}

void GetPossibleRoutine(cell* start, cell* end, std::vector<cell*> arranged)
{
	if(arranged.size()>=minSteps)
	{
		arranged.pop_back();
		return;
	}
	arranged.push_back(start);
	std::vector<cell*> list;
	list=FindNextCellList(start);
	if(TargetInList(list,end))
	{
		//std::cout<<"yes"<<" total steps is: "<<arranged.size()<<std::endl;
		if(arranged.size()<minSteps)
		{
			minSteps=arranged.size();
		}
	}
	else
	{
		for(int i=0;i<list.size();i++)
		{	
			if(TargetInList(arranged,list[i]))
				continue;
			GetPossibleRoutine(list[i],end,arranged);
		}
	}
	arranged.pop_back();
}

bool TargetInList(std::vector<cell*> list, cell* target)
{
	for(int i=0;i<list.size();i++)
	{
		if(list[i]->xPosition==target->xPosition&&list[i]->yPosition==target->yPosition)
			return true;	
	}
	return false;
}
void printAllCell(std::vector<cell*> list)
{
	for(int i=0;i<list.size();i++)
	{
		std::cout<<"x is:"<<list[i]->xPosition<<" y is:"<<list[i]->yPosition;
		std::cout<<std::endl;
	}
}
std::vector<cell*> FindNextCellList(cell* c)
{
	std::vector<cell*> list;
	if(c->xPosition>2&&c->yPosition>1)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition-2;
		next->yPosition=c->yPosition-1;
		list.push_back(next);
	}
	if(c->xPosition>1&&c->yPosition>2)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition-1;
		next->yPosition=c->yPosition-2;
		list.push_back(next);
	}
	if(c->xPosition>1&&c->yPosition<7)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition-1;
		next->yPosition=c->yPosition+2;
		list.push_back(next);
	}
	if(c->xPosition>2&&c->yPosition<8)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition-2;
		next->yPosition=c->yPosition+1;
		list.push_back(next);
	}
	if(c->xPosition<7&&c->yPosition>1)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition+2;
		next->yPosition=c->yPosition-1;
		list.push_back(next);
	}
	if(c->xPosition<8&&c->yPosition>2)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition+1;
		next->yPosition=c->yPosition-2;
		list.push_back(next);
	}
	if(c->xPosition<8&&c->yPosition<7)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition+1;
		next->yPosition=c->yPosition+2;
		list.push_back(next);
	}	
	if(c->xPosition<7&&c->yPosition<8)
	{
		cell* next=new cell;
		next->xPosition=c->xPosition+2;
		next->yPosition=c->yPosition+1;
		list.push_back(next);
	}
	return list;
}


