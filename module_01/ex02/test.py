#!/usr/bin/env python3
"""
Unit tests
"""

import unittest

from vector import Vector


class TestVectorClass(unittest.TestCase):
    """Test Class for functions and constant from vector module"""

    def test_vector_from_size(self):
        """Test vector_from_size static method"""
        # pylint: disable=protected-access
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        self.assertEqual(Vector._define_vector(4), valid_vec)
        valid_vec = [[0.0], [1.0], [2.0]]
        self.assertEqual(Vector._define_vector(3), valid_vec)
        invalid_vec = 0.0
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)

    def test_vector_from_tuple(self):
        """Test vector_from_tuple static method"""
        # pylint: disable=protected-access
        invalid_vec = (4,)
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = (4, 8, 12)
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        self.assertEqual(Vector._define_vector((0, 4)), valid_vec)
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        self.assertEqual(Vector._define_vector((0, 4)), valid_vec)
        valid_vec = [[3.0]]
        self.assertEqual(Vector._define_vector((3, 4)), valid_vec)
        valid_vec = (4, 4)
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        valid_vec = [[3.0], [2.0], [1.0], [0.0]]
        self.assertEqual(Vector._define_vector((4, 0)), valid_vec)
        valid_vec = [[14.0], [13.0], [12.0], [11.0], [10.0]]
        self.assertEqual(Vector._define_vector((15, 10)), valid_vec)
        valid_vec = [[10.0], [11.0], [12.0], [13.0], [14.0]]
        self.assertEqual(Vector._define_vector((10, 15)), valid_vec)

    # pylint: disable=invalid-name
    def test_define_vector_1D(self):
        """Test check_vector with vector of dimension 1"""
        # pylint: disable=protected-access
        invalid_vec = ['0.0']
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = ['0']
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = ()
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [()]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [0]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [0, 0, 0, 0, 0, 0, 0]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = ['1.2', '3.4']
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = ['', '']
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = []
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        valid_vec = [0.0]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [1.2, 3.4]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [0.0, 1.0, 2.0, 3.0]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)

    # pylint: disable=invalid-name
    def test_define_vector_2D(self):
        """Test check_vector with vector of dimension 2"""
        # pylint: disable=protected-access
        invalid_vec = [[]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[], [], [], []]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[0]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        valid_vec = [[0.0]]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [[1.2]]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 2.5], [1.0, 5.7], [2.0, 7.9], [3.0, 7.7]]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        valid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]
        self.assertEqual(Vector._define_vector(valid_vec), valid_vec)
        invalid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0], [3.0, 3.1]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[0.5, 0.1], [1.0, 1.1], [2.0, 4.1], [3.0, 3]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[[0.0, 0.0]], [[1.0, 1.0]], [[2.0, 2.0]], [[3.0, 3.0]]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = ([0.0, 1.0], [1.0, 2.0], [2.0, 3.0], [3.0, 4.2])
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[0.0], [1.0], [2.0], [0.321, 0.321]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[], []]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[], [0.1]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[1.0], []]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)

    # pylint: disable=invalid-name
    def test_define_vector_invalidD(self):
        """Test check_vector with vector of invalid dimension"""
        # pylint: disable=protected-access
        invalid_vec = [[[], []], [[], []]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[[1.0], [1.0]], [[0.0], [0.0]]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)
        invalid_vec = [[[1.0, 1.0], [1.0, 0.0]], [[0.0, 4.5], [0.0, 4.5]]]
        self.assertRaises(ValueError, Vector._define_vector, invalid_vec)

    def test_init(self):
        """Test vector constructor"""
        with self.assertRaises(ValueError):
            invalid_vec = []
            Vector(invalid_vec)
        with self.assertRaises(ValueError):
            invalid_vec = [[[], []], [[], []]]
            Vector(invalid_vec)
        self.assertTrue(Vector([0.0, 1.0, 2.0, 3.0]))

    def test_values(self):
        """Test Vector values getter"""
        valid_vec = [0.0, 1.0, 2.0, 3.0]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.values, valid_vec)
        valid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.values, valid_vec)

    def test_shape(self):
        """Test Vector shape getter"""
        vec_b = Vector(4)
        self.assertEqual(vec_b.shape, (4, 1))
        valid_vec = [[0.0], [1.0], [2.0], [3.0]]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.shape, (4, 1))
        valid_vec = [0.0, 1.0, 2.0, 3.0]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.shape, (1, 4))
        valid_vec = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.shape, (4, 2))
        valid_vec = [[0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.shape, (1, 10))
        valid_vec = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
        vec_b = Vector(valid_vec)
        self.assertEqual(vec_b.shape, (1, 10))

    def test_add(self):
        """Test __add__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_a = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            v_result = vec_a + vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_a = [[0.0], [1.0], [2.0], [3.0]]
            v_result = vec_a + vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            v_result = vec_a + vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_a = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            v_result = vec_a + vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            v_result = vec_a + vec_b
        vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
        v_expected = Vector([[0.0], [2.0], [4.0], [6.0]])
        v_result = vec_b + vec_b
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 2.0], [4.0, 6.0], [8.0, 10.0]])
        v_result = vec_b + vec_b
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 2.0, 4.0, 6.0])
        v_result = vec_b + vec_b
        self.assertEqual(v_result.values, v_expected.values)

    def test_radd(self):
        """Test __radd__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_a = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            vec_a += vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_a = [[0.0], [1.0], [2.0], [3.0]]
            vec_a += vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            vec_a += vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_a = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            vec_a += vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            vec_a += vec_b
        vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
        v_expected = Vector([[0.0], [2.0], [4.0], [6.0]])
        vec_b += vec_b
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 2.0], [4.0, 6.0], [8.0, 10.0]])
        vec_b += vec_b
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 2.0, 4.0, 6.0])
        vec_b += vec_b
        self.assertEqual(vec_b.values, v_expected.values)

    def test_sub(self):
        """Test __sub__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_a = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            v_result = vec_a - vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_a = [[0.0], [1.0], [2.0], [3.0]]
            v_result = vec_a - vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            v_result = vec_a - vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_a = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            v_result = vec_a - vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            v_result = vec_a - vec_b
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.0, 0.0, 0.0])
        v_result = vec_b - vec_b
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        vec_c = Vector([0.0, 2.0, 4.0, 6.0])
        v_expected = Vector([0.0, -1.0, -2.0, -3.0])
        v_result = vec_b - vec_c
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
        v_result = vec_b - vec_b
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.0, 0.0, 0.0])
        v_result = vec_b - vec_b
        self.assertEqual(v_result.values, v_expected.values)

    def test_rsub(self):
        """Test __rsub__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_a = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            vec_a -= vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
            vec_a = [[0.0], [1.0], [2.0], [3.0]]
            vec_a -= vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            vec_a -= vec_b
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_a = [0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7]
            vec_a -= vec_b
        with self.assertRaises(ValueError):
            vec_a = Vector([0.0, 2.5, 0.0, 0.0, 1.0, 5.7, 2.0, 7.9, 3.0, 7.7])
            vec_b = [[0.0], [1.0], [2.0], [3.0]]
            vec_a -= vec_b
        vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
        v_expected = Vector([[0.0], [0.0], [0.0], [0.0]])
        vec_b -= vec_b
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
        vec_b -= vec_b
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.0, 0.0, 0.0])
        vec_b -= vec_b
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([[0.0], [1.0], [2.0], [3.0]])
        vec_c = Vector([[0.0], [-1.0], [-2.0], [-3.0]])
        v_expected = Vector([[0.0], [2.0], [4.0], [6.0]])
        vec_b -= vec_c
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        vec_c = Vector([[0.0, 2.0], [4.0, 6.0], [8.0, 10.0]])
        v_expected = Vector([[0.0, -1.0], [-2.0, -3.0], [-4.0, -5.0]])
        vec_b -= vec_c
        self.assertEqual(vec_b.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, -2.0, 3.0])
        vec_c = Vector([-100.0, 1.0, -2.0, 999.0])
        v_expected = Vector([100.0, 0.0, 0.0, -996.0])
        vec_b -= vec_c
        self.assertEqual(vec_b.values, v_expected.values)

    def test_truediv(self):
        """Test __truediv__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b / 'Hello'
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b / ('Hello',)
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b / []
        with self.assertRaises(ZeroDivisionError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b / 0
        with self.assertRaises(ZeroDivisionError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b / 0.0
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.5, 1.0, 1.5])
        v_result = vec_b / 2
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.5, 1.0, 1.5])
        v_result = vec_b / 2.0
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([-0.0, -0.5, -1.0, -1.5])
        v_result = vec_b / -2.0
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 0.5], [1.0, 1.5], [2.0, 2.5]])
        v_result = vec_b / 2.0
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[-0.0, -0.5], [-1.0, -1.5], [-2.0, -2.5]])
        v_result = vec_b / -2
        self.assertEqual(v_result.values, v_expected.values)

    def test_rtruediv(self):
        """Test __rtruediv__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b /= 'Hello'
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b /= ('Hello',)
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b /= []
        with self.assertRaises(ZeroDivisionError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b /= 0
        with self.assertRaises(ZeroDivisionError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b /= 0.0
        v_result = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.5, 1.0, 1.5])
        v_result /= 2
        self.assertEqual(v_result.values, v_expected.values)
        v_result = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([0.0, 0.5, 1.0, 1.5])
        v_result /= 2.0
        self.assertEqual(v_result.values, v_expected.values)
        v_result = Vector([0.0, 1.0, 2.0, 3.0])
        v_expected = Vector([-0.0, -0.5, -1.0, -1.5])
        v_result /= -2.0
        self.assertEqual(v_result.values, v_expected.values)
        v_result = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 0.5], [1.0, 1.5], [2.0, 2.5]])
        v_result /= 2.0
        self.assertEqual(v_result.values, v_expected.values)
        v_result = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[-0.0, -0.5], [-1.0, -1.5], [-2.0, -2.5]])
        v_result /= -2
        self.assertEqual(v_result.values, v_expected.values)

    def test_mul(self):
        """Test __mul__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b * 'Hello'
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b * ('Hello',)
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b = vec_b * []
        vec_b = Vector([0.0, 1.0, 2.0, 3.0])
        v_result = vec_b * 0
        v_expected = Vector([0.0, 0.0, 0.0, 0.0])
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
        v_result = vec_b * 0.0
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, 2.0], [4.0, 6.0], [8.0, 10.0]])
        v_result = vec_b * 2.0
        self.assertEqual(v_result.values, v_expected.values)
        vec_b = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, -2.0], [-4.0, -6.0], [-8.0, -10.0]])
        v_result = vec_b * -2.0
        self.assertEqual(v_result.values, v_expected.values)

    def test_rmul(self):
        """Test __rmul__ Vector class method"""
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b *= 'Hello'
        with self.assertRaises(ValueError):
            vec_b = Vector([0.0, 1.0, 2.0, 3.0])
            vec_b *= []
        v_result = Vector([0.0, 1.0, 2.0, 3.0])
        v_result *= 0
        v_expected = Vector([0.0, 0.0, 0.0, 0.0])
        self.assertEqual(v_result.values, v_expected.values)
        v_result = Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
        v_expected = Vector([[0.0, -2.0], [-4.0, -6.0], [-8.0, -10.0]])
        v_result *= -2.0
        self.assertEqual(v_result.values, v_expected.values)

    def test_str(self):
        """Test __str__ Vector class method"""
        self.assertEqual(str(Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])),
                         '[0.0 1.0 2.0 3.0 4.0 5.0]')
        self.assertEqual(str(Vector([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])),
                         '[[ 0.0 1.0]\n [ 2.0 3.0]\n [ 4.0 5.0]]')

    def test_repr(self):
        """Test __repr__ Vector class method"""
        vector_r = Vector([[0.0, 1.0, 2.0, 3.0, 4.0],
                           [5.0, 6.0, 7.0, 8.0, 9.0],
                           [10.0, 11.0, 12.0, 13.0, 14.0]])
        self.assertEqual(repr(vector_r), 'array([[ 0.0 1.0 2.0 3.0 4.0]\n\
       [ 5.0 6.0 7.0 8.0 9.0]\n\
       [ 10.0 11.0 12.0 13.0 14.0]])')
        vector_r = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(repr(vector_r), 'array([0.0 1.0 2.0 3.0 4.0 5.0])')

    def test_dot(self):
        """Test dot Vector class method"""
        with self.assertRaises(ValueError):
            vec_test = Vector([[0.0, 3.0, 5.0], [5.0, 5.0, 2.0]])
            vec_res = Vector([[3.0], [4.0], [3.0], [5.0]])
            vec_test.dot(vec_res)
        with self.assertRaises(ValueError):
            vec_test = Vector([[0.0, 3.0, 6.0]])
            vec_res = Vector([[0.0]])
            vec_test.dot(vec_res)
        with self.assertRaises(TypeError):
            vec_test = [[0.0, 3.0, 5.0], [5.0, 5.0, 2.0]]
            vec_res = Vector([[3.0], [4.0], [3.0]])
            vec_res.dot(vec_test)
        vec_test = Vector([[1.0]])
        vec_res = Vector([[4.0]])
        self.assertEqual(vec_test.dot(vec_res), [[4.0]])
        vec_test = Vector([1.0])
        vec_res = Vector([[4.0]])
        self.assertEqual(vec_test.dot(vec_res), [[4.0]])
        vec_test = Vector([[1.0]])
        vec_res = Vector([4.0])
        self.assertEqual(vec_test.dot(vec_res), [[4.0]])
        vec_test = Vector([1.0])
        vec_res = Vector([4.0])
        self.assertEqual(vec_test.dot(vec_res), [[4.0]])
        vec_test = Vector([0.0, 1.0, 2.0, 3.0])
        vec_res = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(vec_test.dot(vec_res), [[14.0]])
        vec_test = Vector([-0.0, -1.0, -2.0, -3.0])
        vec_res = Vector([[-0.0], [-1.0], [-2.0], [-3.0]])
        self.assertEqual(vec_test.dot(vec_res), [[14.0]])
        vec_test = Vector([[0.0]])
        vec_res = Vector([[0.0]])
        self.assertEqual(vec_test.dot(vec_res), [[0.0]])
        vec_test = Vector([[0.0, 3.0, 5.0], [5.0, 5.0, 2.0]])
        vec_res = Vector([[3.0], [4.0], [3.0]])
        self.assertEqual(vec_test.dot(vec_res), [[27.0], [41.0]])
        vec_res = Vector([[3.0, 1.0], [4.0, 2.0], [3.0, 3.0]])
        self.assertEqual(vec_test.dot(vec_res), [[27.0, 21.0], [41.0, 21.0]])

    # pylint: disable=invalid-name
    def test_T(self):
        """Test T Vector class method"""
        vec_test = Vector([[1.0]])
        self.assertEqual(vec_test.T().values, [[1.0]])
        vec_test = Vector([-1.0])
        self.assertEqual(vec_test.T().values, [[-1.0]])
        vec_test = Vector([4.0])
        self.assertEqual(vec_test.T().values, [[4.0]])
        vec_test = Vector([0.0, 1.0, 2.0, 3.0])
        vec_res = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(vec_test.T().values, vec_res.values)
        vec_test = Vector([[0.0, 1.0, 2.0, 3.0]])
        vec_res = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(vec_test.T().values, vec_res.values)
        vec_test = Vector([[0.0, 3.0, 5.0], [5.0, 5.0, 2.0]])
        self.assertEqual(vec_test.T().values,
                         [[0.0, 5.0], [3.0, 5.0], [5.0, 2.0]])
        vec_test = Vector([[3.0], [4.0], [3.0]])
        self.assertEqual(vec_test.T().values, [[3.0, 4.0, 3.0]])


if __name__ == '__main__':
    unittest.main(verbosity=2)
