#load needed libraries
from OCC.Core.IGESControl import IGESControl_Reader
from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.TopAbs import TopAbs_WIRE
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path +="\\..\\data"
file_path_sur= dir_path +"\\test_1_hull_exported.igs"
#
reader_sur = IGESControl_Reader()
#read file, make sure you update path. Note in Windows slash needs to be used
reader_sur.ReadFile(file_path_sur)

#no idea what this does but without it the shape won't be created :)
reader_sur.TransferRoots()
shape_sur = reader_sur.Shape()
#initialize built-in viewer
display, start_display, add_menu, add_function_to_menu = init_display()
#load shape from IGES
display.DisplayShape(shape_sur, update=True)
#show viewer
start_display()