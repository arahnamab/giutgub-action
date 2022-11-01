
import os
def main():
  print("Hello from GitGub Action!")
  token = os.environ.get("AZURE_SECRET_TOKEN")
  if not token:
    raise RuntimeError("Not Azure SECRET provided"
  print("All good, we got aan AZURE SECRET TOEKEN")
  
if __name__ == "__main__":
  main()
