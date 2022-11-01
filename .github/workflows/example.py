
import os
def main():
  print("Hello from GitGub Action!")
  token = os.environ.get("AZURE_SECRET_TOKEN")
  if not token:
    raise RuntimeError("Not Azure secrete found")
  print("All good, we got an AZURE SECRET TOEKEN")
  
if __name__ == "__main__":
  main()
