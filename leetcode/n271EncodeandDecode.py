# import json # this is serialized method; DO NOT USE THIS.
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Insert non-ASCII delimiter between strings
        return '©'.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('©')


# Your Codec object will be instantiated and called as such:
codec = Codec()
# Testing Encode
strs = ["Hello","World"]
# test_res = codec.encode(test_str)
# print(f"TEST: {test_res}")
codec.decode(codec.encode(strs))