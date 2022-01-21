# reverse nodes in a circularly linked list

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class CircularLinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def insert ( self , data ) :
        if self.head == None :
            self.head = Node ( data )
            self.head.next = self.head
            return
        
        # find last element
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            prev = temp
            if temp.next != None : temp = temp.next
            
        # insert element
        prev.next = Node ( data )
        prev.next.next = flag
        return
    
    def printList ( self ) :
        if self.head == None :
            print ( "List empty" )
            return
        
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            print ( temp.data )
            temp = temp.next
        return
    
    def find ( self , data ) :
        if self.head == None :
            print ( "Not found" )
            return None
        
        temp = self.head.next
        found = False
        flag = self.head
        count = 0
        
        while temp != flag:
            count += 1
            if temp.data == data :
                found = True
                break
            temp = temp.next
            
        if found == False : print ( "Not found" )
        return count
    
    def delete ( self , data ) :
        catch = self.find ( data )
        if catch == None : return
        
        caught = 0
        prev = self.head
        temp = self.head
        
        while catch != caught :
            prev = temp
            temp = temp.next
            caught += 1
        
        prev.next = temp.next
        self.printList()
        return
    
    def exchange ( self , data_a , data_b ) :
        catch_a = self.find ( data_a )
        if catch_a == None : 
            print ( "Target node 1 not found" )
            return
        
        catch_b = self.find ( data_b )
        if catch_b == None : 
            print ( "Target node 2 not found" )
            return
        
        caught = 0
        prev_A = self.head
        node_A = self.head
        while catch_a != caught :
            prev_A = node_A
            node_A = node_A.next
            caught += 1
        
        caught = 0
        prev_B = self.head
        node_B = self.head
        while catch_b != caught :
            prev_B = node_B
            node_B = node_B.next
            caught += 1
        
        prev_A.next = node_B
        prev_B.next = node_A
        
        temp = node_A.next
        node_A.next = node_B.next
        node_B.next = temp
        
        return
    
    def size ( self ) :
        if self.head == None :
            print ( "Not found" )
            return 0
        
        temp = self.head.next
        found = False
        flag = self.head
        count = 0
        
        while temp != flag:
            count += 1
            temp = temp.next

        return count
        
    def getDataList ( self ) :
        if self.head == None :
            print ( "List empty" )
            return None
        
        arr = []
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            arr.append ( temp.data )
            temp = temp.next
        return arr
        
    def reverse ( self ) :
        size = self.size () + 1
        if size <= 2 : return
        if size % 2 == 1 : mid = int ( size / 2 )
        else : mid = int ( ( size + 1 ) / 2 )
        
        data_list = self.getDataList ()
        for index in range ( mid ) :
            self.exchange ( mid-index , mid+index ) 
        self.printList ()
            
CllObj = CircularLinkedList ()

for index in range ( 10 ) : 
    CllObj.insert ( index )
    
CllObj.reverse ( )
