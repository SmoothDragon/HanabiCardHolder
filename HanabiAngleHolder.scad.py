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

from solid import *
import solid as sd
from solid.utils import *

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


def card_notch(gap=.3, base_w=25, notch_r=6):
    notch = sd.cube([50,3,20],center=True)
    notch = sd.translate([0,0,10])(notch)
    notch -= sd.translate([0,notch_r+gap,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch -= sd.translate([0,-notch_r,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch = sd.rotate([5,0,180])(notch)
    notch = sd.translate([0,6.5,2.01])(notch)
    return notch

lr_offset = 10
top_d=18
gap = .3
bevel=.4

leg_x = 5
leg_y = 45
leg_z = 2
leg = beveled_box(XYZ=[leg_x, leg_y, leg_z], bevel=bevel, center=True)
leg = sd.translate([0,leg_y/2,leg_z/2])(leg)

cross_x = 36
cross_y = 10
cross_z = 3
cross = beveled_box(XYZ=[cross_x, cross_y-gap, cross_z], bevel=bevel, center=True)
cross = sd.translate([0, -5+(leg_y-leg_x*3**.5)/2*3**.5-20, cross_z/2+leg_z])(cross)

post = beveled_box(XYZ=[leg_x, cross_y, cross_z+leg_z], bevel=bevel, center=True)
post = sd.translate([0,0,(cross_z+leg_z)/2])(post)

nub = beveled_box(XYZ=[leg_x, cross_y, cross_z+2*bevel-.2], bevel=bevel, center=True)
nub = sd.translate([0,0,(cross_z+2*bevel)/2+leg_z-bevel-gap/2])(nub)

leg1 = sd.translate([leg_y/2-leg_x*3**.5/2,0,0])(sd.rotate([0,0,30])(leg))
leg2 = sd.translate([-(leg_y/2-leg_x*3**.5/2),0,0])(sd.rotate([0,0,-30])(leg))
tip = sd.intersection()(leg1,leg2)

sleg_x = 5
sleg_y = 26.5
sleg_z = 2
sleg = beveled_box(XYZ=[sleg_x, sleg_y, sleg_z], bevel=bevel, center=True)
sleg = sd.translate([0,sleg_y/2,sleg_z/2])(sleg)

leg1 = sd.translate([leg_y/2-leg_x*3**.5/2,0,0])(sd.rotate([0,0,30])(sleg)),
leg2 = sd.translate([-(leg_y/2-leg_x*3**.5/2),0,0])(sd.rotate([0,0,-30])(sleg)),

hexagon = beveled_box(XYZ=[10*3**-.5, 10-gap, 5], bevel=bevel, center=True)
hexagon = sd.hull()(hexagon,
                     sd.rotate([0,0,60])(hexagon),
                     sd.rotate([0,0,120])(hexagon),
                     )
hexagon2 = beveled_box(XYZ=[10*3**-.5, 10-gap, 3], bevel=bevel, center=True)
hexagon2 = sd.hull()(hexagon2,
                     sd.rotate([0,0,60])(hexagon2),
                     sd.rotate([0,0,120])(hexagon2),
                     )
hexagon3 = sd.translate([0, -5+(leg_y-leg_x*3**.5)/2*3**.5-20, cross_z/2])(hexagon2)
hexagon2 = sd.translate([0, -5+(leg_y-leg_x*3**.5)/2*3**.5-20, cross_z/2+leg_z+gap])(hexagon2)
hexagon4 = sd.intersection()(leg1, sd.translate([20*3**-.5+gap*.5,0, 0])(hexagon3))
hexagon5 = sd.intersection()(leg2, sd.translate([-20*3**-.5-gap/2,0, 0])(hexagon3))

total = sd.union()(
    leg1,
    leg2,
    # sd.translate([leg_y/2-leg_x*3**.5/2,0,0])(sd.rotate([0,0,30])(sleg)),
    # sd.translate([-(leg_y/2-leg_x*3**.5/2),0,0])(sd.rotate([0,0,-30])(sleg)),
    # tip,
    # cross,
    sd.translate([0, -5+(leg_y-leg_x*3**.5)/2*3**.5-20, cross_z/2+leg_z-1])(hexagon),
    sd.hull()(
    sd.translate([20*3**-.5+gap*.5,0, 0])(hexagon2),
    sd.translate([-20*3**-.5-gap*.5, 0, 0])(hexagon2),
        ),
    sd.translate([0,0, 1.1])(hexagon4),
    sd.translate([0,0, 1.1])(hexagon5),
    # sd.translate([-(cross_x-leg_x)/2,0,0])(leg),
    # sd.translate([(cross_x-leg_x)/2,0,0])(leg),
    # cross,
    # sd.translate([(cross_x-leg_x)/2,27,0])(post),
    # sd.translate([-(cross_x-leg_x)/2,27,0])(post),
    # sd.translate([0,27,0])(post),
    # sd.translate([(leg_x+2*gap)/2,27,0])(post),
    # sd.translate([-(leg_x+2*gap)/2,27,0])(post),
    # sd.translate([(cross_x-leg_x+2)/2,27,0])(nub),
    # sd.translate([-(cross_x-leg_x+2)/2,27,0])(nub),
    )

# total += sd.translate([0,-10,0])(total)
# total += sd.translate([0,-20,0])(total)

# notch = sd.cube([50,1,20],center=True)
# notch = sd.translate([0,0,10])(notch)
# notch = sd.rotate([0,0,0])(notch)
# notch = sd.translate([0,18,2])(notch)

total -= sd.translate([0,0,1])(card_notch(gap=.3))
# total = beveled_box([10,20,30],1)

# total = beveled_hexagon(20,4,.5)

fn = 256
fa = 6
print(scad_render(total,file_header=f'$fn={fn};$fa={fa};'))
