mult_two_num: mult_two_num.o productOperation.o productOperation.h
	gcc -o mult_two_num mult_two_num.o productOperation.o productOperation.h

mult_two_num.o: mult_two_num.c
	gcc -c mult_two_num.c

productOperation.o: productOperation.c
	gcc -c productOperation.c

clean:
	rm mult_two_num.o productOperation.o
