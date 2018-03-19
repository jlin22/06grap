from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [66, 206, 244]
edges = []
transform = new_matrix()
parse_file( 's', edges, transform, screen, color )