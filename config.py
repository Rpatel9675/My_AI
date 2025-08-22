OLLAMA_HOST = "http://127.0.0.1:11434"

# Primary models
MODEL_REASON = "mixtral:8x7b-instruct"      # Strong reasoning (MoE)
MODEL_GENERAL = "llama3.1:70b"              # Very strong general chat
MODEL_CODE   = "deepseek-coder:33b-instruct"# Code/embedded help
MODEL_VISION = "llava:13b"                  # Image Q&A

# If you want lighter variants:
# MODEL_GENERAL = "llama3.1:8b"
# MODEL_CODE = "deepseek-coder:6.7b"
