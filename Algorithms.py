from time import sleep
import random

def Scramble(Cube):

    commands = [r,r_,l,l_,f,f_,b,b_,u,u_,d,d_,M,M_,E,E_,S,S_,U,U_,D,D_,R,R_,L,L_,F,F_,B,B_]

    for i in range(10):
        move = random.choice(commands)
        move(Cube)
        sleep(0.3)
        

    return Cube


def Track_Yellow_Edges (Cube):
    Edge_Tracker = []
    for side in Cube.Sides:
        for edge in Cube.State[side]['Edges']:
            if Cube.State[side]['Edges'][edge] == Cube.Colours['Yellow']:
                Edge_Tracker.append([side,edge,0,0])
    for side in Cube.Sides:
        for edge in Cube.State[side]['Edges']:
            for piece in Edge_Tracker:
                if edge == piece[1] and side != piece[0]:
                    piece[2] = side
                    piece[3] = Cube.State[side]['Edges'][edge]

    Yellow_Edges ={
        'Red' : [],
        'Blue' : [],
        'Green' : [],
        'Orange' : []
    }
    for piece in Edge_Tracker:
        if piece[3] == Cube.Colours['Red']:
            Yellow_Edges['Red'] = piece[:3]
        elif piece[3] == Cube.Colours['Blue']:
            Yellow_Edges['Blue'] = piece[:3]
        elif piece[3] == Cube.Colours['Green']:
            Yellow_Edges['Green'] = piece[:3]
        else:
            Yellow_Edges['Orange'] = piece[:3]

    return Yellow_Edges


def Wrong_Orientation(Cube,Position,Other_Face):
    if Other_Face == 'Up':
        if Position == 'Front Right Up':
            for move in [R_,F,R]:
                move(Cube)
        elif Position == 'Front Left Up':
            for move in [U_,R_,F,R]:
                move(Cube)
        elif Position == 'Back Right Up':
            for move in [U,R_,F,R]:
                move(Cube)
        elif Position == 'Back Left Up':
            for move in [U,U,R_,F,R]:
                move(Cube)
    elif Other_Face == 'Down':
        if Position == 'Front Right Down':
            for move in [R,F,R]: #Change this [R,R,R_,F,R]
                move(Cube)
        elif Position == 'Front Left Down':
            for move in [F,F,U_,R_,F,R]:
                move(Cube)
        elif Position == 'Back Right Down':
            for move in [B,B,U,R_,F,R]:
                move(Cube)
        elif Position == 'Back Left Down':
            for move in [L,L,U,U,R_,F,R]:
                move(Cube)

import vpython as vp

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


def Align_Upper_Edges(Cube,Position):
    if Position == 'Front Right Up':
        U(Cube)
        F(Cube,2)
    elif Position == 'Front Left Up':
        F(Cube,2)
    elif Position == 'Back Right Up':
        U(Cube,2)
        F(Cube,2)
    elif Position == 'Back Left Up':
        U_(Cube)
        F(Cube,2)
def Align_Lower_Edges(Cube,Position):
    if Position == 'Front Right Down':
        for move in [R,R,U,F,F]:
            move(Cube)
    elif Position == 'Front Left Down':
        pass
    elif Position == 'Back Right Down':
        for move in [B,B,U,U,F,F]:
            move(Cube)
    elif Position == 'Back Left Down':
        for move in [L,L,U_,F,F]:
            move(Cube)
def Align_Middle_Edges(Cube,Position,Face):
    if Position == 'Front':
        if Face == 'Front Right':
            F(Cube)
        else:
            for move in [R,U,R_,F,F]:
                move(Cube)
    elif Position == 'Back':
        if Face == 'Back Right':
            for move in [L,U_,L_,F,F]:
                move(Cube)
        else:
            for move in [B_,U,U,B,F,F]:
                move(Cube)
    elif Position == 'Right':
        if Face == 'Front Right':
            for move in [B,U_,U_,B_,F,F]:
                move(Cube)
        else:
            for move in [R_,U,R,F,F]:
                move(Cube)
    elif Position == 'Left':
        if Face == 'Front Left':
            for move in [L_,U_,L,F,F]:
                move(Cube)
        else:
            F_(Cube)

