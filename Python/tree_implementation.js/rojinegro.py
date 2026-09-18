import tkinter as tk


class BinNode:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.right_son = None
        self.color = "Red"
        
class BinArbol:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value, node=None):
        if not self.root:
            self.root = BinNode(value)
            self.root.color = "Black"
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
        
        #Conflicto por el lado izquierdo?
        if node.left_son and node.left_son.color == "Red":
            #"node" va ser tomado como abuelo, su hijo izquierdo 
            # sera un padre y si tiene algun hijo sera un nieto
            father_node = node.left_son
            #Se pregunta si tengo algun nieto rojo
            if (father_node.left_son and father_node.left_son.color == "Red" or
                father_node.right_son and father_node.right_son.color == "Red"):
                
                uncle_node = node.right_son
                uncle_color = uncle_node.color if uncle_node else "black"
                
                #caso 1: Tio es Rojo
                if uncle_color == "Red":
                    father_node.color = "Black"
                    uncle_node.color = "Black"
                    node.color = "Red"
                #caso 2: Tio es Negro
                else:
                    if father_node.right_son and father_node.right_son.color:
                        node.left_son = self.rot_izq(father_node)
                        father_node = node.left_son
                    
                    node = self.rot_der(node)
                    node.color = "Black"
                    if node.right_son:
                        node.right_son.color = "Red"
        
        #Conflicto por el lado derecho?
        if node.right_son and node.right_son.color == "Red":
            #"node" va ser tomado como abuelo, su hijo izquierdo 
            # sera un padre y si tiene algun hijo sera un nieto
            father_node = node.right_son
            #Se pregunta si tengo algun nieto rojo
            if (father_node.left_son and father_node.left_son.color == "Red" or
                father_node.right_son and father_node.right_son.color == "Red"):
                
                uncle_node = node.left_son
                uncle_color = uncle_node.color if uncle_node else "black"

                #caso 1: Tio es Rojo
                if uncle_color == "Red":
                    father_node.color = "Black"
                    uncle_node.color = "Black"
                    node.color = "Red"
                #caso 2: Tio es Negro
                else:
                    if father_node.left_son and father_node.right_son.color:
                        node.right_son = self.rot_der(father_node)
                        father_node = node.right_son
                    
                    node = self.rot_izq(node)
                    node.color = "Black"
                    if node.left_son:
                        node.left_son.color = "Red"
                
        if is_root_call:
            self.root = node
            
        return node
    
    def draw_tree(self):
            if not self.root:
                raise IndexError("El árbol está vacío")
            
            window = tk.Tk()
            window.title("Visualizador de Árbol Rojinegro")
            window.geometry("1000x750")
            
            canvas = tk.Canvas(window, bg="white")
            canvas.pack(fill=tk.BOTH, expand = True)
            
            radius = 22
            level_height = 80
            nil_w, nil_h = 22, 12
        
            def _draw_subtree(node, x, y, dx):
                child_x = x - dx
                child_y = y + level_height
                
                if node.left_son:
                    canvas.create_line(
                        x,
                        y + radius,
                        child_x, 
                        child_y - radius,
                        width=1.5,
                        arrow=tk.LAST,
                        fill="black",
                    )
                    _draw_subtree(node.left_son, child_x, child_y, dx / 1.95)
                else:
                    canvas.create_line(
                        x,
                        y + radius,
                        child_x,
                        child_y - nil_h,
                        width=1.5,
                        arrow=tk.LAST,
                        fill="black",
                    )
                    canvas.create_rectangle(
                        child_x - nil_w,
                        child_y - nil_h,
                        child_x + nil_w,
                        child_y + nil_h,
                        fill="black",
                        outline="black"
                    )
                    canvas.create_text(
                        child_x,
                        child_y,
                        text="NIL",
                        fill= "white",
                        font=("Arial", 8, "bold")
                    )
                
                child_x = x + dx
                
                if node.right_son:
                    canvas.create_line(
                        x,
                        y + radius,
                        child_x, 
                        child_y - radius,
                        width=2,
                        arrow=tk.LAST,
                        fill="#000000",
                    )
                    _draw_subtree(node.right_son, child_x, child_y, dx / 1.95)
                else:
                    canvas.create_line(
                    x,
                    y + radius,
                    child_x,
                    child_y - nil_h,
                    width=1.5,
                    arrow=tk.LAST,
                    fill="black"
                    )
                    canvas.create_rectangle(
                        child_x - nil_w,
                        child_y - nil_h,
                        child_x + nil_w,
                        child_y + nil_h,
                        fill="black",
                        outline="black"
                    )
                    canvas.create_text(
                        child_x,
                        child_y,
                        text="NIL",
                        fill="white",
                        font=("Arial", 8, "bold")
                    )
                
                fill_color = "#FF0000" if node.color == "Red" else "black"
                canvas.create_oval(
                    x -radius,
                    y - radius,
                    x + radius,
                    y + radius,
                    fill = fill_color,
                    outline="#000000",
                    width=2,
                )
                
                canvas.create_text(
                    x, 
                    y, 
                    text=str(node.value),
                    fill="white",
                    font=("Arial", 12, "bold"))
            
            _draw_subtree(self.root, x=500, y=50, dx=230)
            window.mainloop()
    
    def rot_der(self, node):
        new_root = node.left_son
        sub_tree = new_root.right_son
        
        new_root.right_son = node
        node.left_son = sub_tree
        
        return new_root
    
    def rot_izq(self, node):
        new_root = node.right_son
        sub_tree = new_root.left_son
        
        new_root.left_son = node
        node.right_son = sub_tree
        
        return new_root

binarbol = BinArbol()
binarbol.insert_node(13)
binarbol.insert_node(8)
binarbol.insert_node(10)

binarbol.draw_tree()
