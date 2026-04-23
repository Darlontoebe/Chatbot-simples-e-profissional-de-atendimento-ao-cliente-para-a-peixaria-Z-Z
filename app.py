import panel as pn
import re

pn.extension("perspective")  # para melhor aparência

# Configurações do Chatbot
CHATBOT_NAME = "Z&Z Atendimento"
AVATAR_BOT = "🐟"   # ou use URL de uma imagem se quiser

def responder_mensagem(contents: str, user: str, instance: pn.chat.ChatInterface):
    texto = contents.lower().strip()
    
    # Respostas pré-definidas
    if any(palavra in texto for palavra in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]):
        return "Olá! Bem-vindo à **Z&Z Peixaria** 🐟\nComo posso te ajudar hoje?"
    
    elif any(palavra in texto for palavra in ["preço", "valor", "quanto", "preços", "tilápia"]):
        return (
            "Aqui estão nossos preços atuais:\n\n"
            "• **Filé de Tilápia** → R$ 52,00 / kg\n"
            "• **Filé de Tilápia Empanado** → R$ 52,00 / 1kg\n"
            "• **Lambari** → R$ 30,00 / 800g\n\n"
            "Todos os produtos são frescos e de alta qualidade!"
        )
    
    elif any(palavra in texto for palavra in ["endereço", "localização", "onde", "fica", "rua"]):
        return (
            "📍 **Estamos localizados em:**\n"
            "Rua Guilherme Wietzke, 659\n"
            "Bairro Copetti, Sobradinho - RS\n\n"
            "venha nos visitar!"
        )
    
    elif any(palavra in texto for palavra in ["horário", "atende", "funciona", "aberto"]):
        return (
            "🕒 **Horário de atendimento:**\n"
            "Segunda a Sábado: 08h às 18h\n"
            "Domingo: 08h às 12h\n\n"
            "Pedidos pelo WhatsApp são atendidos todos os dias!"
        )
    
    # NOVA RESPOSTA - Contato / Telefone
    elif any(palavra in texto for palavra in ["contato", "telefone", "whatsapp", "número", "celular", "ligar", "chamar"]):
        return (
            "📞 **Nosso contato:**\n\n"
            "**(51) 99804-1915**\n\n"
            "✅ Clique abaixo para falar diretamente no WhatsApp:\n"
            "👉 [https://wa.me/555198041915](https://wa.me/555198041915)\n\n"
            "Atendemos pedidos e dúvidas todos os dias!"
        )
    
    elif any(palavra in texto for palavra in ["entrega", "entregar", "delivery"]):
        return "Sim! Fazemos entrega apenas na cidade de sobradinho. Nos chame no wattsapp."
    
    elif any(palavra in texto for palavra in ["pedir", "comprar", "quero", "peça"]):
        return (
            "Para fazer seu pedido é bem simples!\n\n"
            "Clique no botão abaixo ou me chame no WhatsApp:\n"
            "👉 https://wa.me/555198041915\n\n"
            "Qual produto você deseja?"
        )
    
    elif "empanado" in texto:
        return "O **Filé de Tilápia Empanado** é uma delícia! R$ 52,00 o pacote de 1kg. Ideal para fritar ou assar rapidinho."
    
    elif "lambari" in texto:
        return "O **Lambari** é ótimo como petisco! R$ 30,00 o pacote de 800g. Perfeito para acompanhar uma cervejinha gelada 🍺"
    
    # Resposta padrão (caso não entenda)
    return (
        "Desculpe, não entendi completamente 😊\n\n"
        "Posso te ajudar com:\n"
        "• Preços dos produtos\n"
        "• Endereço e localização\n"
        "• Horários de atendimento\n"
        "• Como fazer pedido\n\n"
        "É só perguntar!"
    )

# Criando o ChatInterface
chat_interface = pn.chat.ChatInterface(
    callback=responder_mensagem,
    callback_user=CHATBOT_NAME,
    callback_avatar=AVATAR_BOT,
    user="Você",
    sizing_mode="stretch_both",
    height=700,
    show_button_tooltips=True
)

# Mensagem de boas-vindas
chat_interface.send(
    "Olá! Sou o assistente virtual da **Z&Z Peixaria** 🐟\n"
    "Posso te ajudar com preços, localização, horários, pedidos e se preferir pode chamar direto no whatsapp.\n\n"
    "O que você gostaria de saber?",
    user=CHATBOT_NAME,
    respond=False
)

# Layout final
template = pn.template.FastListTemplate(
    title="🛒 Z&Z Peixaria - Assistente Virtual",
    header_background="#001f3f",
    main=[chat_interface],
    accent_base_color="#25D366",
    sidebar_footer="Feito com Panel • Para portfólio",
)

template.servable()