$fn=256;$fa=6;


union() {
	difference() {
		union() {
			translate(v = [18.1698729811, 0, 0]) {
				rotate(a = [0, 0, 30]) {
					translate(v = [0, 13.2500000000, 1.0000000000]) {
						hull() {
							cube(center = true, size = [5, 25.7000000000, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 26.5000000000, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 25.7000000000, 2]);
						}
					}
				}
			}
			translate(v = [-18.1698729811, 0, 0]) {
				rotate(a = [0, 0, -30]) {
					translate(v = [0, 13.2500000000, 1.0000000000]) {
						hull() {
							cube(center = true, size = [5, 25.7000000000, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 26.5000000000, 1.2000000000]);
							cube(center = true, size = [4.2000000000, 25.7000000000, 2]);
						}
					}
				}
			}
			translate(v = [0, 6.4711431703, 2.5000000000]) {
				hull() {
					hull() {
						cube(center = true, size = [5.7735026919, 8.9000000000, 4.2000000000]);
						cube(center = true, size = [4.9735026919, 9.7000000000, 4.2000000000]);
						cube(center = true, size = [4.9735026919, 8.9000000000, 5]);
					}
					rotate(a = [0, 0, 60]) {
						hull() {
							cube(center = true, size = [5.7735026919, 8.9000000000, 4.2000000000]);
							cube(center = true, size = [4.9735026919, 9.7000000000, 4.2000000000]);
							cube(center = true, size = [4.9735026919, 8.9000000000, 5]);
						}
					}
					rotate(a = [0, 0, 120]) {
						hull() {
							cube(center = true, size = [5.7735026919, 8.9000000000, 4.2000000000]);
							cube(center = true, size = [4.9735026919, 9.7000000000, 4.2000000000]);
							cube(center = true, size = [4.9735026919, 8.9000000000, 5]);
						}
					}
				}
			}
			hull() {
				translate(v = [11.6970053838, 0, 0]) {
					translate(v = [0, 6.4711431703, 3.8000000000]) {
						hull() {
							hull() {
								cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
								cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
								cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
							}
							rotate(a = [0, 0, 60]) {
								hull() {
									cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
								}
							}
							rotate(a = [0, 0, 120]) {
								hull() {
									cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
								}
							}
						}
					}
				}
				translate(v = [-11.6970053838, 0, 0]) {
					translate(v = [0, 6.4711431703, 3.8000000000]) {
						hull() {
							hull() {
								cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
								cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
								cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
							}
							rotate(a = [0, 0, 60]) {
								hull() {
									cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
								}
							}
							rotate(a = [0, 0, 120]) {
								hull() {
									cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 1.1000000000]) {
				intersection() {
					translate(v = [18.1698729811, 0, 0]) {
						rotate(a = [0, 0, 30]) {
							translate(v = [0, 13.2500000000, 1.0000000000]) {
								hull() {
									cube(center = true, size = [5, 25.7000000000, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 26.5000000000, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 25.7000000000, 2]);
								}
							}
						}
					}
					translate(v = [11.6970053838, 0, 0]) {
						translate(v = [0, 6.4711431703, 1.5000000000]) {
							hull() {
								hull() {
									cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
								}
								rotate(a = [0, 0, 60]) {
									hull() {
										cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
									}
								}
								rotate(a = [0, 0, 120]) {
									hull() {
										cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 1.1000000000]) {
				intersection() {
					translate(v = [-18.1698729811, 0, 0]) {
						rotate(a = [0, 0, -30]) {
							translate(v = [0, 13.2500000000, 1.0000000000]) {
								hull() {
									cube(center = true, size = [5, 25.7000000000, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 26.5000000000, 1.2000000000]);
									cube(center = true, size = [4.2000000000, 25.7000000000, 2]);
								}
							}
						}
					}
					translate(v = [-11.6970053838, 0, 0]) {
						translate(v = [0, 6.4711431703, 1.5000000000]) {
							hull() {
								hull() {
									cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
									cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
								}
								rotate(a = [0, 0, 60]) {
									hull() {
										cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
									}
								}
								rotate(a = [0, 0, 120]) {
									hull() {
										cube(center = true, size = [5.7735026919, 8.9000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 9.7000000000, 2.2000000000]);
										cube(center = true, size = [4.9735026919, 8.9000000000, 3]);
									}
								}
							}
						}
					}
				}
			}
		}
		translate(v = [0, 0, 1]) {
			translate(v = [0, 6.5000000000, 2.0100000000]) {
				rotate(a = [5, 0, 180]) {
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
	}
	translate(v = [18.1698729811, 0, 0]) {
		hull() {
			hull() {
				rotate(a = [0, 0, 0]) {
					cube(center = true, size = [2.886751345948129, 5, 1.2000000000]);
				}
				rotate(a = [0, 0, 120]) {
					cube(center = true, size = [2.886751345948129, 5, 1.2000000000]);
				}
				rotate(a = [0, 0, 240]) {
					cube(center = true, size = [2.886751345948129, 5, 1.2000000000]);
				}
			}
			hull() {
				rotate(a = [0, 0, 0]) {
					cube(center = true, size = [2.424871130596429, 4.2000000000, 2]);
				}
				rotate(a = [0, 0, 120]) {
					cube(center = true, size = [2.424871130596429, 4.2000000000, 2]);
				}
				rotate(a = [0, 0, 240]) {
					cube(center = true, size = [2.424871130596429, 4.2000000000, 2]);
				}
			}
		}
	}
}
