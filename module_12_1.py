
import runner
import unittest

# класс RunnerTest,который наследуется от unittest.TestCase.Это позволяет использовать различные методы для тестирования.
class RunnerTest(unittest.TestCase):

    # В этом методе создаём экземпляр `Runner` с именем `'Runner1'`.
    # - В цикле `for` вызываем метод `walk()` 10 раз. Предполагается, что каждый вызов этого метода увеличивает
    # расстояние, которое пробегает бегун.Проверяем, что после 10 вызовов `walk()` общее расстояние равно 50.
    #  Это подразумевает, что каждый раз, когда вызывается `walk()`, бегун проходит 5 единиц расстояния.

    def test_walk(self):
        runner_walk = runner.Runner('Runner1')
        for i in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    # Аналогично, здесь создаём другой экземпляр `Runner` с именем `'Runner2'`.
    # - Вызываем метод `run()` 10 раз. Предполагаем, что каждый раз бегун пробегает 10 единиц расстояния,
    # так что общее расстояние должно быть 100.

    def test_run(self):
        runner_run = runner.Runner('Runner2')
        for i in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    # Создаём два экземпляра `Runner`, как в предыдущих методах.
    # В цикле `for` вызываем `walk()` для `runner1` и `run()` для `runner2` 10 раз.
    # Проверяем, что расстояния, пройденные двумя бегунами, не равны.

    def test_challenge(self):
        runner1 = runner.Runner("Runner1")
        runner2 = runner.Runner("Runner2")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()