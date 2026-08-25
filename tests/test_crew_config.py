import importlib

import ai_finance_intelligence.crew as crew_module


def test_gemini_key_comes_from_environment(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    importlib.reload(crew_module)

    assert crew_module.AiFinanceIntelligence.llm.api_key == "test-gemini-key"
