#This is a file for solving the Rubik's cube.
#Step One is to solve the white cross

#Cube orientation is always as follows: 
# Face 1 is white center with orange centerfacing upward.
# Face 2 is orange center, 3 is blue center, 4 is red center, 5 is green center, and 6 is yellow center, turning the cube exactly around.

#Opposite sides that don't affect each other on move are:

#importing necessary definitions
import copy
import data

#Defining pairs / making a dictionary for opposite pair
pairs = [(w,y), (o,r), (g,b)]
opposites = {}
for i, j in pairs:
    opposites[i]=j
    opposites[j]=i

#Making an index 
index={}
for face in data.cube:
    index[data.cube[face][0]] = face

#create the reference replica of cube state
shadow_cube = copy.deepcopy(cube_object)

def cube_sort(cube_object,side):
    '''
    we want to make side at index 0 in cube_object
    side's opposite should go to index 5
    then pick another side to go at index 1, and alternate with opposites remaining
    '''
    cube_object[0] = shadow_cube[index[side]]
    cube_object[5]=shadow_cube[index[opposites[side]]]

    match side:
        case w:
            #what happens if we turn white?
            break
        case y:
            #what happens if we turn yellow?
            for n in range(1,5):
                for m in range(1,3):
                    cube_object[n][m]=shadow_cube[n][m+2]
                    cube_object[n][m+2]=shadow_cube[n][m]
            
        case o:
            #what happens if we turn orange?
        case r:
            #what happens if we turn red?
        case g:
            #what happens if we turn green?
        case b:
            #what happens if we turn blue?
            
    if side != w or y:
        cube_object[1]=shadow_cube[index[y]]
        cube_object[3]=shadow_cube[index[w]]
        if side == o or r:
            cube_object[2]=shadow_cube[index[g]]
            cube_object[4]=shadow_cube[index[b]]
        else:
            cube_object[2]=shadow_cube[index[o]]
            cube_object[4]=shadow_cube[index[r]]
    else:
        break


    

def turn_cube(cube_object,side,turn_direction):
    #1. sort_cube_data
    #2. turn_algorithm -- don't forget to adjust the algorithm for turn_direction!
    return





#define turn face 1
def turn_face_1(cube_object):

    #effect on other faces
    for n in range(1,5):
        if n == 1:
            cube_object[1][2]=shadow_cube[4][2]
            cube_object[1][1][2] =shadow_cube[4][1][2]
            cube_object[1][3][0] =shadow_cube[4][3][0]
        else:   
            cube_object[n][2]=shadow_cube[n-1][2]
            cube_object[n][1][2]=shadow_cube[n-1][1][2]
            cube_object[n][3][0]=shadow_cube[n-1][3][0]    
    #turn the face we're turning
    for m in range(0,4):
        cube_object[0][m]=shadow_cube[0][m-1]
    

turn_face_1(cube)
print_cube(cube)



def print_cube(cube_object):
    face_names = ["W", "O", "B", "R", "G", "Y"]
    for i, face in enumerate(cube_object):
        print(f"{face_names[i]}:")
        for row in face:
            print("  " + " ".join(row))
        print()
