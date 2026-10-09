class TreeNode:
    def __init__(self, value):
        self.value = value
        self.sons = []
        self.grade = 0


class Tree:
    def __init__(self):
        self.root = None
    
    def look_over(self, current_node , target_node):
        """Buscar en el arbol hasta encontrar el nodo objetivo"""
        if not self.root:
            raise IndexError("El arbol está vacio")
        
        if current_node.value == target_node:
            return current_node
        
        for son in current_node.sons:
            found = self.look_over(son, target_node)
            if found:
                return found
        
        return None
    
    def find_parent(self, current_node, target_node):
        """Busca al padre del nodo objetivo"""
        if not current_node:
            return None
        
        for son in current_node.sons:
            if son.value == target_node:
                return current_node
            
            found_parent = self.find_parent(son, target_node)
            if found_parent:
                return found_parent
        
        return None
    
    def create_node(self, value, target_node = None):
        new_node = TreeNode(value)
        
        if target_node is None:
            if self.root:
                new_node.sons.append(self.root)
                new_node.grade += 1
                self.root = new_node
            else : 
                self.root = new_node
            
            return
        
        father_node = self.look_over(self.root, target_node)
        if father_node:
            father_node.sons.append(new_node)
            father_node.grade += 1
        else:
            raise ValueError(f"No se encontró el nodo padre {target_node}")
    
    def delete_node(self, target_node):
        """Eliminar el nodo objetivo"""
        if not self.root:
            raise IndexError("El árbol esta vacío")
        
        if self.root.value == target_node:
            self.root = None
            return
        
        parent = self.find_parent(self.root, target_node)
        if parent:
            for son in parent.sons:
                if son.value == target_node:
                    parent.sons.remove(son)
                    parent.grade -= 1
                    return
        else:
            raise ValueError(f"No se encontró '{target_node}' en el árbol")
    
    def read_tree(self, current_node=None, target_node=None,
                prefix="", is_last=True, is_first=True):
        if is_first:
            if target_node:
                current_node = self.look_over(self.root, target_node)
            else:
                current_node = self.root
        
        if not current_node:
            return ""
        
        if is_first:
            visual = f"{current_node.value}\n"
        else:
            conector = "└── " if is_last else "├── "
            visual = f"{prefix}{conector}{current_node.value}\n"
        
        if not is_first:
            prefix += "    " if is_last else "|   "
        
        total_sons = len(current_node.sons)
        for index, son in enumerate(current_node.sons):
            is_last_child = (index == total_sons - 1)
            visual += self.read_tree(
                son,
                prefix = prefix,
                is_last = is_last_child,
                is_first = False
            )
        
        return visual
    
    def update_node(self, target_node, new_value):
        """Localiza un nodo objetivo y actualiza su valor"""
        if not self.root:
            raise IndexError("El Árbol está vacío")
        
        node = self.look_over(self.root, target_node)
        if node:
            node.value = new_value
        else :
            raise ValueError(f"No se encontro '{target_node}' para actualizar")
    
    def get_grade(self, target_node):
        """Retorna el grado de un nodo objetivo"""
        if not self.root:
            raise IndexError("El Árbol está vacío")
        
        node = self.look_over(self.root, target_node)
        if node:
            return node.grade
        else :
            raise ValueError(f"No se encontro '{target_node}'")
    
    def get_node_level(self, target_node, 
                    current_node=None, current_level=0, is_first=True):
        """Retorna el nivel de un nodo especifico, Root = level 0"""
        if is_first:
            if not self.root:
                raise IndexError("El árbol está vacío")
            current_node =  self.root
        
        if current_node.value == target_node:
            return current_level
        
        for son in current_node.sons:
            level = self.get_node_level(
                target_node,
                son,
                current_level + 1,
                is_first = False
            )
            if level is not None:
                return level
        
        return None
    
    def get_tree_height(self, current_node=None, is_first=True):
        """Retorna el nivel maximo o altura total del arbol"""
        if is_first:
            if not self.root:
                return 0
            current_node = self.root
        
        if not current_node.sons:
            return 0
        
        return 1 + (max(self.get_tree_height(son, is_first=False) for son in current_node.sons))


arbol = Tree()
arbol.create_node("A")
arbol.create_node("B", "A")
arbol.create_node("C", "A")
arbol.create_node("Z", "B")
arbol.create_node("D", "C")
arbol.create_node("E", "C")
arbol.create_node("F", "E")

print("--- Árbol Original ---")
print(arbol.read_tree())

arbol.update_node("C", "X")

print("--- Árbol tras actualizar 'C' a 'X' ---")
print(arbol.read_tree())


print(f"Grado del nodo X: {arbol.get_grade("X")}")

print("Nivel de 'A' (root):", arbol.get_node_level("A"))
print("Nivel de 'B':", arbol.get_node_level("B"))
print("Nivel de 'E':", arbol.get_node_level("E"))

print("Altura del arbol:", arbol.get_tree_height())
