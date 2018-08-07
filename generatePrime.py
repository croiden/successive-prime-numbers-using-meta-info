import sys
import math
def isfoo(num):
        for i in range(3, int(math.sqrt(num))+1): #the loop starts from 3, because always the even numbers are skipped
                if (num // i * i == num): return 0
        return 1
    
def answer(n):
        LEN = 5
        minion = "";
        i = 3;
        num = int(n)
        
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
            i= 10001
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

        while ( 1 ):
                if ( isfoo(i) == 1):
                        minion += str(i)
                        if (len(minion)>=num+LEN):
                                return minion[num:num+LEN]
                                break
                i+=2 #jumping loop by one number (ignoring all the even numbers)
def main():
        print("minion["+sys.argv[1]+"]="+answer(sys.argv[1]))
if __name__ == "__main__":
    main()