
import os
def main():
  print("Hello from GitGub Action!")
  token = os.environ.get("AZURE_SECRET_TOKEN")
  print(token)
  
if __name__ == "__main__":
  main()
