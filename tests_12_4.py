from rt_with_exceptions import Runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walking = Runner('Max', -5)
            if walking.speed > 0:
                logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                walking.walk()
            self.assertEqual(walking.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            running = Runner(True, 5)
            if isinstance(running.name, str):
                logging.info('"test_run" выполнен успешно')
            for i in range(10):
                running.run()
            self.assertEqual(running.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):

        walking = Runner('Max')
        running = Runner('Miha')
        for i in range(10):
            walking.walk()
            running.run()
        self.assertNotEqual(walking.distance, running.distance)


    if __name__ == '__main__':
        unittest.main()
