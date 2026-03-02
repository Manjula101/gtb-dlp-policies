# GTB DLP Integration Example

This example shows how to integrate GTB DLP policies with a monitoring tool or script.

### Scenario
- Use the sensitive data detection policy to scan outgoing emails or file transfers.
- Block if sensitive data is detected.

### Step 1: Load Policy
Use the Python script to validate the policy:
```bash
python scripts/apply-dlp-policy.py policies/gtb-sensitive-data-detection.yml
