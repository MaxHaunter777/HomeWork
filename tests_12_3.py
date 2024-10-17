from runner import Runner
from runner_and_tournament import Runner1, Tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе не заморожены')
    def test_walk(self):
        walking = Runner('Max')
        for i in range(10):
            walking.walk()
        self.assertEqual(walking.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе не заморожены')
    def test_run(self):
        running = Runner('Max')
        for i in range(10):
            running.run()
        self.assertEqual(running.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе не заморожены')
    def test_challenge(self):
        walking = Runner('Max')
        running = Runner('Miha')
        for i in range(10):
            walking.walk()
            running.run()
        self.assertNotEqual(walking.distance, running.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()


    def setUp(self):
        self.runner = [Runner1('Усэйн', 10),
                       Runner1('Андрей', 9),
                       Runner1('Ник', 3)]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{}:".format(key))
            for k, v in value.items():
                print(f'{k}: {v}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament1(self):
        tournament1 = Tournament(90, self.runner[0], self.runner[2])
        result = tournament1.start()
        self.assertTrue(list(result.values())[1].name == "Ник")
        self.all_results['Результат Усейна и Ника'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament2(self):
        tournament1 = Tournament(90, self.runner[1], self.runner[2])
        result = tournament1.start()
        self.assertTrue(list(result.values())[1].name == "Ник")
        self.all_results['Результат Андрейя и Ника'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament3(self):
        tournament1 = Tournament(90, self.runner[0], self.runner[1], self.runner[2])
        result = tournament1.start()
        self.assertTrue(list(result.values())[2].name == "Ник")
        self.all_results['Результат Усейна, Андрейя и Ника'] = result

