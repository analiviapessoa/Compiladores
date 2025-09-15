from typing import List, Optional

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, main_class, classes: List['ClassDecl']):
        self.main_class = main_class
        self.classes = classes

class MainClass(ASTNode):
    def __init__(self, name: str):
        self.name = name 

class ClassDecl(ASTNode):
    def __init__(self, name: str, superclass: Optional[str], members: List['ClassMember']):
        self.name = name
        self.superclass = superclass  
        self.members = members  

class ClassMember(ASTNode):
    pass

class VarDecl(ClassMember):
    def __init__(self, type_, name: str):
        self.type = type_
        self.name = name

class MethodDecl(ClassMember):
    def __init__(self, return_type, name: str, parameters: List['Param'], body: List[ASTNode]):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body  

class Param(ASTNode):
    def __init__(self, type_, name: str):
        self.type = type_
        self.name = name

class Type(ASTNode):
    def __init__(self, name: str, array_depth: int = 0):
        self.name = name  
        self.array_depth = array_depth  

class Print(ASTNode):
    def __init__(self):
        pass  
