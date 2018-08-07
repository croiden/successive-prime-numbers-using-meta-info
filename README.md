# successive-prime-numbers-using-meta-info
Python: The code lays out successive prime numbers one after the other and spits out the n-th to (n+5)th position substring where n is the input to the program.

-Here the code optimizationsis done by using the meta information. This will help in getting faster results, if the input number is very large

        #The below meta tabel is used to skip generation of certain prime numbers
        #Here i is the start point
        
        if num <=4:
            minion = "2"
            i= 3 
        elif num <=46:
            i= 11
            num-=4
        elif num <=256:
            i= 101
            num-=46
        elif num <=475:
            i= 501
            num-=256
        elif num <=2479:
            i= 1001
            num-=475
        elif num <=4719:
            i= 5001
            num-=2479
        elif num <=12384:
            i= 10001 #if the input is more than 4719, then the prime number generation is started from 10001 
            num-=4719
        elif num <=24239:
            i= 25001
            num-=12384
        elif num <=35539:
            i= 50001
            num-=24239
        elif num <=46534:
            i= 75001
            num-=35539
        elif num <=121246:
            i= 100001
            num-=46534
        elif num <=238210:
            i= 250001
            num-=121246
        elif num <=350410: 
            i= 500001 
            num-=238210
        elif num <=459970:
            i= 750001
            num-=350410
        else:
            i= 1000001 #if the input is more than 459970, then the prime number generation is started from 1000001
            num-=459970
            
-Also the while loop is always skipped by 1 (Even number) number. (i.e i+=2)
