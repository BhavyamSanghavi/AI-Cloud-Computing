#include<bits/stdc++.h>
using namespace std;
vector<vector<vector<char>>>solution;

bool isSafe(vector<vector<char>>& mat, int row, int col)
{
    for(int c=0;c<col;c++)
    {
        if(mat[row][c]=='Q') return false;
    }
    int i=row,j=col;
    while(i>=0 && j>=0)
    {
        if(mat[i--][j--]=='Q') return false;
    }
    i=row, j=col;
    while(i<mat.size() && j>=0)
    {
        if(mat[i++][j--]=='Q') return false;
    }
    return true;
}

void solveNQueens(int n, int row, int col, vector<vector<char>>& mat)
{
    if(row>=n || row<0 ) return ;

    if(col==n)
    {
        solution.push_back(mat);
        return;
    }
    for(int r=0;r<n;r++)
    {
        if(isSafe(mat,r,col))
        {
            mat[r][col]='Q';
            solveNQueens(n,row,col+1,mat);
            mat[r][col]='.';
        }
    }
}
void printSolution(vector<vector<vector<char>>>& solution)
{
    for(int i=0;i<solution.size();i++)
    {
        for(int j=0;j<solution[0].size();j++)
        {
            for(int k=0;k<solution[1].size();k++)
            {
                cout<<solution[i][j][k]<<"  ";
            }
            cout<<endl;
        }
        cout<<endl<<endl;
        cout<<"New solution:"<<endl;
    }
}
int main()
{
    int n;
    cin>>n;
    vector<vector<char>>mat(n,vector<char>(n,'.'));
    solveNQueens(n,0,0,mat);
    // printSolution(solution);
    cout<<solution.size();
}