#imports
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np
import pkg_resources
import os


class Planet:
    def __init__(self, radius, distance, orbit, orbitspeed, acistilt, acisAni, texturepath):
        self.radius = radius
        self.distance = distance
        self.orbit = orbit
        self.orbitspeed = orbitspeed #declaring planet variables
        self.acistilt = acistilt
        self.acisAni = acisAni
        self.material = Material(texturepath)

    def init_material(self):
        self.material.init_texture() 

    
    # function for drawing planets
    def draw(self, quadric):
        self.material.use()
        glPushMatrix()
        glRotatef(self.orbit, 0.0, 1.0, 0.0) #rotation
        glTranslatef(self.distance, 0.0, 0.0) #location
        glRotatef(self.acistilt, 1.0, 0.0, 0.0) #axis 
        glRotatef(self.acisAni, 0.0, 1.0, 0.0) #axis
        glRotatef(90.0, 1.0, 0.0, 0.0)
        gluSphere(quadric, self.radius, 20, 20) # creates sphere with texture
        glPopMatrix()
    
def orbitaltrails(planets):
        glPushMatrix()
        glColor3ub(255, 255, 255)
        glRotatef(90.0, 1.0, 0.0, 0.0)
        for planet in planets:
            glutWireTorus(0.001, planet.distance, 100, 100)
        glPopMatrix()

        

    
    
        

class Material:
    def __init__(self, filepath):
        self.filepath = filepath #declares filepath and texture as variables
        self.texture = None

    #texture generator function
    def init_texture(self):
        self.texture = glGenTextures(1) # defines textures and how many to generate
        glBindTexture(GL_TEXTURE_2D, self.texture) #texture binding
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # maps texture
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        glGenerateMipmap(GL_TEXTURE_2D)

    def use(self):
        if self.texture is not None:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, self.texture)

    def destroy(self):
        if self.texture is not None:
            glDeleteTextures(1, [self.texture])
            
class skybox:
    def __init__(self, filepath_left,filepath_right,filepath_top,filepath_bottom,filepath_front,filepath_back):
        self.filepath_left = filepath_left
        self.filepath_right = filepath_right
        self.filepath_top = filepath_top
        self.filepath_bottom = filepath_bottom
        self.filepath_front = filepath_front
        self.filepath_back = filepath_back#declares filepath and texture as variables
        
        self.texture = None

    #texture generator function
    def init_texture(self):
        self.texture = glGenTextures(1) # defines textures and how many to generate
        glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture) #texture binding
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE) # maps texture
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE) 
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath_left).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath_right).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Y, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath_top).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath_bottom).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath_back).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_X, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        image = pygame.image.load(self.filepath_front).convert_alpha() #declares image variable
        image_width, image_height = image.get_rect().size # gets image width and size
        image_data = pygame.image.tostring(image, "RGBA", True) #converts image to string to opengl can recognise the file
        glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data) #draws texture
        
        glGenerateMipmap(GL_TEXTURE_2D)

    def use(self):
        if self.texture is not None:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture)

    def destroy(self):
        if self.texture is not None:
            glDeleteTextures(1, [self.texture])

    
           



# gets current directory of file
current_dir = os.path.dirname(__file__)

# defines planets and values

sun = Planet(5.0, 0, 0, 0, 0, 0, os.path.join(current_dir, "images", "sunmap.jpg"))
mer = Planet(1.0, 7, 0, 5, 2, 0, os.path.join(current_dir, "images", "mercurymap.jpg"))
ear = Planet(2.0, 16, 0, 3, 24, 0, os.path.join(current_dir, "images", "earthmap1k.jpg"))
ven = Planet(1.5, 11, 0, 3.5, 180, 0, os.path.join(current_dir, "images", "venusmap.jpg"))
sat = Planet(3.0, 37, 0, 1, 27, 0, os.path.join(current_dir, "images", "saturnmap.jpg")) # all textures from https://planetpixelemporium.com/planets.html
jup = Planet(3.5, 28, 0, 1.4, 3, 0, os.path.join(current_dir, "images", "jupitermap.jpg"))
ura = Planet(2.5, 45, 0, 0.7, 98, 0, os.path.join(current_dir, "images", "uranusmap.jpg"))
nep = Planet(2.3, 54, 0, 0.5, 29, 0, os.path.join(current_dir, "images", "neptunemap.jpg"))
plu = Planet(0.4, 59, 0, 0.5, 120, 0, os.path.join(current_dir, "images", "plutomap1k.jpg"))
mar = Planet(1.2, 21, 0, 2.4, 25, 0, os.path.join(current_dir, "images", "mars_1k_color.jpg"))
skybox1 = Planet(500.0, 0, 0, 0, 0, 0, os.path.join(current_dir, "images", "galaxy.jpg"))












    



def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(40, (display[0]/display[1]), 0.1, 1000) #all of this is just setting up opengl and pygame window
    glTranslatef(0.0, -10.0, -150)

    planets = [ sun, mer, ear, ven, mar, jup, sat, ura, nep, plu] #planet declarer for for loop
    
    # Initialize all planet materials here
    for planet in planets:
        planet.init_material()
        
        
    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE) # disables lighting and enables textures
    glDisable(GL_LIGHTING)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when user quits
                pygame.quit()
                quit()
                
        

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears cache
        quadric = gluNewQuadric() #new quadric
        
        
        

        for planet in planets: # for loop for everyplanet instead of manualy typing it out
            quadric = gluNewQuadric() #enables texturing on the spheres
            gluQuadricTexture(quadric, GL_TRUE) #enables texturing on the spheres
            planet.orbit += planet.orbitspeed #planets orbit  
            planet.acisAni += 10.0 #axis
            planet.draw(quadric) #draws sphere with texture
        

        
        

        pygame.display.flip() #updates display
        pygame.time.wait(10)

if __name__ == "__main__":
    main()


