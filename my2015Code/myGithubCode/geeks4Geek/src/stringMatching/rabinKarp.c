/* Following program is a C implementation of the Rabin Karp Algorithm
   given in the CLRS book */
 
#include<stdio.h>
#include<string.h>
 
// d is the number of characters in input alphabet
#define d 10
  
/*  pat  -> pattern
    txt  -> text
    q    -> A prime number
*/
void search(char *pat, char *txt, int q)
{
    int M = strlen(pat);
    int N = strlen(txt);
    int i, j;
    int p = 0;  // hash value for pattern
    int t = 0; // hash value for txt
    int h = 1;
  
    printf("M = %d\n",M);
    printf("q = %d\n",q);
    printf("N = %d\n\n",N);
    // The value of h would be "pow(d, M-1)%q"
    for (i = 0; i < M-1; i++)
    {
        h = (h * d)%q;
        printf("[AniB]: i:[%d] :: h:[%d] \n", i,h);
    }
    printf("\n");    
    
    // Calculate the hash value of pattern and first window of text
    for (i = 0; i < M; i++)
    {
        p = (d*p + pat[i])%q;
        t = (d*t + txt[i])%q;

        printf("[AniB]: d:[%d] p:[%d] pat[%d]: [%d] q:[%d]\n", d,p,i,pat[i],q);
        printf("[AniB]: d:[%d] t:[%d] txt[%d]: [%d] q:[%d]\n", d,t,i,txt[i],q);
    }
    printf("\n");    

    // Slide the pattern over text one by one
    for (i = 0; i <= N - M; i++)
    {
        
        // Check the hash values of current window of text and pattern
        // If the hash values match then only check for characters on by one
        if ( p == t )
        {
            /* Check for characters one by one */
            for (j = 0; j < M; j++)
            {
                if (txt[i+j] != pat[j])
                    break;
            }
            if (j == M)  // if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            {
                printf("Pattern found at index %d \n", i);
            }
        }
         
        // Calculate hash value for next window of text: Remove leading digit,
        // add trailing digit          
        if ( i < N-M )
        {
            t = (d*(t - txt[i+1]*h) + txt[i+M])%q;
             
            // We might get negative value of t, converting it to positive
            if(t < 0)
              t = (t + q);
            printf("[AniB]: i = [%d] t = [%d] txt[i] [%c] txt[i+M] [%c]\n",i,t,txt[i],txt[i+M] );
        }
    }
}
  
/* Driver program to test above function */
int main()
{
    char *txt = "2359023141526739921";
    char *pat = "31415";
    int q = 13;  // A prime number
    search(pat, txt, q);
    getchar();
    return 0;
}
