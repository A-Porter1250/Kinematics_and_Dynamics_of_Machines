'''
Joint Classification:
Type of contact between elements: line, point, surface
• Lower pair - surface contact
• Higher pair - point or line contact
Number of degrees of freedom allowed
• Consider translation and rotation
• 1 DoF - full joint (Rotating full pin joint, translating full slider)
• 2 DoF - half joint (Link against plane, Pin in slot)
• 3+ DoF
Type of physical closure
• Form closed - closed by its geometry
• Force-closed - external force keeps the joint together/closed
Crank
• A link that makes a complete revolution and is pivoted to the ground.
Rocker
• a link that has oscillatory (back and forth) rotation and is
    pivoted to the ground
Coupler
• a connecting rod, a link that has a complex motion and
    is not pivoted to the ground
Ground
• a link or links that are fixed (non-moving) with respect
    to the reference frame
'''

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

"""
Example of types of four-bar mechanisms
if r_2 (driver) = 2, r_3 (coupler) = 4, r_4 (follower) = 5

r_1 (base) (cm)

0 < 1 = Drag Link, 1 = Change Point
1 < 3 = Rocker-rocker, 3 = Change Point
3 < 7 = Crank rocker, 7 = Change Point
7 < 11 = Rocker rocker, 11 = All links collinear (no motion)
r_1 > 11 = r_2 + r_3 + r_4 = Impossible to assemble mechanism
"""