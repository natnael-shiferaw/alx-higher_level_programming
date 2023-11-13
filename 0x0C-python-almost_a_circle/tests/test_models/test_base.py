#!/usr/bin/python3
"""This Python file is used for Unittesting
Unittest classes:
    TestBase_instantiation - line 19
    TestBase_to_json_string - line 107
    TestBase_save_to_file - line 155
    TestBase_from_json_string - line 237
    TestBase_create - line 293
    TestBase_load_from_file - line 346
    TestBase_save_to_file_csv - line 415
    TestBase_load_from_file_csv - line 497
"""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """A class that's used for Unittesting
    instantiation of the Base class."""

    def no_arg_Test(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def Three_bases_Test(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def id_None_Test(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def Unique_id_Test(self):
        self.assertEqual(12, Base(12).id)

    def nb_instances_afterUniqueId_Test(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def Public_id_Test(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def Private_nb_instances_Test(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def Str_id_Test(self):
        self.assertEqual("hello", Base("hello").id)

    def Float_id_Test(self):
        self.assertEqual(5.5, Base(5.5).id)

    def Complex_id_Test(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def Dict_id_Test(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def Bool_id_Test(self):
        self.assertEqual(True, Base(True).id)

    def List_id_Test(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def Tuple_id_Test(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def Set_id_Test(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def FrozenSet_id_Test(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def Range_id_Test(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def Bytes_id_Test(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def ByteArray_id_Test(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def MemoryView_id_Test(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def inf_id_Test(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def NaN_id_Test(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def Two_arg_Test(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """A class used for Unittesting to_json_string
    method of Base class."""

    def to_json_string_Rectangle_Test(self):

        rec = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def to_json_string_Rectangle_1_dict_Test(self):
        rec = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])) == 53)

    def to_json_string_Rectangle_2_dict_Test(self):
        rec1 = Rectangle(2, 3, 5, 19, 2)
        rec2 = Rectangle(4, 2, 4, 1, 12)
        dict_list = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict_list)) == 106)

    def to_json_string_Square_Test(self):
        Sq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([Sq.to_dictionary()])))

    def to_json_string_Square_1_dict_Test(self):
        Sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([Sq.to_dictionary()])) == 39)

    def to_json_String_Square_2_dict_Test(self):
        Sq1 = Square(10, 2, 3, 4)
        Sq2 = Square(4, 5, 21, 2)
        dict_list = [Sq1.to_dictionary(), Sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict_list)) == 78)

    def to_json_String_EmptyList_Test(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def to_json_String_None_Test(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def to_json_String_noArg_Test(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def to_json_String_MoreThan_1_Arg_Test(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """A class used for Unittesting save_to_file
    method of Base class."""

    @classmethod
    def tearDown(self):
        """A function used for deleting
        any created files."""

        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def save_to_file_1_Rect_Test(self):
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as file_name:
            self.assertTrue(len(file_name.read()) == 53)

    def save_to_file_2_Rect_Test(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def save_to_file_1_square_Test(self):
        Sq = Square(10, 7, 2, 8)
        Square.save_to_file([Sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def save_to_file_2_Square_Test(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def save_to_file_clsName_forFileName_Test(self):
        Sq = Square(10, 7, 2, 8)
        Base.save_to_file([Sq])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def save_to_file_OverWrite_Test(self):
        Sq = Square(9, 2, 39, 2)
        Square.save_to_file([Sq])
        Sq = Square(10, 7, 2, 8)
        Square.save_to_file([Sq])

        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def save_to_file_NONE_Test(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def save_to_file_EmptyList_Test(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """A class used for Unittesting from_json_string
    method of Base class."""

    def from_json_StringType_Test(self):
        ListInput = [{"id": 89, "width": 10, "height": 4}]
        Json_ListInput = Rectangle.to_json_string(ListInput)
        List_Output = Rectangle.from_json_string(Json_ListInput)
        self.assertEqual(list, type(List_Output))

    def from_json_String_1_Rect_Test(self):
        ListInput = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        Json_ListInput = Rectangle.to_json_string(ListInput)
        List_Output = Rectangle.from_json_string(Json_ListInput)
        self.assertEqual(ListInput, List_Output)

    def from_json_String_2_Rect_Test(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)


    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """A class used for Unittesting
    Create method of Base class."""

    def create_rectange_Orig_Test(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec1))

    def create_NEW_rectangle_Test(self):
        rec1 = Rectangle(3, 5, 1, 2, 7)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec2))

    def create_rectangle_is_Test(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """A class used for Unittesting
    load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """A function used for deleting
        any created files."""

        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def load_from_file_1st_Rect_Test(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        List_Rectangles_Output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(List_Rectangles_Output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """A class used for Unittesting
    save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """A function used for deleting
        any created files."""

        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def save_to_file_csv_1_Rect_Test(self):
        rec = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def save_to_file_csv_2_Rect_Test(self):
        rec1 = Rectangle(10, 7, 2, 8, 5)
        rec2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())


    def test_save_to_file_csv_one_square(self):
        Sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([Sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """A class used for Unittesting 
    load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """A function used for deleting
        any created files."""

        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def load_from_file_csv_1st_Rec_TEst(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        List_Rectangle_Output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec1), str(List_Rectangle_Output[0]))

    def load_from_file_csv_2nd_Rec_Test(self):
        rec1 = Rectangle(10, 7, 2, 8, 1)
        rec2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        List_Rect_Output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec2), str(List_Rect_Output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()
