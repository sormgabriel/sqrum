import unittest
from test_sqlite_insert_user_story import DatabaseInsert
class TestInsert(unittest.TestCase):
  def test_uno(self):
    db=DatabaseInsert()
    self.assertEqual(len(db.userstories),0)
  


if __name__ == '__name__':
  unittest.main()
