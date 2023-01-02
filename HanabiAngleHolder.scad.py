#!/usr/bin/env python3

'''Hanabi single card holders.
The design is intended to be compact and fit within the Hanabi box.

Hanabi card sleeves are typically 57x89mm.

Philosophy:
-We wish to have 8 interlocking holders on each card half.
-Assume 6mm crossbar width.
-Max Y for holder = 89 - 7*6 = 47
-At 45 degree angle

    If the 
'''

from solid import *
import solid as sd
from solid.utils import *

import numpy as np

def base_rack(
    base_w=25,
    base_d=20,
    base_h=2,
    base_curve_r=3,
    dial_center_diff=15,
    dial_offset=5,
    ):
    corner = sd.cylinder(r=base_curve_r, h=base_h, center=False)
    high_corner = sd.scale([1,1,2.5])(corner)
    corner = sd.translate([.5*(-base_w+.0*base_curve_r),base_curve_r,0])(corner)
    high_corner = sd.translate([.5*(-base_w+.0*base_curve_r),base_curve_r,0])(high_corner)
    base = sd.hull()(
        corner,
        sd.translate([base_w,0,0])(corner),
        sd.translate([0,base_d,0])(corner),
        sd.translate([base_w,base_d,0])(corner),
        )
    base += sd.hull()(
        sd.translate([0,base_d,0])(high_corner),
        sd.translate([base_w,base_d,0])(high_corner),
        )
    base = sd.translate([0,-dial_offset,0])(base)
    return base

def card_notch(gap=.2, base_w=25, notch_r=10):
    notch = sd.cube([50,3,20],center=True)
    notch = sd.translate([0,0,10])(notch)
    notch -= sd.translate([0,notch_r+gap,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch -= sd.translate([0,-notch_r,0])(sd.rotate([0,90,0])(sd.cylinder(r=notch_r, h=2*base_w, center=True)))
    notch = sd.rotate([5,0,0])(notch)
    notch = sd.translate([0,18,2])(notch)
    return notch

lr_offset = 10
top_d=18
gap = .3
# font = 'Liberation Sans'
font = 'DejaVuSansMono-Bold'
numbers = '?12345'
colors = '?RYGBW'

number_dial = dial(top_d=top_d)
for i, ch in enumerate(numbers):
    number_dial += sd.rotate(-60*i)(sd.translate([0,-top_d/3,6.5])(sd.linear_extrude(1.5)(
        sd.text(text=ch, font = font, size = top_d/4, valign='center', halign='center'))))
number_dial = sd.translate([-lr_offset,0,0])(number_dial)

color_dial = dial(top_d=top_d)
for i, ch in enumerate(colors):
    color_dial += sd.rotate(-60*i)(sd.translate([0,-top_d/3,6.5])(sd.linear_extrude(1.5)(
        sd.text(text=ch, font = font, size = top_d/4, valign='center', halign='center'))))
color_dial = sd.translate([lr_offset,0,0])(color_dial)

total = base_rack() \
    - sd.translate([-lr_offset,0,0])(dial(gap=gap)) \
    - sd.translate([lr_offset,0,0])(dial(gap=gap)) \
    + number_dial + color_dial

notch = sd.cube([50,1,20],center=True)
notch = sd.translate([0,0,10])(notch)
notch = sd.rotate([0,0,0])(notch)
notch = sd.translate([0,18,2])(notch)

total -= card_notch(gap=gap)


fn = 256
fa = 6
print(scad_render(total,file_header=f'$fn={fn};$fa={fa};'))
