#!/usr/bin/env python3
from jinja2 import FileSystemLoader, Environment
import os
from glob import glob

def gen_rows(gtype):
    ret = []

    YourTTS = 'data/YourTTS'
    FreeVC = 'data/FreeVC'
    DDDMVC = 'data/DDDMVC'
    TDEVC = 'data/TDEVC'

    wavs = sorted(glob(f'data/TDEVC/{gtype}/*.wav'))

    for wav in wavs:
        basename = os.path.basename(wav)
        src_basename = basename.split('-')[0]
        tgt_basename = basename.split('-')[1][:-4]
        src = os.path.join("data", "wavs", f"{src_basename}.wav")
        tgt = os.path.join("data", "wavs", f"{tgt_basename}.wav")
        row = (
                src_basename,
                tgt_basename,
                src, 
                tgt,
                os.path.join(YourTTS, gtype, f'{src_basename}-{tgt_basename}.wav'),
                os.path.join(FreeVC, gtype, f'{src_basename}-{tgt_basename}.wav'),
                os.path.join(DDDMVC, gtype, f'{src_basename}-{tgt_basename}.wav'),
                os.path.join(TDEVC, gtype, f'{src_basename}-{tgt_basename}.wav'),
        )
        ret.append(row)
    return ret


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("base.html.jinja2")

    s2s_rows = gen_rows("s2s")
    s2u_rows = gen_rows("s2u")
    u2u_rows = gen_rows("u2u")

    html = template.render(
        s2s_rows=s2s_rows,
        s2u_rows=s2u_rows,
        u2u_rows=u2u_rows
    )
    # print(html)
    file_path = "output.txt"

    # 打开文件，写入内容，然后关闭文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)
if __name__ == "__main__":
    main()
