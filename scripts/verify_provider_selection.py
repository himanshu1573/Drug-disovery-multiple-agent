import asyncio
import os
import unittest
from unittest.mock import patch, AsyncMock
from agents.provider_select import select_provider_once, reset_provider_selection

class TestProviderSelection(unittest.TestCase):
    def setUp(self):
        reset_provider_selection()
        if "A4T_LLM_PROVIDER" in os.environ:
            del os.environ["A4T_LLM_PROVIDER"]
        if "A4T_LLM_CALLS_ENABLED" in os.environ:
            del os.environ["A4T_LLM_CALLS_ENABLED"]

    @patch("agents.provider_select._probe_openai")
    @patch("agents.provider_select._probe_google")
    def test_both_working_prefers_openai(self, mock_google, mock_openai):
        mock_openai.return_value = (True, None)
        mock_google.return_value = (True, None)
        
        loop = asyncio.get_event_loop()
        selection = loop.run_until_complete(select_provider_once())
        
        self.assertEqual(selection.provider, "openai")
        self.assertEqual(os.environ["A4T_LLM_PROVIDER"], "openai")
        self.assertEqual(os.environ["A4T_LLM_CALLS_ENABLED"], "1")

    @patch("agents.provider_select._probe_openai")
    @patch("agents.provider_select._probe_google")
    def test_only_google_working_falls_back(self, mock_google, mock_openai):
        mock_openai.return_value = (False, "401 Invalid Key")
        mock_google.return_value = (True, None)
        
        loop = asyncio.get_event_loop()
        selection = loop.run_until_complete(select_provider_once())
        
        self.assertEqual(selection.provider, "google")
        self.assertEqual(os.environ["A4T_LLM_PROVIDER"], "google")

    @patch("agents.provider_select._probe_openai")
    @patch("agents.provider_select._probe_google")
    def test_none_working_disables_llm(self, mock_google, mock_openai):
        mock_openai.return_value = (False, "Error")
        mock_google.return_value = (False, "Error")
        
        loop = asyncio.get_event_loop()
        selection = loop.run_until_complete(select_provider_once())
        
        self.assertEqual(selection.provider, "none")
        self.assertEqual(os.environ["A4T_LLM_CALLS_ENABLED"], "0")

if __name__ == "__main__":
    unittest.main()
