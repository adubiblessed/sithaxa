# Config file to run config opperation for new user

import copy
import os
from pathlib import Path
from typing import Dict, Optional

import yaml


class Config:
    """Making  configuration for first Installment."""

    DEFAULT_PROVIDER = "openai"
    DEFAULT_MODELS = {
        "openai": "gpt-4o-mini",
        "groq": "qwen/qwen3-32b",
    }
    PROVIDER_ENV_VARS = {
        "openai": "OPENAI_API_KEY",
        "groq": "GROQ_API_KEY",
    }

    def __init__(self):
        """Initialize configuration manager."""
        self.config_dir = Path.home() / ".sithaxa"
        self.config_file = self.config_dir / "config.yaml"
        self.env_file = self.config_dir / "env.yaml"

        # Create config directory if it doesn't exist
        self.config_dir.mkdir(exist_ok=True)

        # Load or create config
        self.data = self._load_config()
        self._ensure_defaults()

    def _load_env(self):
        """Load an environment configuration file into memory or initialize an empty environment map."""
        if self.env_file.exists():
            try:
                with open(self.env_file, "r", encoding="utf-8") as f:
                    self.env = yaml.safe_load(f) or {}
            except yaml.YAMLError:
                self.env = {}
        else:
            self.env = {}

    def _save_env(self):
        """Save the environment variable file for just the selected model by user."""
        with open(self.env_file, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.env, f)

    def _load_config(self) -> Dict:
        """
        Load configuration from file.

        Returns:
            Configuration dictionary
        """
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f) or {}
            except yaml.YAMLError:
                return self._get_default_config()
        return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """
        Get default configuration.

        Returns:
            Default config dictionary
        """
        return {
            "model": {
                "provider": self.DEFAULT_PROVIDER,
                "model": self.DEFAULT_MODELS[self.DEFAULT_PROVIDER],
                "models": self.DEFAULT_MODELS.copy(),
            },
            "generation": {
                "temperature": 0.7,
                "max_tokens": 500,
            },
        }

    def get_api_key(self, model: Optional[str] = None) -> Optional[str]:
        """
        Get API key from Envfile.

        Args:
            provider: Provider to get API key for

        Returns:
            API key for provider or None if not found
        """
        model = model or self.get_model()
        data = self.data.get("api", {})
        api_keys = data.get("api_keys", {})
        return api_keys.get(model)

    def set_api_key(self, api_key: str, provider: Optional[str] = None):
        """
        Save API key to config.

        Args:
            api_key: API key to save
        """
        provider = provider or self.get_provider()
        data = self.data.setdefault("api", {})
        api_keys = data.setdefault("api_keys", {})
        api_keys[provider] = api_key
        # Maintain legacy key for backwards compatibility with defaults
        if provider == self.get_provider():
            data["api_key"] = api_key
        self.save()

    def _merge_with_defaults(self, defaults: Dict, current: Optional[Dict]) -> Dict:
        """
        Merge user configuration with defaults without losing user values.

        Args:
            defaults: Default configuration structure
            current: User configuration structure

        Returns:
            Combined configuration dictionary
        """
        if not isinstance(defaults, dict):
            return current if current is not None else defaults

        merged = dict(defaults)
        if isinstance(current, dict):
            for key, value in current.items():
                if key in merged:
                    merged[key] = self._merge_with_defaults(merged[key], value)
                else:
                    merged[key] = value
        return merged

    def _ensure_defaults(self):
        """
        Ensure the configuration contains all default keys.
        """
        defaults = self._get_default_config()
        merged = self._merge_with_defaults(defaults, self.data)
        if merged != self.data:
            self.data = merged
            self.save()
        else:
            self.data = merged

    def save(self):
        """Save configuration to file."""
        with open(self.config_file, "w", encoding="utf-8") as f:
            yaml.dump(self.data, f, default_flow_style=False)

    def get(self, key: str, default=None):
        """
        Get a configuration value.

        Args:
            key: Config key in dot notation (e.g., 'api.model')
            default: Default value if key not found

        Returns:
            Configuration value
        """
        keys = key.split(".")
        value = self.data

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

            if value is None:
                return default

        return value

    def set(self, key: str, value):
        """
        Set a configuration value.

        Args:
            key: Config key in dot notation (e.g., 'api.model')
            value: Value to set
        """
        keys = key.split(".")
        data = self.data

        # Navigate to the nested key
        for k in keys[:-1]:
            if k not in data:
                data[k] = {}
            data = data[k]

        # Set the value
        data[keys[-1]] = value
        self.save()

    