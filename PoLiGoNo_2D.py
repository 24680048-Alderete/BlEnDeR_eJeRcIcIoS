import bpy
import math

def crear_poligono_2d(nombre, lados, radio):
    
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)
    
    
    bpy.context.collection.objects.link(objeto)
    
    vertices = []
    aristas = []
    
    
    for i in range(lados):
        angulo= 2 * math.pi * i/lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 0))
        
    
    for i in range(lados):
        aristas.append((i, (i + 1) % lados))
        
        
    malla.from_pydata(vertices, aristas, [])
    malla.update()
    

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()


crear_poligono_2d("Poligono2D", lados=3, radio=10)
