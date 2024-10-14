'''Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
 Далее 10 раз у объектов вызываются методы run и walk соответственно.
 Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.'''
from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walking = Runner('Max')
        for i in range(10):
            walking.walk()
        self.assertEqual(walking.distance, 50)

    def test_run(self):
        running = Runner('Max')
        for i in range(10):
            running.run()
        self.assertEqual(running.distance, 100)

    def test_challenge(self):
        walking = Runner('Max')
        running = Runner('Miha')
        for i in range(10):
            walking.walk()
            running.run()
        self.assertNotEqual(walking.distance, running.distance)