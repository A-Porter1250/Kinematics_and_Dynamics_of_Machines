import numpy as np

class Point:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __repr__(self):
        return f"{self.real} + {self.imaginary}j"
    
    
# List of points 
loop_array_test = np.array([Point(0,0), Point(1,1), Point(2,3), Point(4,0)])

class loop:
    def __init__(self, loop_array):
        self.loop_array = loop_array
        
    def define_vectors_array(self):
        # Create a vector array
        vector_list = []
        for i in range(len(self.loop_array) - 1):
            vector = np.array([self.loop_array[i + 1].real - self.loop_array[i].real, 
                               self.loop_array[i + 1].imaginary - self.loop_array[i].imaginary])
            vector_list.append(vector)
        vector = np.array([self.loop_array[0].real - self.loop_array[-1].real, self.loop_array[0].imaginary - self.loop_array[-1].imaginary])
        vector_list.append(vector)
        vector_array = np.array(vector_list)
        return vector_array
    
    def magnitude_and_angle_array(self):
        positions_array = self.define_vectors_array()
        vector_list = []
        for i in range(len(positions_array)):
            magnitude = np.sqrt(positions_array[i][0] ** 2 + positions_array[i][1] ** 2)
            angle = np.arctan2(positions_array[i][1], positions_array[i][0])
            vector = [magnitude, angle]
            vector_list.append(vector)
        vector_array = np.array(vector_list)
        return vector_array
    
    def magnitude_array(self):
        list = []
        for i in range(len(self.magnitude_and_angle_array())):
            value = self.magnitude_and_angle_array()[i][0]
            list.append(value)
        return np.array(list)
    
    def angle_array(self):
        list = []
        for i in range(len(self.magnitude_and_angle_array())):
            value = self.magnitude_and_angle_array()[i][1]
            list.append(value)
        return np.array(list)
    
    # Rework so that it works with more than one degree of freedom
    def independent_variable(self, vector_position_in_array: np.array):
        self.magnitude_and_angle_array()
    
    def loop_closure_equations(self, idenpendent_variables):
        
        for i in range(len(self.magnitude_and_angle_array()) - 1):
        
            real_equation = self.magnitude_array()[i] * np.cos(self.angle_array()[i])
            
            imaginary_equation = self.magnitude_array()[i] * np.cos(self.angle_array()[i])
        
        

    
        
        
    
    
# Step 3: Select the independent variables and identify the two dependent variables

# def equations_from_real_and_imaginary_parts(magnitude_and_angle_list: np.array):
    
        
current_loop = loop(loop_array_test)    
answer = current_loop.angle_array()
print(answer)

