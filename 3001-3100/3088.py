# Prob link: https://yukicoder.me/problems/no/3088

# import
import zlib
def decompress_zlib(data):
    return zlib.decompress(data).decode()

# 圧縮後の文字列
compressed = b'x\x9cmOK\x0e\x820\x10\xbd\n\'\xf0\x12\x86\x85\x89q\xe3\x01H-\x034\x96\x0ev\xa6"\x9e^\x19@;\xc6E\xf3~\x93\xbc\xd7\xe3a_\x9e\xceea\xbc/,\x86;\xfa\xc4\x0eC\xcew\xdd0\x145\xa5\xf9\to \x8c\xce^9\x02\xe4\\2\x17\x18b0\xbe\xba8VB\xa7\x96\xa2\x12:\xed\rwZ\xe9\xfc\x96 \xc1\x8f\xd4\x17d\xad\x12:\xe5i\x80\x8a\xa3qL\x7fM\xb9\xf6\xe69\x11\xb4\xf2\xcb\x8cK&\x03?\xbbz\xf3h<\x8e\x1b.\x9e\x0b\x16\x89\x17\xff\xcb\x97\x0c\xebw\xeb\n\xe2\xccs\xb7\x95[g\xdeG\x1c]hW\x10\x87G$\xc3+\xcc\xce\x0b\xe7\x82\xb0\xbd'

# 復元&出力
for s in list(zlib.decompress(compressed).decode()):
    print(s, end="\n")