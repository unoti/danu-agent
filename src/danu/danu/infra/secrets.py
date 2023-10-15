from abc import ABC, abstractmethod
import json

class SecretsProvider(ABC):
    """Abstract interface for secret providers.
    
    We can provide secrets in many ways such as Azure Key Vault or Kubernetes Secrets.
    """
    class NotFound(Exception):
        """Raised when a secret is not found."""
        pass

    @abstractmethod
    def get_secret(self, name: str) -> str:
        pass

class LocalJsonSecretsProvider(SecretsProvider):
    """A secrets provider that uses a local file to store information in JSON.
    
    This should only be used for lightweight experimentation and isn't very secure.
    But it's also easy to use and doesn't involve setting up keyvaults and associated permissions.
    """
    def __init__(self, filename: str):
        """:param filename: The filename where the secrets are stored."""
        self._filename = filename

    def get_secret(self, name: str) -> str:
        """The file is assumed to be structures as nested dictionaries.
        You can refer to levels with dotted notation."""
        content = self._load()
        val = content
        for level_name in name.split('.'):
            val = val.get(level_name)
            if not val:
                raise SecretsProvider.NotFound(f'Unable to find secret {name}')
        return val
    
    def _load(self) -> dict:
        # We're reading the file every time it's used because we want to recognize changes.
        # This is inefficient but not worth optimizing for now.
        with open(self._filename, 'r') as f:
            result = json.load(f)
            return result