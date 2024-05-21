
class EchoPlugin:
    def handle_message(self, message):
        return f"Echo: {message}"
