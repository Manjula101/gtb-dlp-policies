#!/bin/bash
# GTB DLP Policy Appliers
# Automation script to load and validate GTB DLP YAML policies
# Author: Manjula Wickramasuriya

if [ $# -ne 1 ]; then
    echo "Usage: bash apply-dlp-policy.sh <path_to_yaml_policy>"
    exit 1
fi

file_path=$1

# Simple validation using yq (assume yq is installed)
policy_name=$(yq e '.policy_name' "$file_path")
description=$(yq e '.description' "$file_path")

if [ -z "$policy_name" ] || [ -z "$description" ]; then
    echo "Invalid policy: missing policy_name or description"
    exit 1
fi

echo "Policy loaded successfully:"
echo "Name: $policy_name"
echo "Description: $description"
echo "Policy is valid."
