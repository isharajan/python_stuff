class Node:
    def __init__(self,d,l=None,r=None):
        self.d = d
        self.l = l
        self.r = r
        
    @staticmethod    
    def _display_aux(root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root.r is None and root.l is None:
            line = '%s' % root.d
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only l child.
        if root.r is None:
            lines, n, p, x = Node._display_aux(root.l)
            s = '%s' % root.d
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only r child.
        if root.l is None:
            lines, n, p, x = Node._display_aux(root.r)
            s = '%s' % root.d
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        l, n, p, x = Node._display_aux(root.l)
        r, m, q, y = Node._display_aux(root.r)
        s = '%s' % root.d
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            l += [n * ' '] * (q - p)
        elif q < p:
            r += [m * ' '] * (p - q)
        zipped_lines = zip(l, r)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    @staticmethod
    def display(root):
        lines, *_ = Node._display_aux(root)
        for line in lines:
            print(line)
        print("--------------------")
   
    @staticmethod
    def insert(d,root):
        node = Node(d)
        if(root.d>node.d):
            if(root.l==None):
                root.l = node
            else:
                Node.insert(node.d,root.l)
            return root
        else:
            if(root.r == None):
                root.r = node
            else:
                Node.insert(node.d,root.r)
            return root
        
    @staticmethod
    def findmin(node):
        if(node.l != None):
            return Node.findmin(node.l)
        return node
    
    @staticmethod
    def delete(node,d):
        if(node == None):
            return node
        elif(node.d>d):
            node.l = Node.delete(node.l,d)
        elif(node.d<d):
            node.r = Node.delete(node.r,d)
        else:
            if(node.l==None and node.r==None):
                node = None
            elif(node.l == None):
                node = node.r
            elif(node.r == None):
                node = node.l
            else:
                minnode = Node.findmin(node.r)
                node.d = minnode.d
                node.r = Node.delete(node.r,minnode.d)
        return node
    
    @staticmethod
    def print_eachdata(root,data=[]):
        if root!=None:
            data.append(root)
            
            Node.print_eachdata(root.l)
            
            Node.print_eachdata(root.r)
            print (root.d)
        return data


root = Node(50)
root = Node.insert(60,root)
root = Node.insert(40,root)
root = Node.insert(100,root)
root = Node.insert(25,root)
root = Node.insert(10,root)
root = Node.insert(35,root)
root = Node.insert(55,root)
root = Node.insert(45,root)
root = Node.insert(53,root)
root = Node.insert(57,root)
root = Node.insert(43,root)
root = Node.insert(47,root)
root = Node.insert(105,root)
root = Node.insert(95,root)
Node.display(root)