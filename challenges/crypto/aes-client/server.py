import json
import names
import socket
import socketserver
import time

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

import flag


def encrypt_ecb():
    pass

def decrypt_ecb():
    pass

def encrypt_cbc():
    pass

def decrypt_cbc():
    pass

def encrypt_ctr():
    pass

def decrypt_ctr():
    pass


def make_plaintext():
    pt = " ".join(names.get_full_name() for _ in range(10))
    pt = pt[: len(pt) - len(pt) % 16]
    return pt


class TaskHandler(socketserver.BaseRequestHandler):
    def main(self, client):
        modes = [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CTR]
        mode_names = {
            AES.MODE_ECB: "ECB",
            AES.MODE_CBC: "CBC",
            AES.MODE_CTR: "CTR",
        }

        # Encrypt AES (ECB, CBC, CTR)

        for mode in modes:
            key = Random.new().read(16)

            def make_aes():
                if mode == AES.MODE_ECB:
                    return AES.new(key, mode), None
                else:
                    iv = Random.new().read(16)

                    if mode == AES.MODE_CBC:
                        return AES.new(key, mode, iv), iv
                    else:
                        return AES.new(key, mode, counter = Counter.new(128, initial_value=int(iv.hex(), 16))), iv

            aes, iv = make_aes()
            pt = make_plaintext()
            ct = aes.encrypt(pt.encode())

            test_data = {
                "mode": mode_names[mode],
                "key": key.hex(),
                "iv_or_counter": iv.hex() if iv else None,
                "operation": "encrypt",
                "data": pt
            }

            def send_test(test_data, answer, client, expect_hex):
                print(json.dumps(test_data))
                print(f"Expecting {answer.hex() if expect_hex else answer}")

                client.sendall(json.dumps(test_data).encode())
                output = client.recv(1024).decode()
                print(f"Received {output}")

                success = (expect_hex and ct.hex().lower() == output.lower()) or answer == output
                client.sendall(json.dumps({"success": success}).encode())

                # Give the socket time to flush data to make sure every JSON message is separate
                time.sleep(0.1)
                return success

            if not send_test(test_data, ct, client, True):
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                return
            
            aes, iv = make_aes()
            pt = make_plaintext()
            ct = aes.encrypt(pt.encode())

            test_data["iv_or_counter"] = iv.hex() if iv else None
            test_data["operation"] = "decrypt"
            test_data["data"] = ct.hex()

            if not send_test(test_data, pt, client, False):
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                return
        
        client.sendall(json.dumps({"flag": flag.flag}).encode())

    def handle(self):
        self.main(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()