#----------------------------------------------------------
# File __init__.py
#----------------------------------------------------------

if "bpy" in locals():
    import imp
    imp.reload(ModelingCloth28)
else:
    from . import ModelingCloth28

def register():
    ModelingCloth28.register()

def unregister():
    ModelingCloth28.unregister()

if __name__ == "__main__":
    register()
