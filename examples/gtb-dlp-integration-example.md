# GTB DLP Integration Example

This example shows how to integrate GTB DLP policies with a monitoring tool or script.

### Scenario
- Use the sensitive data detection policy to scan outgoing emails or file transfers.
- Block if sensitive data is detected.

### Step 1: Load Policy
Use the Python script to validate the policy:
```bash
python scripts/apply-dlp-policy.py policies/gtb-sensitive-data-detection.yml
# Example Python code to integrate GTB DLP policy
import yaml

def check_sensitive_data(data, policy_file):
    with open(policy_file, 'r') as f:
        policy = yaml.safe_load(f)
    patterns = [p['regex'] for p in policy['triggers'][0]['patterns']]
    for pattern in patterns:
        if re.search(pattern, data):
            return "Blocked: Sensitive data detected"
    return "Allowed: No sensitive data"

# Test
print(check_sensitive_data("Credit card: 4111111111111111", "policies/gtb-sensitive-data-detection.yml"))
