#!/usr/bin/env python3

from solid import *
import solid as sd
from solid.utils import *

import numpy as np

# Dial
'''Dial
Has a base that squeezes in first and then out again.
Should be printed in place so it can turn but not be removed.
Dials should be roughly the size of a quarter.
Print letters and numbers on top of dial.
'''
def dial(
    bottom_d=7,
    bottom_h=.5,
    middle_d=6,
    middle_h=.5,
    top_d=12,
    top_h=1,
    gap=0
    ):
    shifts = [bottom_h, .5*(bottom_d-middle_d), middle_h, .4*(top_d-middle_d), top_h]
    dial = sd.union()(
        sd.cylinder(d=bottom_d+2*gap, h=bottom_h),
        sd.translate([0,0,sum(shifts[:1])])(sd.cylinder(d1=bottom_d+2*gap, d2=middle_d+2*gap, h=.5*(bottom_d - middle_d))),
        sd.translate([0,0,sum(shifts[:2])])(sd.cylinder(d=middle_d+2*gap, h=middle_h)),
        sd.translate([0,0,sum(shifts[:3])])(sd.cylinder(d1=middle_d+2*gap, d2=top_d+2*gap, h=shifts[3])),
        sd.translate([0,0,sum(shifts[:4])])(sd.cylinder(d=top_d+2*gap, h=top_h)),
        )
    return dial

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
