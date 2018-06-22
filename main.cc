/*
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, version 3.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright (c) 2016 Jimmy Aguilar Mena.
 * email: kratsbinovish@gmail.com
 * date: 06/03/2016
 */

#include "libarray.h"

int main()
{
	myclass **myarray=new myclass*[5];

	for (int i = 0; i < 5; ++i)
		myarray[i]=create(3 * i, 3 * i + 1, 3 * i + 2);

	printarray(myarray,5);

	for (int i = 0; i < 5; ++i)
		delete myarray[i];

	delete [] myarray;

	return 0;
}
