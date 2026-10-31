import sys
import datetime

class Logger:
    """Simple logger for Cloudflare AI Agent Starter Kit."""

    LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

    def __init__(self, level: str = "INFO", stream=sys.stdout):
        self.level = self.LEVELS.get(level.upper(), 20)
        self.stream = stream

    def _log(self, level_name: str, message: str):
        if self.LEVELS[level_name] >= self.level:
            timestamp = datetime.datetime.utcnow().isoformat() + "Z"
            self.stream.write(f"[{timestamp}] {level_name}: {message}\n")
            self.stream.flush()

    def debug(self, message: str):
        self._log("DEBUG", message)

    def info(self, message: str):
        self._log("INFO", message)

    def warning(self, message: str):
        self._log("WARNING", message)

    def error(self, message: str):
        self._log("ERROR", message)

    def critical(self, message: str):
        self._log("CRITICAL", message)
