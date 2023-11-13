#!/usr/bin/python3
"""This Python file is used for unittesting
regarding the square.py file.
"""
import unittest
from models.base import Base
import io
from models.square import Square
import sys


class TestSquareInstantiation(unittest.TestCase):
    """A class used for Unittesting
    instantiation of the Square class."""

    def Is_Base_Test(self):
        self.assertIsInstance(Square(10), Base)

    def Is_Rect_Test(self):
        self.assertIsInstance(Square(10), Square)

    def no_args_Test(self):
        with self.assertRaises(TypeError):
            Square()

    def One_Arg_Test(self):
        Sq1 = Square(10)
        Sq2 = Square(11)
        self.assertEqual(Sq1.id, Sq2.id - 1)

    def Two_args_Test(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def Three_args_Test(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def Four_args_Test(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def MoreThan_Four_args_Test(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def Size_Private_Test(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def Size_getter_Test(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def Size_setter_Test(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def Width_getter_Test(self):
        Sq = Square(4, 1, 9, 2)
        Sq.size = 8
        self.assertEqual(8, Sq.width)

    def Height_Getter_Test(self):
        Sq = Square(4, 1, 9, 2)
        Sq.size = 8
        self.assertEqual(8, Sq.height)

    def x_getter_Test(self):
        self.assertEqual(0, Square(10).x)

    def y_getter_Test(self):
        self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """A class used for Unittesting
    size instantiation of the Square class.."""

    def None_Size_Test(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def Str_Size_Test(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def FrozenSet_size_Test(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class Test_square_x(unittest.TestCase):
    """A class used for Unittesting
    initialization of Square x attribute."""

    def None_x_Test(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def Str_x_Test(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def Float_x_Test(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def Complex_x_Test(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def Dict_x_Test(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def List_x_Test(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def Set_x_Test(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def Inf_x_Test(self):

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class Test_square_y(unittest.TestCase):
    """A class used for Unittesting
    initialization of Square y attribute."""

    def None_y_Test(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def Str_y_Test(self):

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def Float_y_Test(self):

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def Complex_y_Test(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def Dict_y_Test(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def List_y_Test(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquareOrder_Of_Initialization(unittest.TestCase):
    """A class used for Unittesting
    order of Square attribute initialization."""

    def Size_Before_x_Test(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def Size_Before_y_Test(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def x_Before_y_Test(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquareArea(unittest.TestCase):
    """A class used for Unittesting
    area method of the Square class."""

    def Area_small_Test(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def Area_Large_Test(self):
        Sq = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, Sq.area())

    def Area_Changed_Attr_Test(self):
        Sq = Square(2, 0, 0, 1)
        Sq.size = 7
        self.assertEqual(49, Sq.area())

    def Area_oneArg_Test(self):
        Sq = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            Sq.area(1)


class TestSquare_stdout(unittest.TestCase):
    """A class used for Unittesting
    __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """A function used for Capturing and
        returning text printed to stdout.

        Args:
            sq (Square): represents the Square ot print to stdout.
            method (str): represents the method to run on sq.
        Returns:
            The printed text to stdout by calling
            the method on sq.
        """

        cap = io.StringIO()
        sys.stdout = cap
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return cap

    def Str_Method_PrintSize_Test(self):
        Sq = Square(4)
        cap = TestSquare_stdout.capture_stdout(Sq, "print")
        Correct = "[Square] ({}) 0/0 - 4\n".format(Sq.id)
        self.assertEqual(Correct, cap.getvalue())

    def Str_Method_Size_x_Test(self):
        Sq = Square(5, 5)
        Correct = "[Square] ({}) 5/0 - 5".format(Sq.id)
        self.assertEqual(Correct, Sq.__str__())

    def Str_Method_Size_x_y_Test(self):
        Sq = Square(7, 4, 22)
        Correct = "[Square] ({}) 4/22 - 7".format(Sq.id)
        self.assertEqual(Correct, str(Sq))

    def Str_Method_Size_x_y_id_Test(self):
        sq = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sq))

    def Str_Method_Changed_Attr_Test(self):
        Sq = Square(7, 0, 0, [4])
        Sq.size = 15
        Sq.x = 8
        Sq.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(Sq))

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def Display_Size_TEst(self):
        Sq = Square(2, 0, 0, 9)
        cap = TestSquare_stdout.capture_stdout(Sq, "display")
        self.assertEqual("##\n##\n", cap.getvalue())

    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """A class used for Unittesting
    update args method of the Square class."""

    def Update_Args_Zero_Test(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(Sq))

    def Update_Args_one_Test(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(Sq))

    def Update_ARGs_2_Test(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(Sq))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def Update_Args_MoreThan_4_Test(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(Sq))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):

        Sq = Square(10, 10, 10, 10)
        Sq.update(89, 2, 3, 4)
        Sq.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(Sq))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def Update_Args_Invalid_Test(self):
        Sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Sq.update(89, 1, "invalid")

    def Update_Args_x_Negative_Test(self):
        Sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Sq.update(98, 1, -4)

    def update_Args_Invalid_TEst(self):
        Sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Sq.update(89, 1, 2, "invalid")

    def Update_ARGs_y_Negative_TEst(self):
        Sq = Square(10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Sq.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquareUpdateKwargs(unittest.TestCase):
    """A class used for Unittesting
    update kwargs method of Square class."""

    def Update_kwargs_1_Test(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(Sq))

    def Update_kwargs_Two_TEst(self):

        Sq = Square(10, 10, 10, 10)
        Sq.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(Sq))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def Update_kwargs_Size_Zero_TEst(self):

        Sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Sq.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def Update_kwargs_Wrong_KEYS_TEst(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(Sq))

    def Update_kwargs_Some_WrongKEYS_Test(self):
        Sq = Square(10, 10, 10, 10)
        Sq.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(Sq))


class TestSquareToDictionary(unittest.TestCase):
    """A class used for Unittesting for
    to_dictionary method of the Square class."""

    def to_dictionary_Output_Test(self):
        Sq = Square(10, 2, 1, 1)
        corr = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(corr, Sq.to_dictionary())

    def to_dictionary_No_Object_Changes_Test(self):

        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def to_dictionary_Arg_TEst(self):

        Sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            Sq.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
