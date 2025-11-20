#!/usr/bin/env python
"""Script de teste para verificar como invocar o agente"""

import asyncio
from agent import root_agent
from google.adk.agents import InvocationContext

async def test_agent():
    url = "https://google.com"

    # Tentar criar um contexto de invocação
    context = InvocationContext(user_message=url)

    # Executar o agente
    result_generator = root_agent.run_async(parent_context=context)

    # Coletar resultados
    results = []
    async for event in result_generator:
        print(f"Evento: {type(event).__name__}")
        print(f"Conteúdo: {event}")
        results.append(event)

    return results

if __name__ == "__main__":
    results = asyncio.run(test_agent())
    print(f"\n\n=== RESULTADO FINAL ===")
    print(f"Total de eventos: {len(results)}")
    for i, r in enumerate(results):
        print(f"\n[{i}] {r}")
