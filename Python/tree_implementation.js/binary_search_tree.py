import tkinter as tk


class BinNode:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.right_son = None

class BinTree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value, node=None):
        if not self.root:
            self.root = BinNode(value);
            return
        
        if not node:
            node = self.root
        
        if value < node.value:
            if node.left_son:
                self.insert_node(value, node.left_son)
            else :
                node.left_son = BinNode(value)
        
        if value > node.value:
            if node.right_son:
                self.insert_node(value, node.right_son)
            else :
                node.right_son = BinNode(value)
        
        return
    
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
        return node
    
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

    def find_succesor(self, node):
        succesor = node.right_son
        while succesor.left_son:
            succesor = succesor.left_son
        return succesor

binarbol = BinTree()
for e in [40, 60, 10, 5, 15, 30, 25, 35, 50, 70, 45, 37, 32, 31]:
    binarbol.insert_node(e)

binarbol.draw_tree()
binarbol.delete_node(30)
binarbol.draw_tree()