import unittest
from Student import Student

class TestStudent(unittest.TestCase):

    def test_init(self):
        # 测试正常情况
        student = Student('张三', 20, '1234567890')
        self.assertEqual(student.name, '张三')
        self.assertEqual(student.age, 20)
        self.assertEqual(student.mobile, '1234567890')

        # 测试边界情况
        with self.assertRaises(TypeError):
            Student(None, 20, '1234567890')
        with self.assertRaises(TypeError):
            Student('张三', None, '1234567890')
        with self.assertRaises(TypeError):
            Student('张三', 20, None)

    def test_str(self):
        student = Student('李四', 25, '0987654321')
        self.assertEqual(str(student), '姓名：李四，年龄：25，手机号：0987654321')

if __name__ == '__main__':
    unittest.main()
