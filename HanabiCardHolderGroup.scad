$fn=256;$fa=6;


difference() {
	union() {
		translate(v = [-15.1500000000, 0, 0]) {
			translate(v = [0, 18.0000000000, 1.0000000000]) {
				hull() {
					cube(center = true, size = [5.7000000000, 35.2000000000, 1.2000000000]);
					cube(center = true, size = [4.9000000000, 36, 1.2000000000]);
					cube(center = true, size = [4.9000000000, 35.2000000000, 2]);
				}
			}
		}
		translate(v = [15.1500000000, 0, 0]) {
			translate(v = [0, 18.0000000000, 1.0000000000]) {
				hull() {
					cube(center = true, size = [5.7000000000, 35.2000000000, 1.2000000000]);
					cube(center = true, size = [4.9000000000, 36, 1.2000000000]);
					cube(center = true, size = [4.9000000000, 35.2000000000, 2]);
				}
			}
		}
		translate(v = [0, 27, 3.6500000000]) {
			hull() {
				cube(center = true, size = [36, 5.2000000000, 2.2000000000]);
				cube(center = true, size = [35.2000000000, 6, 2.2000000000]);
				cube(center = true, size = [35.2000000000, 5.2000000000, 3]);
			}
		}
		translate(v = [15.1500000000, 27, 0]) {
			translate(v = [0, 0, 2.5000000000]) {
				hull() {
					cube(center = true, size = [5.7000000000, 5.2000000000, 4.2000000000]);
					cube(center = true, size = [4.9000000000, 6, 4.2000000000]);
					cube(center = true, size = [4.9000000000, 5.2000000000, 5]);
				}
			}
		}
		translate(v = [-15.1500000000, 27, 0]) {
			translate(v = [0, 0, 2.5000000000]) {
				hull() {
					cube(center = true, size = [5.7000000000, 5.2000000000, 4.2000000000]);
					cube(center = true, size = [4.9000000000, 6, 4.2000000000]);
					cube(center = true, size = [4.9000000000, 5.2000000000, 5]);
				}
			}
		}
		translate(v = [16.1500000000, 27, 0]) {
			translate(v = [0, 0, 3.3500000000]) {
				hull() {
					cube(center = true, size = [5.7000000000, 5.2000000000, 2.8000000000]);
					cube(center = true, size = [4.9000000000, 6, 2.8000000000]);
					cube(center = true, size = [4.9000000000, 5.2000000000, 3.6000000000]);
				}
			}
		}
		translate(v = [-16.1500000000, 27, 0]) {
			translate(v = [0, 0, 3.3500000000]) {
				hull() {
					cube(center = true, size = [5.7000000000, 5.2000000000, 2.8000000000]);
					cube(center = true, size = [4.9000000000, 6, 2.8000000000]);
					cube(center = true, size = [4.9000000000, 5.2000000000, 3.6000000000]);
				}
			}
		}
	}
	translate(v = [0, 27, 2.0100000000]) {
		rotate(a = [5, 0, 0]) {
			difference() {
				translate(v = [0, 0, 10]) {
					cube(center = true, size = [50, 3, 20]);
				}
				translate(v = [0, 6.1500000000, 0]) {
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
