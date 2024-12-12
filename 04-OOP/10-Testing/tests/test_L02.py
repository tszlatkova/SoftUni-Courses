from L02_cat import Cat  # Do not upload to Judge

from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Matsi")

    def test_init_cat(self):

        self.assertEqual("Matsi", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_cat_is_already_fed_raises(self):

        self.cat.fed = True
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)
        self.assertEqual("Already fed.", str(ex.exception))

    def test_eat(self):

        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_cannot_sleep_if_not_fed(self):
        self.cat.sleepy = True
        self.assertFalse(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertFalse(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_cat_sleep(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)
        self.assertTrue(self.cat.fed)


if __name__ == '__main__':
    main()
