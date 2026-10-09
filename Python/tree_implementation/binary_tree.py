"""
In-order:
Entro al root y veo si tiene hijo izquierda hasta que no tenga mas hijos,
imprimo, luego al root y al final a la derecha
                        A               
                B               C
                            D       E
HojaIzq -> Rama -> HojaDer
Output:BADCE

Pre-order: 
Entra al root y se evalua, luego voy al izquierdo y se repite hasta no tener mas hijos
y luego voy al derecho hasta no tener mas hijos
                        A               
                B               C
                            D       E
Rama -> HojaIzq -> HojaDer
Output:ABCDE

Post-order:
Entra al root, si tiene hijo izquiero evalua a ese primero, luego evalua al derecho y luego al root
                        A               
                B               C
            D       E
HojaIzq -> HojaDer -> Rama
Output:BDECA
"""

import tkinter as tk

class BinNode:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.rigth_son = None

class BinTree:
        def __init__(self):
            self.root = None
        
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
                
                if node.rigth_son:
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
                    _draw_subtree(node.rigth_son, child_x, child_y, dx / 1.9)
                
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
        
        def search_node(self, current_node, target):
            if current_node.value == target:
                return current_node
            
            if current_node.left_son:
                found = self.search_node(current_node.left_son, target)
                if found:
                    return found
                
            if current_node.rigth_son:
                found = self.search_node(current_node.rigth_son, target)
                if found:
                    return found
            
        def insert_node_in_depth(self, value, node=None, way="left", target = None, son="left"):
            if not self.root:
                self.root = BinNode(value)
                return
            
            if not node:
                node = self.root
            
            if target:
                father = self.search_node(node, target)
                if father:
                    if son == "left":
                        if father.left_son:
                            print(f"Sobreescribiendo valor de '{father.left_son}' por '{value}'")
                            father.left_son.value = value
                            return
                        else:
                            father.left_son = BinNode(value)
                            return
                    if son == "rigth":
                        if father.rigth_son:
                            print(f"Sobreescribiendo valor de '{father.rigth_son}' por '{value}'")
                            father.rigth_son.value = value
                            return
                        else:
                            father.rigth_son = BinNode(value)
                            return
            
            if not node.left_son:
                node.left_son = BinNode(value)
            elif not node.rigth_son:
                node.rigth_son = BinNode(value)
            else:
                if way == "left":
                    self.insert_node_in_depth(value, node.left_son, "left")
                elif way == "rigth":
                    self.insert_node_in_depth(value, node.rigth_son, "rigth")
            
        def eval_in(self, node = None, eval = None):
            if not node:
                node = self.root
                eval = []
            
            if node.left_son:
                self.eval_in(node.left_son, eval)
            else :
                if not node.value in eval:
                    eval.append(node.value)
            
            if not node.value in eval:
                eval.append(node.value)
            
            if node.rigth_son:
                self.eval_in(node.rigth_son, eval)
            else :
                if not node.value in eval:
                    eval.append(node.value)
            
            return eval
        
        def eval_pre(self, node = None, eval = None):
            if not node:
                node = self.root
                eval = []
            
            if not node.value in eval:
                eval.append(node.value)
            
            if node.left_son:
                self.eval_pre(node.left_son, eval)
            else :
                if not node.value in eval:
                    eval.append(node.value)
            
            if node.rigth_son:
                self.eval_pre(node.rigth_son, eval)
            else :
                if not node.value in eval:
                    eval.append(node.value)
            
            return eval
        
        def eval_post(self, node = None, eval = None):
            if not node:
                node = self.root
                eval = []
            
            if node.left_son:
                self.eval_post(node.left_son, eval)
            else :
                if not node.value in eval:
                    eval.append(node.value)
            
            if node.rigth_son:
                self.eval_post(node.rigth_son, eval)
            else :
                if not node.value in eval:
                    eval.append(node.value)
            
            if not node.value in eval:
                eval.append(node.value)
            
            return eval

binarbol = BinTree()

binarbol.insert_node_in_depth("A")
binarbol.insert_node_in_depth("B", way="rigth")
binarbol.insert_node_in_depth("C", way="rigth")
binarbol.insert_node_in_depth("D", way="rigth")
binarbol.insert_node_in_depth("E", way="rigth")

print("Evaluación In-order:", "".join(binarbol.eval_in()))
print("Evaluación Pre-order:", "".join(binarbol.eval_pre()))
print("Evaluación Post-order:", "".join(binarbol.eval_post()))

binarbol.draw_tree()

binarbol.insert_node_in_depth("F", target="D", son="left")

binarbol.draw_tree()

