import random
import hashlib
import base58

from generate_hex import generate_random_hex
from generate_address import private_key_to_compressed_public_key, public_key_to_address

'''
13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so
'''

# Main logic
def main():
    ohhana = "000000000000000000000000000000000000000000000003"
    while True:
        lenght = 16
        random_hex = generate_random_hex(lenght)
        fullrandomhex = f"{ohhana}{random_hex}"
        public_key = private_key_to_compressed_public_key(fullrandomhex)
        bitcoin_address = public_key_to_address(public_key)
        
        # 16
        if bitcoin_address.startswith("13z"):
            ohhana += (random_hex[0])
            lenght = lenght - 1
            print(f"Initial Random Hex: {fullrandomhex}")
            print(f"Bitcoin Address: {bitcoin_address}")
            while True:

                random_hex = generate_random_hex(lenght)
                fullrandomhex = f"{ohhana}{random_hex}"
                # print(random_hex)
                public_key = private_key_to_compressed_public_key(fullrandomhex)
                bitcoin_address = public_key_to_address(public_key)

                # 15
                if bitcoin_address.startswith("13zb"):
                    ohhana += (random_hex[0])
                    lenght = lenght - 1
                    print(f"Initial Random Hex: {fullrandomhex}")
                    print(f"Bitcoin Address: {bitcoin_address}")
                    while True:
                    
                        random_hex = generate_random_hex(lenght)
                        fullrandomhex = f"{ohhana}{random_hex}"
                        public_key = private_key_to_compressed_public_key(fullrandomhex)
                        bitcoin_address = public_key_to_address(public_key)

                        # 14
                        if bitcoin_address.startswith("13zb1"):
                            ohhana += (random_hex[0])
                            lenght = lenght - 1
                            print(f"Initial Random Hex: {fullrandomhex}")
                            print(f"Bitcoin Address: {bitcoin_address}")
                            while True:
                            
                                random_hex = generate_random_hex(lenght)
                                fullrandomhex = f"{ohhana}{random_hex}"
                                public_key = private_key_to_compressed_public_key(fullrandomhex)
                                bitcoin_address = public_key_to_address(public_key)

                                # 13
                                if bitcoin_address.startswith("13zb1h"):
                                    ohhana += (random_hex[0])
                                    lenght = lenght - 1
                                    print(f"Initial Random Hex: {fullrandomhex}")
                                    print(f"Bitcoin Address: {bitcoin_address}")
                                    while True:
                                    
                                        random_hex = generate_random_hex(lenght)
                                        fullrandomhex = f"{ohhana}{random_hex}"
                                        public_key = private_key_to_compressed_public_key(fullrandomhex)
                                        bitcoin_address = public_key_to_address(public_key)

                                        # 12
                                        if bitcoin_address.startswith("13zb1hQ"):
                                            ohhana += (random_hex[0])
                                            lenght = lenght - 1
                                            print(f"Initial Random Hex: {fullrandomhex}")
                                            print(f"Bitcoin Address: {bitcoin_address}")
                                            while True:
                                            
                                                random_hex = generate_random_hex(lenght)
                                                fullrandomhex = f"{ohhana}{random_hex}"
                                                public_key = private_key_to_compressed_public_key(fullrandomhex)
                                                bitcoin_address = public_key_to_address(public_key)

                                                # 11
                                                if bitcoin_address.startswith("13zb1hQb"):
                                                    ohhana += (random_hex[0])
                                                    lenght = lenght - 1
                                                    print(f"Initial Random Hex: {fullrandomhex}")
                                                    print(f"Bitcoin Address: {bitcoin_address}")
                                                    while True:
                                                    
                                                        random_hex = generate_random_hex(lenght)
                                                        fullrandomhex = f"{ohhana}{random_hex}"
                                                        public_key = private_key_to_compressed_public_key(fullrandomhex)
                                                        bitcoin_address = public_key_to_address(public_key)
                                                        
                                                        # 10
                                                        if bitcoin_address.startswith("13zb1hQb"):
                                                            ohhana += (random_hex[0])
                                                            lenght = lenght - 1
                                                            print(f"Initial Random Hex: {fullrandomhex}")
                                                            print(f"Bitcoin Address: {bitcoin_address}")
                                                            while True:
                                                            
                                                                random_hex = generate_random_hex(lenght)
                                                                fullrandomhex = f"{ohhana}{random_hex}"
                                                                public_key = private_key_to_compressed_public_key(fullrandomhex)
                                                                bitcoin_address = public_key_to_address(public_key)

                                                                # 9
                                                                if bitcoin_address.startswith("13zb1hQb"):
                                                                    ohhana += (random_hex[0])
                                                                    lenght = lenght - 1
                                                                    print(f"Initial Random Hex: {fullrandomhex}")
                                                                    print(f"Bitcoin Address: {bitcoin_address}")
                                                                    while True:
                                                                    
                                                                        random_hex = generate_random_hex(lenght)
                                                                        fullrandomhex = f"{ohhana}{random_hex}"
                                                                        public_key = private_key_to_compressed_public_key(fullrandomhex)
                                                                        bitcoin_address = public_key_to_address(public_key)

                                                                        # 8
                                                                        if bitcoin_address.startswith("13zb1hQb"):
                                                                            ohhana += (random_hex[0])
                                                                            lenght = lenght - 1
                                                                            print(f"Initial Random Hex: {fullrandomhex}")
                                                                            print(f"Bitcoin Address: {bitcoin_address}")
                                                                            while True:
                                                                            
                                                                                random_hex = generate_random_hex(lenght)
                                                                                fullrandomhex = f"{ohhana}{random_hex}"
                                                                                public_key = private_key_to_compressed_public_key(fullrandomhex)
                                                                                bitcoin_address = public_key_to_address(public_key)

                                                                                # 7
                                                                                if bitcoin_address.startswith("13zb1hQb"):
                                                                                    print("this is a 7 char need stop \n stop it !!!! \n")
                                                                                    ohhana += (random_hex[0])
                                                                                    lenght = lenght - 1
                                                                                    print(f"Initial Random Hex: {fullrandomhex}")
                                                                                    print(f"Bitcoin Address: {bitcoin_address}")
                                                                                    while True:
                                                                                    
                                                                                        random_hex = generate_random_hex(lenght)
                                                                                        fullrandomhex = f"{ohhana}{random_hex}"
                                                                                        public_key = private_key_to_compressed_public_key(fullrandomhex)
                                                                                        bitcoin_address = public_key_to_address(public_key)
                                                                                        break

if __name__ == "__main__":
    main()
