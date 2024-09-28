from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import requests

class DragonViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.dragon_public_url = reverse('dragon_public')
        self.redirect_to_map_url = reverse('redirect_to_map')
        self.follow_dragon_earthtexture_url = reverse('follow_dragon_earthtexture')
        self.follow_dragon_earthmap_url = reverse('follow_dragon_earthmap')

    @patch('requests.get')  # Mock the requests.get method to avoid actual external calls
    def test_dragon_public_success(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"message": "Success"}

        response = self.client.get(self.dragon_public_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success"})
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_dragon_public_failure(self, mock_get):
        # Simulate a failed API response
        mock_get.side_effect = requests.exceptions.RequestException("Error fetching data")

        response = self.client.get(self.dragon_public_url)

        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Error fetching data", response.content)
        mock_get.assert_called_once()

    def test_redirect_to_map(self):
        response = self.client.get(self.redirect_to_map_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.follow_dragon_earthmap_url)

    def test_follow_dragon_earthtexture_view(self):
        response = self.client.get(self.follow_dragon_earthtexture_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'follow-dragon-earthtexture.html')

    def test_follow_dragon_earthmap_view(self):
        response = self.client.get(self.follow_dragon_earthmap_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'follow-dragon-earthmap.html')
