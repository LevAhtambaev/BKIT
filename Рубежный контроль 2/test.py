import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class TddTest(unittest.TestCase):
    def test_first_task(self):
        one_to_many = [(s.fio, s.avg, c.name)
                       for c in classes
                       for s in students
                       if s.cls_id == c.id]
        self.assertEqual(first_task(one_to_many), [('Ахтамбаев', '11А'), ('Абрамов', '11А')])

    def test_2(self):
        one_to_many = [(s.fio, s.avg, c.name)
                       for c in classes
                       for s in students
                       if s.cls_id == c.id]
        self.assertEqual(second_task(one_to_many), [('11Б', 3.5), ('11В', 3.7), ('11Г', 3.9), ('11А', 4.7)])

    def test_3(self):
        many_to_many_temp = [(c.name, cs.cls_id, cs.stu_id)
                             for c in classes
                             for cs in classes_students
                             if c.id == cs.cls_id]
        many_to_many = [(s.fio, s.avg, cls_name)
                        for cls_name, cls_id, stu_id in many_to_many_temp
                        for s in students if s.id == stu_id]
        self.assertEqual(third_task(many_to_many),
                         [('Абрамов', '11А'), ('Абрамов', '11Д'), ('Ахтамбаев', '11А'), ('Ахтамбаев', '11Д'),
                          ('Ефремов', '11Б'), ('Зорькин', '11А'), ('Зорькин', '11Е'), ('Некрасов', '11А'),
                          ('Некрасов', '11Е'), ('Семенов', '11Б'), ('Семенов', '11Е'), ('Стебунов', '11В'),
                          ('Требуков', '11Г')])
