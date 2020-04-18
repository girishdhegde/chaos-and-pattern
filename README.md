# fractals

The Mandelbrot set is the set of complex numbers {\displaystyle c}c for which the function {\displaystyle f_{c}(z)=z^{2}+c}{\displaystyle f_{c}(z)=z^{2}+c} does not diverge when iterated from {\displaystyle z=0}z=0, i.e., for which the sequence {\displaystyle f_{c}(0)}{\displaystyle f_{c}(0)}, {\displaystyle f_{c}(f_{c}(0))}{\displaystyle f_{c}(f_{c}(0))}, etc., remains bounded in absolute value.

Mandelbrot set images may be created by sampling the complex numbers and testing, for each sample point {\displaystyle c}c, whether the sequence {\displaystyle f_{c}(0),f_{c}(f_{c}(0)),\dotsc }{\displaystyle f_{c}(0),f_{c}(f_{c}(0)),\dotsc } goes to infinity (in practice – whether it leaves some predetermined bounded neighborhood of 0 after a predetermined number of iterations). Treating the real and imaginary parts of {\displaystyle c}c as image coordinates on the complex plane, pixels may then be coloured according to how soon the sequence {\displaystyle |f_{c}(0)|,|f_{c}(f_{c}(0))|,\dotsc }{\displaystyle |f_{c}(0)|,|f_{c}(f_{c}(0))|,\dotsc } crosses an arbitrarily chosen threshold, with a special color (usually black) used for the values of {\displaystyle c}c for which the sequence has not crossed the threshold after the predetermined number of iterations (this is necessary to clearly distinguish the Mandelbrot set image from the image of its complement). If {\displaystyle c}c is held constant and the initial value of {\displaystyle z}z—denoted by {\displaystyle z_{0}}z_{0}—is variable instead, one obtains the corresponding Julia set for each point {\displaystyle c}c in the parameter space of the simple function.

Images of the Mandelbrot set exhibit an elaborate and infinitely complicated boundary that reveals progressively ever-finer recursive detail at increasing magnifications. In other words, the boundary of the Mandelbrot set is a fractal curve. The "style" of this repeating detail depends on the region of the set being examined. The set's boundary also incorporates smaller versions of the main shape, so the fractal property of self-similarity applies to the entire set, and not just to its parts.

### Formal definition
The Mandelbrot set is the set of values of c in the complex plane for which the orbit of 0 under iteration of the quadratic map

{\displaystyle z_{n+1}=z_{n}^{2}+c}{\displaystyle z_{n+1}=z_{n}^{2}+c}
remains bounded.[13] Thus, a complex number c is a member of the Mandelbrot set if, when starting with z0 = 0 and applying the iteration repeatedly, the absolute value of zn remains bounded for all n>0.

For example, for c=1, the sequence is 0, 1, 2, 5, 26, ..., which tends to infinity, so 1 is not an element of the Mandelbrot set. On the other hand, for c=−1, the sequence is 0, −1, 0, −1, 0, ..., which is bounded, so −1 does belong to the set.


A mathematician's depiction of the Mandelbrot set M. A point c is colored black if it belongs to the set, and white if not. Re[c] and Im[c] denote the real and imaginary parts of c, respectively.
The Mandelbrot set can also be defined as the connectedness locus of a family of polynomials.
