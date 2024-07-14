import hashlib
import ecdsa
import base58
from Crypto.Hash import RIPEMD160

def private_key_to_compressed_public_key(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key_bytes = vk.to_string()
    
    # Compressed public key format
    if public_key_bytes[32] % 2 == 0:
        compressed_public_key = b'\x02' + public_key_bytes[:32]
    else:
        compressed_public_key = b'\x03' + public_key_bytes[:32]
    
    return compressed_public_key

def public_key_to_address(public_key_bytes):
    sha256_bpk = hashlib.sha256(public_key_bytes).digest()
    ripemd160_bpk = RIPEMD160.new(sha256_bpk).digest()
    network_byte = b'\x00' + ripemd160_bpk
    sha256_nbpk = hashlib.sha256(network_byte).digest()
    sha256_2_nbpk = hashlib.sha256(sha256_nbpk).digest()
    checksum = sha256_2_nbpk[:4]
    binary_address = network_byte + checksum
    address = base58.b58encode(binary_address)
    return address.decode()

# def main():
#     private_key_hex = "ceceee4b5d8213798358d18046b7320e94069e273215da0192d854904cd7d9c7"
    
#     compressed_public_key = private_key_to_compressed_public_key(private_key_hex)
#     bitcoin_address = public_key_to_address(compressed_public_key)
    
#     print(f"Compressed Bitcoin Address: {bitcoin_address}")

# if __name__ == "__main__":
#     main()
