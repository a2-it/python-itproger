import pytest
import form
import unittest

# @pytest.mark.parametrize('login, passw', [
#     ('addmeen', 'donneed')
# ])

bot = form.Form('addmeen','password')
alex = form.Form('aaa','bbb','ccc','ddd')
bot12 = form.Form(url= '@itproger.com')

def test_init():
    assert bot.login == 'addmeen'
    assert bot.passw == 'password'
    assert alex.passw == 'bbb'
    assert alex.login == 'aaa'
    assert alex.url == 'ccc'
    assert alex.three == 'ddd'
    assert bot12.url == '@itproger.com'

def test_printAll():
    assert bot12.printAll() == "{}'s password is {}".format(bot12.login, bot12.passw)
    assert bot.printAll() == "{}'s password is {}".format(bot.login, bot.passw)

#
# class TestUser(unittest.TestCase):
#     def setUp(self):
#         self.obj = form.Form()
#
#     # def test_init(self, login, passw):
#     #     assert self.obj.printAll(login, passw) == "addmeen's password is donneed"
#
#     def test_init(self):
#         assert self.obj.login == "bot"
#         assert self.obj.passw == "lemmepass"
#     # self.assertEqual(self.obj.login, "bot")
#     # self.assertEqual(self.obj.passw, "lemmepass")
#
#     def test_printAll(self):
#         self.assertEqual(self.obj.printAll(), "bot's password is lemmepass")
