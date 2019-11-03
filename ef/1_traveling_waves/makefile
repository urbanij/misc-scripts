all:
	python3.7 setup.py build_ext --inplace

show_diff:
	cython -a functions.pyx

clean:
	rm *.so
	functions.html