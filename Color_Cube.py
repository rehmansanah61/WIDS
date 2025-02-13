# Color_Cube.py
import vpython as vp
from Cube_Piece import Cube_Piece
from Algorithms import *
import random
import time
from time import sleep

class Color_Cube:
    def __init__(self):
        cube_size = vp.vector(1,1,1)
        self.scene = vp.canvas(width=1500, height=800, background=vp.vector(0, 0, 139/255))

        self.scene.userpan = True # Enable user panning
        self.scene.userzoom = True # Enable user zooming
        self.scene.userspin = True # Enable user rotation
        self.rotation_angle = vp.pi/2

        lights = [
            vp.vector(10,10,10),
            vp.vector(-10,-10,-10),
            vp.vector(-10,10,10),
            vp.vector(10,-10,10),
            vp.vector(10,10,-10),
            vp.vector(-10,-10,10)
        ]

        for pos in lights:
            vp.local_light(pos=pos, color=vp.color.white*0.5)

        Centers, Edges, Vertices = {}, {}, {}
        all_colors = [
            vp.color.black,
            vp.color.purple,
            vp.color.red,
            vp.color.green,
            vp.color.white,
            vp.color.yellow
        ]

        center_coords = [
            vp.vector(0, 1.05, 0),
            vp.vector(0, -1.05, 0),
            vp.vector(1.05, 0, 0),
            vp.vector(-1.05, 0, 0),
            vp.vector(0, 0, 1.05),
            vp.vector(0, 0, -1.05)
        ]

        edge_coords = [
            vp.vector(1.05,1.05,0),
            vp.vector(1.05,-1.05,0),
            vp.vector(-1.05,1.05,0),
            vp.vector(-1.05,-1.05,0),
            vp.vector(1.05,0,1.05),
            vp.vector(1.05,0,-1.05),
            vp.vector(-1.05,0,1.05),
            vp.vector(-1.05,0,-1.05),
            vp.vector(0,1.05,1.05),
            vp.vector(0,1.05,-1.05),
            vp.vector(0,-1.05,1.05),
            vp.vector(0,-1.05,-1.05)
        ]

        vertex_coords = [
            vp.vector(1.05,1.05,1.05),
            vp.vector(1.05,1.05,-1.05),
            vp.vector(1.05,-1.05,1.05),
            vp.vector(1.05,-1.05,-1.05),
            vp.vector(-1.05,1.05,1.05),
            vp.vector(-1.05,1.05,-1.05),
            vp.vector(-1.05,-1.05,1.05),
            vp.vector(-1.05,-1.05,-1.05)
        ]

        def assign_color(all_colors, active_colors):
            return [color if color in active_colors else vp.color.black for color in all_colors]

        CenterMost = Cube_Piece(center=vp.vector(0,0,0),size=cube_size,color=[vp.color.black]*6)
        center_map = {
            0: ('Up', [vp.color.white]),
            1: ('Down', [vp.color.yellow]),
            2: ('Front Right', [vp.color.red]),
            3: ('Back Left', [vp.color.green]),
            4: ('Front Left', [vp.color.black]),
            5: ('Back Right', [vp.color.purple]),
        }

        for i, coord in enumerate(center_coords):
            name, active_colors = center_map[i]
            c = assign_color(all_colors, active_colors)
            Centers[name] = Cube_Piece(center=coord, size=cube_size, color=c)

        edge_map = {
            0: ('Front Right Up', [vp.color.red, vp.color.white]),
            1: ('Front Right Down', [vp.color.red, vp.color.yellow]),
            2: ('Back Left Up', [vp.color.green, vp.color.white]),
            3: ('Back Left Down', [vp.color.green, vp.color.yellow]),
            4: ('Front', [vp.color.black, vp.color.red]),
            5: ('Right', [vp.color.red, vp.color.purple]),
            6: ('Left', [vp.color.black, vp.color.green]),
            7: ('Back', [vp.color.green, vp.color.purple]),
            8: ('Front Left Up', [vp.color.black, vp.color.white]),
            9: ('Back Right Up', [vp.color.purple, vp.color.white]),
            10: ('Front Left Down', [vp.color.black, vp.color.yellow]),
            11: ('Back Right Down', [vp.color.purple, vp.color.yellow])
        }

        for i, coord in enumerate(edge_coords):
            name, active_colors = edge_map[i]
            c = assign_color(all_colors, active_colors)
            Edges[name] = Cube_Piece(center=coord, size=cube_size, color=c)

        vertex_map = {
            0: ('Front Up', [vp.color.black, vp.color.red, vp.color.white]),
            1: ('Right Up', [vp.color.purple, vp.color.red, vp.color.white]),
            2: ('Front Down', [vp.color.black, vp.color.red, vp.color.yellow]),
            3: ('Right Down', [vp.color.purple, vp.color.red, vp.color.yellow]),
            4: ('Left Up', [vp.color.black, vp.color.green, vp.color.white]),
            5: ('Back Up', [vp.color.purple, vp.color.white, vp.color.green]),
            6: ('Left Down', [vp.color.black, vp.color.green, vp.color.yellow]),
            7: ('Back Down', [vp.color.purple, vp.color.green, vp.color.yellow])
        }

        for i, coord in enumerate(vertex_coords):
            name, active_colors = vertex_map[i]
            c = assign_color(all_colors, active_colors)
            Vertices[name] = Cube_Piece(center=coord, size=cube_size, color=c)

        Cube_colors = {
            'Red': vp.color.black,
            'Orange': vp.color.purple,
            'Blue': vp.color.red,
            'Green': vp.color.green,
            'White': vp.color.white,
            'Yellow': vp.color.yellow
        }

        Cube_Sides = ['Up','Down','Front Right','Front Left','Back Right','Back Left']
        self.update_camera()
        self.Centers = Centers
        self.Edges = Edges
        self.Vertices = Vertices
        self.Colours = Cube_colors
        self.Sides = Cube_Sides
        self.Update_State()

        self.scene.camera.pos = vp.vector(5,5,5)
        self.scene.camera.axis = vp.vector(-5,-5,-5)
        self.scene.camera.up = vp.vector(0,1,0)
        self.scene.bind('keydown', self.handle_keydown)
        self.rotation_angle = 0.1 # Rotation step size
        self.cube_center = vp.vector(0, 0, 0)
        self.Centers = Centers
        self.Edges = Edges
        self.Vertices = Vertices
        self.Colours = Cube_colors
        self.Sides = Cube_Sides
        self.Update_State()

    def handle_keydown(self, evt):
        key = evt.key
        if key == 'x':
            self.rotate_cube(vp.vector(1, 0, 0)) # Rotate around x-axis
        elif key == 'y':
            self.rotate_cube(vp.vector(0, 1, 0)) # Rotate around y-axis
        elif key == 'z':
            self.rotate_cube(vp.vector(0, 0, 1)) # Rotate around z-axis
        elif key == 'X':
            self.rotate_cube(vp.vector(1, 0, 0), reverse=True) # Rotate around x-axis in reverse
        elif key == 'Y':
            self.rotate_cube(vp.vector(0, 1, 0), reverse=True) # Rotate around y-axis in reverse
        elif key == 'Z':
            self.rotate_cube(vp.vector(0, 0, 1), reverse=True) # Rotate around z-axis in reverse
        elif key == 's':  # Scramble the cube
            self.Scramble()
        elif key == 'a':  # Align centers
            self.Align_Centers()
            sleep(2)
            self.Solve_First_Layer()
            sleep(0.5)
            while(Houston_We_Have_A_Problem(self)):
                Solve_First_Layer(self)
                sleep(0.5)

            sleep(3)   
            self.Solve_Second_Layer()
            sleep(3)
            self.Solve_Third_Layer()
            # sleep(50)


    
    def Scramble(self):
        Scramble(self)
        sleep(1)

    def Solve_Second_Layer(self):
        Solve_Second_Layer(self)
    def Solve_Third_Layer(self):
        Solve_Top_Layer(self)

    def Align_Centers(self):
        """
        Aligns the centers of the cube to their correct positions.
        """
        if self.State['Down']['Center'] != self.Colours['Yellow']:
            for side in self.Sides:
                if self.State[side]['Center'] == self.Colours['Yellow']:
                    current_side = side
            if current_side == 'Up':
                self.x(2)
            elif current_side == 'Front Left':
                self.x_()
            elif current_side == 'Back Right':
                self.x()
            elif current_side == 'Front Right':
                self.z()
            else:
                self.z_()

        if self.State['Front Right']['Center'] != self.Colours['Blue']:
            for side in self.Sides[2:]:
                if self.State[side]['Center'] == self.Colours['Blue']:
                    current_side = side
            if current_side == 'Front Left':
                self.y_()
            elif current_side == 'Back Right':
                self.y()
            elif current_side == 'Back Left':
                self.y(2)

    def Solve_First_Layer(self):
        """
        Solves the first layer of the cube (yellow cross and yellow corners).
        """
        Yellow_Cross(self)  # Solve the yellow cross
        Yellow_Corners(self)  # Solve the yellow corners

    
            
            
    
    def U (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            vert_axis = vp.vector(0, 1, 0)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps
            
            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, vert_axis,i)

            Edge_FLU = Cube.Edges['Front Right Up']
            Edge_BLU = Cube.Edges['Front Left Up']
            Edge_FRU = Cube.Edges['Back Right Up']
            Edge_BRU = Cube.Edges['Back Left Up']
            Vert_LU = Cube.Vertices['Front Up']
            Vert_FU = Cube.Vertices['Right Up']
            Vert_BU = Cube.Vertices['Left Up']
            Vert_RU = Cube.Vertices['Back Up']

            Cube.Edges['Front Left Up'] = Edge_FLU
            Cube.Edges['Back Left Up'] = Edge_BLU
            Cube.Edges['Front Right Up'] = Edge_FRU
            Cube.Edges['Back Right Up'] = Edge_BRU
            Cube.Vertices['Left Up'] = Vert_LU
            Cube.Vertices['Front Up'] = Vert_FU
            Cube.Vertices['Back Up'] = Vert_BU
            Cube.Vertices['Right Up'] = Vert_RU
            Cube.Update_State()

        

    def U_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            vert_axis = vp.vector(0, 1, 0)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps
            
            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, vert_axis,i)

            Edge_BRU = Cube.Edges['Front Right Up']
            Edge_FRU = Cube.Edges['Front Left Up']
            Edge_BLU = Cube.Edges['Back Right Up']
            Edge_FLU = Cube.Edges['Back Left Up']
            Vert_RU = Cube.Vertices['Front Up']
            Vert_BU = Cube.Vertices['Right Up']
            Vert_FU = Cube.Vertices['Left Up']
            Vert_LU = Cube.Vertices['Back Up']

            Cube.Edges['Front Left Up'] = Edge_FLU
            Cube.Edges['Back Left Up'] = Edge_BLU
            Cube.Edges['Front Right Up'] = Edge_FRU
            Cube.Edges['Back Right Up'] = Edge_BRU
            Cube.Vertices['Left Up'] = Vert_LU
            Cube.Vertices['Front Up'] = Vert_FU
            Cube.Vertices['Back Up'] = Vert_BU
            Cube.Vertices['Right Up'] = Vert_RU
            Cube.Update_State()


    def D (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            vert_axis = vp.vector(0, 1, 0)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps
            
            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, vert_axis,i)

            Edge_BRD = Cube.Edges['Front Right Down']
            Edge_FRD = Cube.Edges['Front Left Down']
            Edge_BLD = Cube.Edges['Back Right Down']
            Edge_FLD = Cube.Edges['Back Left Down']
            Vert_RD = Cube.Vertices['Front Down']
            Vert_BD = Cube.Vertices['Right Down']
            Vert_FD = Cube.Vertices['Left Down']
            Vert_LD = Cube.Vertices['Back Down']

            Cube.Edges['Front Left Down'] = Edge_FLD
            Cube.Edges['Back Left Down'] = Edge_BLD
            Cube.Edges['Front Right Down'] = Edge_FRD
            Cube.Edges['Back Right Down'] = Edge_BRD
            Cube.Vertices['Left Down'] = Vert_LD
            Cube.Vertices['Front Down'] = Vert_FD
            Cube.Vertices['Back Down'] = Vert_BD
            Cube.Vertices['Right Down'] = Vert_RD
            Cube.Update_State()


    def D_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            vert_axis = vp.vector(0, 1, 0)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps
            
            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, vert_axis,i)

            Edge_FLD = Cube.Edges['Front Right Down']
            Edge_BLD = Cube.Edges['Front Left Down']
            Edge_FRD = Cube.Edges['Back Right Down']
            Edge_BRD = Cube.Edges['Back Left Down']
            Vert_LD = Cube.Vertices['Front Down']
            Vert_FD = Cube.Vertices['Right Down']
            Vert_BD = Cube.Vertices['Left Down']
            Vert_RD = Cube.Vertices['Back Down']

            Cube.Edges['Front Left Down'] = Edge_FLD
            Cube.Edges['Back Left Down'] = Edge_BLD
            Cube.Edges['Front Right Down'] = Edge_FRD
            Cube.Edges['Back Right Down'] = Edge_BRD
            Cube.Vertices['Left Down'] = Vert_LD
            Cube.Vertices['Front Down'] = Vert_FD
            Cube.Vertices['Back Down'] = Vert_BD
            Cube.Vertices['Right Down'] = Vert_RD
            Cube.Update_State()


    def R (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            horz_axis = vp.vector(1, 0, 0)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Front'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

            Edge_F = Cube.Edges['Front Right Down']
            Edge_R = Cube.Edges['Front Right Up']
            Edge_FRU = Cube.Edges['Front']
            Edge_FRD = Cube.Edges['Right']
            Vert_FU = Cube.Vertices['Front Down']
            Vert_FD = Cube.Vertices['Right Down']
            Vert_RD = Cube.Vertices['Right Up']
            Vert_RU = Cube.Vertices['Front Up']

            Cube.Edges['Front'] = Edge_F
            Cube.Edges['Right'] = Edge_R
            Cube.Edges['Front Right Up'] = Edge_FRU
            Cube.Edges['Front Right Down'] = Edge_FRD
            Cube.Vertices['Front Up'] = Vert_FU
            Cube.Vertices['Front Down'] = Vert_FD
            Cube.Vertices['Right Down'] = Vert_RD
            Cube.Vertices['Right Up'] = Vert_RU
            Cube.Update_State()


    def R_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            horz_axis = vp.vector(1, 0, 0)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Front'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Right'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

            Edge_R = Cube.Edges['Front Right Down']
            Edge_F = Cube.Edges['Front Right Up']
            Edge_FRD = Cube.Edges['Front']
            Edge_FRU = Cube.Edges['Right']
            Vert_RD = Cube.Vertices['Front Down']
            Vert_RU = Cube.Vertices['Right Down']
            Vert_FU = Cube.Vertices['Right Up']
            Vert_FD = Cube.Vertices['Front Up']

            Cube.Edges['Front'] = Edge_F
            Cube.Edges['Right'] = Edge_R
            Cube.Edges['Front Right Up'] = Edge_FRU
            Cube.Edges['Front Right Down'] = Edge_FRD
            Cube.Vertices['Front Up'] = Vert_FU
            Cube.Vertices['Front Down'] = Vert_FD
            Cube.Vertices['Right Down'] = Vert_RD
            Cube.Vertices['Right Up'] = Vert_RU
            Cube.Update_State()


    def L (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            horz_axis = vp.vector(1, 0, 0)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Back'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

            Edge_B = Cube.Edges['Back Left Down']
            Edge_L = Cube.Edges['Back Left Up']
            Edge_BLU = Cube.Edges['Back']
            Edge_BLD = Cube.Edges['Left']
            Vert_BU = Cube.Vertices['Back Down']
            Vert_BD = Cube.Vertices['Left Down']
            Vert_LD = Cube.Vertices['Left Up']
            Vert_LU = Cube.Vertices['Back Up']

            Cube.Edges['Back'] = Edge_B
            Cube.Edges['Left'] = Edge_L
            Cube.Edges['Back Left Up'] = Edge_BLU
            Cube.Edges['Back Left Down'] = Edge_BLD
            Cube.Vertices['Back Up'] = Vert_BU
            Cube.Vertices['Back Down'] = Vert_BD
            Cube.Vertices['Left Down'] = Vert_LD
            Cube.Vertices['Left Up'] = Vert_LU
            Cube.Update_State()


    def L_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            horz_axis = vp.vector(1, 0, 0)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Back'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Edges['Left'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)    
                Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, horz_axis,i)    

            Edge_L = Cube.Edges['Back Left Down']
            Edge_B = Cube.Edges['Back Left Up']
            Edge_BLD = Cube.Edges['Back']
            Edge_BLU = Cube.Edges['Left']
            Vert_LD = Cube.Vertices['Back Down']
            Vert_LU = Cube.Vertices['Left Down']
            Vert_BU = Cube.Vertices['Left Up']
            Vert_BD = Cube.Vertices['Back Up']

            Cube.Edges['Back'] = Edge_B
            Cube.Edges['Left'] = Edge_L
            Cube.Edges['Back Left Up'] = Edge_BLU
            Cube.Edges['Back Left Down'] = Edge_BLD
            Cube.Vertices['Back Up'] = Vert_BU
            Cube.Vertices['Back Down'] = Vert_BD
            Cube.Vertices['Left Down'] = Vert_LD
            Cube.Vertices['Left Up'] = Vert_LU
            Cube.Update_State()


    def F (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            z_axis = vp.vector(0, 0, 1)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Front'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Left'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, z_axis,i)    

            Edge_L = Cube.Edges['Front Left Down']
            Edge_F = Cube.Edges['Front Left Up']
            Edge_FLD = Cube.Edges['Front']
            Edge_FLU = Cube.Edges['Left']
            Vert_LD = Cube.Vertices['Front Down']
            Vert_LU = Cube.Vertices['Left Down']
            Vert_FU = Cube.Vertices['Left Up']
            Vert_FD = Cube.Vertices['Front Up']

            Cube.Edges['Front'] = Edge_F
            Cube.Edges['Left'] = Edge_L
            Cube.Edges['Front Left Up'] = Edge_FLU
            Cube.Edges['Front Left Down'] = Edge_FLD
            Cube.Vertices['Front Up'] = Vert_FU
            Cube.Vertices['Front Down'] = Vert_FD
            Cube.Vertices['Left Down'] = Vert_LD
            Cube.Vertices['Left Up'] = Vert_LU    
            Cube.Update_State()


    def F_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            z_axis = vp.vector(0, 0, 1)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Front'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Left'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Front Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Left Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Left Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Front Up'].rotate_piece(rot_angle_anim, z_axis,i)    

            Edge_F = Cube.Edges['Front Left Down']
            Edge_L = Cube.Edges['Front Left Up']
            Edge_FLU = Cube.Edges['Front']
            Edge_FLD = Cube.Edges['Left']
            Vert_FU = Cube.Vertices['Front Down']
            Vert_FD = Cube.Vertices['Left Down']
            Vert_LD = Cube.Vertices['Left Up']
            Vert_LU = Cube.Vertices['Front Up']

            Cube.Edges['Front'] = Edge_F
            Cube.Edges['Left'] = Edge_L
            Cube.Edges['Front Left Up'] = Edge_FLU
            Cube.Edges['Front Left Down'] = Edge_FLD
            Cube.Vertices['Front Up'] = Vert_FU
            Cube.Vertices['Front Down'] = Vert_FD
            Cube.Vertices['Left Down'] = Vert_LD
            Cube.Vertices['Left Up'] = Vert_LU
            Cube.Update_State()


    def B (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            z_axis = vp.vector(0, 0, 1)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Back'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Right'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, z_axis,i)    

            Edge_R = Cube.Edges['Back Right Down']
            Edge_B = Cube.Edges['Back Right Up']
            Edge_BRD = Cube.Edges['Back']
            Edge_BRU = Cube.Edges['Right']
            Vert_RD = Cube.Vertices['Back Down']
            Vert_RU = Cube.Vertices['Right Down']
            Vert_BU = Cube.Vertices['Right Up']
            Vert_BD = Cube.Vertices['Back Up']

            Cube.Edges['Back'] = Edge_B
            Cube.Edges['Right'] = Edge_R
            Cube.Edges['Back Right Up'] = Edge_BRU
            Cube.Edges['Back Right Down'] = Edge_BRD
            Cube.Vertices['Back Up'] = Vert_BU
            Cube.Vertices['Back Down'] = Vert_BD
            Cube.Vertices['Right Down'] = Vert_RD
            Cube.Vertices['Right Up'] = Vert_RU   
            Cube.Update_State()


    def B_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            z_axis = vp.vector(0, 0, 1)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Back'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Edges['Right'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Back Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Right Down'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Right Up'].rotate_piece(rot_angle_anim, z_axis,i)    
                Cube.Vertices['Back Up'].rotate_piece(rot_angle_anim, z_axis,i)    

            Edge_B = Cube.Edges['Back Right Down']
            Edge_R = Cube.Edges['Back Right Up']
            Edge_BRU = Cube.Edges['Back']
            Edge_BRD = Cube.Edges['Right']
            Vert_BU = Cube.Vertices['Back Down']
            Vert_BD = Cube.Vertices['Right Down']
            Vert_RD = Cube.Vertices['Right Up']
            Vert_RU = Cube.Vertices['Back Up']

            Cube.Edges['Back'] = Edge_B
            Cube.Edges['Right'] = Edge_R
            Cube.Edges['Back Right Up'] = Edge_BRU
            Cube.Edges['Back Right Down'] = Edge_BRD
            Cube.Vertices['Back Up'] = Vert_BU
            Cube.Vertices['Back Down'] = Vert_BD
            Cube.Vertices['Right Down'] = Vert_RD
            Cube.Vertices['Right Up'] = Vert_RU  
            Cube.Update_State()


    def M (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            horz_axis = vp.vector(1, 0, 0)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Up'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Centers['Down'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)   

            Center_FL = Cube.Centers['Up']
            Center_D = Cube.Centers['Front Left']
            Center_U = Cube.Centers['Back Right']
            Center_BR = Cube.Centers['Down']
            Edge_FLD = Cube.Edges['Front Left Up']
            Edge_BRD = Cube.Edges['Front Left Down']
            Edge_BRU = Cube.Edges['Back Right Down']
            Edge_FLU = Cube.Edges['Back Right Up'] 

            Cube.Centers['Up'] = Center_U
            Cube.Centers['Front Left'] = Center_FL
            Cube.Centers['Back Right'] = Center_BR
            Cube.Centers['Down'] = Center_D
            Cube.Edges['Front Left Up'] = Edge_FLU
            Cube.Edges['Front Left Down'] = Edge_FLD
            Cube.Edges['Back Right Down'] = Edge_BRD
            Cube.Edges['Back Right Up'] = Edge_BRU
            Cube.Update_State()



    def M_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            horz_axis = vp.vector(1, 0, 0)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Up'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Centers['Down'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Front Left Up'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Front Left Down'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Back Right Down'].rotate_piece(rot_angle_anim, horz_axis,i)
                Cube.Edges['Back Right Up'].rotate_piece(rot_angle_anim, horz_axis,i)   

            Center_BR = Cube.Centers['Up']
            Center_U = Cube.Centers['Front Left']
            Center_D = Cube.Centers['Back Right']
            Center_FL = Cube.Centers['Down']
            Edge_BRU = Cube.Edges['Front Left Up']
            Edge_FLU = Cube.Edges['Front Left Down']
            Edge_FLD = Cube.Edges['Back Right Down']
            Edge_BRD = Cube.Edges['Back Right Up'] 

            Cube.Centers['Up'] = Center_U
            Cube.Centers['Front Left'] = Center_FL
            Cube.Centers['Back Right'] = Center_BR
            Cube.Centers['Down'] = Center_D
            Cube.Edges['Front Left Up'] = Edge_FLU
            Cube.Edges['Front Left Down'] = Edge_FLD
            Cube.Edges['Back Right Down'] = Edge_BRD
            Cube.Edges['Back Right Up'] = Edge_BRU
            Cube.Update_State()



    def E (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            vert_axis = vp.vector(0, 1, 0)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Left'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Right'].rotate_piece(rot_angle_anim, vert_axis,i)   

            Center_BR = Cube.Centers['Front Right']
            Center_FR = Cube.Centers['Front Left']
            Center_BL = Cube.Centers['Back Right']
            Center_FL = Cube.Centers['Back Left']
            Edge_R = Cube.Edges['Front']
            Edge_F = Cube.Edges['Left']
            Edge_L = Cube.Edges['Back']
            Edge_B = Cube.Edges['Right'] 

            Cube.Centers['Front Right'] = Center_FR
            Cube.Centers['Front Left'] = Center_FL
            Cube.Centers['Back Right'] = Center_BR
            Cube.Centers['Back Left'] = Center_BL
            Cube.Edges['Front'] = Edge_F
            Cube.Edges['Left'] = Edge_L
            Cube.Edges['Back'] = Edge_B
            Cube.Edges['Right'] = Edge_R
            Cube.Update_State()



    def E_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            vert_axis = vp.vector(0, 1, 0)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Centers['Front Left'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Centers['Back Right'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Front'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Left'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Back'].rotate_piece(rot_angle_anim, vert_axis,i)
                Cube.Edges['Right'].rotate_piece(rot_angle_anim, vert_axis,i)   

            Center_FL = Cube.Centers['Front Right']
            Center_BL = Cube.Centers['Front Left']
            Center_FR = Cube.Centers['Back Right']
            Center_BR = Cube.Centers['Back Left']
            Edge_L = Cube.Edges['Front']
            Edge_B = Cube.Edges['Left']
            Edge_R = Cube.Edges['Back']
            Edge_F = Cube.Edges['Right'] 

            Cube.Centers['Front Right'] = Center_FR
            Cube.Centers['Front Left'] = Center_FL
            Cube.Centers['Back Right'] = Center_BR
            Cube.Centers['Back Left'] = Center_BL
            Cube.Edges['Front'] = Edge_F
            Cube.Edges['Left'] = Edge_L
            Cube.Edges['Back'] = Edge_B
            Cube.Edges['Right'] = Edge_R
            Cube.Update_State()



    def S (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            z_axis = vp.vector(0, 0, 1)
            rot_angle = (-1)*vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Centers['Up'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Centers['Down'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, z_axis,i)   

            Center_D = Cube.Centers['Front Right'] 
            Center_FR = Cube.Centers['Up']
            Center_BL = Cube.Centers['Down']
            Center_U = Cube.Centers['Back Left']
            Edge_FRD = Cube.Edges['Front Right Up']
            Edge_FRU = Cube.Edges['Back Left Up']
            Edge_BLU = Cube.Edges['Back Left Down']
            Edge_BLD = Cube.Edges['Front Right Down'] 

            Cube.Centers['Front Right'] = Center_FR
            Cube.Centers['Up'] = Center_U
            Cube.Centers['Down'] = Center_D
            Cube.Centers['Back Left'] = Center_BL
            Cube.Edges['Front Right Up'] = Edge_FRU
            Cube.Edges['Back Left Up'] = Edge_BLU
            Cube.Edges['Back Left Down'] = Edge_BLD
            Cube.Edges['Front Right Down'] = Edge_FRD    
            Cube.Update_State()



    def S_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            fps , speed = 100 , 4
            z_axis = vp.vector(0, 0, 1)
            rot_angle = vp.pi / 2
            rot_angle_anim = rot_angle/fps

            for i in range(fps):
                vp.rate(speed*fps)
                Cube.Centers['Front Right'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Centers['Up'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Centers['Down'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Centers['Back Left'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Front Right Up'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Back Left Up'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Back Left Down'].rotate_piece(rot_angle_anim, z_axis,i)
                Cube.Edges['Front Right Down'].rotate_piece(rot_angle_anim, z_axis,i)   

            Center_U = Cube.Centers['Front Right'] 
            Center_BL = Cube.Centers['Up']
            Center_FR = Cube.Centers['Down']
            Center_D = Cube.Centers['Back Left']
            Edge_BLU = Cube.Edges['Front Right Up']
            Edge_BLD = Cube.Edges['Back Left Up']
            Edge_FRD = Cube.Edges['Back Left Down']
            Edge_FRU = Cube.Edges['Front Right Down'] 

            Cube.Centers['Front Right'] = Center_FR
            Cube.Centers['Up'] = Center_U
            Cube.Centers['Down'] = Center_D
            Cube.Centers['Back Left'] = Center_BL
            Cube.Edges['Front Right Up'] = Edge_FRU
            Cube.Edges['Back Left Up'] = Edge_BLU
            Cube.Edges['Back Left Down'] = Edge_BLD
            Cube.Edges['Front Right Down'] = Edge_FRD  
            Cube.Update_State()



    def x (Cube,num_rotations=1):
        for counter in range(num_rotations):
            L_(Cube,num_rotations=1)
            M_(Cube,num_rotations=1)
            R(Cube,num_rotations=1)
            Cube.Update_State()


    def x_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            L(Cube,num_rotations=1)
            M(Cube,num_rotations=1)
            R_(Cube,num_rotations=1)
            Cube.Update_State()


    def y (Cube,num_rotations=1):
        for counter in range(num_rotations):
            U(Cube,num_rotations=1)
            E_(Cube,num_rotations=1)
            D_(Cube,num_rotations=1)
            Cube.Update_State()


    def y_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            U_(Cube,num_rotations=1)
            E(Cube,num_rotations=1)
            D(Cube,num_rotations=1)
            Cube.Update_State()


    def z (Cube,num_rotations=1):
        for counter in range(num_rotations):
            F(Cube,num_rotations=1)
            S(Cube,num_rotations=1)
            B_(Cube,num_rotations=1)
            Cube.Update_State()


    def z_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            F_(Cube,num_rotations=1)
            S_(Cube,num_rotations=1)
            B(Cube,num_rotations=1)
            Cube.Update_State()


    def u (Cube,num_rotations=1):
        for counter in range(num_rotations):
            U(Cube,num_rotations=1)
            E_(Cube,num_rotations=1)
            Cube.Update_State()


    def u_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            U_(Cube,num_rotations=1)
            E(Cube,num_rotations=1)
            Cube.Update_State()


    def d (Cube,num_rotations=1):
        for counter in range(num_rotations):
            D(Cube,num_rotations=1)
            E(Cube,num_rotations=1)
            Cube.Update_State()


    def d_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            D_(Cube,num_rotations=1)
            E_(Cube,num_rotations=1)
            Cube.Update_State()


    def r (Cube,num_rotations=1):
        for counter in range(num_rotations):
            R(Cube,num_rotations=1)
            M_(Cube,num_rotations=1)
            Cube.Update_State()


    def r_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            R_(Cube,num_rotations=1)
            M(Cube,num_rotations=1)
            Cube.Update_State()


    def l (Cube,num_rotations=1):
        for counter in range(num_rotations):
            L(Cube,num_rotations=1)
            M(Cube,num_rotations=1)
            Cube.Update_State()


    def l_(Cube,num_rotations=1):
        for counter in range(num_rotations):
            L_(Cube,num_rotations=1)
            M_(Cube,num_rotations=1)
            Cube.Update_State()


    def f (Cube,num_rotations=1):
        for counter in range(num_rotations):
            F(Cube,num_rotations=1)
            S(Cube,num_rotations=1)
            Cube.Update_State()


    def f_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            F_(Cube,num_rotations=1)
            S_(Cube,num_rotations=1)
            Cube.Update_State()


    def b (Cube,num_rotations=1):
        for counter in range(num_rotations):
            B(Cube,num_rotations=1)
            S_(Cube,num_rotations=1)
            Cube.Update_State()


    def b_ (Cube,num_rotations=1):
        for counter in range(num_rotations):
            B_(Cube,num_rotations=1)
            S(Cube,num_rotations=1)
            Cube.Update_State()
            
    def rotate_cube(self, axis, reverse=False):
        angle = self.rotation_angle if not reverse else -self.rotation_angle
        for key, piece in self.Centers.items():
            piece.rotate_piece(angle, axis, 0)
        for key, piece in self.Edges.items():
            piece.rotate_piece(angle, axis, 0)
        for key, piece in self.Vertices.items():
            piece.rotate_piece(angle, axis, 0)
        self.Update_State()    


    def update_camera(self):
        self.scene.camera.pos = vp.vector(5, 5, 5)
        self.scene.camera.axis = vp.vector(-5,-5,-5)
        self.scene.camera.up = vp.vector(0, 1, 0)

    def Update_State(self):
    # Dynamically determine the current state of the cube
        Unwrapped = {
            'Up': {
                'Center': self.Centers['Up'].sides['Up'].color,
                'Edges': {
                    'Front Right Up': self.Edges['Front Right Up'].sides['Up'].color,
                    'Front Left Up': self.Edges['Front Left Up'].sides['Up'].color,
                    'Back Right Up': self.Edges['Back Right Up'].sides['Up'].color,
                    'Back Left Up': self.Edges['Back Left Up'].sides['Up'].color
                },
                'Vertices': {
                    'Front Up': self.Vertices['Front Up'].sides['Up'].color,
                    'Right Up': self.Vertices['Right Up'].sides['Up'].color,
                    'Left Up': self.Vertices['Left Up'].sides['Up'].color,
                    'Back Up': self.Vertices['Back Up'].sides['Up'].color
                }
            },
            'Down': {
                'Center': self.Centers['Down'].sides['Down'].color,
                'Edges': {
                    'Front Right Down': self.Edges['Front Right Down'].sides['Down'].color,
                    'Front Left Down': self.Edges['Front Left Down'].sides['Down'].color,
                    'Back Right Down': self.Edges['Back Right Down'].sides['Down'].color,
                    'Back Left Down': self.Edges['Back Left Down'].sides['Down'].color
                },
                'Vertices': {
                    'Front Down': self.Vertices['Front Down'].sides['Down'].color,
                    'Right Down': self.Vertices['Right Down'].sides['Down'].color,
                    'Left Down': self.Vertices['Left Down'].sides['Down'].color,
                    'Back Down': self.Vertices['Back Down'].sides['Down'].color
                }
            },
            'Front Right': {
                'Center': self.Centers['Front Right'].sides['Right'].color,
                'Edges': {
                    'Front Right Up': self.Edges['Front Right Up'].sides['Right'].color,
                    'Front Right Down': self.Edges['Front Right Down'].sides['Right'].color,
                    'Front': self.Edges['Front'].sides['Right'].color,
                    'Right': self.Edges['Right'].sides['Right'].color
                },
                'Vertices': {
                    'Front Up': self.Vertices['Front Up'].sides['Right'].color,
                    'Right Up': self.Vertices['Right Up'].sides['Right'].color,
                    'Front Down': self.Vertices['Front Down'].sides['Right'].color,
                    'Right Down': self.Vertices['Right Down'].sides['Right'].color
                }
            },
            'Back Left': {
                'Center': self.Centers['Back Left'].sides['Left'].color,
                'Edges': {
                    'Back Left Up': self.Edges['Back Left Up'].sides['Left'].color,
                    'Back Left Down': self.Edges['Back Left Down'].sides['Left'].color,
                    'Back': self.Edges['Back'].sides['Left'].color,
                    'Left': self.Edges['Left'].sides['Left'].color
                },
                'Vertices': {
                    'Back Up': self.Vertices['Back Up'].sides['Left'].color,
                    'Left Up': self.Vertices['Left Up'].sides['Left'].color,
                    'Back Down': self.Vertices['Back Down'].sides['Left'].color,
                    'Left Down': self.Vertices['Left Down'].sides['Left'].color
                }
            },
            'Front Left': {
                'Center': self.Centers['Front Left'].sides['Front'].color,
                'Edges': {
                    'Front Left Up': self.Edges['Front Left Up'].sides['Front'].color,
                    'Front Left Down': self.Edges['Front Left Down'].sides['Front'].color,
                    'Front': self.Edges['Front'].sides['Front'].color,
                    'Left': self.Edges['Left'].sides['Front'].color
                },
                'Vertices': {
                    'Front Up': self.Vertices['Front Up'].sides['Front'].color,
                    'Left Up': self.Vertices['Left Up'].sides['Front'].color,
                    'Front Down': self.Vertices['Front Down'].sides['Front'].color,
                    'Left Down': self.Vertices['Left Down'].sides['Front'].color
                }
            },
            'Back Right': {
                'Center': self.Centers['Back Right'].sides['Back'].color,
                'Edges': {
                    'Back Right Up': self.Edges['Back Right Up'].sides['Back'].color,
                    'Back Right Down': self.Edges['Back Right Down'].sides['Back'].color,
                    'Back': self.Edges['Back'].sides['Back'].color,
                    'Right': self.Edges['Right'].sides['Back'].color
                },
                'Vertices': {
                    'Back Up': self.Vertices['Back Up'].sides['Back'].color,
                    'Right Up': self.Vertices['Right Up'].sides['Back'].color,
                    'Back Down': self.Vertices['Back Down'].sides['Back'].color,
                    'Right Down': self.Vertices['Right Down'].sides['Back'].color
                }
            }
        }
        self.State = Unwrapped
        return Unwrapped

if __name__ == '__main__':
    cube = Color_Cube()
    while True:
        vp.rate(30)
