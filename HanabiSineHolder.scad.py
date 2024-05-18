#!/usr/bin/env python3

'''Hanabi single card holders.
The design is intended to be compact and fit within the Hanabi box.

Hanabi card sleeves are typically 57x89mm.

Philosophy:
-We wish to have 8 interlocking holders on each card half.
-Assume 6mm crossbar width.
-Max Y for holder = 89 - 7*6 = 47
-At 45 degree angle, triangle height would be 57/2=28.5
-At 60 degree angle, triangle height would be sqrt(3)/2*57=49
-At a height of 40.7, the hypotenuse (leg) would be 47.

Box inner dimensions 115x90mm
If we want a depth of 40mm per card holder, then (115-40)/15=5.
If we have two 115mm rows, then (115-40)/7 > 10.
This will support a width of 5mm at 60 degrees.
The width for the card holder would them be 45mm.
'''

import solid2 as sd

import numpy as np



def beveled_box(XYZ, bevel, center=False):
    '''Box with beveled corners
    Ends are cut so that two rods can be joined at 90 degrees
    XYZ: [X-direction, Y-direction, Z-direction]
    bevel: length of non-hypotenuse sides
    Will be placed in the same location as cube([X,Y,Z])
    center: Positions beveled_box with respect to origin identically to cube()
    '''
    x,y,z = XYZ
    box = sd.hull()(
        sd.cube([x, y-2*bevel, z-2*bevel], center=True),
        sd.cube([x-2*bevel, y, z-2*bevel], center=True),
        sd.cube([x-2*bevel, y-2*bevel, z], center=True),
        )
    if not center:
        box = sd.translate([x/2, y/2, z/2])(box)
    return box

def beveled_hexagon(inradius, height, bevel, center=False):
    '''Hexagon with beveled edges on top and bottom.
    middle is like a hamburger patty.
    outer is like the bun.
    '''
    middle = sd.cube([1/np.sqrt(3)*inradius, inradius, height-2*bevel], center=True)
    middle = sd.hull()(*[sd.rotate([0,0,theta])(middle) for theta in range(0,360,120)])
    outer = sd.cube([1/np.sqrt(3)*(inradius-2*bevel), inradius-2*bevel, height], center=True)
    outer = sd.hull()(*[sd.rotate([0,0,theta])(outer) for theta in range(0,360,120)])
    return sd.hull()(middle, outer)

def beveled_half_hexagon(inradius, height, bevel, center=False):
    '''Upper half of hexagon with beveled edges on top and bottom.
    middle is like a hamburger patty.
    outer is like the bun.
    '''
    middle = sd.cube([1/np.sqrt(3)*inradius, inradius, height-2*bevel], center=True)
    middle = sd.hull()(*[sd.rotate([0,0,theta])(middle) for theta in range(0,360,120)])
    y_shift = 2*inradius
    middle = sd.intersection()(middle, sd.translate([0,y_shift/2,0])(sd.cube(y_shift,center=True)))
    outer = sd.cube([1/np.sqrt(3)*(inradius-2*bevel), inradius-2*bevel, height], center=True)
    outer = sd.hull()(*[sd.rotate([0,0,theta])(outer) for theta in range(0,360,120)])
    outer = sd.intersection()(outer, sd.translate([0,y_shift/2+bevel,0])(sd.cube(y_shift, center=True)))
    return sd.hull()(middle, outer)


def card_notch(gap=.3, base_w=25, notch_r=6):
    notch = sd.cube([50,3,20],center=True)
    notch = sd.translate([0,0,10])(notch)
    notch -= sd.translate([0,notch_r+gap,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch -= sd.translate([0,-notch_r,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch = sd.rotate([5,0,180])(notch)
    notch = sd.translate([0,7.5,2.01])(notch)
    return notch

def card_notch(gap=.3, base_w=25, notch_r=6):
    notch = sd.cube([50,2,20],center=True)
    notch = sd.translate([0,0,10.01])(notch)
    bump = sd.cylinder(h=1.7, d=3)
    bump += sd.translate([0,0,1.7])(sd.sphere(d=3))
    bump = sd.translate([0,1.4,0])(bump)
    bump = sd.union()(*[sd.translate([8*i,0,0])(bump) for i in range(-3,4)])
    other = sd.rotate([0,0,180])(bump)
    other = sd.translate([4,0,0])(other)
    bump += other
    bump = sd.rotate([0,0,180])(bump)
    notch -= bump
    # notch -= other
    notch = sd.translate([0,9.5,2.01])(notch)
    return notch

lr_offset = 10
top_d=18
v_gap = .3
gap = .1
infty = 1000
bevel=.4

leg_x = 5
leg_y = 45
leg_z = 2
leg = beveled_box(XYZ=[leg_x, leg_y, leg_z], bevel=bevel, center=True)
leg = sd.translate([0,leg_y/2,leg_z/2])(leg)

cross_x = 36
cross_y = 10
cross_z = 3

hex_x = 5*3**-.5
hex_y = 5
hex_z = 2
shift_x = 20
unit_hex = sd.translate([0,0,hex_z/2])(beveled_hexagon(hex_y, hex_z, bevel))


hex_r = [sd.translate([(6.5-ii)*hex_x, (ii+.5)*hex_y,0])(unit_hex) for ii in range(5)]
leg_r = sd.hull()(hex_r[0]+hex_r[-1]) + sd.translate([0,0,bevel])(hex_r[0])

hex_l = [sd.translate([-(6.5-ii)*hex_x, (ii+.5)*hex_y,0])(unit_hex) for ii in range(5)]
leg_l = sd.hull()(hex_l[0]+hex_l[-1]) + sd.translate([0,0,bevel])(hex_l[0])

base = leg_l + leg_r

post_y = 15
post_z = 6
post = sd.translate([0,hex_y,post_z/2])(beveled_half_hexagon(post_y,post_z,bevel))
post += sd.translate([0,2*hex_y,post_z/2])(beveled_half_hexagon(2/3*post_y,post_z,bevel))

cross = sd.hull()(
    sd.translate([-4*hex_x,0,0])(post), 
    sd.translate([4*hex_x,0,0])(post),
    )
cross = sd.intersection()(cross, sd.translate([0,0,2*post_y+hex_z+v_gap])(sd.cube(4*post_y,center=True)))
cross += post
cross += sd.translate([0,0,hex_z/2])(sd.intersection()(sd.translate([0,0,-hex_z])(cross), base))
cross = sd.intersection()(cross, sd.translate([0,infty/2+hex_y+gap,0])(sd.cube(infty, center=True)))

total = sd.union()(
    base,
    cross,
    )


# Test how shifts overlap
# total += sd.translate([0,-10,0])(total)
# total += sd.translate([0,-20,0])(total)

total -= sd.translate([0,0,1])(card_notch(gap=.3))


fn = 64
fa = 6
# total = card_notch()
print(sd.scad_render(total,file_header=f'$fn={fn};$fa={fa};'))
