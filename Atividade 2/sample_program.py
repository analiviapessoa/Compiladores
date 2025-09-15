from astminijava import *

main_class = MainClass(name="Main")

program = Program(
    main_class=MainClass("Main"),
    classes=[
        ClassDecl(
            name="Point",
            superclass=None,
            members=[
                VarDecl(Type("int"), "x"),
                VarDecl(Type("int"), "y"),
            ]
        )
    ]
)