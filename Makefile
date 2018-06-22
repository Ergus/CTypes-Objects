# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (c) 2016 Jimmy Aguilar Mena.
# email: kratsbinovish@gmail.com
# date: 06/03/2016

all: main.x libarray.so

main.x: main.cc libarray.so
	g++ -L${PWD} $< -o $@ -larray -Wl,-rpath,${PWD}


libarray.so: libarray.cpp libarray.h
	g++ -shared -fPIC $< -o $@

.PHONY: clean test

clean:
	rm -rf *.x *.so

test: main.x main.py
	./$<
	./main.py
