#include <iostream>
#include <list>
#include <vector>

using namespace std;
class Paper
{
public:
	Paper(int _frontLeft,int _frontRight,int _backLeft,int _backRight)
	{
		frontLeft=_frontLeft;
		frontRight=_frontRight;
		backLeft=_backLeft;
		backRight=_backRight;
	};
	int frontLeft;
	int frontRight;
	int backLeft;
	int backRight;
};
std::list<int> PagesList;
std::list<Paper> getPaperListByPages(int pages);
int main()
{

	int ch;
	cin>>ch;
	while(ch!=0)
	{
		PagesList.push_back(ch);
		cin>>ch;
	}
	std::list<int>::iterator ir;
	std::list<Paper>::iterator ip;
	for(ir=PagesList.begin();ir!=PagesList.end();++ir)
	{
		cout<<"Printing order for "<<*ir<<" pages:"<<endl;
		std::list<Paper> paperlist=getPaperListByPages(*ir);
		int paperIndex=1;
		for(ip=paperlist.begin();ip!=paperlist.end();++ip)
		{
			cout<<"paper "<<paperIndex<<"'s front left is"<<ip->frontLeft<<endl;
			cout<<"paper "<<paperIndex<<"'s front right is"<<ip->frontRight<<endl;
			cout<<"paper "<<paperIndex<<"'s back left is"<<ip->backLeft<<endl;
			cout<<"paper "<<paperIndex<<"'s back right is"<<ip->backRight<<endl;
			paperIndex++;
		}
	}
	cout<<"end";	
}

std::list<Paper> getPaperListByPages(int pages)
{
	std::list<Paper> paperlist;
	cout<<"call begin"<<endl;
	int papers=pages/4+1;
	int frontLeft,frontRight,backLeft,backRight;
	for(int i=0;i<papers;i++)
	{
		frontLeft=4*papers-2*i;
		frontRight=1+2*i;
		backLeft=frontRight+1;
		backRight=frontLeft-1;
		if(frontLeft>pages) frontLeft=0;
		if(backRight>pages) backRight=0;
		if(backLeft>pages) backLeft=0;
		Paper p(frontLeft, frontRight, backLeft, backRight);
		paperlist.push_back(p);
	}
	return paperlist;
}

