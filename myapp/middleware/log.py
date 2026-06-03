from datetime import datetime
import os

class LoggerConsoleMiddleware:
   def __init__(self, get_response): # викликається 1 раз при першому старті сервера
      self.get_response = get_response
      os.makedirs("logs", exist_ok=True)
   def __call__(self, request): # викликається на кожен request
      ip = request.META.get('REMOTE_ADDR')
      path = request.path
      time = datetime.now().strftime('%Y-%m-%d %H:%M')
      info = f'[{time}] {ip} visited {path}\n'
      try:
         with open("logs/myfile.txt", "a", encoding="utf-8") as file:
            file.write(info)
      except OSError as e:
         print(f"File operation failed: {e}")

      response = self.get_response(request)
      return response