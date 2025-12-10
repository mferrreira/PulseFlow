import pywhatkit as kit

class WhatsAppService:
    def __init__(self):
        ...

    def send_message(self, number: str, message: str):
        print("[WHATSAPP SERVICE]: Enviando mensagem!")
        print(number, message)

whatsapp_service = WhatsAppService()
