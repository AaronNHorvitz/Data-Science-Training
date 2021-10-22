#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pi = 3.14159

def area(radius):
    
    """
    Takes the radius of a circle and calculates the area of the circle.
    
    args:
    radius: float value or integer
    
    retuns: 
    area: float value that is the area of the cirucle

    """
    area = pi*(radius**2)
    return area

def circumferance(radius):
    
    """
    Takes the radius of a circle and calculates the circumferance of the circle.
    
    args:
    radius: float value or integer
    
    retuns: 
    circumferance: float value that is the circumferance of the cirucle

    """
    circumferance = 2*pi*radius
    return circumferance


def sphere_surface_area(radius):
    
    """
    Takes the radius of a sphere and calculates the surface area.
    
    args:
    radius: float value or integer
    
    retuns: 
    surface_area: float value that is the circumferance of the cirucle

    """
    surface_area = 4.0*area(radius)
    return surface_area

def sphere_volume(radius):
    
    """
    Takes the radius of a sphere and calculates the volume.
    
    args:
    radius: float value or integer
    
    retuns: 
    volume: float value that is the volume of the cirucle

    """
    volume = (4.0/3.0)*pi*(radius**3)
    
    return volume

