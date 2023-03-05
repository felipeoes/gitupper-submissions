#include <bits/stdc++.h> 
using namespace std;
 
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define sz(x) ((int)(x.size()))
#define ii pair<int,int>
#define vii vector<ii>
#define vi vector<int>
//#define int long long
#define EPS 0.00001
#define oo 1000000005
 
int G[1005][30];
char en[1005];
int t;
 
int tamanho;
char palavra[1005];
 
int DFS(int v){
 
    for(int i = 0; i < 30; i++){
        if( G[v][i] ){
            palavra[ tamanho ] = 'a' + i;
            tamanho++;
            palavra[ tamanho ] = '\0';
            printf("%s\n", palavra);
            DFS( G[v][i] );
            tamanho--;
        }
    }
}
 
 main(){
 
    while(scanf("%s", en+1) != EOF ){
        en[0] = 'X';
        t = strlen(en);
 
        memset(G, 0, sizeof G);
        int lig[30];
        memset(lig, 0, sizeof lig);
 
        for(int i = t-1; i >= 0; i--){
            for(int j = 0; j < 30; j++) G[i][j] = lig[j];
 
            lig[ en[i] - 'a' ] = i;
        }
 
        tamanho = 0;
        DFS(0);
        printf("\n");
    }
 
}