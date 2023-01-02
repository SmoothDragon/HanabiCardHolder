$fn=256;$fa=6;


difference() {
	translate(v = [0, -5, 0]) {
		union() {
			hull() {
				translate(v = [-12.5000000000, 3, 0]) {
					cylinder(center = false, h = 2, r = 3);
				}
				translate(v = [0, 26, 0]) {
					translate(v = [-12.5000000000, 3, 0]) {
						cylinder(center = false, h = 2, r = 3);
					}
				}
			}
			hull() {
				translate(v = [25, 0, 0]) {
					translate(v = [-12.5000000000, 3, 0]) {
						cylinder(center = false, h = 2, r = 3);
					}
				}
				translate(v = [25, 26, 0]) {
					translate(v = [-12.5000000000, 3, 0]) {
						cylinder(center = false, h = 2, r = 3);
					}
				}
			}
			hull() {
				translate(v = [0, 20, 0]) {
					translate(v = [-12.5000000000, 3, 0]) {
						translate(v = [0, 0, 2]) {
							cylinder(center = false, h = 3.0000000000, r = 3);
						}
					}
				}
				translate(v = [25, 20, 0]) {
					translate(v = [-12.5000000000, 3, 0]) {
						translate(v = [0, 0, 2]) {
							cylinder(center = false, h = 3.0000000000, r = 3);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 18, 2]) {
		rotate(a = [5, 0, 0]) {
			difference() {
				translate(v = [0, 0, 10]) {
					cube(center = true, size = [50, 3, 20]);
				}
				translate(v = [0, 6.3000000000, 0]) {
					rotate(a = [0, 90, 0]) {
						cylinder(center = true, h = 50, r = 6);
					}
				}
				translate(v = [0, -6, 0]) {
					rotate(a = [0, 90, 0]) {
						cylinder(center = true, h = 50, r = 6);
					}
				}
			}
		}
	}
}
