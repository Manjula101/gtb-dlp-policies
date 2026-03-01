#!/usr/bin/env python3
"""
GTB DLP Policy Appliers
Automation script to load and validate GTB DLP YAML policies
Author: Manjula Wickramasuriya
"""

import yaml
import sys

def load_policy(file_path):
    """Load and validate a GTB DLP YAML policy"""
    try:
        with open(file_path, 'r') as f:
            policy = yaml.safe_load(f)
        # Simple validation
        if 'policy_name' not in policy or 'description' not in policy:
            raise ValueError("Invalid policy: missing policy_name or description")
        print("Policy loaded successfully:")
        print(f"Name: {policy['policy_name']}")
        print(f"Description: {policy['description']}")
        print("Policy is valid.")
    except Exception as e:
        print(f"Error loading policy: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python apply-dlp-policy.py <path_to_yaml_policy>")
        sys.exit(1)
    load_policy(sys.argv[1])
