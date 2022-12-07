#load needed libraries
from OCC.Core.IGESControl import IGESControl_Reader
from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.TopAbs import TopAbs_WIRE
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path +="\\..\\data"
file_path_sections= dir_path +"\\test_1_hull_sections.igs"
file_path_sim= dir_path +"\\test_1_simetry_line.igs"
#file_path= dir_path +"\\paluba.igs"
#create new IGES reader class
reader_sections = IGESControl_Reader()
reader_sim = IGESControl_Reader()
#read file, make sure you update path. Note in Windows slash needs to be used
reader_sections.ReadFile(file_path_sections)
reader_sim.ReadFile(file_path_sim)
#no idea what this does but without it the shape won't be created :)
reader_sections.TransferRoots()
reader_sim.TransferRoots()
nbr = reader_sections.NbShapes()
all_shapes = []
#load shape from IGES
for i in range(1, nbr + 1):
        a_shp = reader_sections.Shape(i)
        if not a_shp.IsNull():
            if a_shp.ShapeType() in [TopAbs_WIRE]:
                all_shapes.append(a_shp)
print('number of shapes:',nbr)
#generate Shape
sim_line = reader_sim.Shape(1)
if not sim_line.IsNull():
    if sim_line.ShapeType() in [TopAbs_WIRE]:
        all_shapes.append(sim_line)
#initialize built-in viewer
display, start_display, add_menu, add_function_to_menu = init_display()

display.DisplayShape(all_shapes, update=True)
#show viewer
start_display()