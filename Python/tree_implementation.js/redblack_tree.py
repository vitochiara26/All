import tkinter as tk


class BinNode:
    def __init__(self, value):
        self.value = value
        self.left_son = None
        self.right_son = None
        self.color = "Red"
    
class BinTree:
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
        
        #conflicto rama Izq
        if node.left_son and node.left_son.color == "Red":
            padre = node.left_son
            #algun nieto es rojo?
            if (padre.left_son and padre.left_son.color == "Red") or \
                (padre.right_son and padre.right_son.color == "Red"):
                
                tio = node.right_son
                color_tio = tio.color if tio else "Black"
                
                if color_tio == "Red":
                    #Caso 1 tio rojo -> recolorear
                    padre.color = "Black"
                    tio.color = "Black"
                    node.color = "Red"
                else:
                    #Caso 2 tio negro -> Rotacion + recolorear
                    #subcaso, si es Izq-Der (Zig-Zag)
                    if padre.right_son and padre.right_son.color == "Red":
                        node.left_son = self.rot_izq(padre)
                        padre = node.left_son

                    #subcaso, si es Izq-Izq (Diagonal)
                    node = self.rot_der(node)
                    node.color = "Black"
                    if node.right_son:
                        node.right_son.color = "Red"
        
        #conflicto rama der
        if node.right_son and node.right_son.color == "Red":
            padre = node.right_son
            #algun nieto es rojo?
            if (padre.left_son and padre.left_son.color == "Red") or \
                (padre.right_son and padre.right_son.color == "Red"):
                
                tio = node.left_son
                color_tio = tio.color if tio else "Black"
                
                if color_tio == "Red":
                    #Caso 1 tio rojo -> recolorear
                    padre.color = "Black"
                    tio.color = "Black"
                    node.color = "Red"
                else:
                    #Caso 2 tio negro -> Rotacion + recolorear
                    #subcaso, si es Der-Izq (Zig-Zag)
                    if padre.left_son and padre.left_son.color == "Red":
                        node.right_son = self.rot_der(padre)
                        padre = node.right_son
                    
                    #subcaso, si es Der-Der (Diagonal)
                    node = self.rot_izq(node)
                    node.color = "Black"
                    if node.left_son:
                        node.left_son.color = "Red"
        
        if is_root_call:
            self.root = node
            self.root.color = "Black"
            
        return node
    
    def delete_node(self, value, node=None):
        if not self.root:
            return None
        
        self.root, _ = self._delete_recursive(self.root, value)

        if self.root:
            self.root.color = "Black"
        return self.root
    
    def _delete_recursive(self, node, value):
        if not node:
            return None, False
        
        needs_fix = False
        
        if value < node.value:
            node.left_son, needs_fix = self._delete_recursive(node.left_son, value)
            if needs_fix:
                node, needs_fix = self._fix_left_deficit(node)
        
        elif value > node.value:
            node.right_son, needs_fix = self._delete_recursive(node.right_son, value)
            if needs_fix:
                node, needs_fix = self._fix_right_deficit(node)
        
        else :
            #Found node to delete!!!
            if not node.left_son or not node.right_son:
                temp = node.left_son if node.left_son else node.right_son
                original_color = node.color
                
                if temp is None:
                    #Leaf node deleted: is was black, require black-height fix
                    return None, (original_color == "Black")
                else:
                    #It's have only one son: the son take his place and must be black
                    temp.color = "Black"
                    return temp, False
            
            else:
                #have two sons
                succesor = self.find_succesor(node)
                node.value = succesor.value
                node.right_son, needs_fix = self._delete_recursive(
                    node.right_son, succesor.value
                )
                if needs_fix:
                    node, needs_fix = self._fix_right_deficit(node)
            
        return node, needs_fix
    
    def _fix_left_deficit(self, node):
        brother = node.right_son
        if not brother:
            return node, True
        
        #Case 1: Bro is red
        if brother.color == "Red":
            brother.color = "Black"
            node.color = "Red"
            node = self.rot_izq(node)
            sub_node, needs_fix = self._fix_left_deficit(node.left_son)
            node.left_son = sub_node
            return node, needs_fix
        
        #Bro is Black
        bro_left_color = brother.left_son.color if brother.left_son else "Black"
        bro_right_color = brother.right_son.color if brother.right_son else "Black"
        
        #Case 2: Both nephew are Black
        if bro_left_color == "Black" and bro_right_color == "Black":
            brother.color = "Red"
            if node.color == "Red":
                node.color = "Black"
                return node, False
            return node, True
        
        #Case 3: Outer nephew is Black, inner is Red
        if bro_right_color == "Black":
            if brother.left_son:
                brother.left_son.color = "Black"
            brother.color = "Red"
            node.right_son = self.rot_der(brother)
            brother = node.right_son
        
        #Case 4: Outer nephew is Red
        brother.color = node.color
        node.color = "Black"
        if brother.right_son:
            brother.right_son.color = "Black"
        node = self.rot_izq(node)
        
        return node, False
    
    def _fix_right_deficit(self, node):
        brother = node.left_son
        if not brother:
            return node, True
        
        #Case 1: Bro is Red
        if brother.color == "Red":
            brother.color = "Black"
            node.color = "Red"
            node = self.rot_der(node)
            sub_node, needs_fix = self._fix_right_deficit(node.right_son)
            node.right_son = sub_node
            return node, needs_fix
        
        #Bro is Black
        bro_left_color = brother.left_son.color if brother.left_son else "Black"
        bro_right_color = brother.right_son.color if brother.right_son else "Black"
        
        #Case 2: Both nephew are Black
        if bro_left_color == "Black" and bro_right_color == "Black":
            brother.color = "Red"
            if node.color == "Red":
                node.color = "Black"
                return node, False
            return node, True
        
        #Case 3: Outer nephew is Black, inner is Red
        if bro_left_color == "Black":
            if brother.right_son:
                brother.right_son.color = "Black"
            brother.color = "Red"
            node.left_son = self.rot_izq(brother)
            brother = node.left_son
        
        #Case 4: Outer nephew is Red
        brother.color = node.color
        node.color = "Black"
        if brother.left_son:
            brother.left_son.color = "Black"
        node = self.rot_der(node)
        return node, False
    
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
        
        return new_root
    
    def rot_izq(self, node):
        new_root = node.right_son
        sub_tree = new_root.left_son
        
        new_root.left_son = node
        node.right_son = sub_tree
        
        return new_root
    
    def draw_tree(self):
        if not self.root:
            raise IndexError("El árbol está vacío")
        
        window = tk.Tk()
        window.title("Visualizador de Árbol RedBlack")
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
            
            child_x = x + dx
            
            if node.right_son:
                canvas.create_line(
                    x,
                    y + radius,
                    child_x, 
                    child_y - radius,
                    width=1.5,
                    arrow=tk.LAST,
                    fill="black",
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
            
            fill_color = "#FF0000" if str(node.color).lower() in ["red", "rojo"] else "black"
            canvas.create_oval(
                x -radius,
                y - radius,
                x + radius,
                y + radius,
                fill = fill_color,
                outline="black",
                width=1.5,
            )
            canvas.create_text(
                x,
                y,
                text=str(node.value),
                fill="white",
                font=("Arial", 12, "bold"))
        
        _draw_subtree(self.root, x=500, y=50, dx=230)
        window.mainloop()


redblack_tree = BinTree()
for val in [13, 8, 17, 1, 25, 11, 15, 6, 27, 22]:
    redblack_tree.insert_node(val)

print("Mostrando árbol antes de eliminar el 25...")
redblack_tree.draw_tree()

redblack_tree.delete_node(25)

print("Mostrando árbol despues de eliminar el 25...")
redblack_tree.draw_tree()
