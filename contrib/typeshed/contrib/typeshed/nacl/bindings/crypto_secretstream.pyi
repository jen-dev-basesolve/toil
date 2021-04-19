from nacl._sodium import ffi as ffi, lib as lib
from nacl.exceptions import ensure as ensure
from typing import Any, Optional

crypto_secretstream_xchacha20poly1305_ABYTES: Any
crypto_secretstream_xchacha20poly1305_HEADERBYTES: Any
crypto_secretstream_xchacha20poly1305_KEYBYTES: Any
crypto_secretstream_xchacha20poly1305_MESSAGEBYTES_MAX: Any
crypto_secretstream_xchacha20poly1305_STATEBYTES: Any
crypto_secretstream_xchacha20poly1305_TAG_MESSAGE: Any
crypto_secretstream_xchacha20poly1305_TAG_PUSH: Any
crypto_secretstream_xchacha20poly1305_TAG_REKEY: Any
crypto_secretstream_xchacha20poly1305_TAG_FINAL: Any

def crypto_secretstream_xchacha20poly1305_keygen(): ...

class crypto_secretstream_xchacha20poly1305_state:
    statebuf: Any = ...
    rawbuf: Any = ...
    tagbuf: Any = ...
    def __init__(self) -> None: ...

def crypto_secretstream_xchacha20poly1305_init_push(state: Any, key: Any): ...
def crypto_secretstream_xchacha20poly1305_push(state: Any, m: Any, ad: Optional[Any] = ..., tag: Any = ...): ...
def crypto_secretstream_xchacha20poly1305_init_pull(state: Any, header: Any, key: Any) -> None: ...
def crypto_secretstream_xchacha20poly1305_pull(state: Any, c: Any, ad: Optional[Any] = ...): ...
def crypto_secretstream_xchacha20poly1305_rekey(state: Any) -> None: ...
