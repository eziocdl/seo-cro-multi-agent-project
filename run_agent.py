#!/usr/bin/env python
"""Script simples para executar o agente e retornar resultado via stdout"""

import sys
import asyncio
from agent import root_agent
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

async def main():
    if len(sys.argv) < 2:
        print("Erro: URL não fornecida", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    # Criar sessão
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="seo_audit",
        user_id="web_user"
    )

    # Adicionar mensagem do usuário
    session.messages.append(Content(parts=[Part(text=url)], role="user"))

    # Criar contexto
    context = root_agent._create_invocation_context(
        session_service=session_service,
        session=session,
        invocation_id="cli_invocation"
    )

    # Executar e coletar output
    output_text = ""
    async for event in root_agent.run_async(parent_context=context):
        # Extrair conteúdo de eventos
        if hasattr(event, 'content'):
            if isinstance(event.content, str):
                output_text += event.content
            elif hasattr(event.content, 'text'):
                output_text += event.content.text
            elif hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        output_text += part.text
        elif hasattr(event, 'text'):
            output_text += event.text

    # Imprimir resultado no stdout
    print(output_text)

if __name__ == "__main__":
    asyncio.run(main())
