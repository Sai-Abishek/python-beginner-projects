'''
Project: Rock Paper and Scissor
Ver: 1.0.0
Developer: Abisheek Kumar
Country: India

'''

class arrayMethods:
    
    def __init__(self,array=[]):
        self.array = array

    def add_element(self,value,index=None) -> list:
        try:
            if index != None and index >= 0:
                self.array.insert(index,value)
                return self.array
            else:
                self.array.append(value)
                return self.array
        
        except Exception as add_error:
            print(f"Error while executing \"add_error()\" method: {add_error}")
            pass
        
        finally:
            print("Executed add_element() method")
    
    def remove_element(self,value,by_index=False) -> list:
        try:
            if value in self.array:
                if by_index:
                    elem_position = self.array.index(value)
                    self.array.pop(elem_position)
                    return self.array
                else:
                    self.array.remove(value)
                    return self.array
            else:
                print(f"The element {value} is not present in the array")
            
        except Exception as remove_error:
            print(f"Error while executing \"remove_element()\" method: {remove_error}")
            pass
        
        finally:
            print("Executed remove_element() method")
            
    def update_element(self,target_elem,new_elem) -> list:
        try:
            if target_elem in self.array:
                elem_position = self.array.index(target_elem)
                self.array[elem_position] = new_elem
                return self.array
            else:
                print(f"The element {target_elem} is not present in the array")
        
        except Exception as update_error:
            print(f"Error while executing \"update_error()\" method: {update_error}")
            pass
        
        finally:
            print("Executed update_element() method")
            
    def read_array(self):
        return self.array
            
    def clear_array(self):
        return self.array.clear()
    
            
            