class Sol:
    def __init__(self,number):
        self.number=number
    def check(self):
        s=str(self.number)
        left,right=0,len(s)-1
        while(right>left):
            if(s[left]!=s[right]):
                return False
            right-=1
            left+=1
        return True
if __name__ == '__main__':
    number=int(input("Enter a num to check if its palindrom:  "))
    p1=Sol(number)
    print(p1.check())
