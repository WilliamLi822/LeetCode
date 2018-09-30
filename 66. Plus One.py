class Solution(object):
    def plusOne(self, digits):
        digits=map(str,digits)
        StrDigits="".join(digits)
        IntDigits=int(StrDigits)
        IntDigits+=1
        StrDigits=str(IntDigits)
        digits=list(StrDigits)
        digits=map(int,digits)
        return digits




class Solution(object):
    def plusOne(self, digits):
    	for i in range(len(digits)-1,-1,-1):
    		if digits[i]+1<10:
    			digits[i]+=1
    			return digits
    		else:
    			digits[i]=0
    			if i==0:
    				digits.insert(0,1)
    				return digits

    		
    			