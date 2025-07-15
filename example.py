#!/usr/bin/env python3
"""
Example usage of the llm-digitalocean plugin
"""

import os
import sys
import llm
from pathlib import Path

# Add the current directory to Python path so we can import the plugin
sys.path.insert(0, str(Path(__file__).parent))

import llm_digitalocean


def main():
    print("=== DigitalOcean LLM Plugin Example ===\n")

    # Check if API key is set
    try:
        headers = llm_digitalocean.get_headers()
        print("✓ API key is configured")
    except Exception as e:
        print(f"✗ API key not configured: {e}")
        print(
            "Please set the DIGITAL_OCEAN environment variable or use 'llm keys set digitalocean'"
        )
        return

    # List available models
    print("\n1. Fetching available models...")
    try:
        models = llm_digitalocean.get_digitalocean_models()
        print(f"Found {len(models)} models:")
        for i, model in enumerate(models[:5]):  # Show first 5 models
            owned_by = model.get("owned_by", "unknown")
            supports_vision = model.get("supports_vision", False)
            vision_str = " (vision)" if supports_vision else ""
            print(f"  {i+1}. {model['id']} (owned by: {owned_by}){vision_str}")

        if len(models) > 5:
            print(f"  ... and {len(models) - 5} more models")

    except Exception as e:
        print(f"Error fetching models: {e}")
        return

    # Show cache information
    print("\n2. Cache information:")
    cache_file = llm.user_dir() / "digitalocean_models.json"
    if cache_file.exists():
        import time

        cache_stat = cache_file.stat()
        cache_age = time.time() - cache_stat.st_mtime
        print(f"  Cache file: {cache_file}")
        print(f"  Cache age: {cache_age:.0f} seconds ({cache_age/3600:.1f} hours)")
        print(f"  Cache size: {cache_stat.st_size} bytes")
    else:
        print("  No cache file found")

    # Test refresh functionality
    print("\n3. Testing refresh functionality...")
    try:
        print("  Refreshing cache...")
        llm_digitalocean.refresh_models()
        print("  ✓ Cache refreshed successfully")
    except Exception as e:
        print(f"  ✗ Error refreshing cache: {e}")

    print("\n=== Example completed ===")
    print("\nTo use the plugin with LLM:")
    print("  llm digitalocean models                    # List all models")
    print("  llm digitalocean refresh                   # Refresh cache")
    print("  llm digitalocean cache-info                # Show cache info")
    print("  llm -m digitalocean/MODEL_NAME 'prompt'    # Use a model")


if __name__ == "__main__":
    main()
