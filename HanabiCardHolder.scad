$fn=256;$fa=6;


difference() {
	union() {
		difference() {
			translate(v = [0, -5, 0]) {
				union() {
					hull() {
						translate(v = [-12.5000000000, 3, 0]) {
							cylinder(center = false, h = 2, r = 3);
						}
						translate(v = [25, 0, 0]) {
							translate(v = [-12.5000000000, 3, 0]) {
								cylinder(center = false, h = 2, r = 3);
							}
						}
						translate(v = [0, 20, 0]) {
							translate(v = [-12.5000000000, 3, 0]) {
								cylinder(center = false, h = 2, r = 3);
							}
						}
						translate(v = [25, 20, 0]) {
							translate(v = [-12.5000000000, 3, 0]) {
								cylinder(center = false, h = 2, r = 3);
							}
						}
					}
					hull() {
						translate(v = [0, 20, 0]) {
							translate(v = [-12.5000000000, 3, 0]) {
								scale(v = [1, 1, 2.5000000000]) {
									cylinder(center = false, h = 2, r = 3);
								}
							}
						}
						translate(v = [25, 20, 0]) {
							translate(v = [-12.5000000000, 3, 0]) {
								scale(v = [1, 1, 2.5000000000]) {
									cylinder(center = false, h = 2, r = 3);
								}
							}
						}
					}
				}
			}
			translate(v = [-10, 0, 0]) {
				union() {
					cylinder(d = 7.6000000000, h = 0.5000000000);
					translate(v = [0, 0, 0.5000000000]) {
						cylinder(d1 = 7.6000000000, d2 = 6.6000000000, h = 0.5000000000);
					}
					translate(v = [0, 0, 1.0000000000]) {
						cylinder(d = 6.6000000000, h = 0.5000000000);
					}
					translate(v = [0, 0, 1.5000000000]) {
						cylinder(d1 = 6.6000000000, d2 = 12.6000000000, h = 2.4000000000);
					}
					translate(v = [0, 0, 3.9000000000]) {
						cylinder(d = 12.6000000000, h = 1);
					}
				}
			}
			translate(v = [10, 0, 0]) {
				union() {
					cylinder(d = 7.6000000000, h = 0.5000000000);
					translate(v = [0, 0, 0.5000000000]) {
						cylinder(d1 = 7.6000000000, d2 = 6.6000000000, h = 0.5000000000);
					}
					translate(v = [0, 0, 1.0000000000]) {
						cylinder(d = 6.6000000000, h = 0.5000000000);
					}
					translate(v = [0, 0, 1.5000000000]) {
						cylinder(d1 = 6.6000000000, d2 = 12.6000000000, h = 2.4000000000);
					}
					translate(v = [0, 0, 3.9000000000]) {
						cylinder(d = 12.6000000000, h = 1);
					}
				}
			}
		}
		translate(v = [-10, 0, 0]) {
			union() {
				cylinder(d = 7, h = 0.5000000000);
				translate(v = [0, 0, 0.5000000000]) {
					cylinder(d1 = 7, d2 = 6, h = 0.5000000000);
				}
				translate(v = [0, 0, 1.0000000000]) {
					cylinder(d = 6, h = 0.5000000000);
				}
				translate(v = [0, 0, 1.5000000000]) {
					cylinder(d1 = 6, d2 = 18, h = 4.8000000000);
				}
				translate(v = [0, 0, 6.3000000000]) {
					cylinder(d = 18, h = 1);
				}
				rotate(a = 0) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "?", valign = "center");
						}
					}
				}
				rotate(a = -60) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "1", valign = "center");
						}
					}
				}
				rotate(a = -120) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "2", valign = "center");
						}
					}
				}
				rotate(a = -180) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "3", valign = "center");
						}
					}
				}
				rotate(a = -240) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "4", valign = "center");
						}
					}
				}
				rotate(a = -300) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "5", valign = "center");
						}
					}
				}
			}
		}
		translate(v = [10, 0, 0]) {
			union() {
				cylinder(d = 7, h = 0.5000000000);
				translate(v = [0, 0, 0.5000000000]) {
					cylinder(d1 = 7, d2 = 6, h = 0.5000000000);
				}
				translate(v = [0, 0, 1.0000000000]) {
					cylinder(d = 6, h = 0.5000000000);
				}
				translate(v = [0, 0, 1.5000000000]) {
					cylinder(d1 = 6, d2 = 18, h = 4.8000000000);
				}
				translate(v = [0, 0, 6.3000000000]) {
					cylinder(d = 18, h = 1);
				}
				rotate(a = 0) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "?", valign = "center");
						}
					}
				}
				rotate(a = -60) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "R", valign = "center");
						}
					}
				}
				rotate(a = -120) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "Y", valign = "center");
						}
					}
				}
				rotate(a = -180) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "G", valign = "center");
						}
					}
				}
				rotate(a = -240) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "B", valign = "center");
						}
					}
				}
				rotate(a = -300) {
					translate(v = [0, -6.0000000000, 6.5000000000]) {
						linear_extrude(height = 1.5000000000) {
							text(font = "DejaVuSansMono-Bold", halign = "center", size = 4.5000000000, text = "W", valign = "center");
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
				translate(v = [0, 10.3000000000, 0]) {
					rotate(a = [0, 90, 0]) {
						cylinder(center = true, h = 50, r = 10);
					}
				}
				translate(v = [0, -10, 0]) {
					rotate(a = [0, 90, 0]) {
						cylinder(center = true, h = 50, r = 10);
					}
				}
			}
		}
	}
}
