all:
	python3.7 setup.py build_ext --inplace

show_diff:
	cython -a functions.pyx

clean:
	rm -rf *.so
	rm -rf functions.html
	rm -rf build
	rm -rf __pycache__