def Align_Centers (Cube):
    if Cube.State['Down']['Center'] != Cube.Colours['Yellow']:
        for side in Cube.Sides:
            if Cube.State[side]['Center'] == Cube.Colours['Yellow']:
                current_side = side
        # print("Current side is",current_side)
        if current_side == 'Up':
            x(Cube,2)
        elif current_side == 'Front Left':
            x_(Cube)
        elif current_side == 'Back Right':
            x(Cube)
        elif current_side == 'Front Right':
            z(Cube)
        else:
            z_(Cube)
    if Cube.State['Front Right']['Center'] != Cube.Colours['Blue']:
        for side in Cube.Sides[2:]:
            # print(side)
            if Cube.State[side]['Center'] == Cube.Colours['Blue']:
                current_side = side
        # print("Current side is",current_side)
        if current_side == 'Front Left':
            y_(Cube)
        elif current_side == 'Back Right':
            y(Cube)
        elif current_side == 'Back Left':
            y(Cube,2)

def Middle_Layer_Right (Cube):
    for move in [U,R,U_,R_,U_,F_,U,F]:
        move(Cube)

def Middle_Layer_Left (Cube):
    for move in [U_,L_,U,L,U,F,U_,F_]:
        move(Cube)

def L_to_Cross (Cube):
    for move in [F,U,R,U_,R_,F_]:
        move(Cube)

def I_to_Cross (Cube):
    for move in [R,B,U,B_,U_,R_]:
        move(Cube)

def Align_Top_Edges (Cube):
    for move in [R,U,R_,U,R,U,U,R_,U]:
        move(Cube)

def Align_Top_Corners (Cube):
    for move in [U,R,U_,L_,U,R_,U_,L]:
        move(Cube)

def Orient_Correctly (Cube):
    for move in [R_,D_,R,D,R_,D_,R,D]:
        move(Cube)                



def Yellow_Cross(Cube):
    for color in ['Red','Blue','Orange','Green']:
        if color == 'Red':
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            # Align_Centers(Cube)
        elif color == 'Blue':
            y(Cube)
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            # Align_Centers(Cube)
        elif color == 'Orange':
            y(Cube)
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            # Align_Centers(Cube)
        else:
            y(Cube)
            Yellow_Edges = Track_Yellow_Edges(Cube)
            Position, Face , Other_Face = Yellow_Edges[color][1] , Yellow_Edges[color][0] , Yellow_Edges[color][2]
            if Other_Face == 'Up' or 'Down':
                Wrong_Orientation(Cube,Position,Other_Face)
            if Face == 'Down':
                Align_Lower_Edges(Cube,Position)
            elif Face == 'Up' :
                Align_Upper_Edges(Cube,Position)
            else:
                Align_Middle_Edges(Cube,Position,Face)
            Align_Centers(Cube)

