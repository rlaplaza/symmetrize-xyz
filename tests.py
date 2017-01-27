import unittest
import io
import symmetrize_xyz
import xyz_n


xyz_methylene = u'''\
 C        0.0000000000   0.0000000000  -0.1584796219
 H       -0.8569426061   0.0000000000   0.5695694992
 H        0.8569426061  -0.0000000000   0.5695694992
'''

xyz_ammonia = u'''\
N  0.0000000000   0.0000000000   0.0000000000
H -0.4882960784   0.8457536168   0.0000000000
H -0.4882960784  -0.8457536168   0.0000000000
H  0.9765921567   0.0000000000   0.0000000000
'''


class CommonSymmetrize(object):
    xyz_data = None
    pgrp = None
    tolerance = 0.7

    def test(self):
        xyz = xyz_n.read_xyz_fobj(io.StringIO(self.xyz_data), fname=self.__class__.__name__)
        symmetrize_xyz.main(None, tolerance=self.tolerance, target_point_group=self.pgrp, xyzin=xyz)


class TestMethylene(unittest.TestCase, CommonSymmetrize):
    xyz_data = xyz_methylene
    pgrp = 'C2v'


class TestAmmonia(unittest.TestCase, CommonSymmetrize):
    xyz_data = xyz_ammonia
    pgrp = 'D3h'
    tolerance = 0.01


if __name__ == '__main__':
    unittest.main()
