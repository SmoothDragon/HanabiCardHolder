$fn=256;$fa=6;


difference() {
	union() {
		translate(v = [18.1698729811, 0, 0]) {
			rotate(a = [0, 0, 30]) {
				translate(v = [0, 18.0000000000, 1.0000000000]) {
					hull() {
						cube(center = true, size = [5, 35.2000000000, 1.2000000000]);
						cube(center = true, size = [4.2000000000, 36, 1.2000000000]);
						cube(center = true, size = [4.2000000000, 35.2000000000, 2]);
					}
				}
			}
		}
		translate(v = [-18.1698729811, 0, 0]) {
			rotate(a = [0, 0, -30]) {
				translate(v = [0, 18.0000000000, 1.0000000000]) {
					hull() {
						cube(center = true, size = [5, 35.2000000000, 1.2000000000]);
						cube(center = true, size = [4.2000000000, 36, 1.2000000000]);
						cube(center = true, size = [4.2000000000, 35.2000000000, 2]);
					}
				}
			}
		}
		intersection() {
			translate(v = [18.1698729811, 0, 0]) {
				rotate(a = [0, 0, 30]) {
					translate(v = [0, 22.5000000000, 1.0000000000]) {
						hull() {
							cube(center = true, size = [5, 44.2000000000, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 45, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 44.2000000000, 2]);
						}
					}
				}
			}
			translate(v = [-18.1698729811, 0, 0]) {
				rotate(a = [0, 0, -30]) {
					translate(v = [0, 22.5000000000, 1.0000000000]) {
						hull() {
							cube(center = true, size = [5, 44.2000000000, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 45, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 44.2000000000, 2]);
						}
					}
				}
			}
		}
		translate(v = [0, 10, 3.5000000000]) {
			hull() {
				cube(center = true, size = [36, 9.2000000000, 2.2000000000]);
				cube(center = true, size = [35.2000000000, 10, 2.2000000000]);
				cube(center = true, size = [35.2000000000, 9.2000000000, 3]);
			}
		}
		translate(v = [0, -10, 0]) {
			union() {
				translate(v = [18.1698729811, 0, 0]) {
					rotate(a = [0, 0, 30]) {
						translate(v = [0, 18.0000000000, 1.0000000000]) {
							hull() {
								cube(center = true, size = [5, 35.2000000000, 1.2000000000]);
								cube(center = true, size = [4.2000000000, 36, 1.2000000000]);
								cube(center = true, size = [4.2000000000, 35.2000000000, 2]);
							}
						}
					}
				}
				translate(v = [-18.1698729811, 0, 0]) {
					rotate(a = [0, 0, -30]) {
						translate(v = [0, 18.0000000000, 1.0000000000]) {
							hull() {
								cube(center = true, size = [5, 35.2000000000, 1.2000000000]);
								cube(center = true, size = [4.2000000000, 36, 1.2000000000]);
								cube(center = true, size = [4.2000000000, 35.2000000000, 2]);
							}
						}
					}
				}
				intersection() {
					translate(v = [18.1698729811, 0, 0]) {
						rotate(a = [0, 0, 30]) {
							translate(v = [0, 22.5000000000, 1.0000000000]) {
								hull() {
									cube(center = true, size = [5, 44.2000000000, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 45, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 44.2000000000, 2]);
								}
							}
						}
					}
					translate(v = [-18.1698729811, 0, 0]) {
						rotate(a = [0, 0, -30]) {
							translate(v = [0, 22.5000000000, 1.0000000000]) {
								hull() {
									cube(center = true, size = [5, 44.2000000000, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 45, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 44.2000000000, 2]);
								}
							}
						}
					}
				}
				translate(v = [0, 10, 3.5000000000]) {
					hull() {
						cube(center = true, size = [36, 9.2000000000, 2.2000000000]);
						cube(center = true, size = [35.2000000000, 10, 2.2000000000]);
						cube(center = true, size = [35.2000000000, 9.2000000000, 3]);
					}
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
