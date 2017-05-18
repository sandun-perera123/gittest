import unittest
from controller.home_controller import HomeController
from flask import Response, request


class HomeTest(unittest.TestCase):

   def test_return_home_page(self):
       resp = request("GET","/")
       self.assertEqual(200, resp.response)



