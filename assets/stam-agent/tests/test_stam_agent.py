"""Integration test for the stam-agent.

Verifies the agent returns "stam" for any input, with LLM calls mocked.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest


@pytest.mark.usefixtures("add_agent_to_path")
class TestStamAgent:
    """End-to-end agent test with mocked LLM."""

    @pytest.mark.asyncio
    async def test_agent_returns_stam(self):
        """Agent must return 'stam' for any user input."""
        from agent import SampleAgent

        mock_message = MagicMock()
        mock_message.content = "stam"

        mock_result = {"messages": [mock_message]}

        with patch("agent.create_agent") as mock_create_agent:
            mock_graph = MagicMock()
            mock_graph.ainvoke = AsyncMock(return_value=mock_result)
            mock_create_agent.return_value = mock_graph

            agent = SampleAgent()
            response = await agent.invoke("Hello", context_id="test-ctx")

        assert response.status == "completed"
        assert response.message == "stam"

    @pytest.mark.asyncio
    async def test_agent_returns_stam_for_any_input(self):
        """Agent must return 'stam' regardless of the input message."""
        from agent import SampleAgent

        mock_message = MagicMock()
        mock_message.content = "stam"
        mock_result = {"messages": [mock_message]}

        for user_input in ["What is the weather?", "Tell me a joke", "12345"]:
            with patch("agent.create_agent") as mock_create_agent:
                mock_graph = MagicMock()
                mock_graph.ainvoke = AsyncMock(return_value=mock_result)
                mock_create_agent.return_value = mock_graph

                agent = SampleAgent()
                response = await agent.invoke(user_input, context_id="test-ctx")

            assert response.status == "completed"
            assert response.message == "stam", f"Expected 'stam' for input: {user_input!r}"

    @pytest.mark.asyncio
    async def test_agent_invoke_error_handling(self):
        """Agent must handle errors gracefully."""
        from agent import SampleAgent

        with patch("agent.create_agent") as mock_create_agent:
            mock_graph = MagicMock()
            mock_graph.ainvoke = AsyncMock(side_effect=Exception("LLM unavailable"))
            mock_create_agent.return_value = mock_graph

            agent = SampleAgent()
            response = await agent.invoke("Hello", context_id="test-ctx")

        assert response.status == "completed"
        assert "error" in response.message.lower()