def Track_Yellow_Corners (Cube):
    Corner_Tracker = []
    for side in Cube.Sides:
        for corner in Cube.State[side]['Vertices']:
            if Cube.State[side]['Vertices'][corner] == Cube.Colours['Yellow']:
                Corner_Tracker.append([side,corner,[],[]])
    for side in Cube.Sides:
        for corner in Cube.State[side]['Vertices']:
            for piece in Corner_Tracker:
                if corner == piece[1] and side != piece[0]:
                    piece[2].append(side)
                    piece[3].append(Cube.State[side]['Vertices'][corner])

    Yellow_Corners ={
        'Red Blue' : [],
        'Blue Orange' : [],
        'Green Red' : [],
        'Orange Green' : []
    }
    for piece in Corner_Tracker:
        if Cube.Colours['Red'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Yellow_Corners['Red Blue'] = piece[:3]
        elif Cube.Colours['Orange'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Yellow_Corners['Blue Orange'] = piece[:3]
        elif Cube.Colours['Green'] in piece[3] and Cube.Colours['Red'] in piece[3]:
            Yellow_Corners['Green Red'] = piece[:3]
        else:
            Yellow_Corners['Orange Green'] = piece[:3]

    return Yellow_Corners

def Change_Corner_Orientation(Cube):
    R(Cube)
    U(Cube)
    R_(Cube)
    U_(Cube)

def Align_Downer (Cube,Position,Face):
    if Position == 'Front Down' :
        if Face == 'Down':
            pass
        elif Face == 'Front Right':
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
        else:
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
            Change_Corner_Orientation(Cube)
    elif Position == 'Right Down':
        if Face == 'Down':
           for move in [B,U,U,B_,R,U_,R_]:
               move(Cube)
        elif Face == 'Front Right':
           for move in [R_,U,U,R,R,U_,R_]:
                move(Cube)             
        else:
            for move in [B,U,B_,U_,F_,U,F]:
                move(Cube)
    elif Position == 'Left Down':
        if Face == 'Down':
            for move in [L_,U,U,L,F_,U,F]:
                move(Cube)
        elif Face == 'Front Left':
            for move in [F,U,U,F_,F_,U,F]:
                move(Cube)         
        else:
            for move in [L_,R,U_,R_,L]:
                move(Cube)
    else:
        if Face == 'Down':
            for move in [L,R,U,U,R_,L_]:
                move(Cube)
        elif Face == 'Back Right':
            for move in [B_,U_,B,R,U_,R_]:
                move(Cube)
        else:
           for move in [L,U,L_,F_,U,F]:
               move(Cube)

def Align_Upper_Corners(Cube,Position,Face):
    if Position == 'Front Up' :
        if Face == 'Up':
            for move in [R,U,U,R_,U_]:
                move(Cube)
            Change_Corner_Orientation(Cube)
        elif Position == 'Front Right':
            Change_Corner_Orientation(Cube)
        else:
            for move in [U,R,U_,R_]:
                move(Cube)
    elif Position == 'Right Up':
        if Face == 'Up':
            for move in [U,R,U,U,R_,U_]:
                move(Cube)
            Change_Corner_Orientation(Cube)
        elif Face == 'Front Right':
           for move in [U,U,R,U_,R_]:
                move(Cube)             
        else:
            for move in [F_,U,F]:
                move(Cube)
    elif Position == 'Left Up':
        if Face == 'Up':
            for move in [U_,R,U,U,R_,U_,Change_Corner_Orientation]:  #### Maybe wrong
                move(Cube)
        elif Face == 'Front Left':
            for move in [U,U,F_,U,F]:
                move(Cube)         
        else:
            for move in [R,U_,R_]:
                move(Cube)
    else:
        if Face == 'Up':
            for move in [U_,U_,R,U,U,R_,U_]:
                move(Cube)
            Change_Corner_Orientation(Cube)
        elif Face == 'Back Right':
            for move in [R,U,U,R_]:
                move(Cube)
        else:
           for move in [F_,U,U,F]:
               move(Cube)
    

def Yellow_Corners (Cube):
    for colors in ['Red Blue','Blue Orange','Orange Green','Green Red']:
        if colors == 'Red Blue':
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
        elif colors == 'Blue Orange':
            y(Cube)
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
            # Align_Centers(Cube)
        elif colors == 'Orange Green':
            y(Cube)
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
            # Align_Centers(Cube)            
        else:
            y(Cube)
            Yellow_Corners = Track_Yellow_Corners(Cube)
            Position , Face = Yellow_Corners[colors][1] , Yellow_Corners[colors][0]
            if Position[-4:] == 'Down':
                Align_Downer(Cube,Position,Face)
            elif Position[-2:] == 'Up':
                Align_Upper_Corners(Cube,Position,Face)
            Align_Centers(Cube)


def Solve_First_Layer (Cube):
    Yellow_Cross(Cube)
    sleep(1)
    Yellow_Corners(Cube)
    sleep(1)


def Track_Middle_Edges (Cube):
    Edge_Tracker = []
    for Col in ['Orange','Green','Blue','Red']:
        for side in Cube.Sides:
            for edge in Cube.State[side]['Edges']:
                if Cube.State[side]['Edges'][edge] == Cube.Colours[Col]:
                    Edge_Tracker.append([side,edge,0,[Cube.Colours[Col]]])
        for side in Cube.Sides:
            for edge in Cube.State[side]['Edges']:
                for piece in Edge_Tracker:
                    if edge == piece[1] and side != piece[0]:
                        if Cube.State[side]['Edges'][edge] not in [Cube.Colours['White'],Cube.Colours['Yellow']]:
                            piece[2] = side
                            piece[3].append(Cube.State[side]['Edges'][edge])


    Middle_Edges ={
        'Red Blue' : [],
        'Blue Orange' : [],
        'Green Red' : [],
        'Orange Green' : []
    }
    for piece in Edge_Tracker:
        if Cube.Colours['Red'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Middle_Edges['Red Blue'] = piece[:3]
        elif Cube.Colours['Orange'] in piece[3] and Cube.Colours['Blue'] in piece[3]:
            Middle_Edges['Blue Orange'] = piece[:3]
        elif Cube.Colours['Green'] in piece[3] and Cube.Colours['Red'] in piece[3]:
            Middle_Edges['Green Red'] = piece[:3]
        elif Cube.Colours['Green'] in piece[3] and Cube.Colours['Orange'] in piece[3]:
            Middle_Edges['Orange Green'] = piece[:3]

    return Middle_Edges

def Insert_Middle_Edge (Cube,Position,Face):
    if Face == 'Up':
        if Position == 'Front Right Up':
            for move in [y,Middle_Layer_Left,y_]:
                move(Cube)
        elif Position == 'Front Left Up':
            for move in [d_,Middle_Layer_Left,y_]:
                move(Cube)
        elif Position == 'Back Right Up':
            for move in [U,y,Middle_Layer_Left,y_]:
                move(Cube)
        else:
            for move in [U_,d_,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face != 'Up' and Position[-2:] == 'Up':
        if Position == 'Front Right Up':
            for move in [U,Middle_Layer_Right]:
                move(Cube)
        elif Position == 'Front Left Up':
            for move in [Middle_Layer_Right]:
                move(Cube)
        elif Position == 'Back Right Up':
            for move in [U,U,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [U_,Middle_Layer_Right]:
                move(Cube)
    elif Face == 'Front Right':
        if Position == 'Front':
            for move in [Middle_Layer_Right,U,U,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [y,Middle_Layer_Right,U_,U_,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face == 'Back Left':
        if Position == 'Left':
            for move in [Middle_Layer_Left,U,U,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [y_,Middle_Layer_Left,y,y,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face == 'Back Right':
        if Position == 'Right':
            for move in [y,Middle_Layer_Right,y_,U_,Middle_Layer_Right]:
                move(Cube)
        else:
            for move in [y,y,Middle_Layer_Right,y_,U_,Middle_Layer_Left,y_]:
                move(Cube)
    elif Face == 'Front Left':
        if Position == 'Left':
            for move in [Middle_Layer_Left,y,U,Middle_Layer_Left,y_]:
                move(Cube)
        else:
            pass
        
def Solve_Second_Layer (Cube):
    for colors in ['Red Blue','Blue Orange','Orange Green','Green Red']:
        if colors == 'Red Blue':
            Middle_Edges = Track_Middle_Edges(Cube)
            Position , Face = Middle_Edges[colors][1] , Middle_Edges[colors][0]
            sleep(0.3)
            Insert_Middle_Edge(Cube,Position,Face)
            sleep(0.3)
            Align_Centers(Cube)
            sleep(0.5)
        elif colors == 'Blue Orange':
            y(Cube)
            Middle_Edges = Track_Middle_Edges(Cube)
            Position, Face = Middle_Edges[colors][1] , Middle_Edges[colors][0]
            sleep(0.3)
            Insert_Middle_Edge(Cube,Position,Face)
            sleep(0.5)
            # Align_Centers(Cube)
        elif colors == 'Orange Green':
            y(Cube)
            Middle_Edges = Track_Middle_Edges(Cube)
            Position, Face = Middle_Edges[colors][1] , Middle_Edges[colors][2]
            sleep(0.3)
            Insert_Middle_Edge(Cube,Position,Face)
            sleep(0.5)
            # Align_Centers(Cube)            
        else:
            y(Cube)
            Middle_Edges = Track_Middle_Edges(Cube)
            Position, Face = Middle_Edges[colors][1] , Middle_Edges[colors][2]
            sleep(0.3)
            Insert_Middle_Edge(Cube,Position,Face)
            sleep(0.5)
            Align_Centers(Cube)
            sleep(0.4)

def White_Cross (Cube):
    if Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        pass
    elif Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        L_to_Cross(Cube)
    elif Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White']:
        for move in [U,L_to_Cross]:
            move(Cube)
    elif Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        for move in [U_,L_to_Cross]:
            move(Cube)
    elif Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White']:
        for move in [U,U,L_to_Cross]:
            move(Cube)

    elif Cube.State['Up']['Edges']['Front Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Back Right Up'] == Cube.Colours['White']:
        I_to_Cross(Cube)
    elif Cube.State['Up']['Edges']['Back Left Up'] == Cube.Colours['White'] and Cube.State['Up']['Edges']['Front Right Up'] == Cube.Colours['White']:
        for move in [U,I_to_Cross]:
            move(Cube)

    else:
        L_to_Cross(Cube)
        White_Cross(Cube)

def Track_Top_Edges (Cube):
    cnt = 0
    while cnt < 2:
        U(Cube)
        Correct_Edges, cnt = [] , 0
        for face in ['Front Left','Front Right','Back Left','Back Right']:
            if Cube.State[face]['Edges'][face+' Up'] == Cube.State[face]['Center']:
                Correct_Edges.append(face)
                cnt += 1
    
    # print(Correct_Edges)
    
    if len(Correct_Edges) == 2:
        if any(set(Correct_Edges) == set(pair) for pair in [['Front Left','Front Right'],['Front Left','Back Left'],['Front Right','Back Right'],['Back Left','Back Right']]):
            Correct_Edges.append('L')
        else:
            Correct_Edges.append('I')
    
    # print(Correct_Edges)
    return Correct_Edges

def Top_Edges (Cube):
    Top_Edges_ = Track_Top_Edges(Cube)
    if len(Top_Edges_) == 4:
        pass
    elif len(Top_Edges_) == 3:
        if Top_Edges_[-1] == 'L':
            if 'Front Right' in Top_Edges_ and 'Back Right' in Top_Edges_:
                Align_Top_Edges(Cube)
            elif 'Front Left' in Top_Edges_ and 'Front Right' in Top_Edges_:
                for move in [y_,Align_Top_Edges,y]:
                    move(Cube)
            elif 'Back Left' in Top_Edges_ and 'Back Right' in Top_Edges_:
                for move in [y,Align_Top_Edges,y_]:
                    move(Cube)
            else:
                for move in [y,y,Align_Top_Edges,y_,y_]:
                    move(Cube)
        elif Top_Edges_[-1] == 'I':
            if 'Front Left' in Top_Edges_:
                for move in [Align_Top_Edges,Top_Edges]:
                    move(Cube)
            else:
                for move in [y,Align_Top_Edges,y_,Top_Edges]:
                    move(Cube)

    Align_Centers(Cube)

def Check_Position (Cube,Position):
    if Position == 'Front Up':
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Red'],Cube.Colours['Blue']]
        Actual_Colors = []
        for side in ['Front Right','Front Left','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True
    elif Position == 'Right Up':
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Orange'],Cube.Colours['Blue']]
        Actual_Colors = []
        for side in ['Front Right','Back Right','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True 
    elif Position == 'Left Up':
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Red'],Cube.Colours['Green']]
        Actual_Colors = []
        for side in ['Back Left','Front Left','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True  
    else:
        Expected_Colors = [Cube.Colours['White'],Cube.Colours['Orange'],Cube.Colours['Green']]
        Actual_Colors = []
        for side in ['Back Right','Back Left','Up']:
            Actual_Colors.append(Cube.State[side]['Vertices'][Position])
        for color in Actual_Colors:        
            if color not in Expected_Colors:
                return False
        return True     
        

def Track_Top_Corners (Cube):
    Corner_Tracker = {}
    for corner in Cube.State['Up']['Vertices']:
        Corner_Tracker[corner] = Check_Position(Cube,corner)
    return Corner_Tracker

def Top_Corners (Cube):
    Corners = Track_Top_Corners(Cube)
    Correct_Corners = []
    for corner, correct_position in Corners.items():
        if correct_position == True:
            Correct_Corners.append(corner)
    
    if len(Correct_Corners) == 4:
        return False
    elif len(Correct_Corners) == 1:
        if Correct_Corners[0] == 'Front Up':
            Align_Top_Corners(Cube)
        elif Correct_Corners[0] == 'Right Up':
            for move in [y,Align_Top_Corners,y_]:
                move(Cube)
        elif Correct_Corners[0] == 'Left Up':
            for move in [y_,Align_Top_Corners,y]:
                move(Cube)
        else:
            for move in [y,y,Align_Top_Corners,y_,y_]:
                move(Cube)
    else:
        Align_Top_Corners(Cube)
        Top_Corners(Cube)

    return True

def Orient_Corners_Correctly (Cube):
    for i in range(4):
        while Cube.State['Up']['Vertices']['Front Up'] != Cube.Colours['White']:
            Orient_Correctly(Cube)
        U(Cube)


def Solve_Top_Layer (Cube):
    White_Cross(Cube)
    sleep(0.5)
    Top_Edges(Cube)
    sleep(0.5)
    cnt = 0
    while(Top_Corners(Cube) and cnt < 10):
        Top_Corners(Cube)
        sleep(0.3)
        cnt += 1
    if cnt == 10:
        Top_Edges(Cube)
        sleep(0.3)
        while(Top_Corners(Cube) and cnt < 10):
            Top_Corners(Cube)
            sleep(0.3)
    sleep(0.3)        
    Orient_Corners_Correctly(Cube)
    sleep(0.5)



def Houston_We_Have_A_Problem (Cube):
    down_section = Cube.State['Down']
    Down = []

    # Printing the Center value
    Down.append(down_section['Center'])

    # Printing all the Edge values
    # print("Edges:")
    for edge, color in down_section['Edges'].items():
        Down.append(color)

    # Printing all the Vertex values
    # print("Vertices:")
    for vertex, color in down_section['Vertices'].items():
        Down.append(color)

    for color in Down:
        if color != Cube.Colours['Yellow']:
            return True
        else:
            pass
    return False



         