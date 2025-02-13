# Cube_Piece.py
import vpython as vp

class Cube_Piece:
    def __init__(self, center, size, color):
        thickness = 1e-3
        self.center = center
        self.size = size
        self.front = vp.box(pos=center+vp.vector(0,0,size.z/2),size=vp.vector(size.x,size.y,thickness),color=color[0])
        self.back = vp.box(pos=center-vp.vector(0,0,size.z/2),size=vp.vector(size.x,size.y,thickness),color=color[1])
        self.right = vp.box(pos=center+vp.vector(size.x/2,0,0),size=vp.vector(thickness,size.y,size.z),color=color[2])
        self.left = vp.box(pos=center-vp.vector(size.x/2,0,0),size=vp.vector(thickness,size.y,size.z),color=color[3])
        self.up = vp.box(pos=center+vp.vector(0,size.y/2,0),size=vp.vector(size.x,thickness,size.z),color=color[4])
        self.down = vp.box(pos=center-vp.vector(0,size.y/2,0),size=vp.vector(size.x,thickness,size.z),color=color[5])
        self.sides = {
            'Front': self.front,
            'Back': self.back,
            'Right': self.right,
            'Left': self.left,
            'Up': self.up,
            'Down': self.down
        }

    def rotate_piece(self,angle_of_rot,axis_of_rot,counter):
        self.center = self.center.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.front.pos = self.front.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.back.pos = self.back.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.right.pos = self.right.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.left.pos = self.left.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.up.pos = self.up.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.down.pos = self.down.pos.rotate(angle=angle_of_rot, axis=axis_of_rot)
        self.front.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.back.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.right.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.left.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.up.rotate(angle=angle_of_rot,axis=axis_of_rot)
        self.down.rotate(angle=angle_of_rot,axis=axis_of_rot)

        if counter == 0:
            if axis_of_rot == vp.vector(1,0,0):
                tempx = self.up
                if angle_of_rot > 0 :
                    self.up,self.front,self.down,self.back= self.back,tempx,self.front,self.down
                elif angle_of_rot < 0 :
                    self.up,self.front,self.down,self.back= self.front,self.down,self.back,tempx
            elif axis_of_rot == vp.vector(0,1,0):
                tempy = self.right
                if angle_of_rot < 0 :
                    self.right,self.front,self.left,self.back = self.back,tempy,self.front,self.left
                elif angle_of_rot > 0 :
                    self.right,self.front,self.left,self.back = self.front,self.left,self.back,tempy
            elif axis_of_rot == vp.vector(0,0,1):
                tempz = self.right
                if angle_of_rot > 0 :
                    self.right,self.up,self.left,self.down = self.down,tempz,self.up,self.left
                elif angle_of_rot < 0 :
                    self.right,self.up,self.left,self.down = self.up,self.left,self.down,tempz

        self.sides = {
            'Front': self.front,
            'Back': self.back,
            'Right': self.right,
            'Left': self.left,
            'Up': self.up,
            'Down': self.down
        }

    def get_side_color(self, side_name):
        """Returns the color of the specified side."""
        if side_name in self.sides:
            return self.sides[side_name].color
        else:
            return None  # Or raise an exception if side_name is invalid

