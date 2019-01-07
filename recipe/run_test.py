import os
import sys
import numpy

import numpy.core.multiarray
import numpy.core.multiarray_tests
import numpy.core.numeric
import numpy.core.operand_flag_tests
import numpy.core.struct_ufunc_test
import numpy.core.test_rational
import numpy.core.umath
import numpy.core.umath_tests
import numpy.fft.fftpack_lite
import numpy.linalg.lapack_lite
import numpy.random.mtrand

# sys.exit(not numpy.test().wasSuccessful())
"""
FAIL: test_longdouble.test_repr_roundtrip
    "repr was %s" % repr(o))
  File "/root/archiconda3/conda-bld/numpy_1546900037232/_test_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/python2.7/site-packages/numpy/testing/utils.py", line 381, in assert_equal
    raise AssertionError(msg)
AssertionError: 
Items are not equal: repr was 1.0
 ACTUAL: 1.0
 DESIRED: 1.0

FAIL: test_umath.TestComplexFunctions.test_loss_of_precision_longcomplex
 File "/root/archiconda3/conda-bld/numpy_1546900037232/_test_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/lib/python2.7/site-packages/numpy/testing/utils.py", line 77, in assert_
    raise AssertionError(smsg)
AssertionError: (120, 1.7809563130653488766e-10, 5.2863423150788228827e-21, 'arcsinh')
"""
 
