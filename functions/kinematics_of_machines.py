import numpy as np
import sympy as sp

S = None
L = None
P = None
Q = None

# arrange link as R1, R2, R3, R4 ... as a loop, where R1 is the base, R2 is driving, and R'last' is following
temporary_link_array = np.array([1.2, 3.4, 5.6, 7.8])

class Mechanism_link_lengths:
    def __init__(self, link_array: np.array):
        self.link_array = link_array
        
    def link_count(self):
        return np.shape(self.link_array)[0]
    
    def arrange_cronologically(self):
        return np.sort(self.link_array)
    
    def shortest_link(self):
        return self.arrange_cronologically()[0]
    
    def longuest_link(self):
        return self.arrange_cronologically()[-1]
    
    def centre_links(self):
        return self.arrange_cronologically()[1:-1]
    
    def moving_links(self):
        return self.link_count() - 1

    def does_it_exist(self):
        if self.longuest_link() < self.shortest_link() + np.sum(self.centre_links(self)):
            return True
        else:
            return False
    
    def Grashof_condition(self):
        if self.link_count() == 4:
            S = self.shortest_link()
            L = self.longuest_link()
            P = self.centre_links()[0]
            Q = self.centre_links()[1]
            
            if S + L < P + Q:
                print("Class I Grashof linkage")
                if self.link_array[0] == S:
                    print("Ground shortest link Double-crank")
                elif self.link_array[1] == S or self.link_array[-1] == S:
                    print("Ground link adjacent to shortest: Crank-rocker")
                elif self.link_array[2] == S:
                    print("Ground link opposite the shortest: Grashof double-rocker")
                else:
                    print("Unkown Error.")
            elif S + L > P + Q:
                print("Class II, non-Grashof linkage: Triple Rocker (ie. double rocker in any)")
            elif S + L == P + Q:
                print("Class III, Special-case Grashof linkage, Change Point Mechanism")
        else:
            print("This is not a 4 link array so the Grashof conditions do not apply.")

classification_dict = {"crank-rocker", "double-crank", "double-rocker","triple-rocker"}


# Class solving unknown length
# Same input as above R1, R2, R3, R4 but as sp.Matrix for symbolic computation
class Mechanism_with_unknown:
    def __init__(self, link_array: sp.Matrix):
        self.link_array = link_array
        
    def arrange_cronologically(self):
        return np.sort(self.link_array)
    
    def shortest_link(self):
        return self.arrange_cronologically()[0]
    
    def longuest_link(self):
        return self.arrange_cronologically()[-1]
    
    def centre_links(self):
        return self.arrange_cronologically()[1:-1]


'''    
    def solve(self, category: str):
        symbol_number = 0
        for item in self.link_array[item]:
            if type(self.link_array[item]) == type(sp.Symbol()):
                symbol_number = item
        
        upper_bound = 0
        for item in self.link_array[item]:
            if type(self.link_array[item]) != type(sp.Symbol()):
                upper_bound += self.link_array[item]
                
        range_to_exist = sp.Matrix[0:upper_bound]
        
        if category == "crank-rocker":
            # Condition S + L < P + Q and S is adjacent to base

        Start here

        S = self.shortest_link()
        L = self.longuest_link()
        P = self.centre_links()[0]
        Q = self.centre_links()[1]
        for item in self.link_array:
            if type(self.link_array[item]) == type(sp.Symbol()):
                if category == "crank-rocker":
                    return sp.solve_rational_inequalities(S + P, Q + P, '<')
                if category == "double-crank":
                    return sp.solve_rational_inequalities(S + P, Q + P, '<')
                
'''

answer = Mechanism_link_lengths(temporary_link_array).moving_links()
print(answer)



class Mechanism_classification:
    def __init__(self, links, full_joints, half_joints):
        self.links = links
        self.full_joints = full_joints
        self.half_joints = half_joints
        
    def moving_links(self):
        return self.links - 1
    
    def degrees_of_freedom(self):
        DoF = self.moving_links - 2 * self.full_joints - self.half_joints
        return DoF
    def classify(self):
        if self.degrees_of_freedom > 0:
            return print("This is a Mechanism")
        elif self.degrees_of_freedom == 0:
            return print("This is a Structure.")
        elif self.degrees_of_freedom < 0:
            return print("This is a Pre-Loaded Structure.")
        
