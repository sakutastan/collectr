import whois
from os import system

def fancySearch(domain: str, debug: bool = True):
    result=whois.whois(domain)
    yaml = "whois:\n"
    for key,value in result.items():
        valueType = type(value)

        if value is None:
            continue

        elif valueType == str:
            yaml += f"  {key}: {value}\n"
        elif valueType == list:
            yaml += f"  {key}:"
            for element in value:
                yaml += f"    - {element}\n"
    if debug:
        print(yaml)
    return yaml

def pinger(domain: str):
    if "&&" in domain:
        raise ValueError("Possible RCE detected.")
    domain = domain.split(" ")[0]

    system(f"ping {domain}")

# Testing
if __name__ == "__main__":
    pinger("google.com")
