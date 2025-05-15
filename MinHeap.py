class heapq:
    def leftNode(self, i):
        return (2*i +1)
    
    def rightNode(self, i):
        return (2*i + 2)

    def parentNode(self, i):
        return (i//2)-1
    
    def hasleft(self, i, arr):
        return self.leftNode(i)<len(arr)
    
    def hasright(self, i, arr):
        return self.rightNode(i)<len(arr)
    
    def hasParent(self, i):
        return self.parentNode(i)>=0
    
    def heappop(self, arr):
        return arr.pop(0)
    
    def swap(self, val1, val2):
        temp = val1
        val1 = val2
        val2 = temp
    
    def heapify(self, arr):
       




        
      


        
    

    

    


        
        





