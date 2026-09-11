import tkinter as tk


class BinNode:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.right_son = None
        self.height = 1
        self.balance_fac = 0
    
class BinTree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value, node=None):
        if not self.root:
            self.root = BinNode(value)
            return self.root
        
        is_root_call = False
        if node is None:
            node = self.root
            is_root_call = True
        
        if value < node.value:
            if node.left_son:
                node.left_son = self.insert_node(value, node.left_son)
            else :
                node.left_son = BinNode(value)
                
        elif value > node.value:
            if node.right_son:
                node.right_son = self.insert_node(value, node.right_son)
            else :
                node.right_son = BinNode(value)
        else :
            return node
        
        self.update_height_and_fb(node)
        
        if node.balance_fac > 1: #desbalance izquierdo
            if node.left_son.balance_fac >= 0 : #condicion izq-izq
                node = self.rot_der(node)
            else : #condicion izq-der
                node.left_son = self.rot_izq(node.left_son)
                node = self.rot_der(node)
        
        if node.balance_fac < -1: #desbalance derecho
            if node.right_son.balance_fac <= 0 : #condicion der-der
                node = self.rot_izq(node)
            else: #condicion der-izq
                node.right_son = self.rot_der(node.right_son)
                node = self.rot_izq(node)
        
        if is_root_call:
            self.root = node
            
        return node
    
    def delete_node(self, value, node=None):
            is_root_call = False
            if node is None:
                if not self.root:
                    return None
                node = self.root
                is_root_call = True
            
            if value < node.value:
                if node.left_son:
                    node.left_son = self.delete_node(value, node.left_son)
            elif value > node.value:
                if node.right_son:
                    node.right_son = self.delete_node(value, node.right_son)
            else :
                if not node.left_son and not node.right_son:
                    print("No tengo hijos")
                    return None
                elif node.left_son and not node.right_son:
                    only_son = node.left_son
                    node.left_son = None
                    return only_son
                elif not node.left_son and node.right_son:
                    only_son = node.right_son
                    node.right_son = None
                    return only_son
                else:
                    succesor_node = self.find_succesor(node)
                    node.value = succesor_node.value
                    node.right_son = self.delete_node(succesor_node.value, node.right_son)
            
            self.update_height_and_fb(node)
            
            if node.balance_fac > 1: #desbalance izquierdo
                if node.left_son and node.left_son.balance_fac >= 0 : #condicion izq-izq
                    node = self.rot_der(node)
                elif node.left_son: #condicion izq-der
                    node.left_son = self.rot_izq(node.left_son)
                    node = self.rot_der(node)
            
            if node.balance_fac < -1: #desbalance derecho
                if node.right_son and node.right_son.balance_fac <= 0 : #condicion der-der
                    node = self.rot_izq(node)
                elif node.right_son: #condicion der-izq
                    node.right_son = self.rot_der(node.right_son)
                    node = self.rot_izq(node)
            
            if is_root_call:
                self.root = node
            
            return node
    
    def find_succesor(self, node):
        succesor = node.right_son
        while succesor.left_son:
            succesor = succesor.left_son
        return succesor
    
    def rot_der(self, node):
        new_root = node.left_son
        sub_tree = new_root.right_son
        
        new_root.right_son = node
        node.left_son = sub_tree
        
        self.update_height_and_fb(node)
        self.update_height_and_fb(new_root)
        
        return new_root
    
    def rot_izq(self, node):
        new_root = node.right_son
        sub_tree = new_root.left_son
        
        new_root.left_son = node
        node.right_son = sub_tree
        
        self.update_height_and_fb(node)
        self.update_height_and_fb(new_root)
        
        return new_root
    
    def draw_tree(self):
        if not self.root:
            raise IndexError("El árbol está vacío")
        
        window = tk.Tk()
        window.title("Visualizador de Árbol Binario")
        window.geometry("900x700")
        
        canvas = tk.Canvas(window, bg="white")
        canvas.pack(fill=tk.BOTH, expand = True)
        
        radius = 22
        level_height = 80
    
        def _draw_subtree(node, x, y, dx):
            if node.left_son:
                child_x = x - dx
                child_y = y + level_height
                canvas.create_line(
                    x,
                    y + radius,
                    child_x, 
                    child_y - radius,
                    width=2,
                    arrow=tk.LAST,
                    fill="#1B4F72",
                )
                _draw_subtree(node.left_son, child_x, child_y, dx / 1.9)
            
            if node.right_son:
                child_x = x + dx
                child_y = y + level_height
                canvas.create_line(
                    x,
                    y + radius,
                    child_x, 
                    child_y - radius,
                    width=2,
                    arrow=tk.LAST,
                    fill="#1B4F72",
                )
                _draw_subtree(node.right_son, child_x, child_y, dx / 1.9)
            
            canvas.create_oval(
                x -radius,
                y - radius,
                x + radius,
                y + radius,
                fill="#82E0AA",
                outline="#1E8449",
                width=2,
            )
            
            canvas.create_text(x, y, text=str(node.value), font=("Arial", 11, "bold"))
        
        _draw_subtree(self.root, x=450, y=50, dx=220)
        window.mainloop()
    
    def update_height_and_fb(self, node):
        if not node:
            return
        
        left_height = node.left_son.height if node.left_son else 0
        right_height = node.right_son.height if node.right_son else 0
        
        node.height = 1 + max(left_height, right_height)
        node.balance_fac = left_height - right_height



binarbol = BinTree()
binarbol.insert_node(50)
binarbol.insert_node(20)
binarbol.insert_node(10)
binarbol.insert_node(90)
binarbol.insert_node(60)
binarbol.insert_node(30)
binarbol.insert_node(70)
binarbol.insert_node(80)
binarbol.draw_tree()

# for e in range(0, 85, 5):
#     binarbol.insert_node(e)
# binarbol.draw_tree()

# for e in ["SE", "PA", "AL", "BA", "OR", "LE", "CA", "LU", "GR"]:
#     binarbol.insert_node(e)
# binarbol.draw_tree()

binarbol.delete_node(70)
binarbol.draw_tree()