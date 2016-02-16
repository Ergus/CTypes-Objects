all: main.x libarray.so

main.x: main.cc libarray.so
	g++ -L${PWD} $< -o $@ -larray -Wl,-rpath,${PWD}


libarray.so: libarray.cpp libarray.h
	g++ -shared -fPIC $< -o $@

.PHONY: clean test

clean:
	rm -rf *.x *.so

test: main.x
	./$<
