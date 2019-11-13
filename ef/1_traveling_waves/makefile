all:
	python3.7 setup.py build_ext --inplace

show_diff:
	cython -a functions.pyx

# exe:
# 	python3.7 -m nuitka --remove-output traveling_wave_1.py -o traveling_wave_1

clean:
	rm -rf *.so
	rm -rf functions.html
	rm -rf functions.c
	rm -rf build
	rm -rf __pycache__


