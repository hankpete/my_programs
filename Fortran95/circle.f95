program circle
 implicit none !disable implicit d

 ! My first Fortran 95 program
 ! Give radius, return area

 real :: r,pi,a,p
 pi = 3.1415926

 print *, 'Give radius r:'
 read *, r

 a = pi*r**2 !** exponentiation
 p = 2*pi*r
 print *, 'Area = ', a, 'Perimeter = ', p

end program circle
