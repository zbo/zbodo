#include <iostream>
#include <list>
#include <vector>
using namespace std;
class Brix
{
public:
	Brix(int x,int y,int z)
	{
		X=x;
		Y=y;
		Z=z;
	};
	int X;
	int Y;
	int Z;
};

class Square
{
public:
	Square(int length,int width)
	{
		Length=length;
		Width=width;
	};
	int Length;
	int Width;
};
int getHeight(int length, int width, Brix brix);
int getHeight(Square base, Brix brix);
bool isLegalPut(Square up,Square base);
int getMaxHeight(Square base,list<Brix> list);
std::list<Brix> BrixList;


int main()
{
	/*Brix b1(6, 8, 10);
	Brix b2(5, 5, 5);
	BrixList.push_back(b1);
	BrixList.push_back(b2);*/
	Brix b1(31, 41, 59);
	Brix b2(26, 53, 58);
	Brix b3(97, 93, 23);
	Brix b4(84, 62, 64);
	Brix b5(33, 83, 27);
	BrixList.push_back(b1);
	BrixList.push_back(b2);
	BrixList.push_back(b3);
	BrixList.push_back(b4);
	BrixList.push_back(b5);
	Square maxBase(1000,1000);//put some value bigger than any input; 
	int maxHeight=getMaxHeight(maxBase,BrixList);
	std::cout<<"max tower height is: "<<maxHeight;

}
int getMaxHeight(Square base,list<Brix> list)
{
	std::list<Brix>::iterator ir; 
	std::vector<int> HeightVector;
	for(ir=list.begin();ir!=list.end();++ir)
	{
		Square A(ir->X,ir->Y);
		if(isLegalPut(A,base)){HeightVector.push_back(getHeight(A,*ir)+getMaxHeight(A,list));}
		Square B(ir->X,ir->Z);
		if(isLegalPut(B,base)){HeightVector.push_back(getHeight(B,*ir)+getMaxHeight(B,list));}
		Square C(ir->Y,ir->Z);
		if(isLegalPut(C,base)){HeightVector.push_back(getHeight(C,*ir)+getMaxHeight(C,list));}
	}
	int max=0;
	for(int i=0;i<HeightVector.size();i++)
	{
		if(HeightVector[i]>max)
			max=HeightVector[i];
	}
	return max;
}
int getHeight(Square base, Brix brix)
{
	int temp=brix.X+brix.Y+brix.Z;
	return temp-base.Length-base.Width;
}

bool isLegalPut(Square up,Square base)
{
	if(up.Length<base.Length&&up.Width<base.Width)
		return true;
	if(up.Width<base.Length&&up.Length<base.Width)
		return true;
	return false;
}