"""
Mechanism Inversion:
    A mechanism inversion is said to occur when the fixed
    link is allowed to move, and an alternative link is fixed.
    Important: The RELATIVE MOTION between the links remains UNCHANGED, but 
            the ABSOLUTE MOTION and the function fo the mechanism is CHANGED.
"""

"""
Grashof Consitions and Classifications:
    S = length of shortestlink
    L = length of longestlink
    P = length of one remaining link
    Q = length of other remaining link
    
    S + L <= P + Q
    
    Class I Kinematic Chain: S + L < P + Q
        If S = input link, Then is crank rocker
        If s = base link, Then is drag link / Double-crank
        If ground-link opposite the shortest: Grashof double-rocker
        If other, Then is rocker-rocker
    Class II Kinematic Chain: S + L > P + Q
        Then is rocker-rocker
    Class III Kinematic Chain: S + L = P + Q
    
    When links are collinear, at change point motion is unpredictable
"""


        
# Feed array/matrix as ([base link, driver link, coupler link, follower link])
def permissible_base_length(link_array, desired_mechanism):
    base = link_array[0]
    driver = link_array[1]
    coupler = link_array[2]
    follower = link_array[3]
    
    sorted_link_array = np.sort(driver, coupler, follower)
    longuest_link = sorted_link_array[2]
    middle_link = sorted_link_array[1]
    shortest_link = sorted_link_array[0]
    total_lower_bound = longuest_link - middle_link - shortest_link
    total_upper_bound = sum(driver, coupler, follower)
    total_interval = sp.Interval(total_lower_bound, total_upper_bound)
    
    # Crank rocker condition: S + L < P + Q
    if desired_mechanism == "Crank-rocker":
        # Case 1: Base = S
        S = base
        L = longuest_link
        P = middle_link
        Q = shortest_link
        
        solution_S = sp.Interval(sp.solve_univariate_inequality(S + L <= P + Q, S))
        intersection = solution_S.intersect(total_interval)
        if intersection:
            print(f"if the base is the shortest link, it must be between {intersection} units.")
        
        # Case 2: Base = L
        S = shortest_link
        L = base
        P = longuest_link
        Q = middle_link
        solution_L = sp.Interval(sp.solve_univariate_inequality(S + L <= P + Q, L))
        intersection = solution_L.intersect(total_interval)
        if intersection:
            print(f"if the base is the longuest link, it must be between {intersection} units.")
            
        # Case 3: Base =  or Q
        S = shortest_link
        L = longuest_link
        P = base
        Q = middle_link
        solution_P = sp.Interval(sp.solve_univariate_inequality(S + L <= P + Q, P))
        intersection = solution_L.intersect(total_interval)
        if intersection:
            print(f"if the base is between the longuest and shortest link, it must be betweem {intersection} units.")
        
        
        # Case 1: Base = S
        if isinstance(S, sp.Symbol):
            solution_S = sp.Interval(sp.solve_univariate_inequality(S + L <= P + Q, S))
            print(f"If S were to be the base: {solution_S}.")
            
        # Case 2: Base = L
        if isinstance(L, sp.Symbol):
            solution_L = sp.solve_univariate_inequality(S + L <= P + Q, L)
            print(f"If S were to be the base: {solution_L}.")
        # Case 3: Base = Q or P
        if isinstance(P, sp.Symbol):
            solution_P = sp.solve_univariate_inequality(S + L <= P + Q, P)
            print(f"If S were to be the base: {solution_P}.")
        if isinstance(Q, sp.Symbol):
            solution_Q = sp.solve_univariate_inequality(S + L <= P + Q, Q)
            print(f"If S were to be the base: {solution_Q}.")
            

   
#links = np.array([30,80,60,70])
#answer = Grashof_condition(links)

#print(answer)

x = sp.symbols('x')


answer = sp.solve(x + 5 - (6 + 3), x)
# print(answer)
    
''' 
Complex Vector Loops
'''
# loop array as list of arrays 
loop_array = np.array([
    []
])

